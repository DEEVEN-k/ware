# 13. Traçabilité du diagramme de classes

Pour chaque classe du diagramme, ce document indique **le fichier AMELEGAL d'où elle vient**,
puis, champ par champ, la source citée. Il est **généré** par `outils/generer_tracabilite_classes.py`
à partir des explications du diagramme (`explications/`), qui citent leurs sources.

## 1. Les fichiers du diagramme de classes

| Fichier | Ce qu'il contient |
|---|---|
| `02-diagrammes-de-classes.md` | **Source unique du modèle** : les classes par paquet (2.1 à 2.6), en Mermaid. Toute modification se fait ici. |
| `09-diagramme-classes-complet.md` | Les 90 classes sur une seule vue, générée depuis le fichier 02. |
| `planches/Waɖɛ_Diagramme_de_classes_complet.pdf` / `.svg` / `.png` / `.dot` | La vue complète en grand format (Graphviz), à zoomer. |
| `Waɖɛ_Diagramme_de_classes_explique.pdf` | Chaque classe, champ et relation expliqué, avec la raison de sa présence. |
| `Waɖɛ_Modélisation.drawio` (page 1) | Le diagramme de classes modifiable dans draw.io. |
| `Waɖɛ_Modélisation.pdf` | Le dossier de modélisation complet, dont le chapitre 2. |
| `07-modele-physique-donnees.md` | La traduction des classes en tables PostgreSQL. |
| `explications/acces.py`, `referentiels.py`, `metier.py` | Les explications des classes et des champs. |
| `explications/relations.py` | Les explications des relations. |
| `outils/generer_classes_complet.py`, `generer_explication_classes.py`, `generer_tracabilite_classes.py` | Les générateurs. |
| `13-tracabilite-classes.md` / `Waɖɛ_Tracabilite_diagramme_de_classes.pdf` | Le présent document. |

## 2. Vue d'ensemble : la source de chaque classe

| Module | Classe | Source principale | Autres sources citées |
|---|---|---|---|
| Accès | Utilisateur | G04, H01 | alertes.json |
| Accès | Organisation | C12, G04, registre-champs.csv | F02, G05, référentiels JSON |
| Accès | ServiceDirection | G04, G05 |  |
| Accès | MembreOrganisation | G04 |  |
| Accès | RoleOrganisation | G04 |  |
| Accès | ResponsableTraitementLegal | C12, registre-champs.csv |  |
| Accès | DesignationCorrespondant | C10, registre-champs.csv | H01, référentiels JSON |
| Accès | Cabinet | G04, H05 | E06, H01 |
| Accès | MembreCabinet | G04 |  |
| Accès | RoleCabinet | G04 |  |
| Accès | Mandat | G05 | G03, alertes.json |
| Accès | NiveauMandat | G04, G05 |  |
| Accès | ActionReservable | G05 |  |
| Accès | AffectationConsultant | G04, G05 |  |
| Accès | StatutMandat | G03, G05 |  |
| Accès | PorteeMandat | G05 |  |
| Accès | StatutCorrespondant | C10, registre-champs.csv |  |
| Référentiels de juridiction | Juridiction | C01, Notice d'implémentation | registre-champs.csv |
| Référentiels de juridiction | ReferentielVersion | C15, Notice d'implémentation | référentiels JSON |
| Référentiels de juridiction | StatutReferentiel | C15, G03 | cas de recette |
| Référentiels de juridiction | Referentiel | référentiels JSON, Notice d'implémentation | G01 |
| Référentiels de juridiction | Regime | C05, référentiels JSON |  |
| Référentiels de juridiction | Logigramme | C06, référentiels JSON |  |
| Référentiels de juridiction | Question | C06, référentiels JSON | bulles-information.json |
| Référentiels de juridiction | Branche | C06, référentiels JSON |  |
| Référentiels de juridiction | TypeBranche | C06, référentiels JSON |  |
| Référentiels de juridiction | ConditionBloquante | C06, référentiels JSON | Notice d'implémentation |
| Référentiels de juridiction | RegleTransverse | référentiels JSON, Notice d'implémentation |  |
| Référentiels de juridiction | EtapeFeuilleDeRoute | C07 |  |
| Référentiels de juridiction | ParametresAutorite | C03 | alertes.json |
| Référentiels de juridiction | DelaiInstruction | C03, C05 |  |
| Référentiels de juridiction | ConfigAipd | C08 |  |
| Référentiels de juridiction | CritereAipd | C08, référentiels JSON |  |
| Référentiels de juridiction | ConfigViolation | C09 |  |
| Référentiels de juridiction | NoeudViolation | C09, référentiels JSON |  |
| Référentiels de juridiction | ConfigIndice | C13, G01 |  |
| Référentiels de juridiction | DefinitionChamp | C12, registre-champs.csv | bulles-information.json, cahier des charges, référentiels JSON, Notice d'implémentation |
| Référentiels de juridiction | ExigenceChamp | registre-champs.csv | Notice d'implémentation |
| Référentiels de juridiction | Exigence | registre-champs.csv | alertes.json, Notice d'implémentation |
| Référentiels de juridiction | BulleInformation | D01, D02, D03, bulles-information.json | Notice d'implémentation |
| Référentiels de juridiction | TypeQuestion | C06, référentiels JSON | Notice d'implémentation |
| Référentiels de juridiction | NiveauChamp | registre-champs.csv |  |
| Référentiels de juridiction | TypeChamp | registre-champs.csv | référentiels JSON, Notice d'implémentation |
| Référentiels de juridiction | Sources | C02 |  |
| Référentiels de juridiction | ArticleCle | C02 |  |
| Référentiels de juridiction | ModaliteDepot | C03 |  |
| Référentiels de juridiction | EcartTextePratique | C02, référentiels JSON |  |
| Référentiels de juridiction | ConfigCorrespondant | C10 |  |
| Référentiels de juridiction | ConfigTransferts | C11 | formulaire unique APDP |
| Référentiels de juridiction | ConsultationPrealable | C08, loi BJ 2017-20 |  |
| Référentiels de juridiction | SectionGrille | F03 |  |
| Référentiels de juridiction | BrancheViolation | C09, référentiels JSON |  |
| Référentiels de juridiction | ComposanteIndice | C13, G01 |  |
| Référentiels de juridiction | SeuilIndice | C13, G01 |  |
| Moteur de qualification | ResultatQualification | C06, D05, Notice d'implémentation |  |
| Moteur de qualification | MoteurQualification | I01, référentiels JSON, Notice d'implémentation, cas de recette | registre-champs.csv |
| Registre et qualification | FicheTraitement | C12, E01, G03, registre-champs.csv | G04, G07, alertes.json, référentiels JSON, Notice d'implémentation |
| Registre et qualification | StatutFiche | G03 | G04 |
| Registre et qualification | VersionFichePubliee | G03, G04 | alertes.json |
| Registre et qualification | Qualification | C06, Notice d'implémentation | H01 |
| Registre et qualification | VoieQualification | Notice d'implémentation |  |
| Registre et qualification | EtapeChemin | C06, référentiels JSON |  |
| Registre et qualification | Prestataire | C14, registre-champs.csv |  |
| Registre et qualification | SousTraitanceFiche | C14, registre-champs.csv | alertes.json |
| Registre et qualification | TransfertFiche | C11, registre-champs.csv | alertes.json |
| Registre et qualification | PieceJointe | E03, registre-champs.csv |  |
| Formalités | DossierFormalite | C07, E03, G03 | alertes.json |
| Formalités | TypeDossier | C05, E03 |  |
| Formalités | StatutDossier | G03 |  |
| Formalités | JalonDossier | C03, G03 |  |
| Formalités | DocumentProduit | E01, E02, E03, E04, E05, E06, E07 |  |
| Analyses d'impact | AnalyseImpact | C08, E04, F03 | loi BJ 2017-20 |
| Analyses d'impact | SectionAipd | F03 |  |
| Analyses d'impact | RisqueAipd | F03 |  |
| Analyses d'impact | InvitationAipd | F03, G04 |  |
| Analyses d'impact | StatutAipd | G03 | alertes.json |
| Violations de données | Violation | C09, E05 | alertes.json |
| Violations de données | NatureViolation | C09, E05 |  |
| Violations de données | StatutViolation | G03 |  |
| Pilotage | DefinitionAlerte | G02, alertes.json | référentiels JSON |
| Pilotage | OccurrenceAlerte | G02, alertes.json |  |
| Pilotage | Tache | C07, G02, G03 | alertes.json |
| Pilotage | StatutTache | G03 |  |
| Pilotage | Notification | G02 |  |
| Pilotage | Parametre | G07 |  |
| Pilotage | PorteeParametre | G07 |  |
| Pilotage | InstantaneIndice | C13, G01 |  |
| Pilotage | EntreeJournal | E07, G05 |  |
| Pilotage | CanalAlerte | G02, alertes.json |  |
| Pilotage | OrigineTache | C07, G02, Notice d'implémentation |  |

## 3. Index : quel fichier AMELEGAL alimente quelles classes

| Source | Fichier(s) dans le dépôt | Classes concernées |
|---|---|---|
| **C01** Identification de la juridiction | `01 Togo/01 Livrables Togo/C01 - Identification de la juridiction.docx`<br>`02 Bénin/01 Livrables Bénin/C01 - Identification de la juridiction.docx` | Juridiction |
| **C02** Sources | `01 Togo/01 Livrables Togo/C02 - Sources.docx`<br>`02 Bénin/01 Livrables Bénin/C02 - Sources.docx` | ArticleCle, EcartTextePratique, Sources |
| **C03** Autorité de contrôle | `01 Togo/01 Livrables Togo/C03 - Autorité de contrôle.docx`<br>`02 Bénin/01 Livrables Bénin/C03 - Autorité de contrôle.docx` | DelaiInstruction, JalonDossier, ModaliteDepot, ParametresAutorite |
| **C05** Régimes de formalité | `01 Togo/01 Livrables Togo/C05 - Régimes de formalité.docx`<br>`02 Bénin/01 Livrables Bénin/C05 - Régimes de formalité.docx` | DelaiInstruction, Regime, TypeDossier |
| **C06** Logigramme de qualification | `01 Togo/01 Livrables Togo/C06 - Logigramme de qualification.docx`<br>`02 Bénin/01 Livrables Bénin/C06 - Logigramme de qualification.docx` | Branche, ConditionBloquante, EtapeChemin, Logigramme, Qualification, Question, ResultatQualification, TypeBranche, TypeQuestion |
| **C07** Feuilles de route | `01 Togo/01 Livrables Togo/C07 - Feuilles de route.docx`<br>`02 Bénin/01 Livrables Bénin/C07 - Feuilles de route.docx` | DossierFormalite, EtapeFeuilleDeRoute, OrigineTache, Tache |
| **C08** Analyse d_impact | `01 Togo/01 Livrables Togo/C08 - Analyse d_impact.docx`<br>`02 Bénin/01 Livrables Bénin/C08 - Analyse d_impact.docx` | AnalyseImpact, ConfigAipd, ConsultationPrealable, CritereAipd |
| **C09** Violations de données | `01 Togo/01 Livrables Togo/C09 - Violations de données.docx`<br>`02 Bénin/01 Livrables Bénin/C09 - Violations de données.docx` | BrancheViolation, ConfigViolation, NatureViolation, NoeudViolation, Violation |
| **C10** Correspondant | `01 Togo/01 Livrables Togo/C10 - Correspondant.docx`<br>`02 Bénin/01 Livrables Bénin/C10 - Correspondant.docx` | ConfigCorrespondant, DesignationCorrespondant, StatutCorrespondant |
| **C11** Transferts internationaux | `01 Togo/01 Livrables Togo/C11 - Transferts internationaux.docx`<br>`02 Bénin/01 Livrables Bénin/C11 - Transferts internationaux.docx` | ConfigTransferts, TransfertFiche |
| **C12** Registre | `01 Togo/01 Livrables Togo/C12 - Registre.docx`<br>`02 Bénin/01 Livrables Bénin/C12 - Registre.docx` | DefinitionChamp, FicheTraitement, Organisation, ResponsableTraitementLegal |
| **C13** Indice de conformité paramètres | `01 Togo/01 Livrables Togo/C13 - Indice de conformité paramètres.docx`<br>`02 Bénin/01 Livrables Bénin/C13 - Indice de conformité paramètres.docx` | ComposanteIndice, ConfigIndice, InstantaneIndice, SeuilIndice |
| **C14** Sous-traitance | `01 Togo/01 Livrables Togo/C14 - Sous-traitance.docx`<br>`02 Bénin/01 Livrables Bénin/C14 - Sous-traitance.docx` | Prestataire, SousTraitanceFiche |
| **C15** Version publiée du référentiel | `01 Togo/01 Livrables Togo/C15 - Version publiée du référentiel.docx`<br>`02 Bénin/01 Livrables Bénin/C15 - Version publiée du référentiel.docx` | ReferentielVersion, StatutReferentiel |
| **D01** Liste arrêtée des notions appelant une bulle | `01 Togo/01 Livrables Togo/D01 - Liste arrêtée des notions appelant une bulle.docx`<br>`02 Bénin/01 Livrables Bénin/D01 - Liste arrêtée des notions appelant une bulle.docx` | BulleInformation |
| **D02** Contenu rédigé des bulles d_information | `01 Togo/01 Livrables Togo/D02 - Contenu rédigé des bulles d_information.docx`<br>`02 Bénin/01 Livrables Bénin/D02 - Contenu rédigé des bulles d_information.docx` | BulleInformation |
| **D03** Fiches d_explication développées | `01 Togo/01 Livrables Togo/D03 - Fiches d_explication développées.docx`<br>`02 Bénin/01 Livrables Bénin/D03 - Fiches d_explication développées.docx` | BulleInformation |
| **D05** Réserve d_interprétation et mentions communes | `00 Commun aux deux pays/02 Livrables communs/D - Aide contextuelle (socle commun)/D05 - Réserve d_interprétation et mentions communes.docx` | ResultatQualification |
| **E01** Fiche de registre | `01 Togo/01 Livrables Togo/E01 - Fiche de registre.docx`<br>`02 Bénin/01 Livrables Bénin/E01 - Fiche de registre.docx` | DocumentProduit, FicheTraitement |
| **E02** Registre complet | `01 Togo/01 Livrables Togo/E02 - Registre complet.docx`<br>`02 Bénin/01 Livrables Bénin/E02 - Registre complet.docx` | DocumentProduit |
| **E03** Dossiers de formalité | `01 Togo/01 Livrables Togo/E03 - Dossiers de formalité.docx`<br>`02 Bénin/01 Livrables Bénin/E03 - Dossiers de formalité.docx` | DocumentProduit, DossierFormalite, PieceJointe, TypeDossier |
| **E04** Rapport d_analyse d_impact | `01 Togo/01 Livrables Togo/E04 - Rapport d_analyse d_impact.docx`<br>`02 Bénin/01 Livrables Bénin/E04 - Rapport d_analyse d_impact.docx` | AnalyseImpact, DocumentProduit |
| **E05** Notifications de violation | `01 Togo/01 Livrables Togo/E05 - Notifications de violation.docx`<br>`02 Bénin/01 Livrables Bénin/E05 - Notifications de violation.docx` | DocumentProduit, NatureViolation, Violation |
| **E06** Rapport d_activité de cabinet | `01 Togo/01 Livrables Togo/E06 - Rapport d_activité de cabinet.docx`<br>`02 Bénin/01 Livrables Bénin/E06 - Rapport d_activité de cabinet.docx` | Cabinet, DocumentProduit |
| **E07** Mentions transverses des exports | `00 Commun aux deux pays/02 Livrables communs/E - Modèles documentaires (socle commun)/E07 - Mentions transverses des exports.docx` | DocumentProduit, EntreeJournal |
| **F02** Modèles sectoriels de traitement | `01 Togo/01 Livrables Togo/F02 - Modèles sectoriels de traitement.docx`<br>`02 Bénin/01 Livrables Bénin/F02 - Modèles sectoriels de traitement.docx` | Organisation |
| **F03** Grille d_analyse d_impact détaillée | `01 Togo/01 Livrables Togo/F03 - Grille d_analyse d_impact détaillée.docx`<br>`02 Bénin/01 Livrables Bénin/F03 - Grille d_analyse d_impact détaillée.docx` | AnalyseImpact, InvitationAipd, RisqueAipd, SectionAipd, SectionGrille |
| **G01** Méthode de calcul de l_indice de conformité | `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G01 - Méthode de calcul de l_indice de conformité.docx` | ComposanteIndice, ConfigIndice, InstantaneIndice, Referentiel, SeuilIndice |
| **G02** Règles de déclenchement des alertes | `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G02 - Règles de déclenchement des alertes.docx` | CanalAlerte, DefinitionAlerte, Notification, OccurrenceAlerte, OrigineTache, Tache |
| **G03** Statuts et cycles de vie | `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G03 - Statuts et cycles de vie.docx` | DossierFormalite, FicheTraitement, JalonDossier, Mandat, StatutAipd, StatutDossier, StatutFiche, StatutMandat, StatutReferentiel, StatutTache, StatutViolation, Tache, VersionFichePubliee |
| **G04** Matrice des habilitations et circuit de validation | `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G04 - Matrice des habilitations et circuit de validation.docx` | AffectationConsultant, Cabinet, FicheTraitement, InvitationAipd, MembreCabinet, MembreOrganisation, NiveauMandat, Organisation, RoleCabinet, RoleOrganisation, ServiceDirection, StatutFiche, Utilisateur, VersionFichePubliee |
| **G05** Régime des mandats | `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G05 - Régime des mandats.docx` | ActionReservable, AffectationConsultant, EntreeJournal, Mandat, NiveauMandat, Organisation, PorteeMandat, ServiceDirection, StatutMandat |
| **G07** Périodes et seuils paramétrables | `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G07 - Périodes et seuils paramétrables.docx` | FicheTraitement, Parametre, PorteeParametre |
| **H01** Textes des pages publiques | `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H01 - Textes des pages publiques.docx` | Cabinet, DesignationCorrespondant, Qualification, Utilisateur |
| **H05** Conditions générales d_utilisation cabinets | `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H05 - Conditions générales d_utilisation cabinets.docx` | Cabinet |
| **I01** Jeu de cas de recette du moteur | `01 Togo/01 Livrables Togo/I01 - Jeu de cas de recette du moteur.docx`<br>`02 Bénin/01 Livrables Bénin/I01 - Jeu de cas de recette du moteur.docx` | MoteurQualification |
| Types d'alerte AL-01 à AL-13 | `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/alertes.json` | CanalAlerte, DefinitionAlerte, DossierFormalite, Exigence, FicheTraitement, Mandat, OccurrenceAlerte, ParametresAutorite, SousTraitanceFiche, StatutAipd, Tache, TransfertFiche, Utilisateur, VersionFichePubliee, Violation |
| Bulles d'information | `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/bulles-information.json` | BulleInformation, DefinitionChamp, Question |
| Cahier des charges (absent du dépôt) | *absent du dépôt* | DefinitionChamp |
| Champs du registre | `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/registre-champs.csv` | DefinitionChamp, DesignationCorrespondant, Exigence, ExigenceChamp, FicheTraitement, Juridiction, MoteurQualification, NiveauChamp, Organisation, PieceJointe, Prestataire, ResponsableTraitementLegal, SousTraitanceFiche, StatutCorrespondant, TransfertFiche, TypeChamp |
| Formulaire unique de l'APDP et annexes | `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/FORMULAIRE-UNIQUE.pdf` | ConfigTransferts |
| Référentiels machine | `01 Togo/01 Livrables Togo/_spécifications développeur/referentiel-togo.json`<br>`02 Bénin/01 Livrables Bénin/_spécifications développeur/referentiel-benin.json` | Branche, BrancheViolation, ConditionBloquante, CritereAipd, DefinitionAlerte, DefinitionChamp, DesignationCorrespondant, EcartTextePratique, EtapeChemin, FicheTraitement, Logigramme, MoteurQualification, NoeudViolation, Organisation, Question, Referentiel, ReferentielVersion, Regime, RegleTransverse, TypeBranche, TypeChamp, TypeQuestion |
| Loi béninoise n° 2017-20, Livre cinquième | `02 Bénin/00 Sources et référentiels/Textes/Benin-Loi-2017-20-Portant-code-du-numerique-en-Republique-du-Benin.pdf` | AnalyseImpact, ConsultationPrealable |
| Notice d'implémentation du référentiel | `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/00 Notice d_implémentation du référentiel.docx` | BulleInformation, ConditionBloquante, DefinitionChamp, Exigence, ExigenceChamp, FicheTraitement, Juridiction, MoteurQualification, OrigineTache, Qualification, Referentiel, ReferentielVersion, RegleTransverse, ResultatQualification, TypeChamp, TypeQuestion, VoieQualification |
| Cas de recette du moteur | `01 Togo/01 Livrables Togo/_spécifications développeur/cas-de-recette-togo.csv`<br>`02 Bénin/01 Livrables Bénin/_spécifications développeur/cas-de-recette-benin.csv` | MoteurQualification, StatutReferentiel |

## 4. Détail par classe et par champ

Pour chaque classe : la source principale, puis les champs et valeurs qui citent une source. Un champ absent du tableau est technique (identifiant, date de création…) ou découle de la classe.

### Accès : organisations, cabinets, utilisateurs, mandats

#### Utilisateur (classe)

**Source principale :** G04, H01
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `Courriel` | alertes.json | Identifiant de connexion et adresse d'envoi des alertes (AL-01, AL-03…). Unique sur la plateforme. |
| `DoubleAuthActive` | H01 | La double authentification est obligatoire pour les administrateurs, les correspondants et les cabinets (H01, section Confiance). Ce champ permet de bloquer l'accès tant qu'elle n'est pas activée pour ces profils. |

#### Organisation (classe)

**Source principale :** C12, G04, registre-champs.csv
<br>**Sources citées par ses champs :** F02, G05, référentiels JSON

| Champ | Source | Explication du champ |
|---|---|---|
| `Denomination` | registre-champs.csv | Rubrique 1 du registre (« Informations sur l'organisme », champ org.denomination). Saisie une fois, reprise dans chaque fiche et chaque export. |
| `FormeJuridique` | registre-champs.csv | Rubrique 1 du registre (org.forme_juridique) ; figure sur les formulaires de l'autorité. |
| `IdentifiantFiscal` | registre-champs.csv | Rubrique 1 du registre (org.identifiant_fiscal) ; identifie l'organisme auprès de l'autorité. |
| `Rccm` | registre-champs.csv | Numéro au registre du commerce (org.rccm), demandé par les formulaires de déclaration. |
| `Adresse` | registre-champs.csv | Coordonnées de l'organisme (org.adresse), reprises dans les dossiers de formalité. |
| `Secteur` | F02, registre-champs.csv | Secteur d'activité (org.secteur). Sert à proposer les modèles sectoriels de traitements (F02). |
| `TrancheEffectif` | registre-champs.csv | Effectif par tranche (org.effectif). Sert à adapter l'accompagnement, par exemple le circuit fusionné pour les petites structures. |
| `NaturePublique` | référentiels JSON | Alimente le moteur : répond à TG-Q6 et BJ-Q4 (traitement pour le compte de l'État ou d'une collectivité). Typé en booléen parce que la logique juridique en dépend. |
| `MissionServicePublic` | référentiels JSON | Alimente le moteur : complète TG-Q6 et BJ-Q4, et ferme l'exemption béninoise BJ-Q8 aux autorités publiques (condition bloquante). |
| `VisaActive` | G04 | Le visa du responsable de traitement avant dépôt est une étape désactivable par l'organisation (G04 §4). |
| `CircuitFusionne` | G04 | Une petite structure peut fusionner soumission, qualification et visa en une seule validation (G04 §4). |
| `GroupeParentId` | G05 | Rattache une entité à son groupe. Permet le mandat « limité à certaines entités du groupe » (G05) et la vision consolidée d'un groupe présent dans plusieurs pays. |

#### ServiceDirection (classe)

**Source principale :** G04, G05

#### MembreOrganisation (classe)

**Source principale :** G04

| Champ | Source | Explication du champ |
|---|---|---|
| `Roles` | G04 | Un ensemble, pas un seul rôle : G04 prévoit le cumul (« le droit le plus favorable s'applique »). Dans une PME, une même personne peut être administrateur et correspondant. |
| `PerimetreServices` | G04 | Les services auxquels le rôle est limité, pour le contributeur métier (le « P » de la matrice G04). |

#### RoleOrganisation (énumération)

**Source principale :** G04

#### ResponsableTraitementLegal (classe)

**Source principale :** C12, registre-champs.csv

#### DesignationCorrespondant (classe)

**Source principale :** C10, registre-champs.csv
<br>**Sources citées par ses champs :** H01, référentiels JSON

| Champ | Source | Explication du champ |
|---|---|---|
| `Designe` | référentiels JSON | Répond à TG-Q3 (désignation qui dispense de formalités au Togo) et ouvre la voie de l'exemption au Bénin. À défaut, réputé faux. |

#### Cabinet (classe)

**Source principale :** G04, H05
<br>**Sources citées par ses champs :** E06, H01

| Champ | Source | Explication du champ |
|---|---|---|
| `Denomination` | E06 | Affichée au client, dans le journal et sur le rapport d'activité E06. |
| `OrganisationPropreId` | H01 | Le cabinet tient sa propre conformité (H01). Son registre est une Organisation ordinaire, ce qui évite tout développement spécifique. |
| `AccesDossierPropreOuvert` | G04 | L'administrateur de cabinet décide si les consultants accèdent au dossier interne du cabinet (G04 §2). |

#### MembreCabinet (classe)

**Source principale :** G04

| Champ | Source | Explication du champ |
|---|---|---|
| `Role` | G04 | Un seul rôle de cabinet par personne (G04 §2). |

#### RoleCabinet (énumération)

**Source principale :** G04

#### Mandat (classe)

**Source principale :** G05
<br>**Sources citées par ses champs :** G03, alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `Id` | G05 | Référencé par le journal : chaque action d'un consultant cite le mandat en vigueur, et cette mention subsiste après la fin du mandat (G05 §4). |
| `DateFin` | alertes.json | Facultative. Si elle est renseignée, le mandat expire automatiquement et les alertes partent à J-30 puis J-7 (AL-10). |
| `Statut` | G03 | Cycle de vie du mandat (G03) ; seul le statut Actif ouvre l'accès. |
| `ActionsReservees` | G05 | Actions que le client garde pour lui même sous mandat de pilotage complet (G05 §3). |

#### NiveauMandat (énumération)

**Source principale :** G04, G05

#### ActionReservable (énumération)

**Source principale :** G05

#### AffectationConsultant (classe)

**Source principale :** G04, G05

| Champ | Source | Explication du champ |
|---|---|---|
| `OpposeeParOrganisation` | G04 | Le client peut s'opposer à l'affectation d'un consultant (G04). |

#### StatutMandat (énumération)

**Source principale :** G03, G05

#### PorteeMandat (énumération)

**Source principale :** G05

#### StatutCorrespondant (énumération)

**Source principale :** C10, registre-champs.csv

### Référentiels de juridiction

#### Juridiction (classe)

**Source principale :** C01, Notice d'implémentation
<br>**Sources citées par ses champs :** registre-champs.csv

#### ReferentielVersion (classe)

**Source principale :** C15, Notice d'implémentation
<br>**Sources citées par ses champs :** référentiels JSON

| Champ | Source | Explication du champ |
|---|---|---|
| `DateVersion` | référentiels JSON | Date du référentiel (meta.date du JSON). |
| `Avertissement` | référentiels JSON | Mention reprise du JSON (« aucune valeur codée en dur »). |
| `Contenu` | référentiels JSON | Le référentiel complet en JSON, tel qu'importé et validé par schéma. |

#### StatutReferentiel (énumération)

**Source principale :** C15, G03
<br>**Sources citées par ses champs :** cas de recette

| Champ | Source | Explication du champ |
|---|---|---|
| `EnSimulation` | cas de recette | Rejoué sur les cas de recette et les fiches existantes avant publication. |

#### Referentiel (classe)

**Source principale :** référentiels JSON, Notice d'implémentation
<br>**Sources citées par ses champs :** G01

| Champ | Source | Explication du champ |
|---|---|---|
| `Regimes` | référentiels JSON | Les sorties possibles du logigramme (clé regimes). |
| `Logigramme` | référentiels JSON | L'arbre de qualification (clé logigramme). |

#### Regime (classe)

**Source principale :** C05, référentiels JSON

| Champ | Source | Explication du champ |
|---|---|---|
| `Id` | référentiels JSON | Code stable (TG-DECLARATION, BJ-EXEMPTION…), clé de rattachement des qualifications et des dossiers. |

#### Logigramme (classe)

**Source principale :** C06, référentiels JSON

#### Question (classe)

**Source principale :** C06, référentiels JSON
<br>**Sources citées par ses champs :** bulles-information.json

| Champ | Source | Explication du champ |
|---|---|---|
| `Id` | référentiels JSON | Code stable (TG-Q3, BJ-Q8), conservé dans le chemin de chaque qualification. |
| `AideId` | bulles-information.json | Bulle d'information obligatoire pour toute notion juridique utilisée. |

#### Branche (classe)

**Source principale :** C06, référentiels JSON

#### TypeBranche (énumération)

**Source principale :** C06, référentiels JSON

#### ConditionBloquante (classe)

**Source principale :** C06, référentiels JSON
<br>**Sources citées par ses champs :** Notice d'implémentation

#### RegleTransverse (classe)

**Source principale :** référentiels JSON, Notice d'implémentation

#### EtapeFeuilleDeRoute (classe)

**Source principale :** C07

#### ParametresAutorite (classe)

**Source principale :** C03
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `ValiditeDecisionMois` | alertes.json | 24 au Bénin : déclenche l'alerte de renouvellement (AL-12). |

#### DelaiInstruction (classe)

**Source principale :** C03, C05

#### ConfigAipd (classe)

**Source principale :** C08

#### CritereAipd (classe)

**Source principale :** C08, référentiels JSON

#### ConfigViolation (classe)

**Source principale :** C09

#### NoeudViolation (classe)

**Source principale :** C09, référentiels JSON

#### ConfigIndice (classe)

**Source principale :** C13, G01

#### DefinitionChamp (classe)

**Source principale :** C12, registre-champs.csv
<br>**Sources citées par ses champs :** bulles-information.json, cahier des charges, référentiels JSON, Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Id` | registre-champs.csv, référentiels JSON | Colonne id. Identifiant technique stable (t.finalites, org.secteur…) : clé de stockage des valeurs et clé par laquelle le logigramme désigne le champ qui répond à une question. |
| `Niveau` | Notice d'implémentation | Colonne niveau. Un champ de niveau organisation est saisi une fois et repris dans chaque fiche (notice § 6). |
| `Bloc` | cahier des charges | Colonne bloc. Bloc d'affichage de la fiche, conformément à l'article 26.2 du cahier des charges. |
| `Type` | Notice d'implémentation | Colonne type. L'un des 12 types arrêtés par la notice ; il détermine l'affichage et les contrôles de saisie. |
| `Juridiction` | Notice d'implémentation | Colonne juridiction (TG, BJ ou commun). Un champ marqué TG n'est ni affiché ni exporté au Bénin, et réciproquement (notice § 6). |
| `AlimenteMoteur` | bulles-information.json, référentiels JSON, Notice d'implémentation | Colonne alimente_moteur. Le champ conditionne une réponse du logigramme ; il appelle obligatoirement une bulle d'information, contrôle prévu en recette (notice § 7). |
| `AideId` | bulles-information.json | Colonne aide_id. La bulle d'information rattachée au champ. |

#### ExigenceChamp (classe)

**Source principale :** registre-champs.csv
<br>**Sources citées par ses champs :** Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Niveau` | registre-champs.csv | O, R ou C du CSV : obligatoire, recommandé ou conditionnel. Une case vide signifie que le champ est sans objet dans ce pays. |

#### Exigence (énumération)

**Source principale :** registre-champs.csv
<br>**Sources citées par ses champs :** alertes.json, Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Obligatoire` | alertes.json | O : bloque la soumission de la fiche si vide (AL-05). |
| `Conditionnel` | registre-champs.csv | C : obligatoire selon la réponse à un autre champ, comme l'indique la note du CSV. |

#### BulleInformation (classe)

**Source principale :** D01, D02, D03, bulles-information.json
<br>**Sources citées par ses champs :** Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Titre` | bulles-information.json | Titre de la bulle. |
| `LienFiche` | D03 | Lien vers une fiche d'explication développée (D03). |

#### TypeQuestion (énumération)

**Source principale :** C06, référentiels JSON
<br>**Sources citées par ses champs :** Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Multiple` | Notice d'implémentation | Vrai dès qu'une option au moins est cochée (notice §4). |

#### NiveauChamp (énumération)

**Source principale :** registre-champs.csv

#### TypeChamp (énumération)

**Source principale :** registre-champs.csv
<br>**Sources citées par ses champs :** référentiels JSON, Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Booleen` | référentiels JSON | Oui / non : la plupart des réponses au logigramme. |

#### Sources (classe)

**Source principale :** C02

#### ArticleCle (classe)

**Source principale :** C02

#### ModaliteDepot (classe)

**Source principale :** C03

#### EcartTextePratique (classe)

**Source principale :** C02, référentiels JSON

#### ConfigCorrespondant (classe)

**Source principale :** C10

#### ConfigTransferts (classe)

**Source principale :** C11
<br>**Sources citées par ses champs :** formulaire unique APDP

| Champ | Source | Explication du champ |
|---|---|---|
| `Piece` | formulaire unique APDP | Annexe à joindre (annexe 4 du formulaire unique au Bénin). |

#### ConsultationPrealable (classe)

**Source principale :** C08, loi BJ 2017-20

#### SectionGrille (classe)

**Source principale :** F03

#### BrancheViolation (classe)

**Source principale :** C09, référentiels JSON

#### ComposanteIndice (classe)

**Source principale :** C13, G01

#### SeuilIndice (classe)

**Source principale :** C13, G01

### Moteur de qualification

#### ResultatQualification (classe)

**Source principale :** C06, D05, Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `ReserveInterpretation` | D05 | Mention du livrable D05 : le résultat est indicatif. |

#### MoteurQualification (classe)

**Source principale :** I01, référentiels JSON, Notice d'implémentation, cas de recette
<br>**Sources citées par ses champs :** registre-champs.csv

| Champ | Source | Explication du champ |
|---|---|---|
| `Qualifier()` | référentiels JSON | Exécute le logigramme et renvoie le résultat complet. |

### Registre et qualification

#### FicheTraitement (classe)

**Source principale :** C12, E01, G03, registre-champs.csv
<br>**Sources citées par ses champs :** G04, G07, alertes.json, référentiels JSON, Notice d'implémentation

| Champ | Source | Explication du champ |
|---|---|---|
| `Reference` | registre-champs.csv | Numéro interne affiché dans le registre (t.reference). |
| `Nom` | registre-champs.csv | Intitulé du traitement (t.nom). |
| `Juridictions` | registre-champs.csv | Un traitement peut relever de plusieurs pays (note du champ t.juridiction) : il est alors qualifié une fois par pays. |
| `Statut` | G03, G04 | Étape du circuit de validation (G03, G04). |
| `Valeurs` | registre-champs.csv, référentiels JSON | Les valeurs des champs de niveau traitement de registre-champs.csv, en JSON, sous l'identifiant stable de chaque champ (t.finalites…). Les champs propres à un pays y figurent seulement pour ce pays. |
| `ProchaineRevue` | G07, alertes.json | Échéance de revue (12 mois, 6 pour les régimes lourds, G07) qui déclenche AL-08. |
| `OrigineCartographie` | Notice d'implémentation | Origine dans la cartographie AMELEGAL : traçabilité interne, jamais exportée (notice §6). |

#### StatutFiche (énumération)

**Source principale :** G03
<br>**Sources citées par ses champs :** G04

#### VersionFichePubliee (classe)

**Source principale :** G03, G04
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `ModificationSubstantielle` | alertes.json | Si vrai, et si la fiche avait été déclarée, une nouvelle déclaration est exigée (AL-13, BJ-T4). |

#### Qualification (classe)

**Source principale :** C06, Notice d'implémentation
<br>**Sources citées par ses champs :** H01

| Champ | Source | Explication du champ |
|---|---|---|
| `ReferentielVersionId` | Notice d'implémentation | La version exacte du référentiel : la qualification reste explicable après une nouvelle version (notice §2). |
| `Voie` | Notice d'implémentation | Depuis la fiche ou par l'assistant : les deux doivent donner le même résultat (recette, notice §7). |
| `RegimeRetenu` | H01 | Ce que l'humain a retenu. Le moteur aide à décider, il ne décide pas (H01). |

#### VoieQualification (énumération)

**Source principale :** Notice d'implémentation

#### EtapeChemin (classe)

**Source principale :** C06, référentiels JSON

#### Prestataire (classe)

**Source principale :** C14, registre-champs.csv

#### SousTraitanceFiche (classe)

**Source principale :** C14, registre-champs.csv
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `ContratConforme` | alertes.json | Si faux, l'alerte « sous-traitant sans contrat conforme » (AL-06) est déclenchée. |

#### TransfertFiche (classe)

**Source principale :** C11, registre-champs.csv
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `PaysReconnu` | alertes.json | Calculé depuis le référentiel ; sinon, alerte « transfert non encadré » (AL-07). |

#### PieceJointe (classe)

**Source principale :** E03, registre-champs.csv

### Formalités

#### DossierFormalite (classe)

**Source principale :** C07, E03, G03
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `Statut` | G03 | Étape du suivi (G03). |
| `EcheanceInstruction` | alertes.json | Échéance calculée : déclenche l'acceptation tacite (Bénin) ou l'alerte AL-04. |
| `ValideJusquau` | alertes.json | Fin de validité (2 ans au Bénin) : déclenche AL-12. |

#### TypeDossier (énumération)

**Source principale :** C05, E03

#### StatutDossier (énumération)

**Source principale :** G03

#### JalonDossier (classe)

**Source principale :** C03, G03

#### DocumentProduit (classe)

**Source principale :** E01, E02, E03, E04, E05, E06, E07

| Champ | Source | Explication du champ |
|---|---|---|
| `Modele` | E03, E05 | Le modèle utilisé (E03 dossier, E05 notification…). |

### Analyses d'impact

#### AnalyseImpact (classe)

**Source principale :** C08, E04, F03
<br>**Sources citées par ses champs :** loi BJ 2017-20

| Champ | Source | Explication du champ |
|---|---|---|
| `ConsultationPrealableRequise` | loi BJ 2017-20 | Si le risque résiduel reste élevé (Bénin, art. 429). |

#### SectionAipd (classe)

**Source principale :** F03

#### RisqueAipd (classe)

**Source principale :** F03

#### InvitationAipd (classe)

**Source principale :** F03, G04

#### StatutAipd (énumération)

**Source principale :** G03
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `ARealiser` | alertes.json | Exigée, pas encore lancée (AL-02). |

### Violations de données

#### Violation (classe)

**Source principale :** C09, E05
<br>**Sources citées par ses champs :** alertes.json

#### NatureViolation (énumération)

**Source principale :** C09, E05

#### StatutViolation (énumération)

**Source principale :** G03

### Pilotage : tâches, alertes, paramètres, indice, journal

#### DefinitionAlerte (classe)

**Source principale :** G02, alertes.json
<br>**Sources citées par ses champs :** référentiels JSON

| Champ | Source | Explication du champ |
|---|---|---|
| `Code` | alertes.json | AL-01 à AL-13. |

#### OccurrenceAlerte (classe)

**Source principale :** G02, alertes.json

#### Tache (classe)

**Source principale :** C07, G02, G03
<br>**Sources citées par ses champs :** alertes.json

| Champ | Source | Explication du champ |
|---|---|---|
| `Echeance` | alertes.json | Date limite ; dépassée, elle déclenche AL-11. |
| `Justification` | G03 | Obligatoire pour ignorer une tâche (G03). |

#### StatutTache (énumération)

**Source principale :** G03

#### Notification (classe)

**Source principale :** G02

#### Parametre (classe)

**Source principale :** G07

| Champ | Source | Explication du champ |
|---|---|---|
| `Valeur` | G07 | La valeur. Au niveau organisation, elle ne peut pas être moins protectrice que celle du pays (G07). |

#### PorteeParametre (énumération)

**Source principale :** G07

#### InstantaneIndice (classe)

**Source principale :** C13, G01

| Champ | Source | Explication du champ |
|---|---|---|
| `DetailComposantes` | G01 | Détail du calcul, affiché à la demande (G01). |

#### EntreeJournal (classe)

**Source principale :** E07, G05

| Champ | Source | Explication du champ |
|---|---|---|
| `MandatId` | G05 | Le mandat en vigueur ; la mention subsiste après la fin du mandat (G05 §4). |

#### CanalAlerte (énumération)

**Source principale :** G02, alertes.json

#### OrigineTache (énumération)

**Source principale :** C07, G02, Notice d'implémentation

## 5. Légende des sources

| Code | Fichier |
|---|---|
| C01 | C01 - Identification de la juridiction — 01 Togo/01 Livrables Togo/C01 - Identification de la juridiction.docx |
| C02 | C02 - Sources — 01 Togo/01 Livrables Togo/C02 - Sources.docx |
| C03 | C03 - Autorité de contrôle — 01 Togo/01 Livrables Togo/C03 - Autorité de contrôle.docx |
| C05 | C05 - Régimes de formalité — 01 Togo/01 Livrables Togo/C05 - Régimes de formalité.docx |
| C06 | C06 - Logigramme de qualification — 01 Togo/01 Livrables Togo/C06 - Logigramme de qualification.docx |
| C07 | C07 - Feuilles de route — 01 Togo/01 Livrables Togo/C07 - Feuilles de route.docx |
| C08 | C08 - Analyse d_impact — 01 Togo/01 Livrables Togo/C08 - Analyse d_impact.docx |
| C09 | C09 - Violations de données — 01 Togo/01 Livrables Togo/C09 - Violations de données.docx |
| C10 | C10 - Correspondant — 01 Togo/01 Livrables Togo/C10 - Correspondant.docx |
| C11 | C11 - Transferts internationaux — 01 Togo/01 Livrables Togo/C11 - Transferts internationaux.docx |
| C12 | C12 - Registre — 01 Togo/01 Livrables Togo/C12 - Registre.docx |
| C13 | C13 - Indice de conformité paramètres — 01 Togo/01 Livrables Togo/C13 - Indice de conformité paramètres.docx |
| C14 | C14 - Sous-traitance — 01 Togo/01 Livrables Togo/C14 - Sous-traitance.docx |
| C15 | C15 - Version publiée du référentiel — 01 Togo/01 Livrables Togo/C15 - Version publiée du référentiel.docx |
| D01 | D01 - Liste arrêtée des notions appelant une bulle — 01 Togo/01 Livrables Togo/D01 - Liste arrêtée des notions appelant une bulle.docx |
| D02 | D02 - Contenu rédigé des bulles d_information — 01 Togo/01 Livrables Togo/D02 - Contenu rédigé des bulles d_information.docx |
| D03 | D03 - Fiches d_explication développées — 01 Togo/01 Livrables Togo/D03 - Fiches d_explication développées.docx |
| D05 | D05 - Réserve d_interprétation et mentions communes — 00 Commun aux deux pays/02 Livrables communs/D - Aide contextuelle (socle commun)/D05 - Réserve d_interprétation et mentions communes.docx |
| E01 | E01 - Fiche de registre — 01 Togo/01 Livrables Togo/E01 - Fiche de registre.docx |
| E02 | E02 - Registre complet — 01 Togo/01 Livrables Togo/E02 - Registre complet.docx |
| E03 | E03 - Dossiers de formalité — 01 Togo/01 Livrables Togo/E03 - Dossiers de formalité.docx |
| E04 | E04 - Rapport d_analyse d_impact — 01 Togo/01 Livrables Togo/E04 - Rapport d_analyse d_impact.docx |
| E05 | E05 - Notifications de violation — 01 Togo/01 Livrables Togo/E05 - Notifications de violation.docx |
| E06 | E06 - Rapport d_activité de cabinet — 01 Togo/01 Livrables Togo/E06 - Rapport d_activité de cabinet.docx |
| E07 | E07 - Mentions transverses des exports — 00 Commun aux deux pays/02 Livrables communs/E - Modèles documentaires (socle commun)/E07 - Mentions transverses des exports.docx |
| F02 | F02 - Modèles sectoriels de traitement — 01 Togo/01 Livrables Togo/F02 - Modèles sectoriels de traitement.docx |
| F03 | F03 - Grille d_analyse d_impact détaillée — 01 Togo/01 Livrables Togo/F03 - Grille d_analyse d_impact détaillée.docx |
| G01 | G01 - Méthode de calcul de l_indice de conformité — 00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G01 - Méthode de calcul de l_indice de conformité.docx |
| G02 | G02 - Règles de déclenchement des alertes — 00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G02 - Règles de déclenchement des alertes.docx |
| G03 | G03 - Statuts et cycles de vie — 00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G03 - Statuts et cycles de vie.docx |
| G04 | G04 - Matrice des habilitations et circuit de validation — 00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G04 - Matrice des habilitations et circuit de validation.docx |
| G05 | G05 - Régime des mandats — 00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G05 - Régime des mandats.docx |
| G07 | G07 - Périodes et seuils paramétrables — 00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G07 - Périodes et seuils paramétrables.docx |
| H01 | H01 - Textes des pages publiques — 00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H01 - Textes des pages publiques.docx |
| H05 | H05 - Conditions générales d_utilisation cabinets — 00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H05 - Conditions générales d_utilisation cabinets.docx |
| I01 | I01 - Jeu de cas de recette du moteur — 01 Togo/01 Livrables Togo/I01 - Jeu de cas de recette du moteur.docx |
| ALERTES | Types d'alerte AL-01 à AL-13 — 00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/alertes.json |
| BULLES | Bulles d'information — 00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/bulles-information.json |
| CDC | Cahier des charges (absent du dépôt) |
| CSV | Champs du registre — 00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/registre-champs.csv |
| FORMULAIRE_BJ | Formulaire unique de l'APDP et annexes — 02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/FORMULAIRE-UNIQUE.pdf |
| JSON | Référentiels machine — 01 Togo/01 Livrables Togo/_spécifications développeur/referentiel-togo.json |
| LOI_BJ | Loi béninoise n° 2017-20, Livre cinquième — 02 Bénin/00 Sources et référentiels/Textes/Benin-Loi-2017-20-Portant-code-du-numerique-en-Republique-du-Benin.pdf |
| NOTICE | Notice d'implémentation du référentiel — 00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/00 Notice d_implémentation du référentiel.docx |
| RECETTE | Cas de recette du moteur — 01 Togo/01 Livrables Togo/_spécifications développeur/cas-de-recette-togo.csv |
