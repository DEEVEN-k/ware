# 4. Flux et diagrammes d'activité

## 4.1 Parcours global d'une organisation

```mermaid
flowchart LR
    A["Création de l'espace<br/>(souscription, 2FA)"] --> B["Décrire l'organisation<br/>secteur, effectif, public/privé,<br/>désignation du correspondant"]
    B --> C{"Mode de recensement"}
    C -->|"diagnostic guidé F01"| D["Traitements détectés"]
    C -->|"import registre existant"| D
    C -->|"modèles sectoriels F02"| D
    C -->|"trames de collecte F04<br/>auprès des services"| D
    D --> E["Fiches en Brouillon"]
    E --> F["Qualification<br/>(moteur + validation humaine)"]
    F --> G{"Régime"}
    G -->|"formalité due"| H["Dossier de formalité<br/>→ dépôt → décision"]
    G -->|"dispense / exclusion"| I["Documentation au registre"]
    F -->|"critère AIPD réuni"| J["Analyse d'impact"]
    J -->|"risque résiduel élevé (BJ)"| H
    H --> K["Registre publié"]
    I --> K
    K --> L["Pilotage continu<br/>indice · alertes · revues · journal"]
    L -->|"revue périodique,<br/>évolution du référentiel"| F
    M["Incident"] --> N["Violation : déclaration,<br/>qualification, notification"]
    N --> L
```

## 4.2 Algorithme d'exécution du moteur de qualification

Générique pour toutes les juridictions, il n'utilise que les données du référentiel (notice §4).

```mermaid
flowchart LR
    S(["Entrée : référentiel publié + valeurs de la fiche + données organisation"]) --> I["q ← logigramme.entree<br/>chemin ← []"]
    I --> R["Lire la valeur du champ q.champ"]
    R --> T{"q.type"}
    T -->|"booleen"| V1["rep ← valeur == vrai<br/>(absente ⇒ faux)"]
    T -->|"multiple"| V2["rep ← au moins une option cochée"]
    V1 --> CB{"q.condition_bloquante<br/>remplie ?"}
    V2 --> CB
    CB -->|"oui"| F["rep ← faux<br/>motif de forçage ajouté"]
    CB -->|"non"| B
    F --> B["branche ← rep ? q.oui : q.non<br/>chemin.ajouter(q, rep)"]
    B --> BT{"branche.type"}
    BT -->|"question"| N["q ← question(branche.cible)"] --> R
    BT -->|"sortie"| O["régime ← branche.cible<br/>motifs ← chemin + branche.motif"]
    O --> TR["Évaluer les règles transverses<br/>(ajoutent tâches / obligations,<br/>ne modifient pas le régime)"]
    TR --> AI["Évaluer les critères AIPD<br/>+ présomption par régime"]
    AI --> RES(["Résultat : juridiction, version du référentiel, régime, motifs,<br/>chemin, besoin d'AIPD, autorité, feuille de route,<br/>réserve d'interprétation (D05)"])
```

Garde-fous d'implémentation :

- Le moteur est une **fonction pure**, sans base de données ni horloge. Il est donc testable par les CSV de recette.
- Protection contre les cycles : au plus `nb_questions` itérations, sinon erreur de référentiel. Ce contrôle est aussi fait à l'import.
- Les deux voies (fiche et assistant) appellent **la même fonction**. Le test de recette compare leurs sorties (notice §7).

## 4.3 Calcul des droits effectifs (à chaque requête)

```mermaid
flowchart LR
    Q(["Requête : utilisateur U, action A, objet O de l'organisation X"]) --> M{"U est membre<br/>de X ?"}
    M -->|"oui"| R1["droits ← union des rôles de U dans X (G04)"]
    R1 --> P1{"rôle limité au périmètre ?<br/>(contributeur métier)"}
    P1 -->|"oui"| P2{"O dans les services<br/>de U ?"}
    P2 -->|"non"| DENY
    P2 -->|"oui"| CHK
    P1 -->|"non"| CHK
    M -->|"non"| C{"U est membre<br/>d'un cabinet ?"}
    C -->|"non"| SUPP{"Intervention support<br/>ouverte et tracée ?"}
    SUPP -->|"non"| DENY
    SUPP -->|"oui"| LOGS["Accès limité dans le temps<br/>+ notification à l'organisation"] --> CHK
    C -->|"oui"| MA{"Mandat Actif entre<br/>le cabinet et X ?"}
    MA -->|"non"| DENY
    MA -->|"oui"| AF{"U nominativement affecté<br/>et non contesté ?"}
    AF -->|"non"| DENY
    AF -->|"oui"| R2["droits ← prérogatives du rôle de cabinet<br/>transposées chez X (G04 §2)"]
    R2 --> PL["droits ← droits ∩ plafond du niveau de mandat<br/>(Consultation / Contribution / Pilotage)"]
    PL --> PE{"O dans le périmètre<br/>du mandat ?"}
    PE -->|"non"| DENY
    PE -->|"oui"| RES{"A ∈ actions réservées<br/>par X ?"}
    RES -->|"oui"| DENY
    RES -->|"non"| CHK
    CHK{"A ∈ droits ?"} -->|"oui"| OK(["Autorisé<br/>journal : U, cabinet, mandat"])
    CHK -->|"non"| DENY(["Refusé (403)"])
```

En .NET, ce flux est implémenté par un `IAuthorizationHandler` unique, alimenté par un cache des
mandats invalidé à chaque changement de statut. Une révocation coupe donc immédiatement les sessions.

## 4.4 Qualification d'une violation et compte à rebours

```mermaid
flowchart LR
    D(["Violation déclarée<br/>ConnaissanceLe = t0"]) --> E["Échéance ← t0 + délai référentiel (72 h)<br/>Rappels à 25/50/75/90 %"]
    E --> V1{"V1 : risque pour les droits<br/>et libertés ?"}
    V1 -->|"non"| NN["Non notifiable<br/>consignation au registre interne"]
    V1 -->|"oui"| V2{"V2 : risque élevé ?"}
    V2 -->|"non"| N1["Notifier l'autorité<br/>pas d'information des personnes"]
    V2 -->|"oui"| N2["Notifier l'autorité<br/>+ informer les personnes concernées"]
    N1 --> DOC["Générer le formulaire de notification (E05)<br/>ou formulaire officiel de l'APDP"]
    N2 --> DOC
    DOC --> ENV["Enregistrer l'envoi → Notifiée<br/>AL-01 résolue"]
    NN --> TRT["En cours de traitement → Résolue → Close"]
    ENV --> TRT
```

## 4.5 Détermination du besoin d'analyse d'impact

```mermaid
flowchart LR
    Q(["Qualification terminée"]) --> P{"Régime ∈<br/>presomption_regimes ?"}
    P -->|"oui"| REQ
    P -->|"non"| C{"Au moins un critère<br/>du référentiel réuni ?<br/>(données sensibles, biométrie,<br/>transfert, volume > seuil…)"}
    C -->|"oui"| REQ["AIPD requise<br/>→ AnalyseImpact « À réaliser »<br/>→ alerte AL-02"]
    C -->|"non"| NO["Pas d'AIPD requise<br/>(motif conservé)"]
```

## 4.6 Calcul de l'indice de conformité

```mermaid
flowchart LR
    EV(["Événement : publication, décision,<br/>AIPD validée, violation close…"]) --> L["Charger la configuration d'indice<br/>(référentiel + paramètres)"]
    L --> C1["completude_registre = moyenne des taux<br/>de complétude des fiches publiées"]
    L --> C2["formalites_accomplies = traitements à formalité aboutie<br/>÷ traitements qualifiés"]
    L --> C3["aipd_realisees = AIPD validées<br/>÷ traitements qui en exigent une"]
    L --> C4["violations_traitees = closes dans le délai<br/>÷ violations des 12 derniers mois"]
    C1 & C2 & C3 & C4 --> Z{"Dénominateur nul ?"}
    Z -->|"oui"| NEU["Neutraliser la composante<br/>et redistribuer son poids au prorata"]
    Z -->|"non"| W
    NEU --> W["Indice = Σ poids × ratio × 100"]
    W --> S["Libellé selon les seuils :<br/>0–39 Action requise · 40–64 À surveiller<br/>65–84 Bon, à consolider · 85–100 Solide"]
    S --> H(["InstantaneIndice historisé"])
```
