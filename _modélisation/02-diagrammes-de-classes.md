# 2. Diagrammes de classes du domaine

Conventions : types C# (.NET 10). `Guid` pour les identifiants techniques ; les codes métier
(`TG-DECLARATION`, `BJ-Q8`, `AL-03`…) sont des `string` **stables**, jamais des valeurs codées en dur.
Les noms de classes sont sans accents pour rester utilisables tels quels dans le code.
Le domaine est découpé en six paquets, qui correspondent aux modules de la solution .NET.

```mermaid
flowchart LR
    ID["Organisations<br/>& accès"] --> REG["Registre &<br/>qualification"]
    REF["Référentiels"] --> REG
    REG --> FOR["Formalités"]
    REG --> AIP["AIPD"]
    ID --> VIO["Violations"]
    REF --> FOR & AIP & VIO
    REG & FOR & AIP & VIO --> PIL["Pilotage<br/>(tâches, alertes, indice, journal)"]
```

## 2.1 Organisations, cabinets, utilisateurs et mandats

```mermaid
classDiagram
    direction TB
    class Utilisateur {
        +Guid Id
        +string Courriel
        +string NomComplet
        +bool DoubleAuthActive
        +bool Actif
        +DateTimeOffset? DerniereConnexion
    }
    class Organisation {
        +Guid Id
        +string Denomination
        +string FormeJuridique
        +string IdentifiantFiscal
        +string Rccm
        +string Adresse
        +string Secteur
        +string TrancheEffectif
        +string PaysEtablissement
        +bool NaturePublique
        +bool MissionServicePublic
        +bool VisaActive
        +bool CircuitFusionne
        +Guid? GroupeParentId
        +Guid VersionFormulaireId
        +JsonDocument ValeursComplementaires
    }
    class ServiceDirection {
        +Guid Id
        +string Libelle
        +Guid? ParentId
    }
    class MembreOrganisation {
        +Guid UtilisateurId
        +Guid OrganisationId
        +Set~RoleOrganisation~ Roles
        +List~Guid~ PerimetreServices
    }
    class RoleOrganisation {
        <<enumeration>>
        AdministrateurOrganisation
        Correspondant
        ResponsableTraitement
        ContributeurMetier
        LecteurAuditeur
    }
    class ResponsableTraitementLegal {
        +string Nom
        +string Fonction
        +string Adresse
        +string Telephone
        +string Courriel
    }
    class DesignationCorrespondant {
        +bool Designe
        +string Nom
        +string Fonction
        +StatutCorrespondant Statut
        +DateOnly? DateDesignation
        +Guid? JustificatifId
    }
    class Cabinet {
        +Guid Id
        +string Denomination
        +Guid OrganisationPropreId
        +bool AccesDossierPropreOuvert
    }
    class MembreCabinet {
        +Guid UtilisateurId
        +Guid CabinetId
        +RoleCabinet Role
    }
    class RoleCabinet {
        <<enumeration>>
        AdministrateurCabinet
        ConsultantReferent
        ConsultantContributeur
        ConsultantLecteur
    }
    class Mandat {
        +Guid Id
        +Guid OrganisationId
        +Guid CabinetId
        +NiveauMandat Niveau
        +PorteeMandat Portee
        +List~Guid~ ServicesOuEntites
        +DateOnly DateDebut
        +DateOnly? DateFin
        +StatutMandat Statut
        +Set~ActionReservable~ ActionsReservees
        +Guid? AccepteParId
        +DateTimeOffset? AccepteLe
    }
    class NiveauMandat {
        <<enumeration>>
        Consultation
        Contribution
        PilotageComplet
    }
    class ActionReservable {
        <<enumeration>>
        VisaAvantDepot
        NotificationViolation
        RevocationMandat
    }
    class AffectationConsultant {
        +Guid MandatId
        +Guid UtilisateurId
        +bool OpposeeParOrganisation
        +DateTimeOffset AffecteLe
    }

    Utilisateur "1" -- "0..1" MembreOrganisation : rattaché à
    Utilisateur "1" -- "0..1" MembreCabinet : ou rattaché à
    Organisation "1" *-- "*" MembreOrganisation
    Organisation "1" *-- "*" ServiceDirection
    Organisation "1" *-- "1" ResponsableTraitementLegal
    Organisation "1" *-- "1" DesignationCorrespondant
    Organisation "0..1" o-- "*" Organisation : groupe / entités
    MembreOrganisation ..> RoleOrganisation
    Cabinet "1" *-- "*" MembreCabinet
    Cabinet "1" -- "1" Organisation : dossier propre
    MembreCabinet ..> RoleCabinet
    Organisation "1" -- "*" Mandat : consent
    Cabinet "1" -- "*" Mandat : reçoit
    Mandat ..> NiveauMandat
    Mandat ..> ActionReservable
    Mandat "1" *-- "*" AffectationConsultant
    AffectationConsultant "*" -- "1" MembreCabinet
```

**Invariants à garantir côté serveur**

- Un utilisateur est rattaché à **une seule** organisation **ou** à un seul cabinet (G04).
- `DesignationCorrespondant` est la désignation **légale**, distincte du rôle applicatif `Correspondant`. Seule la désignation alimente le moteur (FAQ H01, note TG-Q3).
- Un consultant agit chez un client seulement si le mandat est `Actif` **et** s'il y est nominativement affecté. Les deux conditions sont vérifiées à chaque requête (G05).
- Droits effectifs = rôle de cabinet ∩ plafond du niveau de mandat ∩ périmètre, moins les actions réservées. Le plus restrictif l'emporte (voir le flux 4.3).

## 2.2 Référentiels de juridiction

Le référentiel est stocké en JSONB dans `ReferentielVersion.Contenu`, validé par un schéma JSON,
puis désérialisé dans le modèle typé ci-dessous, en lecture seule, que consomme le moteur.

```mermaid
classDiagram
    direction TB
    class Juridiction {
        +string Code
        +string Nom
        +string NomOfficiel
        +string Langue
        +string SocleRegional
        +bool HeriteDuSocle
    }
    class ReferentielVersion {
        +Guid Id
        +string JuridictionCode
        +string Numero
        +StatutReferentiel Statut
        +DateOnly DateVersion
        +DateTimeOffset? PublieLe
        +string Avertissement
        +JsonDocument Contenu
        +string Empreinte
    }
    class StatutReferentiel {
        <<enumeration>>
        Brouillon
        EnSimulation
        Publie
        Remplace
    }
    class Referentiel {
        +Sources Sources
        +ParametresAutorite Autorite
        +Dictionary~string,string~ Terminologie
        +List~Regime~ Regimes
        +Logigramme Logigramme
        +Dictionary~string,List~EtapeFeuilleDeRoute~~ FeuillesDeRoute
        +ConfigAipd Aipd
        +ConfigViolation Violations
        +ConfigCorrespondant Correspondant
        +ConfigTransferts Transferts
        +ConfigIndice Indice
    }
    class Regime {
        +string Id
        +string Libelle
        +string IntituleOfficiel
        +string FamilleCouleur
        +int Ordre
        +string Fondement
        +bool EstUnRegimeDeFormalite
    }
    class Logigramme {
        +string Entree
        +string Principe
        +List~Question~ Questions
        +List~RegleTransverse~ ReglesTransverses
        +EcartTextePratique? Ecart
    }
    class Question {
        +string Id
        +int Ordre
        +string Libelle
        +string Champ
        +TypeQuestion Type
        +List~string~ Options
        +string AideId
        +string Fondement
        +ConditionBloquante? ConditionBloquante
        +Branche Oui
        +Branche Non
    }
    class Branche {
        +TypeBranche Type
        +string Cible
        +string? Motif
    }
    class TypeBranche {
        <<enumeration>>
        Question
        Sortie
    }
    class ConditionBloquante {
        +string Champ
        +JsonElement Valeur
        +string Effet
    }
    class RegleTransverse {
        +string Id
        +string Libelle
        +string Fondement
        +string Regle
    }
    class EtapeFeuilleDeRoute {
        +int Ordre
        +string Etape
        +List~string~ Pieces
    }
    class ParametresAutorite {
        +string Denomination
        +string Sigle
        +List~ModaliteDepot~ ModalitesDepot
        +List~DelaiInstruction~ DelaisInstruction
        +bool SilenceVautAcceptation
        +int? ValiditeDecisionMois
    }
    class DelaiInstruction {
        +string Regime
        +string? Delai
        +string? Prorogeable
        +string? Condition
        +string Fondement
    }
    class ConfigAipd {
        +List~CritereAipd~ Criteres
        +List~string~ PresomptionRegimes
        +ConsultationPrealable? Consultation
        +List~SectionGrille~ Grille
    }
    class CritereAipd {
        +string Id
        +string Libelle
        +string Champ
        +decimal? Seuil
        +string Source
    }
    class ConfigViolation {
        +int DelaiNotificationHeures
        +string PointDeDepart
        +string Destinataire
        +List~NoeudViolation~ Arbre
        +List~decimal~ RappelsProportionDelai
    }
    class NoeudViolation {
        +string Id
        +string Libelle
        +BrancheViolation Oui
        +BrancheViolation Non
    }
    class ConfigIndice {
        +List~ComposanteIndice~ Composantes
        +List~SeuilIndice~ Seuils
    }
    class BulleInformation {
        +string Id
        +string? JuridictionCode
        +string Titre
        +string Texte
        +string? LienFiche
    }

    Juridiction "1" -- "*" ReferentielVersion
    ReferentielVersion ..> StatutReferentiel
    ReferentielVersion "1" --> "1" Referentiel : désérialisé en
    Referentiel *-- Regime
    Referentiel *-- Logigramme
    Referentiel *-- ParametresAutorite
    Referentiel *-- ConfigAipd
    Referentiel *-- ConfigViolation
    Referentiel *-- ConfigIndice
    Referentiel *-- EtapeFeuilleDeRoute
    Logigramme *-- Question
    Logigramme *-- RegleTransverse
    Question *-- "2" Branche
    Question *-- "0..1" ConditionBloquante
    Branche ..> TypeBranche
    Branche ..> Regime : cible si Sortie
    ParametresAutorite *-- DelaiInstruction
    ConfigAipd *-- CritereAipd
    ConfigViolation *-- NoeudViolation
    Juridiction "1" -- "*" ExigenceChamp
    Question ..> DefinitionChamp : Champ alimente
    DefinitionChamp ..> BulleInformation : AideCode
```

> Les **champs** et leurs **types** ne font plus partie du référentiel juridique : ils sont créés
> dans l'application et versionnés par le module Formulaires (section 2.7 et fichier 11). Le
> référentiel ne fait que les **désigner par leur code** (`Question.Champ`, `CritereAipd.Champ`).

## 2.3 Registre et qualification

```mermaid
classDiagram
    direction TB
    class FicheTraitement {
        +Guid Id
        +Guid OrganisationId
        +string Reference
        +string Nom
        +List~string~ Juridictions
        +Guid? ServiceId
        +StatutFiche Statut
        +Guid VersionFormulaireId
        +JsonDocument Valeurs
        +decimal TauxCompletude
        +DateOnly? DerniereRevue
        +DateOnly? ProchaineRevue
        +int NumeroVersion
        +string? OrigineCartographie
        +Soumettre()
        +Qualifier(Qualification q)
        +Viser(Guid responsableId)
        +Publier()
        +MarquerAReviser(string motif)
        +Archiver()
    }
    class StatutFiche {
        <<enumeration>>
        Brouillon
        SoumiseAQualification
        Qualifiee
        Visee
        PublieeAuRegistre
        AReviser
        Archivee
    }
    class VersionFichePubliee {
        +Guid Id
        +Guid FicheId
        +int NumeroVersion
        +JsonDocument Instantane
        +DateTimeOffset PublieeLe
        +bool ModificationSubstantielle
    }
    class Qualification {
        +Guid Id
        +Guid FicheId
        +Guid ReferentielVersionId
        +string JuridictionCode
        +VoieQualification Voie
        +JsonDocument Reponses
        +List~EtapeChemin~ Chemin
        +string RegimeMoteur
        +List~string~ Motifs
        +bool AipdRequise
        +List~string~ CriteresAipdReunis
        +List~string~ ReglesTransversesDeclenchees
        +string RegimeRetenu
        +string? MotifEcart
        +Guid AuteurId
        +Guid? MandatId
        +DateTimeOffset QualifieeLe
        +bool EstCourante
    }
    class VoieQualification {
        <<enumeration>>
        DepuisLaFiche
        AssistantPasAPas
    }
    class EtapeChemin {
        +string QuestionId
        +bool Reponse
        +bool ForceeParConditionBloquante
        +string? Motif
    }
    class Prestataire {
        +Guid Id
        +Guid OrganisationId
        +string Denomination
        +string Pays
    }
    class SousTraitanceFiche {
        +Guid FicheId
        +Guid PrestataireId
        +string Prestation
        +bool ContratConforme
        +Guid? ContratId
    }
    class TransfertFiche {
        +Guid FicheId
        +string PaysDestination
        +string Destinataire
        +string? Garantie
        +bool PaysReconnu
    }
    class PieceJointe {
        +Guid Id
        +Guid OrganisationId
        +string NomFichier
        +string TypeMime
        +long Taille
        +string CleStockage
        +string EmpreinteSha256
    }

    FicheTraitement ..> StatutFiche
    FicheTraitement "1" *-- "*" VersionFichePubliee
    FicheTraitement "1" *-- "*" Qualification : historique
    Qualification ..> VoieQualification
    Qualification "1" *-- "*" EtapeChemin
    Qualification "*" --> "1" ReferentielVersion : version figée
    FicheTraitement "1" *-- "*" SousTraitanceFiche
    SousTraitanceFiche "*" --> "1" Prestataire
    FicheTraitement "1" *-- "*" TransfertFiche
    FicheTraitement "1" o-- "*" PieceJointe
    FicheTraitement ..> DefinitionChamp : Valeurs[code]
```

**Points clés**

- `Valeurs` (JSONB) contient les champs de niveau traitement, indexés par `DefinitionChamp.Code` (`t.finalites`, `t.donnees_sensibles`…). Les champs de niveau organisation sont lus sur `Organisation` et recopiés dans l'instantané à la publication.
- Les tableaux qui nourrissent les alertes, à savoir les sous-traitants (AL-06) et les transferts (AL-07), sont des entités à part entière, interrogeables par requête. Les autres tableaux (catégories de données, durées, accès internes, droits) restent dans le JSONB.
- Un traitement peut relever de **plusieurs juridictions** (note du champ `t.juridiction`). Il reçoit alors une qualification courante **par juridiction**, avec unicité sur (fiche, juridiction) pour `EstCourante`, et autant de dossiers que nécessaire.
- Une `Qualification` n'est **jamais modifiée** : chaque requalification crée une nouvelle ligne, et `EstCourante` désigne la dernière. Elle référence la `ReferentielVersion` exacte, ce qui la rend explicable même après publication d'une nouvelle version.
- `RegimeRetenu ≠ RegimeMoteur` impose `MotifEcart` et déclenche la règle BJ-T3 (proposition de consulter l'APDP).

## 2.4 Formalités, analyses d'impact et violations

```mermaid
classDiagram
    direction TB
    class DossierFormalite {
        +Guid Id
        +Guid OrganisationId
        +Guid FicheId
        +Guid QualificationId
        +string RegimeCode
        +TypeDossier Type
        +StatutDossier Statut
        +string? CanalDepot
        +DateTimeOffset? EnvoyeLe
        +DateTimeOffset? AccuseReceptionLe
        +int? DelaiInstructionJours
        +int Prorogations
        +bool InvestigationEnCours
        +DateOnly? EcheanceInstruction
        +string? ReferenceRecepisseOuDecision
        +DateOnly? DateDecision
        +DateOnly? ValideJusquau
        +CalculerEcheance(ParametresAutorite p)
    }
    class TypeDossier {
        <<enumeration>>
        Formalite
        ConsultationPrealable
        NouvelleDeclaration
        Renouvellement
    }
    class StatutDossier {
        <<enumeration>>
        Brouillon
        AValider
        PreteATransmettre
        Envoyee
        AccuseReceptionRecu
        ObservationsRecues
        EnCoursDeTraitement
        Acceptee
        AcceptationTacite
        Rejetee
        ARegulariser
    }
    class JalonDossier {
        +Guid Id
        +DateTimeOffset Date
        +string Type
        +string? Commentaire
        +Guid? PieceJointeId
    }
    class DocumentProduit {
        +Guid Id
        +string Modele
        +string Format
        +Guid ReferentielVersionId
        +Guid PieceJointeId
        +DateTimeOffset GenereLe
        +Guid GenerePar
    }
    class AnalyseImpact {
        +Guid Id
        +Guid FicheId
        +StatutAipd Statut
        +List~string~ CriteresDeclencheurs
        +int? NiveauRisqueInitial
        +int? NiveauRisqueResiduel
        +bool ConsultationPrealableRequise
        +Guid? ValideeParId
        +DateTimeOffset? ValideeLe
    }
    class SectionAipd {
        +int Numero
        +string Titre
        +string Contenu
        +List~Guid~ Contributeurs
    }
    class RisqueAipd {
        +Guid Id
        +string Libelle
        +int Gravite
        +int Vraisemblance
        +string Mesures
        +int GraviteResiduelle
        +int VraisemblanceResiduelle
    }
    class InvitationAipd {
        +Guid UtilisateurId
        +int Section
        +DateTimeOffset InviteLe
    }
    class Violation {
        +Guid Id
        +Guid OrganisationId
        +string JuridictionCode
        +DateTimeOffset ConnaissanceLe
        +DateTimeOffset DeclareeLe
        +Guid DeclarantId
        +string Description
        +Set~NatureViolation~ Natures
        +List~Guid~ FichesConcernees
        +int? NombrePersonnes
        +StatutViolation Statut
        +bool? RisqueExiste
        +bool? RisqueEleve
        +bool NotificationAutoriteRequise
        +bool InformationPersonnesRequise
        +DateTimeOffset? EcheanceNotification
        +DateTimeOffset? NotifieeLe
        +DateTimeOffset? PersonnesInformeesLe
        +string? MesuresPrises
        +DateTimeOffset? CloseLe
    }
    class NatureViolation {
        <<enumeration>>
        Confidentialite
        Integrite
        Disponibilite
    }
    class StatutViolation {
        <<enumeration>>
        Declaree
        EnCoursDeQualification
        Notifiee
        NonNotifiable
        EnCoursDeTraitement
        Resolue
        CloseEtArchivee
    }
    class StatutAipd {
        <<enumeration>>
        ARealiser
        EnCours
        SoumiseAValidation
        Validee
        AReviser
    }

    FicheTraitement "1" -- "*" DossierFormalite
    Qualification "1" -- "*" DossierFormalite : fonde
    DossierFormalite ..> TypeDossier
    DossierFormalite ..> StatutDossier
    DossierFormalite "1" *-- "*" JalonDossier
    DossierFormalite "1" o-- "*" DocumentProduit
    FicheTraitement "1" -- "*" AnalyseImpact
    AnalyseImpact ..> StatutAipd
    AnalyseImpact "1" *-- "4" SectionAipd
    AnalyseImpact "1" *-- "*" RisqueAipd
    AnalyseImpact "1" *-- "*" InvitationAipd
    AnalyseImpact "0..1" -- "0..1" DossierFormalite : consultation préalable
    Violation ..> StatutViolation
    Violation ..> NatureViolation
    Violation "*" -- "*" FicheTraitement : concerne
    Violation "1" o-- "*" DocumentProduit : notification E05
```

## 2.5 Pilotage : tâches, alertes, paramètres, indice et journal

```mermaid
classDiagram
    direction TB
    class DefinitionAlerte {
        +string Code
        +string Objet
        +string FaitGenerateur
        +string Declenchement
        +string Rappel
        +CanalAlerte Canal
        +int Urgence
        +string ModeleLibelle
        +bool ParametrableOrganisation
    }
    class OccurrenceAlerte {
        +Guid Id
        +string Code
        +Guid OrganisationId
        +string ObjetType
        +Guid ObjetId
        +DateTimeOffset DeclencheeLe
        +DateTimeOffset? Echeance
        +DateTimeOffset? DernierRappel
        +bool Resolue
    }
    class Tache {
        +Guid Id
        +Guid OrganisationId
        +string Titre
        +OrigineTache Origine
        +string? ObjetType
        +Guid? ObjetId
        +Guid? AssigneeAId
        +DateOnly? Echeance
        +StatutTache Statut
        +string? Justification
    }
    class StatutTache {
        <<enumeration>>
        AFaire
        EnCours
        Terminee
        IgnoreeAvecJustification
    }
    class Notification {
        +Guid Id
        +Guid DestinataireId
        +CanalAlerte Canal
        +string Message
        +DateTimeOffset EnvoyeeLe
        +DateTimeOffset? LueLe
    }
    class Parametre {
        +string Cle
        +PorteeParametre Portee
        +string? Cible
        +JsonElement Valeur
        +Guid ModifieParId
        +DateTimeOffset ModifieLe
    }
    class PorteeParametre {
        <<enumeration>>
        Global
        Juridiction
        Organisation
    }
    class InstantaneIndice {
        +Guid OrganisationId
        +DateTimeOffset CalculeLe
        +decimal Valeur
        +string Libelle
        +JsonDocument DetailComposantes
    }
    class EntreeJournal {
        +long Sequence
        +Guid OrganisationId
        +DateTimeOffset Horodatage
        +Guid ActeurId
        +Guid? CabinetId
        +Guid? MandatId
        +bool InterventionSupport
        +string Action
        +string ObjetType
        +Guid ObjetId
        +JsonDocument? Avant
        +JsonDocument? Apres
        +string AdresseIp
        +string EmpreintePrecedente
        +string Empreinte
    }

    DefinitionAlerte "1" -- "*" OccurrenceAlerte
    OccurrenceAlerte "1" --> "*" Notification : émet
    OccurrenceAlerte "0..1" --> "0..1" Tache : peut créer
    Tache ..> StatutTache
    Parametre ..> PorteeParametre
```

**Règles portées par ces classes**

- `Parametre` est résolu de la portée la plus fine à la plus large : organisation, puis juridiction, puis global. Une valeur d'organisation **ne peut être moins protectrice** que celle de la juridiction (G07). Ce contrôle est fait à l'écriture.
- `EntreeJournal` est en **ajout seul**. `Empreinte = SHA-256(EmpreintePrecedente + contenu canonique)`, avec une chaîne par organisation. Toute altération rompt la chaîne et devient détectable.
- `InstantaneIndice` est recalculé à chaque événement qui l'affecte (publication, décision, AIPD validée, violation close). Les instantanés sont historisés pour tracer les courbes d'évolution.

## 2.6 Compléments : énumérations et objets-valeur

Types référencés par les diagrammes précédents et non détaillés plus haut.

```mermaid
classDiagram
    direction TB
    class StatutMandat {
        <<enumeration>>
        Demande
        Accepte
        Refuse
        Actif
        Suspendu
        Revoque
        Expire
    }
    class PorteeMandat {
        <<enumeration>>
        TouteLOrganisation
        ServicesOuDirections
        EntitesDuGroupe
    }
    class StatutCorrespondant {
        <<enumeration>>
        Interne
        Externe
    }
    class TypeQuestion {
        <<enumeration>>
        Booleen
        Multiple
    }
    class CanalAlerte {
        <<enumeration>>
        Application
        ApplicationEtCourriel
    }
    class OrigineTache {
        <<enumeration>>
        Alerte
        RegleTransverse
        FeuilleDeRoute
        Manuelle
    }
    class Sources {
        +TextePrincipal TextePrincipal
        +string EtatTextesApplication
        +List~ArticleCle~ ArticlesCles
        +List~string~ DoctrineAutorite
    }
    class ArticleCle {
        +string Art
        +string Objet
    }
    class ModaliteDepot {
        +string Canal
        +string? Fondement
    }
    class EcartTextePratique {
        +List~string~ SortiesConcernees
        +string Constat
        +string RegleAffichage
    }
    class ConfigCorrespondant {
        +string Denomination
        +bool DesignationObligatoire
        +string Fondement
        +string EffetSurFormalites
        +string Piece
        +string RegleMoteur
    }
    class ConfigTransferts {
        +string Principe
        +List~string~ PaysReconnus
        +string Piece
        +string FormaliteAssociee
    }
    class ConsultationPrealable {
        +string Fondement
        +string Declencheur
        +string DelaiReponse
        +string EffetMoteur
    }
    class SectionGrille {
        +int Section
        +string Titre
        +string Contenu
    }
    class BrancheViolation {
        +string Type
        +string? Cible
        +bool? NotificationAutorite
        +bool? InformationPersonnes
        +string? Motif
    }
    class ComposanteIndice {
        +string Code
        +string Libelle
        +decimal Poids
    }
    class SeuilIndice {
        +string Libelle
        +int Min
        +int Max
    }
    class ResultatQualification {
        +string JuridictionCode
        +string VersionReferentiel
        +string RegimeId
        +List~string~ Motifs
        +List~EtapeChemin~ Chemin
        +bool AipdRequise
        +List~string~ CriteresAipdReunis
        +List~string~ ReglesTransverses
        +string AutoriteSigle
        +List~EtapeFeuilleDeRoute~ FeuilleDeRoute
        +string ReserveInterpretation
    }
    class MoteurQualification {
        <<service>>
        +Qualifier(Referentiel r, ValeursFiche v, DonneesOrganisation o) ResultatQualification
        +EvaluerViolation(ConfigViolation c, bool risque, bool risqueEleve) BrancheViolation
        +CalculerIndice(ConfigIndice c, MesuresIndice m) InstantaneIndice
    }

    Sources *-- ArticleCle
    ConfigAipd *-- ConsultationPrealable
    ConfigAipd *-- SectionGrille
    ConfigIndice *-- ComposanteIndice
    ConfigIndice *-- SeuilIndice
    NoeudViolation *-- "2" BrancheViolation
    ParametresAutorite *-- ModaliteDepot
    Logigramme *-- "0..1" EcartTextePratique
    Referentiel *-- Sources
    Referentiel *-- ConfigCorrespondant
    Referentiel *-- ConfigTransferts
    MoteurQualification ..> Referentiel : lit
    MoteurQualification ..> ResultatQualification : produit
    Mandat ..> StatutMandat
    Mandat ..> PorteeMandat
    DesignationCorrespondant ..> StatutCorrespondant
    Question ..> TypeQuestion
    DefinitionAlerte ..> CanalAlerte
    Tache ..> OrigineTache
```

## 2.7 Formulaires configurables : types et champs créés dans l'application

Aucun champ ni aucun type de champ n'est codé en dur. Un administrateur les crée dans
l'application, les assemble en formulaires versionnés, puis les publie. Seules les **primitives**
(le comportement de base : saisir du texte, un nombre, une date, choisir dans une liste…) existent
dans le code, car chacune exige un composant d'affichage et un validateur. Le détail, les exemples
et les garde-fous sont dans le fichier 11.

```mermaid
classDiagram
    direction TB
    class Primitive {
        <<enumeration>>
        Texte
        TexteLong
        Nombre
        Booleen
        Date
        DateHeure
        Choix
        ChoixMultiple
        Fichier
        Reference
        Groupe
        Collection
    }
    class PorteeConfiguration {
        <<enumeration>>
        Plateforme
        Juridiction
        Organisation
    }
    class StatutConfiguration {
        <<enumeration>>
        Brouillon
        Publie
        Obsolete
    }
    class TypeChamp {
        +Guid Id
        +string Code
        +string Libelle
        +string? Description
        +Primitive Primitive
        +ContraintesType Contraintes
        +Guid? ListeValeursId
        +string? EntiteReferencee
        +string? MasqueSaisie
        +string? MessageErreur
        +PorteeConfiguration Portee
        +string? Cible
        +StatutConfiguration Statut
        +int Version
        +bool EstSysteme
    }
    class ContraintesType {
        +int? LongueurMin
        +int? LongueurMax
        +string? Motif
        +string? Format
        +decimal? Min
        +decimal? Max
        +int? Decimales
        +string? Unite
        +int? SelectionsMax
        +List~string~ ExtensionsAutorisees
        +int? TailleMaxKo
        +int? LignesMin
        +int? LignesMax
    }
    class ListeValeurs {
        +Guid Id
        +string Code
        +string Libelle
        +PorteeConfiguration Portee
        +string? Cible
        +bool Hierarchique
        +StatutConfiguration Statut
        +int Version
    }
    class ValeurListe {
        +string Code
        +string Libelle
        +int Ordre
        +bool Active
        +string? CodeParent
        +string? AideCode
    }
    class Formulaire {
        +Guid Id
        +string Code
        +string Libelle
        +string ObjetCible
        +bool ExtensibleParOrganisation
    }
    class VersionFormulaire {
        +Guid Id
        +Guid FormulaireId
        +int Numero
        +StatutVersionFormulaire Statut
        +DateTimeOffset? PublieeLe
        +Guid? PublieeParId
        +string NotesVersion
        +Publier()
    }
    class StatutVersionFormulaire {
        <<enumeration>>
        Brouillon
        EnVerification
        Publiee
        Remplacee
    }
    class BlocFormulaire {
        +string Code
        +string Libelle
        +int Ordre
        +Condition? ConditionAffichage
    }
    class DefinitionChamp {
        +Guid Id
        +string Code
        +string Libelle
        +string? Placeholder
        +Guid TypeChampId
        +int TypeChampVersion
        +string BlocCode
        +int Ordre
        +string? CodeParent
        +JsonElement? ValeurParDefaut
        +string? AideCode
        +bool ExportRegistre
        +bool Indexable
        +bool Verrouille
        +List~string~ Juridictions
        +PorteeConfiguration Portee
        +string? Cible
        +string? RubriqueSocle
        +Condition? ConditionAffichage
        +string? Note
    }
    class ExigenceChamp {
        +string ChampCode
        +string JuridictionCode
        +Exigence Niveau
        +Condition? ConditionExigence
    }
    class Exigence {
        <<enumeration>>
        Obligatoire
        Recommande
        Conditionnel
    }
    class Condition {
        +Combinaison Combinaison
        +List~Clause~ Clauses
    }
    class Clause {
        +string ChampCode
        +Operateur Operateur
        +JsonElement? Valeur
    }
    class Operateur {
        <<enumeration>>
        Egal
        Different
        Contient
        EstRenseigne
        EstVide
        SuperieurOuEgal
        InferieurOuEgal
    }
    class Combinaison {
        <<enumeration>>
        Toutes
        AuMoinsUne
    }
    class UsageChamp {
        +string ChampCode
        +string Consommateur
        +string Reference
        +List~string~ CodesValeursUtilises
    }
    class ValidateurDynamique {
        <<service>>
        +Valider(VersionFormulaire v, JsonDocument valeurs, string juridiction) ResultatValidation
        +CalculerCompletude(VersionFormulaire v, JsonDocument valeurs, string juridiction) decimal
    }
    class ControleurPublication {
        <<service>>
        +Verifier(VersionFormulaire v, List~ReferentielVersion~ referentiels) RapportControle
    }

    TypeChamp ..> Primitive
    TypeChamp *-- ContraintesType
    TypeChamp "*" --> "0..1" ListeValeurs : valeurs admises
    TypeChamp ..> PorteeConfiguration
    TypeChamp ..> StatutConfiguration
    ListeValeurs "1" *-- "*" ValeurListe
    Formulaire "1" *-- "*" VersionFormulaire
    VersionFormulaire ..> StatutVersionFormulaire
    VersionFormulaire "1" *-- "*" BlocFormulaire
    VersionFormulaire "1" *-- "*" DefinitionChamp
    DefinitionChamp "*" --> "1" TypeChamp : de type
    DefinitionChamp "0..1" o-- "*" DefinitionChamp : sous-champs (Groupe, Collection)
    DefinitionChamp "1" *-- "*" ExigenceChamp
    ExigenceChamp ..> Exigence
    DefinitionChamp ..> Condition : affichage
    ExigenceChamp ..> Condition : si Conditionnel
    BlocFormulaire ..> Condition
    Condition *-- Clause
    Condition ..> Combinaison
    Clause ..> Operateur
    DefinitionChamp "1" -- "*" UsageChamp : utilisé par
    ValidateurDynamique ..> VersionFormulaire : lit
    ValidateurDynamique ..> TypeChamp : applique primitive + contraintes
    ControleurPublication ..> UsageChamp : vérifie
```

**Ce qui change par rapport à la modélisation précédente**

- `TypeChamp` n'est plus une énumération : c'est une **entité** créée dans l'application, qui combine une primitive et des contraintes (format, bornes, liste de valeurs, extensions de fichier…).
- `DefinitionChamp` appartient à une **version de formulaire**. Son `Code` (`t.finalites`, `org.secteur`…) est stable d'une version à l'autre ; c'est la clé de stockage des valeurs et la clé utilisée par les référentiels juridiques.
- `FicheTraitement` (et `Organisation` pour les champs de niveau organisation) mémorise la **version du formulaire** avec laquelle ses valeurs ont été saisies.
- `UsageChamp` est calculé à chaque contrôle de publication : il recense qui dépend d'un champ (question du moteur, critère d'AIPD, condition bloquante, modèle de document, indice). Un champ utilisé est `Verrouille` : sa primitive ne peut plus changer et les codes de valeurs dont le moteur dépend ne peuvent pas être supprimés.
