# 11. Formulaires configurables

**Objectif :** les champs du registre, de l'organisation et des autres formulaires, **y compris
leur type**, se créent directement dans l'application, sans développement ni redéploiement.
C'est le prolongement de la règle cardinale de la notice (« aucune valeur dans le code ») aux
formulaires eux-mêmes.

## 11.1 Le principe : trois niveaux

Un type de champ ne peut pas être entièrement libre : il faut bien qu'un composant sache
afficher la saisie et qu'un validateur sache la contrôler. On sépare donc ce qui relève du code
de ce qui relève de la configuration.

```mermaid
flowchart LR
    subgraph CONF2["③ Dans l'application : champs, assemblés<br/>en formulaires versionnés"]
        direction TB
        C1["org.email : Courriel"]
        C2["org.effectif : Tranche d'effectif"]
        C3["t.sous_traitants : Tableau des sous-traitants"]
        C4["Champ propre d'une organisation :<br/>« Code projet interne » : Texte"]
    end
    subgraph CONF1["② Dans l'application : types de champ"]
        direction TB
        T1["Courriel = Texte + format courriel"]
        T2["Téléphone = Texte + motif international"]
        T3["Tranche d'effectif = Choix + liste « effectifs »"]
        T4["Montant FCFA = Nombre + 0 décimale + unité FCFA"]
        T5["Contrat PDF = Fichier + .pdf + 10 Mo max"]
        T6["Tableau des sous-traitants = Collection<br/>de sous-champs"]
    end
    subgraph CODE["① Dans le code : 12 primitives, figées"]
        direction TB
        P1["Texte · Texte long"]
        P2["Nombre · Booléen"]
        P3["Date · Date et heure"]
        P4["Choix · Choix multiple"]
        P5["Fichier · Référence"]
        P6["Groupe · Collection"]
    end

    classDef code fill:#00370B,color:#fff,stroke:#00370B
    class P1,P2,P3,P4,P5,P6 code
```

| Niveau | Qui le crée | Exemples |
|---|---|---|
| **Primitive** (code) | Les développeurs, une fois pour toutes | Texte, Nombre, Choix, Collection… Ajouter une primitive est le seul cas qui demande un développement. |
| **Type de champ** (application) | Administrateur back-office, ou administrateur d'organisation pour sa portée | « Numéro RCCM », « Tranche d'effectif », « Durée en mois », « Pièce justificative PDF » |
| **Champ** (application) | Juriste AMELEGAL pour les champs réglementaires, administrateur d'organisation pour ses champs propres | `t.finalites`, `t.donnees_sensibles`, « Code projet interne » |

### Les 12 primitives

| Primitive | Contraintes paramétrables dans l'application | Stockage JSON |
|---|---|---|
| Texte | longueur min/max, motif (expression régulière), format prédéfini (courriel, URL, téléphone), masque de saisie | `"chaîne"` |
| Texte long | longueur min/max | `"chaîne"` |
| Nombre | min, max, nombre de décimales, unité | `12.5` |
| Booléen | libellés oui/non | `true` |
| Date, Date et heure | bornes (avant/après une date ou aujourd'hui) | `"2026-11-13"` |
| Choix | liste de valeurs | `"code"` |
| Choix multiple | liste de valeurs, nombre max de sélections | `["code1","code2"]` |
| Fichier | extensions autorisées, taille max, nombre max | `["id-pièce"]` |
| Référence | entité visée : prestataire, service, utilisateur, pays, autre fiche | `"id"` |
| Groupe | sous-champs | `{ "souschamp": … }` |
| Collection (tableau) | sous-champs (colonnes), lignes min/max | `[{…},{…}]` |

`Groupe` et `Collection` permettent de composer des types complexes **sans code** : le
« tableau des catégories de données », le « tableau des durées de conservation » ou le « tableau
des transferts » du registre sont des collections dont les colonnes sont elles-mêmes des champs.

## 11.2 Exemples tirés de `registre-champs.csv`

Les 70 champs actuels deviennent la **configuration initiale**, chargée par import du CSV. Plus
rien de ce qu'ils décrivent n'est figé dans le code.

| Champ | Type dans le CSV | Type de champ créé | Primitive et contraintes |
|---|---|---|---|
| `org.email` | courriel | Courriel | Texte, format courriel |
| `org.telephone` | telephone | Téléphone | Texte, motif `^\+?[0-9 ]{8,20}$` |
| `org.effectif` | tranche | Tranche d'effectif | Choix, liste « effectifs » |
| `org.forme_juridique` | liste | Forme juridique | Choix, liste « formes juridiques » (SA, SARL…) |
| `t.finalites` | liste multiple | Finalités | Choix multiple, liste hiérarchique « finalités / sous-finalités » |
| `t.caracteristiques_article_407` | liste multiple | Caractéristiques art. 407 (BJ) | Choix multiple, liste dont les codes sont **utilisés par BJ-Q6** |
| `t.volume_personnes` | tranche | Volume de personnes | Choix, liste « volumes » ; chaque valeur porte sa borne basse, ce qui règle l'écart n° 5 |
| `t.sous_traitants` | tableau | Tableau des sous-traitants | Collection : prestataire (Référence), prestation (Texte), contrat conforme (Booléen), contrat (Fichier PDF) |
| `dpo.justificatif` | fichier | Pièce justificative | Fichier, PDF/JPG/PNG, 10 Mo |

## 11.3 Ce que l'application garantit malgré la liberté de configuration

La souplesse ne doit pas casser le moteur de qualification, les exports ni les données déjà
saisies. Six garde-fous sont appliqués **à la publication** d'une version de formulaire ou d'un
type :

1. **Champs utilisés par le moteur, verrouillés.** Un champ cité par une question du logigramme, une condition bloquante, un critère d'AIPD ou l'indice ne peut ni changer de primitive, ni perdre une valeur dont le code est cité par le référentiel (par exemple `donnees_biometriques`). Le contrôle croise automatiquement les référentiels publiés : c'est exactement le contrôle qui a révélé les écarts n° 1 et 2 du README, désormais bloquant.
2. **Codes stables.** Le code d'un champ et le code d'une valeur de liste sont immuables une fois publiés. On peut renommer le libellé, désactiver une valeur, jamais réutiliser un code.
3. **Pas de modification destructive en place.** Changer la primitive d'un champ qui a déjà des données est refusé. On crée un nouveau champ et on rend l'ancien obsolète ; un assistant propose de convertir les valeurs quand c'est possible (Texte vers Choix par correspondance, par exemple).
4. **Versions de formulaire immuables.** Chaque fiche mémorise la version avec laquelle elle a été saisie. Une fiche ancienne reste lisible et exportable telle qu'elle était, comme une qualification reste explicable avec son ancienne version de référentiel.
5. **Portée et cloisonnement.** Un champ ou un type de portée « Organisation » n'est visible que de cette organisation. Il ne peut **jamais** alimenter le moteur, et il n'apparaît dans les exports réglementaires que si l'organisation le décide (`ExportRegistre`).
6. **Sécurité des motifs.** Les expressions régulières saisies par les administrateurs sont exécutées avec un délai maximal (protection contre les motifs pathologiques) et testées sur des exemples avant publication.

## 11.4 Cycle de vie d'une version de formulaire

```mermaid
stateDiagram-v2
    direction LR
    [*] --> Brouillon : nouvelle version (copie de la version publiée)
    Brouillon --> EnVerification : demander la publication
    EnVerification --> Brouillon : contrôle en échec<br/>(champ verrouillé modifié, code réutilisé…)
    EnVerification --> Publiee : contrôles réussis + validation
    Publiee --> Remplacee : publication d'une version postérieure
    Remplacee --> [*]

    state "En vérification" as EnVerification
    state "Publiée" as Publiee
    state "Remplacée" as Remplacee
```

Les types de champ et les listes de valeurs suivent le cycle plus simple
`Brouillon → Publié → Obsolète`. Un type obsolète reste valable pour les champs qui l'utilisent
déjà, mais ne peut plus être choisi pour un nouveau champ.

## 11.5 Séquence : créer un type de champ et l'utiliser dans le registre

```mermaid
sequenceDiagram
    autonumber
    actor ADM as Administrateur (back-office)
    participant BO as Back-office (constructeur de formulaires)
    participant API as API
    participant FORM as Module Formulaires
    participant REF as Module Référentiels
    participant DB as PostgreSQL

    ADM->>BO: nouveau type « Durée en mois »
    BO->>BO: choisir la primitive Nombre,<br/>min 1, max 600, 0 décimale, unité « mois »
    BO->>API: POST /formulaires/types
    API->>FORM: valider les contraintes (cohérence min/max, motif testé)
    FORM->>DB: INSERT type_champ (Brouillon)
    ADM->>BO: publier le type
    FORM->>DB: type_champ → Publié

    ADM->>BO: ouvrir le formulaire « Fiche de traitement »
    BO->>API: POST /formulaires/fiche_traitement/versions (nouvelle version)
    FORM->>DB: copie de la version publiée → Brouillon
    ADM->>BO: ajouter le champ t.duree_archivage<br/>(type « Durée en mois », bloc 2, obligatoire au Bénin)
    BO->>BO: aperçu en direct du formulaire
    ADM->>BO: demander la publication
    API->>FORM: ControleurPublication.Verifier(version)
    FORM->>REF: champs et codes de valeurs cités par les référentiels publiés
    REF-->>FORM: usages (questions, critères AIPD, conditions bloquantes)
    FORM->>FORM: champs verrouillés intacts ? codes stables ?<br/>conditions valides ? types publiés ?
    alt contrôle réussi
        FORM->>DB: version → Publiée, précédente → Remplacée
        FORM-->>BO: publiée, les nouvelles fiches l'utilisent
    else anomalies
        FORM-->>BO: rapport : liste des anomalies bloquantes
    end
```

## 11.6 Séquence : saisie d'une fiche avec un formulaire dynamique

```mermaid
sequenceDiagram
    autonumber
    actor U as Contributeur
    participant FE as Front (rendu dynamique)
    participant API as API
    participant FORM as Module Formulaires
    participant REG as Module Registre
    participant MOT as Wade.Moteur

    U->>FE: ouvrir une fiche
    FE->>API: GET /fiches/{id}
    API->>REG: fiche + VersionFormulaireId
    API->>FORM: définition de la version (blocs, champs, types, listes, exigences)
    API-->>FE: valeurs + définition (mise en cache par version)
    FE->>FE: pour chaque champ : composant de la primitive,<br/>contraintes du type, conditions d'affichage
    U->>FE: saisir
    FE->>FE: validation immédiate côté client (même règles)
    FE->>API: PATCH /fiches/{id}/valeurs
    API->>FORM: ValidateurDynamique.Valider(version, valeurs, juridiction)
    FORM-->>API: erreurs par champ + taux de complétude
    API->>REG: enregistrer (JSONB) si valide
    opt champ utilisé par le moteur
        API->>MOT: qualification provisoire (voir 6.1)
    end
    API-->>FE: 200 + complétude + résultat provisoire
```

## 11.7 Flux de validation d'une valeur

Le même algorithme sert côté serveur (C#) et côté client (TypeScript). Il est piloté uniquement
par la configuration.

```mermaid
flowchart LR
    V(["Valeur saisie pour le champ C"]) --> A{"C visible ?<br/>(condition d'affichage)"}
    A -->|"non"| IGN["Ignorée<br/>(non stockée)"]
    A -->|"oui"| E{"Exigence de C pour<br/>la juridiction"}
    E -->|"Obligatoire, ou Conditionnel<br/>avec condition vraie"| VIDE{"Valeur vide ?"}
    E -->|"Recommandé ou facultatif"| VIDE2{"Valeur vide ?"}
    VIDE -->|"oui"| ERR1["Erreur : champ obligatoire"]
    VIDE -->|"non"| PRIM
    VIDE2 -->|"oui"| OKV["Valide<br/>(recommandé : avertissement)"]
    VIDE2 -->|"non"| PRIM
    PRIM["Contrôle de la primitive<br/>type JSON attendu"] --> CONT["Contrôle des contraintes du type<br/>longueur, motif, bornes, décimales,<br/>extensions, taille, sélections"]
    CONT --> LIST{"Choix ?"}
    LIST -->|"oui"| LV["Code présent dans la liste<br/>et valeur active"]
    LIST -->|"non"| COMP
    LV --> COMP{"Groupe ou<br/>Collection ?"}
    COMP -->|"oui"| REC["Valider chaque sous-champ<br/>(récursif) + lignes min/max"]
    COMP -->|"non"| OK(["Valide"])
    REC --> OK
```

## 11.8 Tables PostgreSQL du module Formulaires

```mermaid
erDiagram
    formulaire_type_champ {
        uuid id PK
        text code
        int version
        text libelle
        text primitive
        jsonb contraintes
        uuid liste_valeurs_id FK
        text entite_referencee
        text portee
        text cible
        text statut
        bool est_systeme
    }
    formulaire_liste_valeurs {
        uuid id PK
        text code
        int version
        text libelle
        text portee
        text cible
        bool hierarchique
        text statut
    }
    formulaire_valeur_liste {
        uuid liste_id PK
        text code PK
        text libelle
        int ordre
        bool active
        text code_parent
        jsonb attributs
    }
    formulaire_formulaire {
        uuid id PK
        text code UK
        text libelle
        text objet_cible
        bool extensible_par_organisation
    }
    formulaire_version {
        uuid id PK
        uuid formulaire_id FK
        int numero
        text statut
        timestamptz publiee_le
        uuid publiee_par
    }
    formulaire_bloc {
        uuid version_id PK
        text code PK
        text libelle
        int ordre
        jsonb condition_affichage
    }
    formulaire_champ {
        uuid id PK
        uuid version_id FK
        text code
        text libelle
        uuid type_champ_id FK
        text bloc_code
        int ordre
        text code_parent
        jsonb valeur_defaut
        text aide_code
        bool export_registre
        bool indexable
        bool verrouille
        text_array juridictions
        text portee
        text cible
        jsonb condition_affichage
    }
    formulaire_exigence {
        uuid champ_id PK
        text juridiction_code PK
        char exigence
        jsonb condition
    }
    formulaire_usage_champ {
        text champ_code PK
        text consommateur PK
        text reference PK
        text_array codes_valeurs
    }

    formulaire_liste_valeurs ||--o{ formulaire_valeur_liste : ""
    formulaire_liste_valeurs |o--o{ formulaire_type_champ : "valeurs admises"
    formulaire_formulaire ||--o{ formulaire_version : ""
    formulaire_version ||--o{ formulaire_bloc : ""
    formulaire_version ||--o{ formulaire_champ : ""
    formulaire_type_champ ||--o{ formulaire_champ : "de type"
    formulaire_champ ||--o{ formulaire_exigence : ""
    formulaire_champ |o--o{ formulaire_champ : "sous-champs"
```

Contraintes et index :

- `UNIQUE (code, version)` sur les types et les listes ; `UNIQUE (version_id, code)` sur les champs.
- Un seul `formulaire_version` au statut `Publiee` par formulaire **et par organisation** pour les extensions (index unique partiel).
- Les valeurs restent dans `registre_fiche.valeurs` (JSONB), indexées par code de champ. Les champs marqués `Indexable` sont couverts par l'index GIN `jsonb_path_ops` ; aucune colonne n'est créée dynamiquement, il n'y a donc **jamais de migration de schéma** quand un administrateur ajoute un champ.
- `registre_fiche` et `acces_organisation` portent `version_formulaire_id`.

## 11.9 Conséquences sur les autres modules

| Module | Conséquence |
|---|---|
| Référentiels | Ne définissent plus les champs : ils les citent par **code**. La publication d'un référentiel vérifie que chaque code cité existe dans le formulaire publié avec une primitive compatible (booléen pour une question `booleen`, choix multiple pour `multiple`, codes d'options présents). |
| Moteur | Inchangé : il lit des valeurs par code. Seul le résolveur de champ calculé (`personne_publique_ou_mission_service_public`, écart n° 2) devient un champ de type « Calculé » ou une règle déclarée dans le référentiel. |
| Documents | Les modèles Word citent les champs par code (`{{t.finalites}}`). Une section générique « Autres informations » liste automatiquement les champs ajoutés et marqués `ExportRegistre`, sans modifier le modèle. |
| Indice | La complétude du registre est calculée par le `ValidateurDynamique` sur les exigences de la version en vigueur. |
| Front | Un composant par primitive et un moteur de rendu générique. Le constructeur de formulaires du back-office (glisser-déposer des champs, aperçu en direct) utilise ce même rendu. |
| Journal | Toute création ou publication de type, liste, champ ou version est journalisée comme les autres actions. |

## 11.10 Décisions à confirmer

1. **Les organisations peuvent-elles créer leurs propres champs et types ?** La modélisation le permet (portée « Organisation », formulaire `ExtensibleParOrganisation`), cantonné à un bloc « Informations complémentaires » qui n'alimente jamais le moteur. À désactiver si seul AMELEGAL doit configurer.
2. **Quels formulaires sont configurables ?** Proposé : fiche de traitement, organisation, déclaration de violation, sections d'AIPD, dossier de formalité. Les écrans de gouvernance (mandats, rôles) restent fixes, car leurs règles relèvent du contrôle d'accès.
3. **Faut-il une primitive « Calculé »** (valeur dérivée d'autres champs par une expression), pour des cas comme `personne_publique_ou_mission_service_public` ? C'est la seule extension qui introduirait un petit langage d'expressions ; l'alternative est de déclarer ces dérivations dans le référentiel juridique.
