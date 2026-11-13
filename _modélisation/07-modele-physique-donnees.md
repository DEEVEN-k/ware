# 7. Modèle physique des données (PostgreSQL)

Une base PostgreSQL, **un schéma par module** (`acces`, `formulaire`, `referentiel`, `registre`, `formalite`,
`aipd`, `violation`, `pilotage`, `journal`). Les noms ci-dessous sont préfixés par leur schéma
(par exemple `registre_fiche` pour `registre.fiche`), parce que Mermaid n'accepte pas le point.

Toute table métier porte `organisation_id`, protégé par :

1. un **filtre global EF Core** (`HasQueryFilter`) sur l'organisation courante ;
2. une **politique RLS PostgreSQL** :
   `USING (organisation_id = current_setting('app.organisation_id')::uuid)`.
   Cette variable est fixée par l'API à chaque connexion, par un intercepteur EF Core.

## 7.1 Accès, organisations et mandats

```mermaid
erDiagram
    acces_utilisateur {
        uuid id PK
        text courriel UK
        text nom_complet
        bool double_auth_active
        bool actif
    }
    acces_organisation {
        uuid id PK
        text denomination
        text forme_juridique
        text pays_etablissement
        bool nature_publique
        bool mission_service_public
        bool visa_active
        bool circuit_fusionne
        uuid groupe_parent_id FK
        jsonb designation_correspondant
        jsonb responsable_traitement
        uuid version_formulaire_id FK
        jsonb valeurs_complementaires
    }
    acces_service {
        uuid id PK
        uuid organisation_id FK
        uuid parent_id FK
        text libelle
    }
    acces_membre_organisation {
        uuid utilisateur_id PK
        uuid organisation_id FK
        text_array roles
        uuid_array perimetre_services
    }
    acces_cabinet {
        uuid id PK
        text denomination
        uuid organisation_propre_id FK
    }
    acces_membre_cabinet {
        uuid utilisateur_id PK
        uuid cabinet_id FK
        text role
    }
    acces_mandat {
        uuid id PK
        uuid organisation_id FK
        uuid cabinet_id FK
        text niveau
        text portee
        uuid_array services_ou_entites
        date date_debut
        date date_fin
        text statut
        text_array actions_reservees
    }
    acces_affectation {
        uuid mandat_id PK
        uuid utilisateur_id PK
        bool opposee
    }

    acces_utilisateur ||--o| acces_membre_organisation : ""
    acces_utilisateur ||--o| acces_membre_cabinet : ""
    acces_organisation ||--o{ acces_membre_organisation : ""
    acces_organisation ||--o{ acces_service : ""
    acces_organisation ||--o{ acces_mandat : "consent"
    acces_cabinet ||--o{ acces_mandat : "reçoit"
    acces_cabinet ||--o{ acces_membre_cabinet : ""
    acces_mandat ||--o{ acces_affectation : ""
```

## 7.2 Référentiels et paramètres

```mermaid
erDiagram
    referentiel_juridiction {
        text code PK
        text nom
        text nom_officiel
        text langue
        text socle_regional
    }
    referentiel_version {
        uuid id PK
        text juridiction_code FK
        text numero
        text statut
        date date_version
        timestamptz publie_le
        jsonb contenu
        text empreinte
    }
    referentiel_cas_recette {
        uuid id PK
        text juridiction_code FK
        text libelle
        jsonb entrees
        text regime_attendu
    }
    referentiel_bulle {
        text id PK
        text juridiction_code FK
        text titre
        text texte
    }
    pilotage_definition_alerte {
        text code PK
        text objet
        text declenchement
        text canal
        int urgence
        text modele_libelle
        bool parametrable_organisation
    }
    pilotage_parametre {
        text cle PK
        text portee PK
        text cible PK
        jsonb valeur
        uuid modifie_par
        timestamptz modifie_le
    }

    referentiel_juridiction ||--o{ referentiel_version : ""
    referentiel_juridiction ||--o{ referentiel_cas_recette : ""
```

Contrainte : `UNIQUE (juridiction_code) WHERE statut = 'Publie'`, c'est-à-dire une seule version
publiée par juridiction.

Les définitions de champs, les types de champ et les listes de valeurs ne sont plus dans le schéma
`referentiel` : ils forment le schéma `formulaire`, détaillé en 11.8.

## 7.3 Registre, qualification, formalités, AIPD et violations

```mermaid
erDiagram
    registre_fiche {
        uuid id PK
        uuid organisation_id FK
        text reference
        text nom
        text_array juridictions
        uuid service_id FK
        uuid version_formulaire_id FK
        text statut
        jsonb valeurs
        numeric taux_completude
        date prochaine_revue
        int numero_version
    }
    registre_version_publiee {
        uuid id PK
        uuid fiche_id FK
        int numero_version
        jsonb instantane
        bool modification_substantielle
        timestamptz publiee_le
    }
    registre_qualification {
        uuid id PK
        uuid fiche_id FK
        uuid referentiel_version_id FK
        text juridiction_code FK
        text voie
        jsonb reponses
        jsonb chemin
        text regime_moteur
        text regime_retenu
        text motif_ecart
        bool aipd_requise
        bool est_courante
        uuid auteur_id
        uuid mandat_id
        timestamptz qualifiee_le
    }
    registre_prestataire {
        uuid id PK
        uuid organisation_id FK
        text denomination
        text pays
    }
    registre_sous_traitance {
        uuid fiche_id PK
        uuid prestataire_id PK
        bool contrat_conforme
        uuid contrat_piece_id FK
    }
    registre_transfert {
        uuid id PK
        uuid fiche_id FK
        text pays_destination
        text garantie
        bool pays_reconnu
    }
    registre_piece_jointe {
        uuid id PK
        uuid organisation_id FK
        text nom_fichier
        text cle_stockage
        text empreinte_sha256
    }
    formalite_dossier {
        uuid id PK
        uuid organisation_id FK
        uuid fiche_id FK
        uuid qualification_id FK
        text regime_code
        text type
        text statut
        timestamptz envoye_le
        date echeance_instruction
        text reference_decision
        date valide_jusquau
    }
    formalite_jalon {
        uuid id PK
        uuid dossier_id FK
        timestamptz date
        text type
        uuid piece_id FK
    }
    formalite_document_produit {
        uuid id PK
        text modele
        text format
        uuid referentiel_version_id FK
        uuid piece_id FK
        uuid dossier_id FK
        uuid violation_id FK
    }
    aipd_analyse {
        uuid id PK
        uuid fiche_id FK
        text statut
        text_array criteres_declencheurs
        int risque_initial
        int risque_residuel
        uuid dossier_consultation_id FK
    }
    aipd_section {
        uuid analyse_id PK
        int numero PK
        text contenu
    }
    aipd_risque {
        uuid id PK
        uuid analyse_id FK
        int gravite
        int vraisemblance
        int gravite_residuelle
        int vraisemblance_residuelle
    }
    violation_violation {
        uuid id PK
        uuid organisation_id FK
        text juridiction_code FK
        timestamptz connaissance_le
        timestamptz echeance_notification
        text statut
        bool notification_requise
        bool information_requise
        timestamptz notifiee_le
    }
    violation_fiche {
        uuid violation_id PK
        uuid fiche_id PK
    }

    registre_fiche ||--o{ registre_version_publiee : ""
    registre_fiche ||--o{ registre_qualification : ""
    registre_qualification }o--|| referentiel_version : "version figée"
    registre_fiche ||--o{ registre_sous_traitance : ""
    registre_prestataire ||--o{ registre_sous_traitance : ""
    registre_fiche ||--o{ registre_transfert : ""
    registre_fiche ||--o{ formalite_dossier : ""
    registre_qualification ||--o{ formalite_dossier : "fonde"
    formalite_dossier ||--o{ formalite_jalon : ""
    formalite_dossier ||--o{ formalite_document_produit : ""
    registre_fiche ||--o{ aipd_analyse : ""
    aipd_analyse ||--|{ aipd_section : "4 sections"
    aipd_analyse ||--o{ aipd_risque : ""
    violation_violation ||--o{ violation_fiche : ""
    registre_fiche ||--o{ violation_fiche : ""
    violation_violation ||--o{ formalite_document_produit : ""
    referentiel_version {
        uuid id PK
    }
```

Index recommandés :

- `registre_fiche (organisation_id, statut)` ;
- un index GIN sur `registre_fiche.valeurs` (recherche par champ) ;
- `UNIQUE registre_qualification (fiche_id, juridiction_code) WHERE est_courante` ;
- `formalite_dossier (statut, echeance_instruction)` pour les tâches planifiées.

## 7.4 Pilotage et journal

```mermaid
erDiagram
    pilotage_occurrence_alerte {
        uuid id PK
        text code FK
        uuid organisation_id FK
        text objet_type
        uuid objet_id
        timestamptz echeance
        bool resolue
    }
    pilotage_tache {
        uuid id PK
        uuid organisation_id FK
        text titre
        text origine
        uuid assignee_a
        date echeance
        text statut
        text justification
    }
    pilotage_notification {
        uuid id PK
        uuid destinataire_id FK
        text canal
        text message
        timestamptz lue_le
    }
    pilotage_instantane_indice {
        uuid organisation_id PK
        timestamptz calcule_le PK
        numeric valeur
        text libelle
        jsonb detail
    }
    journal_entree {
        bigint sequence PK
        uuid organisation_id
        timestamptz horodatage
        uuid acteur_id
        uuid cabinet_id
        uuid mandat_id
        bool intervention_support
        text action
        text objet_type
        uuid objet_id
        jsonb avant
        jsonb apres
        bytea empreinte_precedente
        bytea empreinte
    }
    pilotage_occurrence_alerte ||--o{ pilotage_notification : ""
    pilotage_occurrence_alerte |o--o| pilotage_tache : ""
```

`journal_entree` : l'utilisateur applicatif n'a que le droit `INSERT` (`REVOKE UPDATE, DELETE`).
La table est partitionnée par mois et une vérification nocturne de la chaîne d'empreintes est
programmée dans Hangfire.
