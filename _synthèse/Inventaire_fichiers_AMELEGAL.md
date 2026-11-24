# Inventaire des fichiers AMELEGAL : ce que chaque fichier contient

Établi à partir du contenu des fichiers du dépôt (livrables version 1.0, septembre 2026).
★ = source des cas d'utilisation. ★★ = source principale.

## 1. Commun aux deux pays : références du projet

| Fichier | Ce qu'il donne |
|---|---|
| Cartographie_traitements_donnees_personnelles_v3.docx | La nomenclature des traitements proposés par défaut aux utilisateurs (liste des intitulés de fiches modèles). Ne contient pas encore les champs des fiches. |
| Registre_original_socle_TG_BJ.pdf / .xlsx | Le registre d'origine qui sert de socle commun aux deux pays : les 12 rubriques du registre. |
| Registre_type_traitements_Waɖɛ_TG_BJ.pdf / .xlsx | Le registre type de Waɖɛ pour les deux pays, avec des fiches pré-remplies. |
| waɖɛ-maquette-v2.html | La maquette d'origine de l'interface : écrans, couleurs des régimes, parcours. |

## 2. Commun aux deux pays : identité visuelle

| Fichier | Ce qu'il donne |
|---|---|
| LOGOTYPE HORIZONTALE / VERTICALE .png | Le logo officiel, en version horizontale et en version verticale. |
| LOGOTYPE BLANC HORIZONTALE / VERTCALE .png | Le logo en blanc, pour les fonds sombres. |
| WARE PROPO 1_1 à 1_7 .jpeg | Sept propositions graphiques du logo. |
| Wade LOGOBOOK.pdf | La charte graphique : couleurs, typographies, usages du logo. |

## 3. Commun aux deux pays : livrables

| Famille | Fichier | Ce qu'il donne |
|---|---|---|
| D | D05 Réserve d'interprétation et mentions communes | Les textes types de la réserve d'interprétation (« cette aide est générale… »), à afficher sous tout résultat du moteur, toute bulle et tout document produit. |
| E | E07 Mentions transverses des exports | Les mentions obligatoires sur tout document produit (juridiction, texte appliqué, version du référentiel) et la liste des documents concernés. Toute production est consignée au journal. |
| F | ★ F01 Diagnostic guidé d'amorçage | Le questionnaire d'environ 10 minutes de l'étape 6 de l'onboarding. Il crée les premières fiches au statut Brouillon, sans vocabulaire juridique. Les questions 8, 9, 10, 12 et 13 alimentent le moteur. |
| F | ★ F04 Trames de collecte auprès des services métier | Des questionnaires imprimables pour les services métier, remplis hors ligne. Chaque question indique le champ de la fiche qu'elle alimente. |
| G | G01 Méthode de calcul de l'indice de conformité | La formule de l'indice : moyenne pondérée de 4 composantes (ratios de 0 à 1), neutralisation d'une composante si son dénominateur est nul, seuils des libellés. |
| G | G02 Règles de déclenchement des alertes | Les 13 types d'alerte (11 du cahier des charges et 2 propres au Bénin), leurs libellés, leur ordre d'urgence (de 1 à 8). |
| G | ★ G03 Statuts et cycles de vie | Les statuts de chaque objet (fiche, dossier, AIPD, violation, mandat…). Ajoute le statut « Acceptation tacite » (silence vaut acceptation au Bénin). |
| G | ★★ G04 Matrice des habilitations et circuit de validation | Qui peut faire quoi : rôles dans l'organisation (X, P = dans son périmètre, – = interdit), rôles dans le cabinet, combinaison rôle × mandat (le plus restrictif l'emporte), circuit de validation et visa. |
| G | ★ G05 Régime des mandats | Les règles du mandat cabinet → organisation : 3 dimensions de portée, consenti par l'organisation seule, exprès, révocable à tout moment avec effet immédiat, plafond des droits du consultant. |
| G | ★ G07 Périodes et seuils paramétrables | Les valeurs par défaut (délais, durées, seuils) et leur niveau d'administration. Aucune valeur dans le code ; l'organisation ne peut être moins protectrice que la juridiction. |
| H | ★ H01 Textes des pages publiques | Tous les textes du site public : accueil, offre organisations, offre cabinets, présentation d'AMELEGAL, contact, en-tête, pied de page, écrans de connexion et de création de compte. |
| H | H02 Mentions légales | La page des mentions légales : éditeur AMELEGAL SARL, hébergeur, propriété intellectuelle. |
| H | H03 Politique de confidentialité | Les données que Waɖɛ traite sur ses propres utilisateurs, pourquoi, à qui, combien de temps, et leurs droits. |
| H | ★ H04 CGU organisations | Les conditions d'utilisation des organisations, avec en annexe l'accord de traitement (AMELEGAL sous-traitant du contenu des dossiers). |
| H | ★ H05 CGU cabinets | Les conditions propres aux cabinets : mandats, affectations, erreur de destination, bibliothèque de modèles, dossier propre, rapports, facturation indexée sur les mandats. |
| H | H06 Conditions générales de vente | Les aspects financiers de l'abonnement, pour une clientèle uniquement professionnelle. |
| H | H07 Déclaration d'accessibilité | L'engagement d'accessibilité (RGAA 4.1.2, niveau WCAG 2.1 AA). |
| H | H08 Actualités et contenus de lancement | Les articles de lancement du service, avec leur plan de publication. |
| H | H09 Éléments de référencement | Le SEO : mots-clés, balises de chaque page, données structurées, règles d'indexation (espaces connectés exclus). |
| I | I02 Plan de tests fonctionnels et juridiques | Les scénarios de recette juridique conduits par AMELEGAL à chaque version (T1, T2…), et la manière de consigner les écarts. |
| I | I05 Contrôle des documents produits | La grille de contrôle de chaque document généré (fiche, registre, dossier, AIPD, notification, rapport de cabinet, journal). |

## 4. Commun aux deux pays : spécifications développeur

| Fichier | Ce qu'il donne |
|---|---|
| ★ 00 Notice d'implémentation du référentiel.docx | Le mode d'emploi des fichiers machine pour GENKIBO. Règle cardinale : aucune valeur dans le code ; tout est chargé en base, rattaché à une juridiction et versionné. Identifiants stables. Structure d'un référentiel et exécution du moteur. |
| alertes.json | Les 13 types d'alerte (AL-01 à AL-13) en format machine : déclencheur, urgence, destinataires, juridictions. |
| bulles-information.json | Le contenu des 61 bulles d'information en format machine, avec les juridictions servies. Le glossaire en est généré. |
| registre-champs.csv | Les 70 champs de la fiche de registre : identifiant, type (12 types), valeurs possibles, caractère obligatoire par pays (O, R, C), lien avec le moteur. |

## 5. Livrables par pays (même liste au Togo et au Bénin)

| Fichier | Ce qu'il donne | Togo | Bénin |
|---|---|---|---|
| C01 Identification de la juridiction | La fiche d'identité de la juridiction et le texte de loi applicable. | Loi n° 2019-014 | Loi n° 2017-20, Livre 5 |
| C02 Sources | Le texte principal, les articles utiles et la doctrine de l'autorité. | Paramètres AIPD, registre et violations tirés des standards internationaux | Décisions et rapports de l'APDP, formulaire unique |
| C03 Autorité de contrôle | L'autorité, ses modalités de dépôt et ses délais d'instruction. | IPDCP ; modalités à renseigner | APDP ; dépôt électronique, postal ou guichet ; silence vaut acceptation ; validité des décisions |
| C04 Terminologie | Les libellés affichés et les intitulés officiels des régimes. | | |
| C05 Régimes de formalité | La liste des régimes, leur portée et leur couleur. | 5 régimes | 8 régimes |
| C06 Logigramme de qualification | L'ordre des questions du moteur, le champ qui alimente chaque question, les motifs affichés à l'utilisateur. | 8 questions, 5 sorties | 8 questions, 8 sorties |
| C07 Feuilles de route | Les étapes à suivre pour chaque régime. | | Ajoute le déclenchement automatique des annexes du formulaire |
| ★ C08 Analyse d'impact | Les critères qui rendent l'AIPD obligatoire. | Standards internationaux (pas de régime dans la loi) | Art. 428 ; présomption pour autorisation et décret ; consultation préalable (art. 429) |
| ★ C09 Violations de données | Le délai de notification, l'arbre de qualification du risque, les motifs. | Standards internationaux (la loi ne prévoit rien) | Standards internationaux |
| C10 Correspondant | Le statut et les missions du correspondant ou délégué. | | Sa désignation ouvre la voie à l'exemption de l'art. 408 |
| C11 Transferts internationaux | Le principe, les pays reconnus, les dérogations. | Avis motivé de l'IPDCP (art. 28) | Autorisation préalable (art. 407) et annexe 4 |
| C12 Registre | Le socle de champs du registre et la correspondance avec les rubriques. | Socle de 12 rubriques et mentions de la loi | Reprend tout le modèle de registre de l'APDP |
| C13 Indice de conformité : paramètres | Les poids des composantes, les seuils des libellés, la jauge. La sensibilisation est inactive (lot 2). | | |
| C14 Sous-traitance | Les mentions minimales du contrat de sous-traitance. | Art. 20, 51 et 52 | Annexe 1 du formulaire unique |
| C15 Version publiée du référentiel | La procédure de publication d'une version (Brouillon → En simulation → Publiée) et ce qu'il faut réunir avant. | | |
| D01 Notions appelant une bulle | La liste des notions qui ont une bulle, dont celles déterminantes pour le moteur. | 57 servies, 26 déterminantes | 60 servies, 29 déterminantes |
| D02 Contenu rédigé des bulles | Le texte de chaque bulle : définition, exemples, article cité, effet sur la qualification. | | |
| D03 Fiches d'explication développées | Les fiches longues, ouvertes depuis une bulle, pour les notions difficiles. | | |
| D04 Glossaire consolidé | Le glossaire des notions, généré à partir des bulles. | 57 notions | 60 notions |
| E01 Fiche de registre | Le gabarit imprimable d'une fiche de traitement. | | |
| E02 Registre complet | Les formats d'export du registre (PDF, CSV, XLSX) et l'ordre des colonnes. | | |
| ★ E03 Dossiers de formalité | Le contenu du dossier par régime, le pré-remplissage depuis la fiche, le contrôle de complétude avant « Prêt à être transmis ». | | Formulaire unique et annexes déclenchées par les champs |
| E04 Rapport d'analyse d'impact | La structure et les mentions du rapport d'AIPD (score, risque résiduel, avis du correspondant, validation). | | |
| ★ E05 Notifications de violation | Les deux modèles : notification à l'autorité et communication aux personnes, pré-remplis depuis la fiche d'incident. | | |
| ★ E06 Rapport d'activité de cabinet | Le rapport par client (remis à l'organisation) et le rapport consolidé interne : charge, échéances, mandats, facturation. | | |
| ★ F02 Modèles sectoriels de traitement | Les fiches modèles par secteur, tirées du registre type. Un modèle ne pré-remplit jamais un champ déterminant pour le moteur. | 156 fiches | 139 fiches |
| F03 Grille d'analyse d'impact détaillée | Les questions de l'AIPD en 4 sections et le calcul du score (gravité × vraisemblance, de 0 à 100). | | |
| I01 Jeu de cas de recette du moteur | Les cas de test du moteur, un par chemin du logigramme, et les cas d'opposition. | 9 cas | 12 cas |
| K01 Banque pédagogique complétée | Le contenu du jeu de sensibilisation (paniers de régimes, banque de cas). Lot 2. | Oui | Absent |
| K02 Barème, jauges et paliers | Le barème des sanctions, les jauges, les paliers et les minuteurs du jeu. Lot 2. | Oui | Absent |
| referentiel-togo.json / referentiel-benin.json | Le référentiel machine : régimes, questions, logigramme, conditions bloquantes, critères d'AIPD, paramètres de violation. C'est ce que le moteur exécute. | | |
| cas-de-recette-togo.csv / cas-de-recette-benin.csv | Les cas de I01 en format exécutable : une ligne par cas, une colonne par question, le régime, le motif et le besoin d'AIPD attendus. | 9 lignes | 12 lignes |

## 6. Sources juridiques par pays

| Pays | Fichier | Ce qu'il donne |
|---|---|---|
| Togo | Loi n° 2019-014 du 29 octobre 2019 (JO n° 26 ter) | Le texte de loi togolais sur la protection des données. |
| Togo | Registre_type_Togo.pdf / .xlsx | Le registre type togolais (156 fiches), matière des modèles sectoriels F02. |
| Bénin | Loi n° 2017-20 portant code du numérique | Le texte de loi béninois ; le Livre 5 traite des données personnelles. |
| Bénin | Decision-2019-N°020, 2022-0007, 2024-008, 2024-009 | Les décisions de l'APDP qui précisent la pratique (formalités, dispenses, durées de validité). |
| Bénin | Rapports d'activité 2022, 2023, 2024 | Les rapports annuels de l'APDP : pratique de l'autorité, chiffres, priorités. |
| Bénin | 2--FORMATION-DPO-2025-bn.pdf | Un support de formation pour les DPO. |
| Bénin | Pratique de la protection des données personnelles au Bénin (.docx, .pdf, « BON ») | L'étude d'AMELEGAL sur la pratique béninoise (plusieurs versions du même document). |
| Bénin | Decisiometre_Benin_A4_2pages.pdf | L'arbre de décision des formalités préalables (8 questions, 8 sorties), base du logigramme C06. |
| Bénin | FORMULAIRE-UNIQUE.pdf et LISTE.PIECES-A-JOINDRE | Le formulaire officiel de déclaration et la liste des pièces à joindre. |
| Bénin | ANNEXE 1 à 4 | Les annexes du formulaire : sous-traitance, communication, interconnexion, transfert. |
| Bénin | Analyse-dmpact-relative-a-la-protection-des-donnees.pdf | Le modèle d'analyse d'impact de l'APDP. |
| Bénin | FORMULAIRE-ENGAGEMENT-DE-CONFORMITE, Lettre.Engagement.DPO | L'engagement de conformité et la lettre d'engagement du DPO. |
| Bénin | Formulaire-de-signalement, Formulaire-complementaire-capture | Le signalement d'une violation et son formulaire complémentaire. |
| Bénin | Formulaire du consentement à la transmission électronique | L'accord pour recevoir les courriers de l'APDP par voie électronique. |
| Bénin | Fiche.Pratique.Mise-en-conformite | La fiche pratique de mise en conformité de l'APDP. |
| Bénin | Guide-delaboration-du-rapport-annuel | Le guide du rapport annuel du DPO. |
| Bénin | GUIDE-PRATIQUE-VIDEOSURVEILLANCE, guide-videosurveillance | Les règles applicables à la vidéosurveillance. |
| Bénin | certification_c2, labellisation_c2 | Les procédures de certification et de labellisation de l'APDP. |
| Bénin | Modèle de registre des activités de traitement (APDP) | Le modèle officiel de registre, repris intégralement par C12 Bénin. |
| Bénin | Modele-de-Registre-des-activites-de-Videosurveillance | Le registre propre à la vidéosurveillance. |
| Bénin | Registre_type_Benin.pdf / .xlsx | Le registre type béninois (139 fiches), matière des modèles sectoriels F02. |

## 7. Documents cités mais absents du dépôt

Le cahier des charges fonctionnel et technique (v1.0 du 12 août 2026), les familles A, B et J, G06 (abonnement), I03 (grille des écarts), I04, et K01 et K02 pour le Bénin.
