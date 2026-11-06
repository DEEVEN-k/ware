# 6. Diagrammes de séquence

Participants techniques : front (React), API (ASP.NET Core), modules de l'application,
PostgreSQL, Hangfire (tâches planifiées), stockage S3, Gotenberg et SMTP.

## 6.1 Qualification en direct pendant la saisie, puis enregistrement

```mermaid
sequenceDiagram
    autonumber
    actor U as Correspondant
    participant FE as Front (fiche)
    participant API as API ASP.NET Core
    participant AZ as Autorisation
    participant REF as Module Référentiels
    participant MOT as Wade.Moteur
    participant REG as Module Registre
    participant DB as PostgreSQL
    participant J as Journal

    U->>FE: modifie un champ qui alimente le moteur
    FE->>FE: pause de frappe (≈ 400 ms)
    FE->>API: POST /api/qualifications/simulation {ficheId, valeurs}
    API->>AZ: peut « consulter » la fiche ?
    AZ-->>API: oui
    API->>REF: référentiel publié de chaque juridiction de la fiche
    REF-->>API: Referentiel typé (cache mémoire, clé = version)
    API->>MOT: Qualifier(referentiel, valeurs, organisation)<br/>(une exécution par juridiction)
    MOT-->>API: régime, motifs, chemin, AIPD, feuille de route
    API-->>FE: 200 résultat provisoire (non enregistré)
    FE-->>U: badge du régime + motifs + bulle d'aide + réserve D05

    U->>FE: « Arrêter le régime » (option : autre régime + motif)
    FE->>API: POST /api/fiches/{id}/qualifications {regimeRetenu?, motifEcart?}
    API->>AZ: peut « qualifier » ? (rôle ∩ mandat)
    AZ-->>API: oui
    API->>MOT: ré-exécution côté serveur (même fonction)
    MOT-->>API: résultat certifié
    API->>REG: fiche.Qualifier(qualification)
    REG->>DB: INSERT qualification (version de référentiel figée)<br/>UPDATE fiche.statut = Qualifiée
    REG->>J: entrée chaînée (acteur, mandat, avant/après)
    alt AIPD requise
        REG->>DB: INSERT analyse_impact (À réaliser) + alerte AL-02
    end
    alt règles transverses déclenchées
        REG->>DB: INSERT tâches (BJ-T3 consultation si écart, etc.)
    end
    API-->>FE: 201 Qualification
```

## 6.2 Circuit soumission, qualification, visa, publication

```mermaid
sequenceDiagram
    autonumber
    actor CM as Contributeur métier
    actor COR as Correspondant
    actor RT as Responsable de traitement
    participant API as API
    participant REG as Module Registre
    participant PIL as Module Pilotage
    participant MAIL as SMTP

    CM->>API: POST /fiches/{id}/soumettre
    API->>REG: contrôle de complétude (ExigenceChamp de la juridiction)
    alt champs obligatoires manquants
        REG-->>API: 422 + liste des champs (AL-05)
    else complet
        REG->>REG: Brouillon → Soumise à qualification
        REG->>PIL: événement FicheSoumise
        PIL->>MAIL: notification au correspondant
    end
    COR->>API: qualifier (voir 6.1)
    REG->>PIL: événement FicheQualifiee
    alt visa activé
        PIL->>MAIL: demande de visa au RT
        RT->>API: POST /fiches/{id}/viser
        REG->>REG: Qualifiée → Visée
    end
    COR->>API: POST /fiches/{id}/publier
    REG->>REG: → Publiée au registre + VersionFichePubliee
    REG->>PIL: événement FichePubliee
    PIL->>PIL: recalcul de l'indice, planifier la revue (12 ou 6 mois)
    alt formalité due
        PIL->>PIL: programmer AL-03 (J+30 si non déposée)
    end
```

## 6.3 Dossier de formalité : dépôt, délais et acceptation tacite

```mermaid
sequenceDiagram
    autonumber
    actor COR as Correspondant
    participant API as API
    participant FOR as Module Formalités
    participant DOC as Module Documents
    participant GOT as Gotenberg
    participant S3 as Stockage S3
    participant HF as Hangfire
    participant PIL as Module Pilotage

    COR->>API: POST /fiches/{id}/dossiers
    API->>FOR: créer le dossier (prérempli depuis fiche + qualification)
    FOR->>DOC: générer E03 (modèle Word de la juridiction)
    DOC->>DOC: Open XML : fusion des champs, terminologie, mentions E07
    DOC->>GOT: conversion PDF
    GOT-->>DOC: PDF
    DOC->>S3: dépôt du .docx et du .pdf (empreinte SHA-256)
    DOC-->>FOR: DocumentProduit
    COR->>API: valider, puis « déposé le … par … » (canal)
    FOR->>FOR: Prête à être transmise → Envoyée
    FOR->>FOR: échéance = date de dépôt + délai_instruction(régime)<br/>(+ prorogation, × 2 si investigation)
    FOR->>HF: Schedule(VerifierEcheance, échéance)
    FOR->>HF: Schedule(AL-04, échéance + 15 j)

    Note over HF: … à l'échéance …
    HF->>FOR: VerifierEcheance(dossierId)
    alt décision déjà enregistrée
        FOR-->>HF: rien à faire
    else silence_vaut_acceptation (Bénin)
        FOR->>FOR: → Acceptation tacite
        FOR->>FOR: ValideJusquau = échéance + 24 mois
        FOR->>HF: Schedule(AL-12, J-60 et J-15)
        FOR->>PIL: recalcul de l'indice + notification
    else Togo (silence sans effet)
        FOR->>PIL: AL-04 « dossier déposé sans suite » à échéance + 15 j
    end
```

## 6.4 Déclaration et notification d'une violation

```mermaid
sequenceDiagram
    autonumber
    actor D as Déclarant (mobile)
    actor COR as Correspondant
    participant API as API
    participant VIO as Module Violations
    participant HF as Hangfire
    participant DOC as Module Documents
    participant MAIL as SMTP

    D->>API: POST /violations {connaissanceLe, description, natures}
    Note right of API: aucune expiration de session<br/>pendant cette saisie (G07)
    API->>VIO: créer (Déclarée), échéance = connaissanceLe + 72 h
    VIO->>HF: Schedule rappels à 25, 50, 75 et 90 % du délai
    VIO->>MAIL: AL-01 immédiate au correspondant
    COR->>API: répondre à V1 / V2
    VIO->>VIO: décision : notifier ? informer ?
    alt notification requise
        COR->>API: générer la notification
        API->>DOC: E05 (ou formulaire de l'APDP pré-rempli)
        DOC-->>COR: PDF
        COR->>API: « notifiée le … »
        VIO->>VIO: → Notifiée, rappels annulés
    else aucun risque
        VIO->>VIO: → Non notifiable (registre interne)
    end
    loop à chaque rappel tant que non notifiée
        HF->>VIO: Rappel(violationId)
        VIO->>MAIL: « Il reste {reste} »
    end
```

## 6.5 Mandat : demande, acceptation, accès d'un consultant, révocation

```mermaid
sequenceDiagram
    autonumber
    actor AC as Admin cabinet
    actor AO as Admin organisation
    actor CS as Consultant
    participant API as API
    participant MAN as Module Organisations/Mandats
    participant AZ as Autorisation
    participant J as Journal

    AC->>API: POST /mandats {organisation, niveau, périmètre, durée}
    MAN->>MAN: Demandé
    MAN-->>AO: notification
    AO->>API: accepter (réauthentification 2FA)
    MAN->>MAN: Accepté → Actif (date de début)
    MAN->>J: trace (acteur, termes du mandat)
    AC->>API: affecter CS au mandat
    MAN-->>AO: information (possibilité de s'opposer)

    CS->>API: GET /organisations/{X}/fiches
    API->>AZ: évaluer (flux 4.3)
    AZ->>MAN: mandat actif ? CS affecté ? périmètre ? plafond ?
    MAN-->>AZ: oui, Contribution, services RH
    AZ-->>API: autorisé (filtré sur le périmètre)
    API->>J: accès tracé (CS, cabinet, mandat)
    API-->>CS: fiches RH uniquement

    AO->>API: révoquer le mandat
    MAN->>MAN: → Révoqué
    MAN->>AZ: invalider le cache des droits + couper les sessions du cabinet sur X
    CS->>API: nouvelle requête
    API-->>CS: 403
```

## 6.6 Publication d'une nouvelle version de référentiel

```mermaid
sequenceDiagram
    autonumber
    actor JUR as Juriste AMELEGAL
    participant BO as Back-office
    participant REF as Module Référentiels
    participant MOT as Wade.Moteur
    participant DB as PostgreSQL
    participant PIL as Module Pilotage

    JUR->>BO: importer referentiel-benin.json (v1.1)
    BO->>REF: valider (schéma JSON + cohérence du graphe :<br/>cibles existantes, pas de cycle, champs connus)
    REF->>DB: INSERT referentiel_version (Brouillon)
    JUR->>BO: lancer la simulation
    REF->>MOT: rejouer cas-de-recette-benin.csv
    REF->>MOT: rejouer les fiches publiées (avant / après)
    MOT-->>REF: écarts de recette + fiches dont le régime change
    REF-->>JUR: rapport de simulation
    alt aucun écart de recette
        JUR->>BO: publier
        REF->>DB: v1.0 → Remplacé, v1.1 → Publié (transaction)
        REF->>PIL: événement ReferentielPublie
        PIL->>PIL: AL-09 aux organisations concernées<br/>fiches au régime modifié → À réviser
    else écarts
        REF->>DB: retour en Brouillon
    end
```
