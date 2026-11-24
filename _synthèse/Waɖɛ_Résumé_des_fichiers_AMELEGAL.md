
# Waɖɛ — Résumé de chaque fichier AMELEGAL

Ce document résume, fichier par fichier, les **143 fichiers** fournis par AMELEGAL dans le dépôt (livrables version 1.0, septembre 2026). Chaque fichier a été lu en entier, tableaux compris. Les PDF scannés ont été lus page par page.

Chaque résumé donne :

- **En une phrase** : à quoi sert le fichier ;
- **Contenu** : les informations concrètes qu'il apporte (listes, chiffres, délais, articles de loi, règles, identifiants) ;
- **Utile pour** : la partie de l'application ou de la conception qui s'en sert.

Quand un même document existe en deux formats (xlsx et pdf, docx et pdf), il a un seul résumé.

| Partie | Dossier |
|---|---|
| 1 | Commun aux deux pays : références, identité visuelle, livrables D, E, F, G, spécifications développeur |
| 2 | Commun aux deux pays : contenus éditoriaux et juridiques (H), recette (I) |
| 3 | Togo : sources, livrables, spécifications |
| 4 | Bénin : livrables et spécifications |
| 5 | Bénin : sources et référentiels (loi, décisions et formulaires de l'APDP) |
| 6 | Anomalies relevées pendant la lecture |

# Partie 1 — dossier commun (références, identité visuelle, livrables D, E, F, G, spécifications développeur)

## Cartographie_traitements_donnees_personnelles_v3.docx
*Chemin :* `00 Commun aux deux pays/00 Références du projet/Cartographie_traitements_donnees_personnelles_v3.docx`

**En une phrase :** Nomenclature de référence (version 3, AMELEGAL, septembre 2026) des traitements de données personnelles que Waɖɛ propose par défaut aux organisations togolaises et béninoises selon leur secteur et leur taille.

**Contenu :**
- Document de travail interne : liste uniquement les intitulés des traitements. Les champs de la fiche (finalité, base légale, données, durées, formalité, analyse d'impact) sont renvoyés à un « lot distinct ». Aucun intitulé ne vaut avis juridique.
- Trois principes : une compétence ou un service n'est pas un traitement ; le référentiel est régional et non transposé du droit européen ou français (ajouts locaux : paie par porte-monnaie électronique, agrégateurs de paiement, identification des abonnés mobiles, agents de terrain, identifiants nationaux) ; chaque intitulé reçoit un code stable, à ne plus modifier une fois chargé (ex. G-RH-04, S-EME-01, C-TG-COM-ETA-01).
- Partie 1, socle générique proposé à toute organisation (151 codes G-) : recrutement REC (11), personnel et paie RH (17), carrière et relations sociales SOC (10), santé et sécurité au travail SST (8), clients et prospection CLI (11), numérique NUM (8), vente VTE (11), support SUP (7), système d'information SSI (13), sûreté des sites SUR (6), finance FIN (9), achats ACH (8), gouvernance GOV (12), études et innovation RD (6).
- Rubrique 1.15 « vigilance renforcée » : 14 marqueurs G-VIG-01 à 14 (biométrie, santé, condamnations, opinions, origine ethnique, surveillance continue, géolocalisation, profilage, notation automatisée, interconnexion, personnes vulnérables ou mineurs, identifiant national, transfert hors espace communautaire, sous-traitant étranger ou en nuage). Le moteur doit les traiter comme des facteurs de risque, pas comme des fiches.
- Partie 2, rubriques sectorielles qui s'ajoutent au socle (142 codes S-) : santé SAN (19), banque BQE (13), microfinance SFD (12), monnaie électronique EME (13), assurance ASS (12), télécoms TEL (14), éducation privée EDU (17), commerce extérieur et logistique LOG (15), ONG et projets OSC (16), associations et mutuelles ASO (11).
- Partie 3, collectivités territoriales (113 codes C-) : neuf rubriques pour le Togo (communes : état civil, urbanisme, services, environnement, funéraire, social, économie ; régions ; organes et personnel) et une rubrique pour les communes béninoises (C-BJ-COM-01 à 23). Au total, 406 intitulés codés.
- Textes cités en notes : loi togolaise n° 2019-014 (IPDCP), loi béninoise n° 2017-20, Livre cinquième (APDP), acte additionnel CEDEAO A/SA.1/01/10, convention de Malabo, codes du travail, AUDCIF, instruction BCEAO 008-05-2015, loi LBC-FT 2018-004, lois de décentralisation. Deux vérifications restent signalées : la facturation électronique certifiée au Togo et la loi béninoise de transposition LBC-FT.
- Anomalie : l'annexe annoncée des compétences « hors traitement » est absente. Le texte s'arrête sur un fragment tronqué : « rchives locales, qui n'a pas été instruit à ce stade. »

**Utile pour :** le catalogue de fiches types proposées à l'onboarding et au diagnostic, filtrées par secteur, ainsi que les codes de rattachement chargés dans le référentiel.

## Registre_original_socle_TG_BJ (.xlsx et .pdf)
*Chemin :* `00 Commun aux deux pays/00 Références du projet/Registre_original_socle_TG_BJ.xlsx` (et `.pdf`, même document en 235 pages A4)

**En une phrase :** Registre maître (version 4.0, septembre 2026, AMELEGAL Conseils) qui regroupe tous les intitulés de la cartographie v3 en fiches de traitement modèles, qualifiées pour le Togo et pour le Bénin. Les registres nationaux en sont extraits.

**Contenu :**
- 164 fiches et 709 finalités. Par partie : socle générique 49, sectoriel 60, collectivités Togo 25, collectivités Bénin 8, et une partie 4 « personne morale de droit public » de 22 fiches (préfixes SG-, SE-, CT-, CB-, PP-).
- Onglets : Notice, Registre (65 colonnes A à BM, à charger dans Waɖɛ), Finalités (une ligne par finalité), Cartographie v3 (418 intitulés : 392 rattachés à une fiche, 14 marqueurs de vigilance, 12 hors registre renvoyés à l'annexe 1), Marqueurs de vigilance, Bases légales (25 textes), Durées, Référentiels, Injection Waɖɛ, Synthèse, Fiches imprimables.
- Colonnes du registre : base juridique Togo (art. 14 de la loi 2019-014) et Bénin (art. 389 du code du numérique) ; valeur de repli Waɖɛ (Contrat 37, Obligation légale 52, Consentement 18, Intérêt légitime 15, Mission d'intérêt public 42) ; personnes ; classification APDP ; destinataires ; sous-traitants ; durée et fondement ; mesures de sécurité ; drapeaux de qualification.
- Drapeaux Togo : perso, registrePublic, public, sensible, bio, interconnexion, nni, recherche, souverain, transfert. Drapeaux Bénin : perso, domestique, dispense art. 410, public, sensible, penal, filiation, salairesImpots, bio, nni, difficultesSociales, interconnexion, recherche, profilage, categorieAPDP, souverain, transfert.
- Régimes calculés pour le Togo : déclaration à l'IPDCP 130, autorisation 27, acte réglementaire 7. Si un correspondant est désigné : pas de formalité (153) ou avis motivé pour transfert (11). Analyse d'impact requise pour 75 fiches.
- Régimes calculés pour le Bénin : déclaration (art. 405) 70, autorisation (art. 407) 53, décret (art. 411) 35, dispense (art. 410) 6. Si un délégué est désigné, les 70 déclarations deviennent des exemptions (art. 408). Analyse d'impact requise pour 89 fiches.
- Durées en deux couches. Ancrages contraignants : COMPTA (10 ans, AUDCIF art. 24), LBCFT (10 ans, art. 35), FINALITE, TRAVAIL, USAGE, ARCHIVES (non instruit). Repères européens indicatifs CNIL : CAND (2 ans), PAIE, REGPERS (5 ans), TEMPS, MANDAT, PROSPECT (3 ans), CONTRAT, COMPTA10, VIDEO (1 mois), LOGS (6 mois à 1 an), TRACEURS (13 et 25 mois), SATISF.
- L'onglet Injection fait correspondre chaque colonne à un champ de la maquette (ref, nom, finalite, base, dataClasses…). Il signale que le champ finalité doit devenir multivalué et que des champs restent à créer : description (art. 409 béninois), dureeIndicative, dureeSource. Les colonnes de régime et d'analyse d'impact servent de contrôle pour qualifier() et besoinAIPD().
- Dans le PDF, le nom Waɖɛ s'affiche « Warê » (police) et certaines lignes longues sont coupées en marge droite.

**Utile pour :** le chargement des fiches types dans le référentiel, les contrôles de non-régression du moteur de qualification, et les listes fermées (bases, classifications, catégories de données).

## Registre_type_traitements_Waɖɛ_TG_BJ (.xlsx et .pdf)
*Chemin :* `00 Commun aux deux pays/00 Références du projet/Registre_type_traitements_Waɖɛ_TG_BJ.xlsx` (et `.pdf`, même document en 193 pages A4)

**En une phrase :** Version antérieure (3.0, septembre 2026) du registre type des traitements modèles destiné à alimenter Waɖɛ, sans la partie « personne morale de droit public » ni l'onglet de contrôle de la cartographie.

**Contenu :**
- 142 fiches et 593 finalités : socle générique 49, sectoriel 60, collectivités Togo 25, collectivités Bénin 8.
- Onglets : Notice, Registre (colonnes A à BK, imprimable en A3 paysage), Finalités (avec le code de cartographie rattaché à chaque finalité), Bases légales (24 textes), Durées (6 ancrages seulement, avec leur statut de vérification), Référentiels, Injection Waɖɛ, Synthèse, Fiches imprimables.
- Colonnes identiques à celles du registre original, sauf les colonnes de durée indicative européenne, absentes.
- Régimes pour le Togo : déclaration 122, autorisation 18, acte réglementaire 2. Si un correspondant est désigné : 131 sans formalité et 11 avis motivés pour transfert. Analyse d'impact requise pour 59 fiches.
- Régimes pour le Bénin : déclaration 67, autorisation 50, décret (art. 411) 19, dispense 6. Si un délégué est désigné, les 67 déclarations deviennent des exemptions. Analyse d'impact requise pour 70 fiches.
- La notice précise que ce n'est ni un registre renseigné (les valeurs sont des points de départ) ni un avis juridique : les régimes résultent de l'application mécanique des deux logigrammes.
- Injection : retenir la colonne de base juridique selon la juridiction. La colonne « dispense art. 410 » doit être ventilée sur six drapeaux (dispPaie et suivants).
- Le PDF présente les mêmes défauts de rendu (« Warê », lignes coupées).

**Utile pour :** les données de démonstration et le chargement initial des fiches types. Il est remplacé par le registre original v4.0.

## waɖɛ-maquette-v2.html
*Chemin :* `00 Commun aux deux pays/00 Références du projet/waɖɛ-maquette-v2.html`

**En une phrase :** Maquette interactive monopage (environ 400 Ko, version 2.0) qui simule l'application Waɖɛ avec des données fictives et un moteur de qualification générique piloté par les référentiels des juridictions.

**Contenu :**
- Trois espaces, avec une bascule entre eux : organisation, cabinet et back-office. Deux niveaux d'usage : direct et accompagné (« guide »), plus un mode « Expliquer les questions ».
- Écrans de l'espace organisation :
  - Tableau de bord : indice de conformité, répartition des formalités, traitements récents, « À traiter », et un encadré de violation en cours prioritaire.
  - Registre des traitements et fiche de traitement en trois blocs : Identification ; Données et personnes concernées ; Destinataires, sous-traitance et transferts.
  - Assistant de formalités : questions du logigramme une à une avec chemin de réponses, puis « Ce qu'il faut faire », « Pourquoi ce régime », analyse d'impact, « Où déposer », étapes, et comparaison « Si ce traitement relevait d'un autre droit ».
  - Formalités (dossiers demandant une action, formalités dues sans dossier, pièces, étapes, suivi, dépôt) et analyses d'impact.
  - Violations de données : journal et fiche d'incident avec compte à rebours (« 46 h 12 min »), décisions, plan d'action et projet de notification.
  - Tâches et échéances, journal de conformité et glossaire.
  - Modules annoncés « Bientôt » : rédaction juridique, recherche et veille, sensibilisation.
- Espace cabinet : portefeuille (mandats actifs, conformité moyenne, violations en cours, mandats à renouveler, « Ce qui demande une action »), mandats (en cours, demandes adressées, ce que chaque niveau autorise), échéancier, modèles, rapports d'activité (par client, charge par consultant, clients sans intervention récente, facturation) et équipe (accès au dossier du cabinet). Un sélecteur permet d'ouvrir une organisation.
- Back-office :
  - Juridictions : régimes, logigramme, analyse d'impact, violations, indice, versions, couverture des champs déterminants, et rubriques à renseigner pour ouvrir une juridiction.
  - Référentiels.
  - Aides et glossaire (notions administrées).
  - Modèles documentaires.
  - Comptes (dont les mandats en vigueur).
  - Supervision : comptes actifs, traitements, juridictions publiées, mandats actifs, répartition par juridiction et usage des modules.
- Données fictives : GENKIBO SARL (TG), Clinique AGBADO SANTÉ (BJ), Commune de Kara (TG), Mairie de Sèmè-Podji (BJ), MicroFin Bénin SA (BJ), Fondation Zéphyr (TG) et le dossier propre d'Amelegal Conseils. Cinq mandats M1 à M5 (pilotage complet, contribution, consultation ; un mandat suspendu), environ 25 fiches et des modèles de cabinet.
- Le moteur qualifier() « ne connaît aucune règle de droit ». Il parcourt le logigramme du référentiel de la juridiction (champs dérivés, combinaisons ou, et, non) et restitue le régime, les motifs, la juridiction et la version. La saisie continue de la fiche et l'assistant appellent la même fonction. Les statuts de fiche vont de brouillon à soumise, qualifiée, visée, publiée et à réviser.

**Utile pour :** la conception de l'interface et des parcours (navigation, écrans, espaces cabinet et back-office) et la logique de référence du moteur de qualification.

## LOGOTYPE BLANC HORIZONTALE.png
*Chemin :* `00 Commun aux deux pays/01 Ware identité visuelle/LOGOTYPE BLANC HORIZONTALE.png`
Logo horizontal blanc sur fond transparent (symbole en « V » et mot « Waɖɛ by AMELEGAL »), en petite résolution (542 × 178 px), pour les fonds sombres ou verts.

## LOGOTYPE BLANC VERTCALE.png
*Chemin :* `00 Commun aux deux pays/01 Ware identité visuelle/LOGOTYPE BLANC VERTCALE.png`
Logo vertical blanc (symbole au-dessus, « Waɖɛ by AMELEGAL » dessous) sur fond transparent, en 350 × 284 px. Le nom du fichier comporte une faute de frappe (« VERTCALE »).

## LOGOTYPE HORIZONTALE.png
*Chemin :* `00 Commun aux deux pays/01 Ware identité visuelle/LOGOTYPE HORIZONTALE.png`
Logo horizontal en couleurs (verts #00901D et #00370B) sur fond transparent, en haute résolution (5420 × 1790 px).

## LOGOTYPE VERTICALE.png
*Chemin :* `00 Commun aux deux pays/01 Ware identité visuelle/LOGOTYPE VERTICALE.png`
Logo vertical en couleurs sur fond transparent, en haute résolution (3500 × 2840 px).

## WARE PROPO 1_1 à 1_7.jpg.jpeg (7 images)
*Chemin :* `00 Commun aux deux pays/01 Ware identité visuelle/WARE PROPO 1_1.jpg.jpeg` … `WARE PROPO 1_7.jpg.jpeg`
Sept planches carrées (1000 × 1000 px) de la proposition d'identité, qui reprennent les pages du logobook :
- 1_1 : logo sur fond blanc et sur fond vert ;
- 1_2 : logo vertical sur fond blanc ;
- 1_3 : logo blanc sur fond vert ;
- 1_4 : icônes d'application verte et vert foncé, avec pastille de notification « 3 » ;
- 1_5 : fond vert texturé avec le logo ;
- 1_6 : palette de couleurs ;
- 1_7 : polices.

## Wade LOGOBOOK.pdf
*Chemin :* `00 Commun aux deux pays/01 Ware identité visuelle/Wade LOGOBOOK.pdf`

**En une phrase :** Charte graphique de Waɖɛ (« Waɖɛ by AMELEGAL ») en 7 pages. Elle a le même contenu que les planches WARE PROPO 1_1 à 1_7.

**Contenu :**
- Déclinaisons du logo : horizontal et vertical, couleur et blanc, sur fond clair, vert ou texturé, et icône d'application.
- Couleurs : vert principal HEX 00901D, vert foncé HEX 00370B, un dégradé entre les deux, blanc HEX FFFFFB et noir HEX 0B0B0B.
- Polices : titres en Montserrat Bold, corps de texte en Open Sans Regular (Google Fonts).
- Le texte extractible est très réduit : l'essentiel du contenu est graphique.

**Utile pour :** les jetons de design de l'interface (couleurs, typographies), le logo, le favicon et l'icône d'application.

## D05 - Réserve d_interprétation et mentions communes.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/D - Aide contextuelle (socle commun)/D05 - Réserve d_interprétation et mentions communes.docx`

**En une phrase :** Textes types des réserves et mentions juridiques que Waɖɛ affiche sur ses résultats automatiques, ses bulles et ses documents.

**Contenu :**
- Fiche : commune aux deux juridictions ; fondement art. 12 et 36.3 du cahier des charges ; phase 4 ; bloquant ; version 1.0 du 6 septembre 2026 ; validation de la gérance requise.
- Réserve d'interprétation, portée par tout résultat automatique, toute bulle et tout document : « Cette aide est générale. Elle ne constitue pas un conseil juridique adapté à une situation particulière et ne se substitue pas à l'analyse d'un juriste. »
- Mention accompagnant un résultat du moteur : le résultat est indicatif, il procède du référentiel de la juridiction dans sa version en vigueur à la date de qualification, et un utilisateur habilité peut retenir un autre régime en énonçant son motif.
- Mention « standards internationaux » : elle se déclenche automatiquement quand un paramètre porte source=standard_international. Elle couvre aujourd'hui le délai de notification des violations (dans les deux pays), les critères d'analyse d'impact au Togo et le seuil de volume de personnes.
- Mentions des documents : date d'édition, auteur, cabinet sous mandat, juridiction, texte appliqué et version du référentiel.
- Mention des attestations de sensibilisation : « atteste d'une participation, non d'une compétence », sans valeur de certification.

**Utile pour :** les composants de résultat du moteur, les bulles d'information et les pieds de page des documents produits.

## E07 - Mentions transverses des exports.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/E - Modèles documentaires (socle commun)/E07 - Mentions transverses des exports.docx`

**En une phrase :** Liste des mentions obligatoires sur tout document produit par Waɖɛ, avec leur emplacement et leur condition d'affichage.

**Contenu :**
- Fiche : commune ; fondement art. 26.4 et 12 ; phase 7 ; bloquant ; version 1.0.
- En-tête, toujours présent : identité du document (type, référence du dossier, identité Waɖɛ), organisation, juridiction et texte de référence.
- Pied de page :
  - version du référentiel, si le document porte un résultat du moteur ;
  - date et heure d'édition ;
  - auteur ;
  - mention du mandat (cabinet et référence), si le document est produit sous mandat ;
  - réserve d'interprétation D05 ;
  - pagination « Page n sur N », si plus d'une page ;
  - confidentialité, paramétrable par l'organisation.
- Mention de source « standard international », placée en regard du résultat concerné.
- Documents concernés : fiche de registre, registre complet, dossier de formalité, rapport d'analyse d'impact, notification de violation, communication aux personnes, rapport d'activité de cabinet, export du journal, attestation de sensibilisation.
- Règles :
  - aucun document sans la juridiction et le texte appliqué ;
  - chaque production est consignée au journal ;
  - la mention du cabinet doit être apparente, non en note ;
  - les mentions sont administrables en back-office ;
  - aucun champ export_registre=non n'apparaît sur un document.

**Utile pour :** le moteur de génération des PDF et exports, et le journal de conformité.

## F01 - Diagnostic guidé d_amorçage.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/F - Questionnaires et contenus métier/F01 - Diagnostic guidé d_amorçage.docx`

**En une phrase :** Questionnaire de 13 questions (environ 10 minutes, étape 6 de l'onboarding) qui crée les premières fiches de traitement en brouillon, en langage courant.

**Contenu :**
- Fiche : commune ; fondement art. 14 ; phases 6 et 11 ; bloquant ; version 1.0. Ne produit jamais de fiche publiée : tout reste au statut Brouillon.
- Questions sur l'organisation et ses traitements :
  - Q1 activité (choisit le jeu de fiches types) ;
  - Q2 effectif ;
  - Q3 personnel salarié (paie, dossier du personnel) ;
  - Q4 recrutement ;
  - Q5 fichiers de clients, usagers, patients ou élèves ;
  - Q6 prospection et communications ;
  - Q7 caméras et contrôle d'accès.
- Questions qui alimentent le moteur :
  - Q8 santé, données judiciaires ou syndicales (indicateur de données sensibles) ;
  - Q9 identifiant national ou biométrie (caractéristiques appelant l'autorisation) ;
  - Q10 hébergement ou consultation depuis l'étranger (transfert) ;
  - Q11 prestataires (sous-traitance) ;
  - Q12 administration ou mission de service public (qualité de l'organisme) ;
  - Q13 correspondant désigné auprès de l'autorité.
- Q8, Q9, Q10, Q12 et Q13 alimentent directement le moteur. « Je ne sais pas » ne vaut jamais oui : la réponse vaut non et ouvre une tâche de vérification affectée au correspondant.
- Pas de champ juridique brut ; les notions déterminantes portent leur bulle. Chaque fiche indique son origine et son taux de complétude. Le parcours est interruptible et affiche « Étape n sur 13 ».
- Le tronc est commun aux deux pays ; Q8, Q9 et Q12 suivent le référentiel de la juridiction. Le questionnaire est administrable en back-office.
- Sortie : nombre de fiches créées, champs manquants les plus fréquents et une seule action recommandée (étape 8 de l'onboarding).

**Utile pour :** le parcours d'onboarding et la génération initiale du registre.

## F04 - Trames de collecte auprès des services métier.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/F - Questionnaires et contenus métier/F04 - Trames de collecte auprès des services métier.docx`

**En une phrase :** Six questionnaires imprimables, à remplir hors ligne par les services métier, générés depuis le mode « tout expliquer ».

**Contenu :**
- Fiche : commune ; fondement art. 13.4 et 34.6 ; phase 11 ; criticité Recommandé ; version 1.0.
- Recensement d'un traitement, pour tout service : ce que vous faites, pourquoi, avec quelles informations, sur qui, qui y accède, combien de temps.
- Ressources humaines : recrutement, dossier individuel, paie, absences, discipline, formation, santé au travail.
- Commercial et relation client : prospection, contrats, facturation, réclamations, fidélité, satisfaction.
- Systèmes d'information : comptes et habilitations, journalisation, sauvegardes, prestataires, hébergement et localisation.
- Sécurité et locaux : vidéosurveillance, contrôle d'accès, visiteurs, alarme. Prestataires (achats et juridique) : liste des prestataires, prestation confiée, contrat, pays d'exécution.
- Règles de rédaction :
  - une question par information, sans terme juridique, avec l'aide imprimée en regard ;
  - chaque question indique le champ de fiche qu'elle alimente ;
  - les questions déterminantes portent un repère visuel et ne peuvent rester vides ;
  - un encadré rappelle que la réponse engage le service ;
  - les trames sont administrables et rattachées à une juridiction.

**Utile pour :** les exports de questionnaires (espace organisation et modèles de cabinet) et la saisie des fiches.

## G01 - Méthode de calcul de l_indice de conformité.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G01 - Méthode de calcul de l_indice de conformité.docx`

**En une phrase :** Formule de l'indice de conformité : un pourcentage égal à la moyenne pondérée de quatre ratios.

**Contenu :**
- Fiche : commune ; fondement art. 25.2 ; phases 4 et 10 ; bloquant ; version 1.0. Le calcul porte sur l'organisation active, toutes juridictions confondues, et chaque ratio est borné entre 0 et 1.
- completude_registre (35 %) : somme des taux de complétude des fiches publiées, divisée par le nombre de fiches publiées.
- formalites_accomplies (35 %) : traitements dont la formalité est Acceptée, Récépissé reçu, Acceptation tacite ou Dispense documentée, divisés par les traitements qualifiés.
- aipd_realisees (20 %) : analyses validées, divisées par les traitements qui appellent une analyse d'impact. violations_traitees (10 %) : violations closes dans le délai, divisées par les violations des 12 derniers mois.
- Si un dénominateur est nul, la composante est neutralisée et son poids est redistribué proportionnellement. Le détail du calcul s'affiche à la demande.
- Seuils : Action requise de 0 à 39, À surveiller de 40 à 64, Bon, à consolider de 65 à 84, Solide de 85 à 100.
- Composantes, poids et seuils sont administrables par juridiction. La composante de sensibilisation reste inactive tant que le module du lot 2 n'est pas livré.

**Utile pour :** le tableau de bord, le portefeuille du cabinet (conformité moyenne) et la rubrique indice du référentiel.

## G02 - Règles de déclenchement des alertes.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G02 - Règles de déclenchement des alertes.docx`

**En une phrase :** Définition des 13 types d'alerte du lot 1 : fait générateur, déclenchement, rappel, canal, urgence et libellé affiché.

**Contenu :**
- Fiche : commune ; fondement art. 25.5, 28.3 et 32 ; phases 8 et 10 ; bloquant ; validation de la gérance requise. Onze types viennent de l'art. 25.5. Deux sont ajoutés pour le droit béninois (AL-12 et AL-13) et ne sont servis que là où le référentiel les prévoit.
- Les 13 alertes sont détaillées (avec urgence et délais) sous alertes.json, plus bas.
- Libellés à variables, par exemple « Violation à notifier avant le {echeance}. Il reste {reste}. » ou « Cette fiche ne peut être publiée : {champs} manquent. »
- Paramétrables par l'organisation : AL-03 (délai), AL-04 (durée), AL-08 (période) et AL-12 (préavis).
- Ordre d'affichage par urgence (1 = la plus urgente) puis par échéance la plus proche. Au plus 3 alertes sur le tableau de bord au niveau accompagné, sans limite au niveau direct.
- Chaque alerte mène directement à l'écran d'action. Dans le portefeuille, elle porte le nom de l'organisation. Une alerte close par l'action disparaît seule ; une alerte ignorée doit être motivée et le motif est consigné. Seuils, délais et canaux sont administrables en back-office.

**Utile pour :** le moteur d'alertes, le tableau de bord, l'échéancier du cabinet et les notifications par courriel.

## G03 - Statuts et cycles de vie.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G03 - Statuts et cycles de vie.docx`

**En une phrase :** Liste fermée des états de chaque objet métier de Waɖɛ.

**Contenu :**
- Fiche : commune ; fondement art. 28.2 et annexe 2 ; phases 4 et 8 ; bloquant ; version 1.0.
- Fiche de traitement : Brouillon, Soumise à qualification, Qualifiée, Visée, Publiée au registre, À réviser, Archivée.
- Dossier de formalité : Brouillon, À valider, Prête à être transmise, Envoyée, Accusé de réception reçu, Observations reçues, En cours de traitement, Acceptée, Acceptation tacite, Rejetée, À régulariser.
- Analyse d'impact : À réaliser, En cours, Soumise à validation, Validée, À réviser. Violation : Déclarée, En cours de qualification, Notifiée, Non notifiable, En cours de traitement, Résolue, Close et archivée.
- Tâche : À faire, En cours, Terminée, Ignorée avec justification. Mandat : Demandé, Accepté, Refusé, Actif, Suspendu, Révoqué, Expiré. Référentiel : Brouillon, En simulation, Publié, Remplacé par une version postérieure.
- « Acceptation tacite » est ajoutée pour le silence valant acceptation au Bénin (autorite.silence_vaut_acceptation à vrai). Ce statut est distinct d'« Acceptée » et n'est jamais atteint au Togo.
- Chaque changement de statut est horodaté, attribué (avec le cabinet le cas échéant) et journalisé. Une frise de jalons retrace le dossier. Une modification substantielle fait passer la fiche « À réviser » et, là où c'est exigé, ouvre une nouvelle déclaration. Une décision à durée limitée déclenche une alerte de renouvellement.

**Utile pour :** les machines à états du modèle de données, les badges de statut et la frise des dossiers.

## G04 - Matrice des habilitations et circuit de validation.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G04 - Matrice des habilitations et circuit de validation.docx`

**En une phrase :** Matrice des droits par rôle (organisation et cabinet), plafonnement par niveau de mandat et circuit de validation des fiches.

**Contenu :**
- Fiche : commune ; fondement art. 6.5 et 6.7 ; phases 3 et 6 ; bloquant ; version 1.0.
- Cinq rôles d'organisation : Administrateur d'organisation, Correspondant, Responsable de traitement, Contributeur métier, Lecteur-auditeur. La matrice couvre 29 actions, notées X (permis), P (permis dans le périmètre affecté) ou « - » (interdit). En cas de cumul de rôles, le droit le plus favorable s'applique ; un compte appartient à une seule organisation ou à un seul cabinet.
- Exemples de la matrice :
  - seul le Responsable de traitement vise une fiche ;
  - seul le Correspondant publie au registre ;
  - seuls le Correspondant et le Responsable qualifient, déposent, valident une analyse d'impact et notifient une violation ;
  - tous les rôles sauf le Lecteur peuvent déclarer une violation ;
  - seul l'Administrateur invite des utilisateurs, paramètre les alertes et gère les mandats.
- Quatre rôles de cabinet :
  - Administrateur de cabinet et Consultant référent : prérogatives du Correspondant ;
  - Consultant contributeur : prérogatives du Contributeur métier ;
  - Consultant lecteur : prérogatives du Lecteur-auditeur.
- Le plus restrictif du rôle et du mandat l'emporte. L'accès suppose un mandat actif et une affectation nominative.
- Plafond par niveau de mandat :
  - Consultation : lecture et export ;
  - Contribution : création et modification, sans qualifier, viser, publier ni déposer ;
  - Pilotage complet : prérogatives du Correspondant, sauf les actions réservées par l'organisation (visa, notification de violation, révocation de mandat).
- Circuit en 6 étapes : 1 Brouillon, 2 Soumise à qualification (contrôle de complétude), 3 Qualifiée (régime motivé, besoin d'analyse d'impact statué, tâches), 4 Visée (étape désactivable), 5 Publiée, 6 À réviser. Une petite structure peut fusionner les étapes 2 à 4.
- Recette : tester chaque rôle et chaque action, y compris par manipulation d'adresse ; croiser les 4 rôles de cabinet avec les 3 niveaux de mandat ; vérifier un contrôle côté serveur à chaque requête et l'absence de fuite par identifiant d'objet.

**Utile pour :** le contrôle d'accès (RBAC), l'espace cabinet et le workflow de publication des fiches.

## G05 - Régime des mandats.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G05 - Régime des mandats.docx`

**En une phrase :** Règles du mandat par lequel une organisation ouvre son dossier à un cabinet.

**Contenu :**
- Fiche : commune ; fondement art. 7 ; phases 3 et 6 ; bloquant ; version 1.0.
- Trois dimensions :
  - niveau : Consultation, Contribution ou Pilotage complet ;
  - périmètre : toute l'organisation, certains services ou directions, ou certaines entités du groupe (un mandat RH ne donne aucun accès au commercial) ;
  - durée : indéterminée ou à terme fixe. Un mandat à terme expire automatiquement, avec alerte aux deux parties 30 puis 7 jours avant.
- Le mandat est consenti par l'organisation seule. Aucun rôle de cabinet ou de back-office ne peut s'octroyer, étendre ou prolonger un mandat.
- Le mandat est exprès : il ne prend effet qu'après acceptation par un administrateur d'organisation authentifié. Il est révocable à tout moment, sans préavis ni motif, avec effet immédiat, sessions ouvertes comprises.
- Il ne transfère pas la propriété des données et ne vaut pas désignation comme correspondant. La suspension coupe les accès sans mettre fin au mandat ; seule l'organisation la lève.
- Actions réservables par défaut, même en pilotage complet : visa avant dépôt, notification d'une violation, révocation d'un mandat.
- Traçabilité : chaque action sous mandat est journalisée avec la personne physique, le cabinet et la référence du mandat. Cette mention subsiste après la fin du mandat.

**Utile pour :** le module de mandats, le contrôle d'accès des consultants et le journal de conformité.

## G07 - Périodes et seuils paramétrables.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/G - Règles de gestion/G07 - Périodes et seuils paramétrables.docx`

**En une phrase :** Valeurs par défaut des délais et seuils de Waɖɛ, avec leur portée et le niveau autorisé à les modifier.

**Contenu :**
- Fiche : commune ; fondement art. 25.5, 27.4 et 30.4 ; phases 8 et 10 ; bloquant ; version 1.0.
- Revue des fiches : 12 mois, ou 6 mois pour les régimes lourds (autorisation, décret, acte réglementaire). Modifiable par l'administrateur d'organisation.
- Dossier sans suite : délai d'instruction de la juridiction plus 15 jours (back-office). Formalité non déposée : 30 jours (organisation).
- Seuil de volume de personnes concernées : 10 000 (par juridiction). Rappels du délai de notification à 25, 50, 75 et 90 % du délai écoulé.
- Préavis d'échéance de mandat : 30 puis 7 jours (réglage global). Préavis d'expiration d'une décision : 60 puis 15 jours (par juridiction). Relance des tâches en retard : tous les 7 jours.
- Sécurité : expiration de session après 30 minutes d'inactivité ; blocage temporaire de 15 minutes après 5 tentatives de connexion.
- Règles :
  - aucune valeur n'est codée en dur ;
  - une valeur fixée par l'organisation ne peut être moins protectrice que celle de la juridiction ;
  - aucune expiration de session pendant la saisie d'une violation ;
  - chaque modification est horodatée et consignée.

**Utile pour :** la table de paramètres du back-office, le moteur d'alertes et la sécurité de session.

## 00 Notice d_implémentation du référentiel.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/00 Notice d_implémentation du référentiel.docx`

**En une phrase :** Notice destinée à GENKIBO (version 1.0 du 6 septembre 2026) qui explique comment charger et exécuter les référentiels machine des juridictions et le modèle de champs du registre.

**Contenu :**
- Fichiers décrits : referentiel-togo.json et cas-de-recette-togo.csv (9 cas) ; referentiel-benin.json et cas-de-recette-benin.csv (12 cas) ; registre-champs.csv (70 champs).
- Règle cardinale : aucune valeur dans le code. Les valeurs sont chargées en base, rattachées à une juridiction et versionnées (art. 8.1 et 27.6). Les identifiants de régime, de question et de critère sont stables, pour qu'une qualification ancienne reste explicable.
- Clés d'un référentiel : meta, juridiction, sources, autorite, terminologie, regimes, logigramme, feuilles_de_route, aipd, violations, correspondant, transferts, indice.
- Exécution du logigramme :
  - partir de logigramme.entree et suivre les branches oui ou non ;
  - une branche type=question renvoie à la question cible, une branche type=sortie donne le régime avec son motif ;
  - une question « multiple » est vraie dès qu'une option est cochée ;
  - condition_bloquante force la réponse à faux (exemple : l'exemption béninoise est fermée aux autorités publiques) ;
  - les règles transverses ajoutent des obligations sans changer la sortie.
- Le résultat comprend toujours : juridiction, version, régime, motifs, besoin d'analyse d'impact, autorité, feuille de route et réserve d'interprétation.
- Comparaison Togo et Bénin :

  | Point | Togo | Bénin |
  |---|---|---|
  | Questions du logigramme | 8 | 8 |
  | Sorties | 5 | 8, dont 2 exclusions |
  | Autorité | IPDCP | APDP |
  | Personne désignée | correspondant | délégué |
  | Effet de la désignation | dispense, sauf transfert | voie de l'exemption, avec décision de l'autorité |
  | Délai d'instruction | 1 mois prorogeable une fois | 60 jours (+30, doublés en cas d'investigation) |
  | Silence de l'autorité | sans effet | vaut acceptation |
  | Validité des décisions | non prévue | 2 ans |
  | Analyse d'impact | standards internationaux | art. 428 et 429 |
  | Violations | standards internationaux | standards internationaux |

- Colonnes de registre-champs.csv : id, niveau, bloc, libelle_affiche, type, valeurs, obligatoire_TG et obligatoire_BJ (O, R, C ou vide), alimente_moteur (bulle obligatoire), juridiction (TG, BJ ou commun), rubrique_socle_commun, export_registre, aide_id, note. Le socle de 12 rubriques reprend le modèle de registre de l'APDP béninoise.
- Recette :
  - exécuter les cas de recette ;
  - obtenir le même régime par la fiche et par l'assistant ;
  - créer une juridiction de test sans toucher au code ;
  - aucun champ moteur sans bulle ;
  - lisibilité des qualifications anciennes ;
  - compte à rebours de notification pour deux délais distincts et persistant après déconnexion.
- Réserve : les textes d'application togolais ne sont pas publiés et le Livre cinquième béninois ne fixe pas de délai de notification. Les standards internationaux sont donc retenus.

**Utile pour :** l'architecture du moteur de qualification, le schéma de base des référentiels et le plan de recette.

## alertes.json
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/alertes.json`

**En une phrase :** Version machine du livrable G02 : un tableau JSON de 13 objets d'alerte.

**Contenu :**
- Champs de chaque objet : code, objet, fait_generateur, declenchement, rappel, canal, urgence, libelle, parametrable_organisation.
- AL-01 Violation à notifier : dès la déclaration ; application et courriel ; urgence 1.
- AL-02 Analyse d'impact requise et non réalisée : à la qualification ; urgence 2.
- AL-03 Formalité qualifiée non déposée : 30 jours après la qualification ; courriel ; urgence 3 ; délai paramétrable.
- AL-04 Dossier déposé sans suite : délai d'instruction plus 15 jours ; urgence 4 ; durée paramétrable.
- AL-05 Fiche incomplète : base juridique, durée ou sécurité manquantes, à la soumission ; urgence 5.
- AL-06 Sous-traitant sans contrat conforme : à la qualification ; urgence 6.
- AL-07 Transfert non encadré : à la qualification ; urgence 6.
- AL-08 Fiche non revue : 12 mois par défaut ; urgence 7 ; période paramétrable.
- AL-09 Évolution du référentiel : à la publication ; courriel ; urgence 3.
- AL-10 Mandat à échéance : 30 puis 7 jours avant ; courriel ; urgence 4.
- AL-11 Tâche en retard : rappel tous les 7 jours ; urgence 8.
- AL-12 Décision arrivant à expiration : 60 puis 15 jours avant ; courriel ; urgence 4 ; préavis paramétrable.
- AL-13 Modification appelant une nouvelle déclaration : urgence 3.
- Contenu identique au tableau de G02.

**Utile pour :** le chargement des types d'alerte et de leurs libellés dans le moteur d'alertes.

## bulles-information.json
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/bulles-information.json`

**En une phrase :** Contenu des bulles d'information et du glossaire (version 1.0, 6 septembre 2026, AMELEGAL SARL) : un socle commun et des surcharges par juridiction.

**Contenu :**
- Structure : meta (règle d'héritage, réserve d'interprétation), socle (61 notions) et surcharges TG et BJ.
- Champs d'une notion : id, domaine, libelle, determinante, champs (identifiants de registre-champs liés), definition, exemples, contre_exemple, consequence, fiche_developpee.
- Les 61 notions se répartissent en domaines : Objet du traitement, Licéité, Nature des données, Qualité de l'organisme, Correspondant, Formalités, Conservation et sécurité, Transferts, Analyse d'impact, Violations, Cadre de l'intervention. Sept d'entre elles ont une fiche développée : donnée personnelle, base juridique, données sensibles, correspondant, transfert international, analyse d'impact, violation.
- Règle d'héritage : une notion non surchargée reprend la définition du socle. Une surcharge avec reference=null est servie sans article de loi, et sa conséquence indique la source retenue.
- Surcharges Togo (39), loi n° 2019-014 :
  - articles cités : art. 4 (définitions), art. 8 (autorisation), art. 75 à 78 (correspondant, dispense sauf transfert), art. 6 (récépissé), art. 28 à 31 (transferts) ;
  - le silence de l'IPDCP ne vaut pas acceptation ;
  - analyse d'impact (art. 76, 3°), violations et délai de 72 heures relèvent des standards internationaux ;
  - pas d'exclusion domestique ;
  - aucune norme simplifiée publiée.
- Surcharges Bénin (30), loi n° 2017-20, Livre cinquième :
  - articles cités : art. 380 à 382 (champ et exclusion domestique), art. 394 (sensibles), art. 407 (autorisation), art. 408 (exemption avec décision de l'APDP), art. 410 (dispenses), art. 411 (décret), art. 412 (silence vaut acceptation) ;
  - analyse d'impact : art. 428 et 429 ;
  - délai de notification de 72 heures selon les standards internationaux.
- Les notions propres à l'autre pays sont marquées « Non servie ici ».

**Utile pour :** les infobulles (hint), le glossaire, les aides du diagnostic et des trames, et le contrôle de couverture des champs déterminants.

## registre-champs.csv
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/_spécifications développeur/registre-champs.csv`

**En une phrase :** Modèle de données de la fiche de traitement : 70 champs, au format CSV séparé par des points-virgules et encodé en UTF-8 avec BOM.

**Contenu :**
- 14 colonnes : id, niveau, juridiction, bloc, libelle_affiche, type, valeurs, obligatoire_TG, obligatoire_BJ, alimente_moteur, rubrique_socle_commun, aide_id, export_registre, note.
- Préfixes d'identifiant : org.*, rt.*, dpo.* et t.*.
- Niveau : 26 champs organisation (saisis une fois et repris dans chaque fiche) et 44 champs traitement.
- Juridiction : 60 champs communs, 4 propres au Togo (registre d'information du public, art. 8, correspondant pour ce traitement, mission régalienne) et 6 propres au Bénin (cadre domestique, dispense art. 410, norme simplifiée, art. 407, objets art. 411, exemption art. 408).
- Blocs d'affichage : Organisme (12), Responsable de traitement (5), Correspondant ou délégué (9), Bloc 1 Identification (16), Traçabilité interne (1), Bloc 2 Données et personnes (10), Bloc 3 Destinataires et qualification (17).
- 12 types utilisés : texte (16), booleen (12), liste (11), liste multiple (8), tableau (7), texte long (3), date (3), courriel (3), telephone (3), tranche (2), fichier (1), fichiers (1).
- Les 12 rubriques du socle commun suivent le modèle APDP :
  1. Informations sur l'organisme ;
  2. Coordonnées du responsable ;
  3. Nom et coordonnées du délégué ;
  4. Activité (code, dénomination, date de création, finalités, fondement) ;
  5. Principes relatifs au traitement (consentement, droits des personnes) ;
  6. Données traitées (et classifications) ;
  7. Cibles et personnes concernées ;
  8. Durées de conservation ;
  9. Liste des personnes ayant accès (et sous-traitance) ;
  10. Communication à d'autres organismes ;
  11. Transfert vers un pays tiers ;
  12. Mesures de sécurité.

  S'y ajoutent des en-têtes : référence de la fiche, référence de la décision, validité de la décision.
- 21 champs alimentent le moteur. Leurs notes indiquent les questions concernées (TG-Q1 à Q8, BJ-Q1 à Q8). Par exemple, t.donnees_sensibles alimente TG-Q5 et BJ-Q6 ; org.mission_service_public ferme l'exemption BJ-Q8.
- Caractère obligatoire au Togo : O 43, R 11, C 10, vide 6. Au Bénin : O 50, R 5, C 11, vide 4.
- Un seul champ a export_registre=non : t.origine_cartographie (identifiant de production interne).
- Remarques :
  - la notice annonce 11 types, alors que le CSV utilise aussi « fichiers » ;
  - les aide_id « categorie_donnees » et « droits_personnes » n'existent pas dans bulles-information.json ;
  - org.nature_publique renvoie à la bulle mission_service_public plutôt qu'à personne_publique.

**Utile pour :** le schéma de base de données de la fiche, le formulaire en trois blocs, les règles d'export et la liaison entre champs, logigramme et bulles.

# Partie 2 — contenus éditoriaux et juridiques (H), recette et validation (I)

## H01 - Textes des pages publiques.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H01 - Textes des pages publiques.docx`

**En une phrase :** Fiche AMELEGAL (v1.0 du 26/09/2026, phase 11, préalable à la mise en production, à valider par la gérance) qui fournit, prêts à saisir au back-office, tous les textes de la partie publique de Waɖɛ, zone par zone de la maquette.

**Contenu :**
- Parti pris : structure inspirée de Dastra, Adequacy, Provacy, Legal Data Drive, InTouch Group, mais avec le droit applicable affiché au premier plan, aucune preuve sociale fabriquée (ni logo, ni témoignage, ni chiffre) et aucune promesse de résultat juridique (réserve d'interprétation du livrable D05 sous le moteur).
- Accueil en 13 sections : bandeau facultatif « Waɖɛ couvre le Togo et le Bénin », H1 « Pour chaque traitement, la bonne formalité. », boutons « Créer mon espace organisation » / « Découvrir l'offre cabinets » / « Demander une démonstration », constat, moteur, 8 cartes de fonctionnalités (registre, qualification, dossiers de formalité, analyse d'impact en 4 étapes, incidents, tableau de bord, journal, tâches et alertes), deux offres, 8 publics cibles, juridictions, 4 étapes, confiance et sécurité, actualités, 6 questions fréquentes, section finale.
- Tableau des juridictions : Togo, loi n° 2019-014 du 29/10/2019, IPDCP ; Bénin, loi n° 2017-20 (code du numérique, Livre cinquième), APDP. La phrase « D'autres juridictions de la CEDEAO sont en préparation » est à retirer si aucune ouverture n'est décidée (CDC art. 8.5).
- FAQ : Waɖɛ ne remplace pas un juriste ; le rôle « Correspondant » de l'outil ne vaut pas désignation légale ; Waɖɛ ne dépose pas les dossiers auprès de l'IPDCP/APDP ; un traitement bi-pays reçoit deux qualifications côte à côte ; l'accès du support AMELEGAL est tracé et notifié.
- Pages « Waɖɛ » (finalité, 5 principes, ce que Waɖɛ fait et ne fait pas : pas de dépôt, pas de désignation, pas de certification, pas de consultation juridique), « Offre organisations » (5 rôles : administrateur, correspondant, responsable du traitement/délégataire, contributeur métier, lecteur ; circuit contributeur, correspondant, visa, registre ; niveaux « accompagné » et « direct » ; mandat de niveau consultation/contribution/pilotage complet), « Offre cabinets » (portefeuille, organisation active toujours affichée, 2FA obligatoire non désactivable), « AMELEGAL » (9 domaines d'intervention, étude Bénin d'août 2026 ; mention de GENKIBO non retenue par défaut).
- Contact : AMELEGAL SARL, Lomé, Avepozo ; +228 91 86 35 35 / +228 70 79 34 34 ; contact@amelegalconseils.com ; formulaire de 9 champs (objet en liste à 6 valeurs, pays Togo/Bénin/autre CEDEAO/autre, message limité à 2 000 caractères, case newsletter non précochée) ; conservation 3 ans après le dernier échange.
- En-tête (6 rubriques, lien externe, « Se connecter », « Créer un compte », menu replié sur mobile) et pied de page (7 colonnes ; liens légaux dont la déclaration d'accessibilité, obligatoire sur toutes les pages ; CGV affichées seulement quand elles seront applicables).
- Écrans d'accès : code 2FA à six chiffres, message d'erreur générique avec suspension temporaire, 3 types de création de compte, case CGU obligatoire non précochée, courriel de vérification (durée de validité à fixer).
- Variables surlignées à renseigner : adresse du service, réseaux sociaux, hébergement (A06), prix (G06). Les affirmations de sécurité ne sont publiables qu'après vérification en recette (CDC art. 45.1).

**Utile pour :** site vitrine public, back-office de contenus, écrans de connexion et d'inscription.

## H02 - Mentions légales.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H02 - Mentions légales.docx`

**En une phrase :** Texte à publier de la page « Mentions légales » de Waɖɛ (v1.0 du 26/09/2026, d'après le pied de page du document ; pas de fiche de livrable).

**Contenu :**
- Éditeur : AMELEGAL SARL, SARL de droit togolais, siège Lomé, Avepozo ; capital, numéro RCCM et NIF à compléter.
- Représentant légal et directeur de la publication : M. Essowèdeou SIGNAN, gérant.
- Coordonnées : +228 91 86 35 35 / +228 70 79 34 34, contact@amelegalconseils.com, amelegalconseils.com.
- Hébergeur : OVH SAS (capital 50 000 000 €, RCS Lille Métropole 424 761 419, 2 rue Kellermann, 59100 Roubaix) ; centre de données et pays à compléter.
- Conception juridique et fonctionnelle : AMELEGAL ; mention de GENKIBO pour la conception technique à décider (renvoi à H01 section 5).
- Contact données personnelles : adresse dédiée à créer (ex. donnees@amelegalconseils.com), sinon contact@.
- Propriété intellectuelle d'AMELEGAL sur les marques, référentiels, aides contextuelles et modèles ; les textes de loi cités restent publics, avec leur source.
- Liens externes non garantis ; contenus juridiques publics à visée d'information générale, sans valeur de consultation ; droit togolais applicable.

**Utile pour :** page publique /mentions-legales et pied de page.

## H03 - Politique de confidentialité.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H03 - Politique de confidentialité.docx`

**En une phrase :** Texte à publier de la politique de confidentialité de Waɖɛ pour les traitements dont AMELEGAL est responsable, au regard de la loi togolaise n° 2019-014 et du Livre 5 du code du numérique béninois (v1.0 du 26/09/2026).

**Contenu :**
- Qualification : AMELEGAL est responsable pour les comptes, la sécurité, la facturation, etc. ; elle est sous-traitante pour le contenu des dossiers de conformité, dont l'organisation (ou le cabinet pour son dossier propre) est responsable. Variantes A/B pour le correspondant d'AMELEGAL.
- Tableau de 10 finalités avec données, fondement et durée : compte (durée du compte, désactivation après 24 mois sans connexion, puis suppression) ; journal de conformité (abonnement + 5 ans) ; historique d'un cabinet après le mandat (5 ans, sans le contenu des fiches) ; journaux de sécurité (12 mois) ; contact/démo (3 ans) ; newsletter (consentement, 3 ans sans interaction) ; audience (13 mois au plus) ; demandes de droits (3 ans, à confirmer) ; comptabilité (durée à confirmer ; 10 ans pour les contrats électroniques au Bénin, art. 346).
- Aucune décision automatisée sur les personnes ; aucune donnée sensible collectée ; ni vente, ni location, ni publicité.
- Sous-traitants : OVH SAS (hébergement et sauvegardes), GENKIBO SARL (maintenance, Togo), prestataires de courriels et de paiement à préciser. Transferts : variante A (hors sous-région, avis IPDCP et autorisation APDP) ou variante B (hébergement local).
- Sécurité : cloisonnement, mandat actif + affectation nominative, 2FA pour administrateurs, correspondants, cabinets et équipe AMELEGAL, chiffrement, journalisation notifiée, sauvegardes ; sauvegardes conservées 35 jours ; archive de 12 mois après résiliation, puis suppression.
- Droits avec articles : accès (TG 39-40, BJ 437), rectification (TG 46, BJ 441), effacement (TG 47-48, BJ 443), opposition (TG 45, BJ 440), retrait du consentement (BJ 390), portabilité (BJ 438, étendue au Togo), décès (TG 50, BJ 441 al. 6).
- Réponse en 1 mois, délai aligné sur le plus court des délais légaux (TG 1 mois ; BJ 60 j pour l'accès, 30 j pour l'opposition, 45 j pour la rectification) ; réclamation auprès de l'IPDCP (art. 13 et 56) ou de l'APDP (art. 448).
- Cookies : session et sécurité (durée de la session), mémorisation des choix (6 mois), mesure d'audience optionnelle avec consentement (13 mois) ; aucun traceur publicitaire ; lien « Gestion des cookies » (TG art. 36).
- Service non destiné aux mineurs ; information en cas de modification substantielle.

**Utile pour :** page /confidentialite, bandeau cookies, politique de purge et de conservation, mentions des formulaires.

## H04 - Conditions générales d_utilisation organisations.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H04 - Conditions générales d_utilisation organisations.docx`

**En une phrase :** CGU applicables aux organisations (fiche v1.0 du 26/09/2026, phase 17, préalable à la mise en production), avec en annexe l'accord de sous-traitance des données de conformité.

**Contenu :**
- 17 articles : objet, définitions (Organisation, Administrateur, Utilisateur, Cabinet, Mandat, Données de conformité, Référentiel, Juridiction), acceptation par case non précochée, modifications notifiées 30 jours à l'avance.
- Comptes : fiche d'organisation obligatoire (secteur, effectif, pays, public/privé, mission de service public, correspondant désigné ou non), sans quoi aucune qualification n'est produite ; 2FA obligatoire pour l'administrateur et le correspondant ; un compte = une organisation.
- Rôles : administrateur, correspondant, responsable du traitement/délégataire, contributeur, lecteur, avec un périmètre par service ; circuit de validation paramétrable (visa désactivable, étapes fusionnables).
- Art. 7, réserve d'interprétation : résultats indicatifs, motivés, versionnés ; écart possible avec un motif ; standards internationaux signalés quand le texte est muet ; le rôle « correspondant » ne vaut pas désignation (organisation réputée sans correspondant à défaut de saisie) ; aucun dépôt auprès de l'autorité.
- Art. 9, mandats : consentis par l'administrateur seul ; niveau consultation/contribution/pilotage complet, périmètre, durée ; actions réservables (visa, notification de violation) ; affectation nominative contestable ; révocation immédiate sans préavis, sessions comprises ; tout est tracé au journal.
- Art. 10 : les données appartiennent à l'organisation, y compris celles saisies par le cabinet ; aucune réutilisation, seulement des statistiques agrégées et anonymes ; accès du support tracé et notifié.
- Disponibilité 24 h/24, 7 j/7 en obligation de moyens ; réversibilité (export complet, registre en PDF/CSV/XLSX) ; responsabilité plafonnée aux sommes versées sur 12 mois (plafond à arrêter) ; résiliation pour manquement après 30 jours ; droit togolais, tribunaux de Lomé.
- Annexe (DPA) en 12 rubriques : instructions, confidentialité, sécurité, sous-traitants ultérieurs (préavis de 30 jours, opposition par résiliation), transferts, assistance, notification des violations sans délai, suppression après archivage, audit une fois par an avec un préavis de 30 jours.
- Fondements : TG art. 20 et 51 ; BJ art. 338 et 386 ; loi togolaise 2017-07 sur les transactions électroniques, art. 40 (référence non vérifiée).

**Utile pour :** acceptation à l'inscription, modèle des rôles, mandats et droits, réversibilité et exports, page /cgu-organisations.

## H05 - Conditions générales d_utilisation cabinets.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H05 - Conditions générales d_utilisation cabinets.docx`

**En une phrase :** CGU propres aux cabinets et prestataires de conformité (v1.0 du 26/09/2026, phase 17), qui règlent ce qui est propre au cabinet et renvoient aux CGU organisations pour le reste (art. 14).

**Contenu :**
- Compte cabinet distinct : ses utilisateurs, sa facturation, sa bibliothèque et son dossier propre ; 2FA obligatoire pour tous, sans désactivation possible ; rôles de cabinet : administrateur, consultant référent, consultant contributeur, lecteur.
- Accès seulement par mandat exprès accepté par l'organisation (demande ou invitation, refus sans motif possible) ; le cabinet ne peut ni s'octroyer, ni étendre, ni prolonger un mandat ; double condition mandat actif + affectation nominative ; le plus restrictif du rôle et du niveau de mandat l'emporte (un référent sous mandat de contribution ne peut ni valider ni déposer).
- Vigilance : vérifier l'organisation active avant toute action irréversible, ne pas mélanger les dossiers, respecter les actions réservées par l'organisation, secret professionnel.
- Traçabilité au journal (consultant, cabinet, référence du mandat), conservée après le mandat ; mention du cabinet sur les documents produits sous mandat.
- Le cabinet est sous-traitant de l'organisation mandante ; le contrat écrit entre eux est hors de Waɖɛ (TG art. 20, BJ art. 386).
- Interdiction de réutilisation : rien dans la bibliothèque sans anonymisation et confirmation explicite ; exports limités à la mission.
- Fin de mandat : perte d'accès immédiate ; alertes à J-30 et J-7 avant le terme d'un mandat à durée fixe ; l'organisation garde toutes les données ; le cabinet ne garde que l'historique de ses interventions, sans le contenu des fiches.
- Dossier propre : créé d'office, accès des consultants fermé par défaut (réglage de l'administrateur), juridiction d'établissement du cabinet, non décompté comme mandat. Rapports par client communicables à ce seul client ; abonnement éventuellement indexé sur les mandats actifs.

**Utile pour :** espace cabinet (portefeuille, mandats, affectations, bibliothèque de modèles, dossier propre, facturation), page /cgu-cabinets.

## H06 - Conditions générales de vente.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H06 - Conditions générales de vente.docx`

**En une phrase :** Trame des CGV des abonnements Waɖɛ (v1.0 du 26/09/2026, criticité « recommandé », publication ultérieure), dont prix et formules dépendent du livrable G06, encore ouvert.

**Contenu :**
- Clientèle exclusivement professionnelle, ce qui écarte le droit de rétractation (BJ art. 347 ; dérogation entre professionnels, art. 326 al. 5) ; informations précontractuelles reprises par prudence car leur omission est sanctionnée par la nullité (art. 338 et 340).
- Deux abonnements, Organisation et Cabinet, ce dernier indexé sur les mandats actifs, dossier propre non décompté ; prestations complémentaires sur devis ; période d'essai éventuelle ; prix en franc CFA.
- Conclusion en ligne en 5 étapes (formule, récapitulatif, correction, case CGV non précochée, confirmation) et accusé de réception horodaté ; contrat archivé et accessible.
- Révision des prix à chaque renouvellement avec un préavis de 60 jours ; paiement à [30] jours ; suspension possible après une mise en demeure restée sans effet 15 jours, l'export des données restant ouvert.
- Durée de [12 mois] renouvelable tacitement, dénonciation [30] jours avant l'échéance ; résiliation pour manquement après 30 jours ; pas de remboursement sauf faute d'AMELEGAL (au prorata).
- Responsabilité plafonnée aux sommes de 12 mois ; force majeure (résiliation au-delà de 60 jours) ; réponse aux réclamations en [15] jours ouvrables ; droit togolais, tribunaux de Lomé.
- Variables à arrêter : formules, prix, taxes, moyens de paiement, périodicité, pénalités ; durée OHADA de conservation des pièces à vérifier ; 10 ans pour les contrats électroniques au Bénin (art. 346).

**Utile pour :** module d'abonnement et de facturation (décompte des mandats actifs), page /cgv (affichée seulement quand elle devient applicable).

## H07 - Déclaration d_accessibilité.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H07 - Déclaration d_accessibilité.docx`

**En une phrase :** Modèle de déclaration d'accessibilité de Waɖɛ (v1.0 du 26/09/2026, phase 14, préalable à la mise en production), à compléter avec les résultats de l'audit remis par GENKIBO.

**Contenu :**
- Engagement volontaire : RGAA 4.1.2 (niveau AA des WCAG 2.1), pour la partie publique et les espaces authentifiés.
- À compléter : état de conformité (totale, partielle ou nulle), date et auteur de l'audit, taux de critères respectés, taux moyen, liste des non-conformités écran par écran (exemple donné : jauge de l'indice sans équivalent textuel, critère 1.1), dérogations.
- Contenus exclus : pièces jointes des utilisateurs, documents de tiers (dont ceux des autorités).
- Technologies : HTML5, CSS, JavaScript ; environnement de test suggéré (NVDA/Firefox, VoiceOver/Safari, TalkBack/Chrome) et outils à compléter.
- Échantillon de pages : accueil, contact, mentions légales, connexion, création de compte, tableau de bord, vue portefeuille, fiche de traitement, assistant de formalités, bulle d'information, déclaration de violation.
- Contact avec l'objet « Accessibilité » (courriel, +228 91 86 35 35, courrier, formulaire), réponse en [15] jours ouvrables ; recours écrit auprès de la gérance, réponse en 1 mois.
- La voie de recours renvoie à une « note de présentation » qui ne figure pas dans le document.

**Utile pour :** page /accessibilite et recette d'accessibilité (CDC art. 24, 44 16° et 45.1).

## H08 - Actualités et contenus de lancement.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H08 - Actualités et contenus de lancement.docx`

**En une phrase :** Six actualités de lancement prêtes à saisir (v1.0 du 26/09/2026, phase 11), avec plan de publication, métadonnées SEO et articles de loi en notes.

**Contenu :**
- Plan de publication : 1 Lancement (jour J), 2 Togo (J), 3 Bénin (J), 4 Deux juridictions/CEDEAO (J+7), 5 Cabinets (J+14), 6 Étude AMELEGAL sur le Bénin (J+21).
- Togo (loi 2019-014) : déclaration et récépissé de l'IPDCP sous 1 mois, prorogeable une fois (art. 6) ; normes simplifiées (art. 7) ; autorisation pour les données génétiques ou de santé-recherche, les infractions, les interconnexions, les identifiants nationaux, la biométrie, l'intérêt public (art. 8) ; avis pour la sphère publique (art. 9) ; dispense si un correspondant est désigné, sauf transfert (art. 5 3°, notification art. 77) ; transfert avec information et avis de l'IPDCP (art. 28) ; sanctions pénales de 1 à 5 ans et de 1 à 10 M FCFA (art. 79) ; amende administrative jusqu'à 100 M FCFA (art. 71) ; pas de délai légal de notification des violations.
- Bénin (Livre 5) : portée extraterritoriale (art. 381) ; déclaration ou inscription au registre (art. 405) ; normes et exemption, notamment avec un délégué (art. 406, 408) ; autorisation pour les données sensibles, le NIN, la biométrie, les interconnexions, les traitements d'exclusion et les transferts (art. 407) ; dispenses comptabilité, paie, fournisseurs (art. 410) ; délai de 60 j + 30 j, le silence valant acceptation (art. 412), statut « Acceptation tacite » dans Waɖɛ ; notification des violations sans délai (art. 427) ; délégué obligatoire (art. 430) ; registre obligatoire sauf PME (art. 435).
- Article 4 : comparaison TG/BJ, juridiction traitée comme un paramètre, terminologie correspondant/délégué et IPDCP/APDP ; acte additionnel CEDEAO A/SA.1/01/10 du 16/02/2010.
- Article 5 : espace cabinet (portefeuille, file d'alertes, bascule sûre, mandat). Article 6 : étude de 76 pages d'août 2026, base du référentiel béninois (sommaire à compléter par la gérance).
- Métadonnées : slugs /actualites/lancement-wade, togo-formalites-loi-2019-014, benin-formalites-apdp, juridictions-togo-benin-cedeao, cabinets-portefeuille-mandats, etude-protection-donnees-benin, avec balises title et meta descriptions.

**Utile pour :** module Actualités du back-office, contenus de lancement, SEO, et contrôle de cohérence des référentiels TG/BJ.

## H09 - Éléments de référencement.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/H - Contenus éditoriaux et juridiques/H09 - Éléments de référencement.docx`

**En une phrase :** Livrable SEO (v1.0 du 26/09/2026, phase 11 ; contenus AMELEGAL, intégration GENKIBO) : mots-clés, balises par page, règles d'indexation, robots.txt, données structurées et vocabulaire.

**Contenu :**
- Règles des balises : title de 60 caractères au plus avec « · Waɖɛ » en fin, meta description de 155 caractères au plus, un seul H1, adresses sans accent (« wade »), lang="fr", pas d'autre langue au lancement ; « RGPD » seulement comme mot-clé secondaire, formulé exactement.
- Univers de mots-clés en 8 intentions : produit, Togo, Bénin, registre, AIPD, violations, cabinets, régional.
- Balises title, meta et H1 pour 13 pages : /, /wade, /organisations, /cabinets, /amelegal, /actualites, /contact, /mentions-legales, /confidentialite, /cgu-organisations, /cgu-cabinets, /cgv, /accessibilite.
- Indexation : pages publiques avec canonique ; espaces authentifiés et back-office en « noindex, nofollow » + X-Robots-Tag ; écrans de connexion, d'inscription, de réinitialisation, d'invitation et de mandat, ainsi que la recherche et la pagination, en « noindex, follow » ; documents générés jamais accessibles sans authentification ; robots.txt n'est pas une mesure de sécurité (contrôle serveur, CDC art. 38).
- Modèle de robots.txt : Disallow /app/, /cabinet/, /admin/, /connexion, /inscription, /recherche, plus le sitemap ; sitemap.xml régénéré à chaque publication.
- JSON-LD : Organization (AMELEGAL SARL, TG, LinkedIn), SoftwareApplication (Waɖɛ/« Wade », BusinessApplication, areaServed TG et BJ), Article pour les actualités, FAQPage ; pas d'aggregateRating ni de review ; « offers » seulement après G06.
- Open Graph : og:site_name « Waɖɛ by amelegal », image de 1200 × 630, twitter:card summary_large_image.
- Vocabulaire à préférer ou éviter (ex. correspondant au Togo, délégué au Bénin ; IPDCP/APDP et non CNIL ; « indicatif » plutôt que « garanti/certifié » ; jamais « conforme RGPD »).

**Utile pour :** intégration front publique (head, robots, sitemap, schema.org) par GENKIBO.

## I02 - Plan de tests fonctionnels et juridiques.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/I - Recette et validation/I02 - Plan de tests fonctionnels et juridiques.docx`

**En une phrase :** Plan de recette juridique d'AMELEGAL (v1.0 du 6/09/2026, CDC art. 45.1, phase 13, bloquant) : 14 scénarios qui vérifient que le logiciel applique fidèlement le référentiel validé.

**Contenu :**
- Principe : un écart entre le logiciel et le référentiel validé est une anomalie ; une erreur du référentiel lui-même relève d'AMELEGAL.
- T1 jeu de cas de recette complet par juridiction, sans écart, motifs compris ; T2 même résultat entre la fiche et l'assistant pas à pas ; T3 rôle applicatif Correspondant sans désignation : droit commun, aucune dispense ; T4 mandat de cabinet sans désignation : aucune dispense.
- T5 traitement bi-juridiction : deux qualifications côte à côte, sans primauté, suivis séparés ; T6 qualification ancienne lisible avec sa version ; T7 couverture des bulles (publication bloquée en cas de lacune) ; T8 bulles fidèles au texte cité.
- T9 violation avec deux délais distincts (point de départ, décompte, rappels, persistance après reconnexion) ; T10 seuil de volume déclenchant l'AIPD ; T11 documents dans les deux juridictions (mentions E07, aucun champ exclu, aucune référence à l'autre droit) ; T12 écart retenu par un utilisateur habilité et consigné.
- T13 nouvelle version du référentiel : revue par tâches, sans modification automatique ; T14 création d'une juridiction de test depuis le back-office, sans code.
- Conduite : à chaque version, sur l'environnement de test, avec des données fictives ; écarts consignés selon la grille I03 et transmis à GENKIBO ; T1, T2, T7 et T11 conditionnent la validation finale ; plan enrichi à chaque nouvelle juridiction.
- Sources : registre-champs.csv, bulles-information.json, alertes.json.

**Utile pour :** recette du moteur de qualification, des bulles, des alertes de violation, des exports et du back-office des référentiels.

## I05 - Contrôle des documents produits.docx
*Chemin :* `00 Commun aux deux pays/02 Livrables communs/I - Recette et validation/I05 - Contrôle des documents produits.docx`

**En une phrase :** Grille de contrôle des documents générés par Waɖɛ (v1.0 du 6/09/2026, art. 45.1, phase 13, bloquant).

**Contenu :**
- Documents contrôlés : fiche de registre, registre complet aux 3 formats, dossier de formalité de chaque régime, rapport d'AIPD, notification de violation, communication aux personnes, rapport d'activité de cabinet, export du journal.
- C1 gabarit E01/E04 ; C2 exhaustivité des champs de registre-champs.csv ; C3 aucun champ marqué export_registre=non (ex. origine dans la cartographie) ; C4 aucune référence au droit d'une autre juridiction.
- C5 mentions E07 (juridiction, texte, version, date, auteur, réserve) ; C6 mention du cabinet sous mandat, pas reléguée en note ; C7 régime, motifs et AIPD identiques au panneau de qualification ; C8 emplacements de signature et de visa.
- C9 lisibilité en noir et blanc (rien porté par la seule couleur, pas de tableau tronqué) ; C10 production consignée au journal ; C11 cohérence PDF/tabulaire ; C12 terminologie de la juridiction et de la version en vigueur.
- Jeu de démonstration : au moins une organisation, un cabinet avec dossier propre, deux mandats, un traitement par régime et par juridiction ; tout défaut sur C3, C4 ou C7 est bloquant.
- Le fichier pèse 209 Ko à cause des polices Noto Sans Symbols embarquées ; le texte est court.

**Utile pour :** recette des générateurs de documents et d'exports (PDF, CSV, XLSX).

# Partie 3 — dossier « 01 Togo »

Toutes les fiches de livrables AMELEGAL (C01 à K02) partagent le même cartouche : juridiction Togo, responsable AMELEGAL, version 1.0 du 6 septembre 2026 (0.1 pour K01 et K02), fondement renvoyant aux articles du cahier des charges Waɖɛ (v1.0 du 12 août 2026), « Document de travail, strictement confidentiel ». Elles se terminent par la même liste de sources (loi n° 2019-014, referentiel-togo.json, cas-de-recette-togo.csv, cahier des charges, registre type) et le même critère d'achèvement : le jeu de cas de recette passe sans écart en simulation et le contrôle de couverture des bulles ne signale plus de lacune.

---

## Registre_type_Togo.xlsx / Registre_type_Togo.pdf
*Chemin :* `01 Togo/00 Sources et référentiels/Registre/Registre_type_Togo.xlsx` (et `.pdf`)

**En une phrase :** registre type des activités de traitement pour le Togo, établi par AMELEGAL (version 4.0, septembre 2026), à charger dans l'application comme base des modèles de fiches. Le PDF (206 pages) imprime le même classeur.

**Contenu :**
- 156 fiches et 675 finalités. Quatre parties : Socle générique (49 fiches, préfixe SG-), Sectoriel (60, SE-), Collectivité Togo (25, CT-), Personne morale de droit public (22, PP-). Les secteurs couverts sont notamment la santé (8 fiches), les établissements de crédit (7), les télécoms (7), la monnaie électronique (6), l'enseignement (6), les transitaires (6), les OSC (6), les SFD (5), l'assurance (5) et les associations (4).
- Onglet « Registre » : 41 colonnes (A à AO). On y trouve la référence, la rubrique, les finalités, les codes de la cartographie v3, la base juridique et son fondement (art. 14), les catégories de personnes et de données, les destinataires, les sous-traitants types, la durée active, le sort à l'échéance, le fondement contraignant, la durée indicative européenne et sa source, et les mesures de sécurité. S'y ajoutent dix drapeaux de qualification (TG perso, registrePublic, public, sensible, bio, interconnexion, nni, recherche, souverain, transfert), puis le régime et le motif Togo, le régime si un correspondant est désigné, le besoin d'AIPD et ses motifs.
- Régimes calculés sans correspondant : 125 Déclaration, 24 Autorisation, 7 Acte réglementaire après avis. Avec un correspondant désigné : 145 Pas de formalité et 11 Avis motivé (transfert). AIPD requise pour 71 fiches, non requise pour 85.
- Bases juridiques, en liste fermée de 5 valeurs conformes à l'art. 14 : Obligation légale (51), Exécution d'un contrat (37), Mission d'intérêt public (35), Consentement (18), Sauvegarde de l'intérêt ou des droits fondamentaux (15). Une réserve explique que « Intérêt légitime », présent dans la maquette, n'est pas retenu par l'art. 14. Une colonne de repli sert à l'injection.
- Onglet « Durées » sur deux couches. Les ancrages contraignants sont COMPTA (10 ans, AUDCIF art. 24), LBCFT (10 ans, loi uniforme UMOA art. 35 / loi togolaise n° 2018-004), FINALITE (art. 16), TRAVAIL (durée à caler), USAGE et ARCHIVES (non instruit). Les repères européens indicatifs, tirés de la CNIL, sont CAND 2 ans, PAIE, REGPERS 5 ans, TEMPS 5 ans, MANDAT, PROSPECT 3 ans, CONTRAT, COMPTA10, VIDEO 1 mois max, LOGS 6 mois-1 an (3 ans max), TRACEURS 13/25 mois et SATISF.
- Onglet « Bases légales » : 15 textes. On y trouve l'Acte additionnel CEDEAO A/SA.1/01/10 de 2010, la Convention de Malabo (2014, en vigueur le 8 juin 2023), la loi 2019-014 (art. 5-9, 14, 16, 21-22, 24, 28-30, 75-78), l'AUDCIF art. 24, la LBC-FT UMOA art. 35, l'instruction BCEAO 008-05-2015 sur la monnaie électronique, la loi 2020-009 sur l'identification biométrique, la loi 2022-011 sur la décentralisation et le code du travail 2021-012.
- Autres onglets : « Finalités » (une ligne par finalité), « Référentiels » (9 classifications de données, vocabulaire détaillé, 34 catégories de personnes, régimes et drapeaux Togo, modèles de mesures de sécurité), « Injection Waɖɛ » (colonne → champ de la maquette : ref, nom, finalite, base, persons, dataClasses, duree, dureeIndicative…), « Synthèse » (formules COUNTIF) et « Fiches imprimables ».
- Règles d'injection : le champ finalité doit devenir multivalué, le drapeau correspondant reste à faux, et le régime comme l'AIPD sont des colonnes de contrôle que qualifier() et besoinAIPD() doivent retrouver.
- Écart entre les formats : la notice du PDF est une version antérieure. Elle mentionne le Bénin (« fiches propres aux communes béninoises retirées », art. 409 et 383 du code du numérique béninois), là où la notice du xlsx est purement togolaise.

**Utile pour :** les modèles sectoriels (F02), le chargement initial du registre et le contrôle croisé du moteur de qualification et de l'AIPD.

## Loi n° 2019-014 du 29 octobre 2019 - JO 64e année n° 26 ter.pdf
*Chemin :* `01 Togo/00 Sources et référentiels/Textes/Loi n° 2019-014 du 29 octobre 2019 - JO 64e année n° 26 ter.pdf`

**En une phrase :** Journal officiel togolais (numéro spécial de 20 pages) qui publie la loi relative à la protection des données à caractère personnel. C'est le texte source de tout le référentiel Togo. Le numéro contient aussi deux décrets de nomination sans rapport avec la loi.

**Contenu :**
- Structure en 8 chapitres et 97 articles. Ch. I, dispositions générales (art. 1-4) : objet, champ, exclusions, définitions. Ch. II, conformité des traitements (art. 5-34) : formalités, principes, données sensibles, transferts, interconnexion. Ch. III, droits des personnes (art. 35-50). Ch. IV, obligations du responsable (art. 51-54). Ch. V, IPDCP (art. 55-74). Ch. VI, correspondant (art. 75-78). Ch. VII, dispositions pénales (art. 79-93). Ch. VIII, dispositions transitoires (art. 94-97). Loi signée à Lomé le 30 octobre 2019.
- Formalités. Art. 5, dispense : 1° traitements « mentionnés à l'art. 2 » (sic) ; 2° registre destiné exclusivement à l'information du public ; 3° correspondant désigné, sauf transfert vers un pays tiers. Art. 6, déclaration de droit commun : accusé de réception puis récépissé sous 1 mois maximum, prorogeable une fois. Seul le récépissé permet la mise en œuvre. Art. 7 : normes de simplification et d'exonération publiées par l'IPDCP.
- Art. 8, autorisation : 1° données génétiques et recherche en santé ; 2° infractions, condamnations, mesures de sûreté ; 3° interconnexion ; 4° numéro national d'identification ; 5° biométrie ; 6° motif d'intérêt public (fins historiques, statistiques, scientifiques).
- Art. 9 : les traitements pour le compte de l'État, d'un établissement public, d'une collectivité ou d'un gestionnaire de service public sont décidés par acte réglementaire pris après avis motivé. Ils portent sur : 1° sûreté, défense, sécurité publique ; 2° infractions ; 3° recensement ; 4° données sensibles (origines, opinions, santé…) ; 5° salaires, pensions, impôts.
- Art. 10 : 11 mentions obligatoires des déclarations et demandes. Art. 11 : délai d'instruction fixé par voie réglementaire et prorogeable une fois ; le silence vaut autorisation « réputée favorable ». Art. 12 : dépôt par voie électronique ou postale.
- Principes : art. 14 (consentement, plus 4 dérogations : obligation légale, mission d'intérêt public, contrat, sauvegarde des droits), art. 16 (finalité, conservation), art. 19 et 52 (sécurité, 10 mesures), art. 20 (sous-traitant : garanties suffisantes et contrat écrit). Données sensibles : interdiction de principe (art. 21) et 9 exceptions (art. 22). Santé : art. 24. Prospection sans consentement interdite (art. 26). Décision fondée uniquement sur un traitement automatisé interdite (art. 27).
- Transferts : pays tiers à niveau suffisant et information préalable de l'IPDCP, qui rend un avis motivé (art. 28). Dérogations ponctuelles et non massives (art. 29). Autorisation sur garanties (art. 30). Données venant de l'étranger (art. 31). Interconnexion soumise à autorisation (art. 32-34).
- Droits : information (art. 35-38), accès et copie (art. 39-44), opposition (art. 45), rectification sous 1 mois (art. 46), effacement (art. 47 : saisine de l'IPDCP après 1 mois sans réponse, décision en 3 semaines), données d'une personne décédée (art. 50).
- IPDCP : autorité administrative indépendante (art. 55). Comité de direction de 10 membres (art. 57), mandat de 3 ans renouvelable une fois (art. 59). Sanctions après mise en demeure : retrait de l'autorisation pour 3 mois, puis définitif, et amende jusqu'à 100 000 000 FCFA (art. 71). Mesures d'urgence de 3 mois maximum (art. 72). Recours devant la chambre administrative de la Cour suprême (art. 74).
- Correspondant : statut (art. 75), 6 missions dont le conseil sur l'AIPD (3°) et la liste des traitements (5°) (art. 76), désignation notifiée à l'IPDCP (art. 77), révocation (art. 78). Pénal : défaut de formalités puni de 1 à 5 ans et de 1 à 10 millions FCFA (art. 79), mêmes peines pour les art. 83 et 86, notamment. Transitoire : déclaration seule pour les traitements publics déjà créés (art. 94) ; mise en conformité en 2 ans pour le secteur public et 1 an pour les autres (art. 95). La loi ne prévoit ni notification des violations ni régime d'AIPD.

**Utile pour :** le fondement de tout le référentiel Togo : logigramme, bulles, transferts, correspondant, sanctions de la future banque pédagogique (K02).

## C01 - Identification de la juridiction.docx
*Chemin :* `01 Togo/01 Livrables Togo/C01 - Identification de la juridiction.docx`

**En une phrase :** fiche d'identité de la juridiction Togo dans le référentiel.

**Contenu :**
- Nom Togo, nom officiel République togolaise, code pays TG, langue d'affichage fr.
- Rattachement au socle régional CEDEAO, avec « hérite du socle : oui ».
- Statut : à publier au lot 1. Criticité : bloquant. Phase 4 du chronogramme. Fondement : annexe 3 du cahier des charges.
- L'héritage du socle reste sans effet tant que le socle n'est pas renseigné : toutes les règles viennent du droit interne.

**Utile pour :** la création de la juridiction en back-office (bloc `juridiction` du referentiel-togo.json).

## C02 - Sources.docx
*Chemin :* `01 Togo/01 Livrables Togo/C02 - Sources.docx`

**En une phrase :** inventaire des textes sources et des articles de la loi exploités par le référentiel.

**Contenu :**
- Texte principal : loi n° 2019-014, JO 64e année n° 26 ter du 29 octobre 2019.
- Aucun texte d'application. Les paramètres du registre, de l'AIPD et des violations viennent des standards internationaux (source=standard_international), sous la réserve d'interprétation de l'art. 12 du cahier des charges.
- Table des articles utiles : 2 (champ), 3 (exclusions), 4 (définitions), 5 (dispense), 6 (déclaration), 7 (normes), 8 (autorisation), 9 (acte réglementaire), 10, 12, 13, 21-22 (sensibles), 28-31 (transferts), 32-34 (interconnexion), 51-54 (sécurité, conservation), 55-74 (IPDCP), 75-78 (correspondant), 79 (sanction), 94 (régime dérogatoire), 95 (délai de mise en conformité).

**Utile pour :** le bloc `sources` du référentiel et les références affichées dans les bulles et les résultats.

## C03 - Autorité de contrôle.docx
*Chemin :* `01 Togo/01 Livrables Togo/C03 - Autorité de contrôle.docx`

**En une phrase :** coordonnées et délais de l'autorité de contrôle togolaise.

**Contenu :**
- Instance de protection des données à caractère personnel (IPDCP), créée par l'art. 55.
- Adresse Agoe 2 Lions ; tél. +228 70 36 33 33 ; contact@ipdcp.tg ; https://ipdcp.tg/.
- Modalités de dépôt : « à renseigner (pratique de l'IPDCP) ».
- Délais : déclaration 1 mois, prorogeable une fois sur décision motivée (art. 6). Autorisation, avis motivé et acte réglementaire : délai non chiffré par la loi.
- Écart : le referentiel-togo.json porte adresse, téléphone, courriel et site à null, alors que ce document les renseigne.

**Utile pour :** l'affichage de l'autorité dans le résultat de qualification et dans les feuilles de route (bloc `autorite`).

## C04 - Terminologie.docx
*Chemin :* `01 Togo/01 Livrables Togo/C04 - Terminologie.docx`

**En une phrase :** libellés propres au Togo et intitulés officiels des 5 régimes. Statut : à valider par la gérance.

**Contenu :**
- Clés de libellés : autorite = IPDCP ; correspondant = correspondant à la protection des données à caractère personnel (CPDCP) ; analyse_impact = AIPD ; registre = registre des activités de traitement ; personne concernée ; responsable du traitement ; sous-traitant.
- Régimes : TG-DISPENSE « Pas de formalité » (art. 5), TG-DECLARATION (art. 6), TG-AVIS « Avis motivé de l'IPDCP préalable au transfert » (art. 28 al. 2), TG-AUTORISATION (art. 8), TG-ACTE « Acte réglementaire pris après avis motivé » (art. 9).
- Réserve : la loi n'emploie pas le terme « registre ». L'art. 76, 5° parle d'une liste des traitements tenue par le correspondant, et le libellé retenu vient du standard international.

**Utile pour :** les libellés de l'interface et le bloc `terminologie` du référentiel.

## C05 - Régimes de formalité.docx
*Chemin :* `01 Togo/01 Livrables Togo/C05 - Régimes de formalité.docx`

**En une phrase :** liste ordonnée des 5 régimes togolais, avec leur famille de couleur et leur portée. Validé par AMELEGAL le 6 septembre 2026.

**Contenu :**
- 1 TG-DISPENSE (famille neutre), 2 TG-DECLARATION (standard), 3 TG-AVIS (attention), 4 TG-AUTORISATION (élevé), 5 TG-ACTE (critique). Les couleurs suivent l'art. 23.2 du cahier des charges.
- Dispense : aucune formalité, mais toutes les autres obligations demeurent.
- Déclaration : accusé de réception puis récépissé sous 1 mois, prorogeable une fois. Seul le récépissé autorise la mise en œuvre.
- Avis motivé : information préalable de l'IPDCP avant tout transfert vers un pays tiers.
- Autorisation : autorisation expresse de l'IPDCP. Acte réglementaire : pris après avis motivé et publié avant la mise en œuvre.

**Utile pour :** le bloc `regimes` du référentiel et le code couleur des résultats de qualification.

## C06 - Logigramme de qualification.docx
*Chemin :* `01 Togo/01 Livrables Togo/C06 - Logigramme de qualification.docx`

**En une phrase :** arbre de décision du moteur de qualification togolais : 8 questions, 5 sorties, la première sortie atteinte l'emporte. Validé le 6 septembre 2026.

**Contenu :**
- TG-Q1, données personnelles ? Non → TG-DISPENSE. TG-Q2, registre d'information du public ? Oui → TG-DISPENSE (art. 5, 2°).
- TG-Q3, correspondant désigné ? Oui → TG-Q4, transfert hors du Togo ? Oui → TG-AVIS ; non → TG-DISPENSE (art. 5, 3° et art. 28 al. 2).
- Sans correspondant → TG-Q5, données sensibles ? Non → TG-DECLARATION. Oui → TG-Q6, État, collectivité ou mission de service public ?
- TG-Q6 oui → TG-Q7, sûreté de l'État, sécurité publique, défense ou recensement ? Oui → TG-ACTE (art. 9, 1° et 3°) ; non → TG-AUTORISATION.
- TG-Q6 non → TG-Q8, génétique, biométrie, interconnexion, NNI, statistiques, recherche ou intérêt public ? Oui → TG-AUTORISATION (art. 8, 1° à 6°) ; non → TG-DECLARATION.
- Champs alimentant le moteur : bloc2.nature_donnees_personnelles, bloc1.registre_information_public, bloc3.correspondant_designe, bloc3.transfert_international, bloc2.donnees_sensibles, bloc1.personne_publique_ou_mission_service_public, bloc3.mission_regalienne, bloc2.caracteristiques_article_8 (choix multiple). Chacun a sa bulle d'aide.
- Motifs rédigés et restitués à l'utilisateur pour chaque branche. Règle : TG-Q3 est l'indicateur juridique de désignation, distinct du rôle applicatif et du mandat de cabinet. Il vaut faux par défaut.
- Constat de lecture : les cas de l'art. 8 ne sont examinés qu'après une réponse « oui » sur les données sensibles (TG-Q5), alors que l'art. 8 ne l'exige pas. De même, l'art. 9, 4° (données sensibles traitées par une personne publique) et 5° (salaires, impôts) n'est pas repris en TG-Q7.

**Utile pour :** le moteur de qualification (bloc `logigramme`), l'assistant pas à pas et la qualification continue.

## C07 - Feuilles de route.docx
*Chemin :* `01 Togo/01 Livrables Togo/C07 - Feuilles de route.docx`

**En une phrase :** étapes et pièces attendues pour chaque régime togolais. Statut : à valider par la gérance.

**Contenu :**
- Dispense (3 étapes) : documenter la dispense au registre, conserver sa justification, réévaluer en cas de changement de finalité, de données, de destinataires ou de transfert.
- Déclaration (4) : formulaire conforme au modèle de l'IPDCP, fiche de registre Waɖɛ, dépôt et accusé de réception, puis conservation du récépissé.
- Avis motivé (4) : description du transfert, vérification du niveau de protection, demande d'avis à l'IPDCP, clauses et garanties.
- Autorisation (4) : demande avec les mentions de l'art. 10, rapport d'AIPD, description des mesures de sécurité, dépôt puis décision.
- Acte réglementaire (4) : projet d'acte, dossier de saisine, avis motivé, publication de l'acte avant la mise en œuvre.

**Utile pour :** le module des formalités (feuille de route affichée après qualification, bloc `feuilles_de_route`).

## C08 - Analyse d_impact.docx
*Chemin :* `01 Togo/01 Livrables Togo/C08 - Analyse d_impact.docx`

**En une phrase :** paramètres de déclenchement et grille de l'AIPD au Togo.

**Contenu :**
- Fondement : l'art. 76, 3° (conseil du correspondant). La loi ne crée pas de régime d'AIPD, donc les critères viennent du standard international, sous la réserve de l'art. 12 du cahier des charges.
- Une AIPD est requise dès qu'un critère est réuni. TG-AIPD-1 : données sensibles. TG-AIPD-2 : génétique, biométrie ou interconnexion. TG-AIPD-3 : transfert international. TG-AIPD-4 : mission régalienne ou recensement. TG-AIPD-5 : volume de personnes supérieur à 10 000.
- L'AIPD est présumée pour TG-AUTORISATION et TG-ACTE ; l'analyse validée est alors jointe au dossier.
- Grille en 4 sections : description et finalité, nécessité et proportionnalité, risques pour les personnes, mesures et risque résiduel avec avis du correspondant. Niveaux de risque : faible, modéré, élevé.
- La numérotation passe de la section 3 à la section 5 : il n'y a pas de section 4.

**Utile pour :** le module d'AIPD et la fonction besoinAIPD() (bloc `aipd`).

## C09 - Violations de données.docx
*Chemin :* `01 Togo/01 Livrables Togo/C09 - Violations de données.docx`

**En une phrase :** paramètres de gestion des violations de données, tirés du standard international faute de texte togolais.

**Contenu :**
- La loi ne prévoit ni notification, ni délai, ni information des personnes. Les paramètres sont marqués standard_international.
- Délai de 72 heures à compter de la prise de connaissance de la violation par le responsable. Destinataire : l'IPDCP. Rappels à 25 %, 50 %, 75 % et 90 % du délai.
- Consignation au registre interne obligatoire dans tous les cas.
- Arbre de décision. TG-V1, risque pour les droits et libertés ? Non : ni notification ni information. TG-V2, risque élevé ? Oui : notification et information des personnes. Non : notification seule.
- Les motifs restitués sont rédigés pour chaque branche.

**Utile pour :** le module des incidents (compte à rebours, arbre de qualification, bloc `violations`).

## C10 - Correspondant.docx
*Chemin :* `01 Togo/01 Livrables Togo/C10 - Correspondant.docx`

**En une phrase :** régime du correspondant à la protection des données (CPDCP) et son effet sur le moteur. Statut : à valider par la gérance.

**Contenu :**
- Fondement : art. 75 à 78. Désignation non obligatoire.
- Statut : qualifié, ne peut être sanctionné pour ses missions, peut saisir l'IPDCP. Son profil est précisé par l'IPDCP.
- Six missions : informer et conseiller, veiller au respect de la loi (sensibilisation, formation), conseiller sur l'AIPD, coopérer avec l'IPDCP, tenir la liste des traitements, servir de point de contact.
- La désignation est notifiée à l'IPDCP (art. 77). La révocation relève de l'art. 78.
- Effet : la désignation dispense des formalités, sauf transfert vers un pays tiers (art. 5, 3°). Seul l'indicateur juridique alimente le moteur, ni le rôle applicatif ni le mandat de cabinet.
- Point ouvert : le correspondant externe, que la loi ni n'exclut ni ne consacre. AMELEGAL doit trancher, ce qui conditionne l'offre aux cabinets.

**Utile pour :** la question TG-Q3, la gestion des rôles et des mandats, l'offre cabinet (bloc `correspondant`).

## C11 - Transferts internationaux.docx
*Chemin :* `01 Togo/01 Livrables Togo/C11 - Transferts internationaux.docx`

**En une phrase :** règles des transferts hors du Togo. Statut : à valider par la gérance.

**Contenu :**
- Principe : transfert possible vers un pays à niveau suffisant, avec information préalable de l'IPDCP qui rend un avis motivé (art. 28).
- Pays reconnus : aucune liste publiée à ce jour.
- Dérogations ponctuelles (art. 29) : transfert ponctuel et non massif avec consentement exprès, sauvegarde de la vie, intérêt public, droit en justice, contrat ou mesures précontractuelles.
- Autorisation sur garanties suffisantes vers un pays non adéquat (art. 30). Vérification préalable par l'IPDCP pour les données venant de l'étranger (art. 31).
- Un transfert international conduit au régime TG-AVIS.

**Utile pour :** la question TG-Q4, le tableau des transferts de la fiche et le dossier d'avis (bloc `transferts`).

## C12 - Registre.docx
*Chemin :* `01 Togo/01 Livrables Togo/C12 - Registre.docx`

**En une phrase :** correspondance entre le socle commun de registre (12 rubriques) et les champs Waɖɛ, avec la liste des champs de la fiche.

**Contenu :**
- Socle commun de 12 rubriques, complété par les mentions de la loi et les champs du moteur, sans rien en retrancher.
- Table de correspondance des rubriques : organisme (NIF, RCCM), responsable, délégué, activité, personnes, données, durées, accès, communications, transferts, principes, sécurité. Les champs propres à Waɖɛ y figurent aussi : secteur, effectif, personne publique, mission de service public, caractéristiques d'autorisation, volume, mission régalienne, etc.
- Le fichier registre-champs.csv compte 70 champs, dont 64 applicables au Togo.
- Champs listés avec identifiant, bloc, type, caractère obligatoire (O, R, C) et lien avec le moteur : org.* (12), rt.* (5), dpo.* (9), t.* (38), de t.reference à t.validite_decision.
- Champs « moteur » : org.pays_etablissement, org.nature_publique, org.mission_service_public, dpo.designe, dpo.statut, t.juridiction, t.registre_information_public, t.nature_donnees_personnelles, t.classification_donnees, t.donnees_sensibles, t.caracteristiques_article_8, t.volume_personnes, t.transfert_international, t.correspondant_designe, t.mission_regalienne.

**Utile pour :** le modèle de données de la fiche de registre, les formulaires et la validation des champs obligatoires.

## C13 - Indice de conformité paramètres.docx
*Chemin :* `01 Togo/01 Livrables Togo/C13 - Indice de conformité paramètres.docx`

**En une phrase :** composantes, poids et seuils de l'indice de conformité.

**Contenu :**
- La complétude du registre pèse 35 %, calculée comme la moyenne de complétude des fiches publiées.
- Les formalités accomplies pèsent 35 % : statut Acceptée, Récépissé reçu ou Dispense documentée.
- Les AIPD réalisées pèsent 20 %, les violations closes dans le délai sur 12 mois 10 %. Les poids sont administrables par juridiction et leur somme vaut 1.
- Seuils des libellés : Action requise 0-39, À surveiller 40-64, Bon, à consolider 65-84, Solide 85-100.
- La composante de sensibilisation reste inactive jusqu'au lot 2 ; les poids seront alors revus.
- Restitution : jauge circulaire, valeur, libellé, détail du calcul et équivalent textuel pour l'accessibilité.

**Utile pour :** le tableau de bord (jauge de l'indice, bloc `indice`).

## C14 - Sous-traitance.docx
*Chemin :* `01 Togo/01 Livrables Togo/C14 - Sous-traitance.docx`

**En une phrase :** exigences contractuelles de la sous-traitance et alerte associée. Criticité : recommandé.

**Contenu :**
- Fondement : art. 20, complété par les art. 51 et 52 (garanties suffisantes, acte écrit).
- Dix mentions minimales du contrat : parties, objet et durée, catégories de données et de personnes, instructions documentées, confidentialité, sécurité, sous-traitance ultérieure, assistance (droits, AIPD, violations), sort des données en fin de contrat, audit.
- Le champ t.sous_traitance impose de renseigner le contrat. À défaut, l'alerte de l'art. 25.5 du cahier des charges se déclenche.
- Les mentions viennent des standards internationaux et sont marquées comme telles.

**Utile pour :** le tableau des sous-traitants de la fiche et le moteur d'alertes.

## C15 - Version publiée du référentiel.docx
*Chemin :* `01 Togo/01 Livrables Togo/C15 - Version publiée du référentiel.docx`

**En une phrase :** procédure de publication d'une version du référentiel juridictionnel, préalable à la mise en production.

**Contenu :**
- La publication est un acte explicite. Avant elle, la version reste au statut Brouillon ou En simulation et ne s'applique à aucune qualification.
- Six étapes : saisir les rubriques de l'annexe 3, contrôler la couverture des bulles, exécuter la recette en simulation sans écart, mesurer l'incidence sur les organisations, publier (acte horodaté, attribué et irréversible), informer et ouvrir des revues, sans changement automatique des régimes déjà arrêtés.
- Prérequis : coordonnées de l'autorité, liste des pays adéquats si elle est publiée, validation des couleurs, bulles des champs déterminants rédigées.
- Traçabilité : chaque qualification porte la juridiction et la version appliquée.

**Utile pour :** le back-office de gestion des versions du référentiel et le workflow de publication.

## D01 - Liste arrêtée des notions appelant une bulle.docx
*Chemin :* `01 Togo/01 Livrables Togo/D01 - Liste arrêtée des notions appelant une bulle.docx`

**En une phrase :** périmètre des notions qui ont une bulle d'aide. Validé le 6 septembre 2026.

**Contenu :**
- 61 notions au total, dont 57 servies au Togo et 26 déterminantes. Une notion déterminante sans bulle bloque la publication.
- Notions déterminantes, avec les champs liés : donnee_a_caractere_personnel, donnees_sensibles, donnees_genetiques, donnees_biometriques, interconnexion, numero_national_identification, interet_public_recherche, personne_publique, mission_service_public, mission_regalienne, registre_information_public, cadre_domestique, correspondant, correspondant_role_applicatif, correspondant_interne_externe, formalite_prealable, transfert_international, risque_eleve, violation_donnees, risque_droits_libertes, delai_notification, information_personnes, juridiction_applicable, volume_personnes, caracteristiques_autorisation, norme_simplifiee.
- 31 autres notions servies, réparties par domaine : objet, licéité, formalités, conservation et sécurité, transferts, AIPD, mandat.
- 4 notions propres au Bénin ne sont pas servies : caracteristiques_autorisation_benin, dispense_benin, objets_411, exemption_benin.

**Utile pour :** le contrôle de couverture des bulles et le fichier bulles-information.json.

## D02 - Contenu rédigé des bulles d_information.docx
*Chemin :* `01 Togo/01 Livrables Togo/D02 - Contenu rédigé des bulles d_information.docx`

**En une phrase :** texte complet des 57 bulles d'aide servies au Togo.

**Contenu :**
- Gabarit de chaque bulle : identifiant, définition en 2 ou 3 phrases, exemples, contre-exemple, référence citée, conséquence sur la qualification, indicateur « fiche développée ». Réserve commune : « Cette aide est générale… ne se substitue pas à l'analyse d'un juriste. »
- 11 domaines : objet, licéité, nature des données, qualité de l'organisme, correspondant, formalités, conservation et sécurité, transferts, AIPD, violations, cadre de l'intervention.
- Références notables : données personnelles et définitions (art. 4) ; base juridique (art. 14 et 15) ; sensibles (art. 4 et 21) ; génétiques (art. 8, 1°), biométriques (8, 5°), interconnexion (8, 3° et 32-34), NNI (8, 4°), recherche et intérêt public (8, 6°) ; mission régalienne (9, 1° à 3°) ; récépissé (art. 6) ; norme simplifiée (art. 7, aucune publiée) ; conservation (art. 16 et 53) ; sécurité (art. 19 et 52) ; transferts (art. 28 à 31).
- Conséquences chiffrées : récépissé sous 1 mois, seuil de 10 000 personnes, 72 heures pour les violations (standard international, pas la loi togolaise).
- La bulle « cadre domestique » indique que la loi togolaise ne consacrerait pas d'exclusion domestique autonome et que la notion n'est pas servie. Or l'art. 3, 1° de la loi prévoit cette exclusion.
- La bulle « données sensibles » dit que leur présence « écarte le régime de la déclaration ». C'est contraire au logigramme C06 et au cas CAS-TG-07 (sensibles hors art. 8 → déclaration).
- La bulle « instruction » dit que le silence de l'IPDCP ne vaut pas acceptation, alors que l'art. 11 de la loi répute l'autorisation favorable en cas de silence.
- Sept bulles ouvrent une fiche développée : donnée personnelle, base juridique, sensibles, correspondant, transfert, AIPD, violation.

**Utile pour :** les bulles d'aide contextuelles (bulles-information.json) et, par génération, le glossaire D04.

## D03 - Fiches d_explication développées.docx
*Chemin :* `01 Togo/01 Livrables Togo/D03 - Fiches d_explication développées.docx`

**En une phrase :** cadrage des fiches d'explication longues qui s'ouvrent depuis les bulles. Statut : « Cadré, rédaction à venir ». Criticité : recommandé.

**Contenu :**
- Sept notions : donnee_a_caractere_personnel, base_juridique, donnees_sensibles, correspondant, transfert_international, aipd, violation_donnees.
- Plan type : 3 à 5 paragraphes, exemples sectoriels tirés de F02, cas limites, texte cité, effet sur la qualification, réserve.
- Fiches non rédigées. Elles ne conditionnent pas la publication, car le contrôle ne porte que sur les bulles.

**Utile pour :** l'aide contextuelle approfondie (fonction future).

## D04 - Glossaire consolidé.docx
*Chemin :* `01 Togo/01 Livrables Togo/D04 - Glossaire consolidé.docx`

**En une phrase :** glossaire alphabétique des 57 notions servies au Togo, généré à partir du contenu des bulles.

**Contenu :**
- Tableau terme / définition / référence, d'« Analyse d'impact » (art. 76, 3°) à « Vraisemblance ».
- Les définitions sont identiques à celles de D02 (même source, jamais rédigé à part).
- Accessible depuis la recherche transverse et exportable.
- Nombreux termes sans référence textuelle : finalité, contrat, intérêt légitime, gravité, mandat, etc.

**Utile pour :** la page glossaire et la recherche transverse.

## E01 - Fiche de registre.docx
*Chemin :* `01 Togo/01 Livrables Togo/E01 - Fiche de registre.docx`

**En une phrase :** gabarit de la fiche de registre imprimable (une fiche par page). Statut : à valider par la gérance.

**Contenu :**
- En-tête : référence de la fiche, référence et validité de la décision de l'autorité, juridiction et texte appliqués, date et auteur, mention du cabinet sous mandat.
- Corps : 34 sections qui suivent l'ordre des rubriques du socle (de 1. Organisme à 12. Mesures de sécurité). Plusieurs entrées ne portent que le numéro de rubrique (« 2 », « 4 », « 9 »…), sans libellé de champ.
- Pied de fiche : régime, motifs et juridiction ; besoin d'AIPD et fondement ; réserve de l'art. 12 ; signature du correspondant ; visa du responsable.

**Utile pour :** la génération PDF de la fiche de registre.

## E02 - Registre complet.docx
*Chemin :* `01 Togo/01 Livrables Togo/E02 - Registre complet.docx`

**En une phrase :** spécification des exports du registre complet.

**Contenu :**
- Formats : PDF (gabarit E01), CSV et XLSX (une ligne par traitement), export structuré complet pour la réversibilité (art. 41 du cahier des charges).
- 37 colonnes ordonnées, de t.reference à t.validite_decision.
- Tableaux imbriqués (accès, communications, transferts, sous-traitants, droits) : un onglet séparé lié par la référence est préféré.
- Les champs export_registre=non sont exclus, par exemple t.origine_cartographie.
- Pied de document : date, auteur, cabinet, juridiction et version. L'export est consigné au journal de conformité.

**Utile pour :** le module d'export du registre.

## E03 - Dossiers de formalité.docx
*Chemin :* `01 Togo/01 Livrables Togo/E03 - Dossiers de formalité.docx`

**En une phrase :** pièces de dossier par régime, pré-remplissage et contrôle avant dépôt.

**Contenu :**
- Dispense : aucune pièce. Déclaration : formulaire IPDCP, fiche de registre, accusé de réception, récépissé. Avis motivé : niveau de protection, demande d'avis, clauses.
- Autorisation : demande selon l'art. 10, rapport d'AIPD, mesures de sécurité, accusé de réception et décision. Acte réglementaire : projet et saisine, avis motivé, acte publié.
- Le pré-remplissage s'appuie sur registre-champs.csv. Pour un champ sans correspondance, le choix est consigné champ par champ.
- Le statut « Prêt à être transmis » est bloqué tant qu'il manque une pièce ou un champ ; la liste des manques est affichée.
- La numérotation saute la section 2.

**Utile pour :** le module des formalités (génération et dépôt des dossiers).

## E04 - Rapport d_analyse d_impact.docx
*Chemin :* `01 Togo/01 Livrables Togo/E04 - Rapport d_analyse d_impact.docx`

**En une phrase :** structure et mentions du rapport d'AIPD exporté. Statut : à valider par la gérance.

**Contenu :**
- Quatre sections, identiques à la grille de C08.
- Mentions : références du traitement, juridiction et version du référentiel, critères déclencheurs et leur source, score, mode de calcul et niveau, risque résiduel et conclusion.
- Avis et signature du correspondant, validation horodatée, réserve de l'art. 12.

**Utile pour :** la génération du rapport d'AIPD.

## E05 - Notifications de violation.docx
*Chemin :* `01 Togo/01 Livrables Togo/E05 - Notifications de violation.docx`

**En une phrase :** modèles de notification à l'autorité et de communication aux personnes.

**Contenu :**
- Deux modèles, pré-remplis depuis la fiche d'incident.
- Notification à l'IPDCP : identités, dates de survenance et de découverte, nature (fuite, perte, vol, accès non autorisé, altération, indisponibilité), personnes et données touchées en nombre approximatif, traitements et juridictions, conséquences, mesures, décision d'informer les personnes, pièces jointes.
- Communication aux personnes : nature de la violation en clair, point de contact, conséquences, mesures et recommandations.
- Paramètres : 72 heures après la prise de connaissance, destinataire IPDCP, source standard_international.

**Utile pour :** le module des incidents (documents générés).

## E06 - Rapport d_activité de cabinet.docx
*Chemin :* `01 Togo/01 Livrables Togo/E06 - Rapport d_activité de cabinet.docx`

**En une phrase :** contenu des rapports d'activité d'un cabinet mandaté.

**Contenu :**
- Rapport par client en PDF et en tableau. Rubriques : en-tête du mandat, interventions, fiches traitées, qualifications, formalités et délais, AIPD, incidents, sensibilisation (lot 2), réactivité, état à la clôture (indice et échéances), pied de page.
- Chaque rubrique est sourcée : journal de conformité, moteur, modules, tableau de bord.
- Rapport consolidé interne au cabinet : charge par consultant, échéances, clients inactifs, mandats expirants, décompte des mandats actifs pour la facturation. Le dossier propre du cabinet est exclu.
- Règles : seule l'activité du cabinet figure au rapport. Il reste disponible après la fin du mandat, sans le contenu des fiches. Sa production est journalisée et strictement bornée à l'organisation active.

**Utile pour :** l'espace cabinet (reporting et facturation).

## F02 - Modèles sectoriels de traitement.docx
*Chemin :* `01 Togo/01 Livrables Togo/F02 - Modèles sectoriels de traitement.docx`

**En une phrase :** modèles de fiches pré-remplies du lot 1, tirés du registre type (156 fiches). Criticité : recommandé.

**Contenu :**
- Huit modèles : paie, clients et prospects, vidéosurveillance, contrôle d'accès, dossier médical (santé), dossier scolaire (éducation), bénéficiaires (ONG), connaissance du client (finance inclusive et paiement).
- Pour chaque modèle sont indiqués les champs pré-remplis (finalité, catégories, base, durée…) et les champs laissés vides (volume, sécurité, outils, transferts, sous-traitants, biométrie…).
- Règles : jamais de pré-remplissage d'un champ déterminant pour le moteur. Le modèle est rattaché à une ou plusieurs juridictions, avec un signalement s'il est appliqué hors de sa juridiction. Les durées sont indicatives et modifiables. Une fiche issue d'un modèle naît au statut Brouillon.

**Utile pour :** la bibliothèque de modèles de traitement.

## F03 - Grille d_analyse d_impact détaillée.docx
*Chemin :* `01 Togo/01 Livrables Togo/F03 - Grille d_analyse d_impact détaillée.docx`

**En une phrase :** questions, poids et calcul du score de l'AIPD. Statut : à valider par la gérance.

**Contenu :**
- 20 questions en 4 sections, chaque section ayant son propre avancement.
- Section 1 : 1.1 à 1.4 (reprises automatiques, technologies employées).
- Section 2 : 2.1 à 2.5. Les questions 2.4 (durée justifiée) et 2.5 (information et droits) se répondent par oui, non ou partiellement, avec un poids de 2.
- Section 3 : 3.1 à 3.6 cotent la gravité et la vraisemblance de trois événements (accès non autorisé, modification non désirée, disparition), de négligeable à maximale, avec un poids de 4. La question 3.7 (réversibilité) a un poids de 3.
- Section 4 : 4.1 à 4.4 (mesures en place, plan d'actions, risque résiduel faible, modéré ou élevé avec un poids de 5, avis du correspondant).
- Score : risque d'un événement = gravité × vraisemblance (chacune cotée de 1 à 4). On retient le maximum des trois événements, corrigé par la section 2, sur une échelle de 0 à 100. Paliers : 0-33 faible, 34-66 modéré, 67-100 élevé.
- Si le risque résiduel est élevé, la loi ne prévoit aucune consultation préalable au Togo : Waɖɛ recommande de saisir l'IPDCP et consigne la décision. Tout est administrable en back-office.

**Utile pour :** le module d'AIPD (questionnaire et score).

## I01 - Jeu de cas de recette du moteur.docx
*Chemin :* `01 Togo/01 Livrables Togo/I01 - Jeu de cas de recette du moteur.docx`

**En une phrase :** présentation des 9 cas de recette du logigramme togolais (un par chemin, 5 sorties couvertes).

**Contenu :**
- CAS-TG-01 à CAS-TG-09, avec les réponses et le régime attendu. Ce sont les mêmes que dans cas-de-recette-togo.csv.
- Cas d'opposition : rôle Correspondant sans désignation (droit commun attendu) ; mandat de cabinet sans désignation (pas de dispense).
- Autres cas d'opposition : double qualification Togo et Bénin présentée côte à côte sans primauté ; qualification ancienne restant explicable après une nouvelle version ; même résultat par la qualification continue et par l'assistant.

**Utile pour :** la recette du moteur (tests automatisés, simulation avant publication).

## K01 - Banque pédagogique complétée.docx
*Chemin :* `01 Togo/01 Livrables Togo/K01 - Banque pédagogique complétée.docx`

**En une phrase :** livrable du lot 2 non rempli (version 0.1, « Ouvert, à renseigner », pour mémoire).

**Contenu :**
- Contenu attendu : un 5e panier pour le tri des régimes, au moins 3 cas par panier dont plusieurs opposant la dispense à la réserve du transfert, et la correction du nom du panier « acte réglementaire ».
- Sources prévues : cours de protection des données au Togo, bordereau AMELEGAL du 6 septembre 2026.
- Section « Contenu du livrable » : « À renseigner ».

**Utile pour :** le module de sensibilisation et le jeu (lot 2).

## K02 - Barème jauges et paliers.docx
*Chemin :* `01 Togo/01 Livrables Togo/K02 - Barème jauges et paliers.docx`

**En une phrase :** livrable du lot 2 non rempli (version 0.1, « Ouvert, à renseigner »).

**Contenu :**
- Contenu attendu : barème des sanctions en FCFA d'après les montants légaux, effets des décisions sur les 3 jauges, seuils des 5 paliers de maîtrise, durée des minuteurs.
- Mêmes sources prévues que K01. Contenu : « À renseigner ».

**Utile pour :** le module de sensibilisation et le jeu (lot 2).

## cas-de-recette-togo.csv
*Chemin :* `01 Togo/01 Livrables Togo/_spécifications développeur/cas-de-recette-togo.csv`

**En une phrase :** jeu de tests exécutable du moteur de qualification togolais (séparateur « ; », avec BOM).

**Contenu :**
- Colonnes : cas, reponses, TG-Q1 à TG-Q8, regime_attendu, libelle_attendu, fondement, motif_attendu, aipd_attendue.
- 9 lignes. 01 (Q1 oui, Q2 oui) → TG-DISPENSE. 02 (correspondant + transfert) → TG-AVIS. 03 (correspondant, pas de transfert) → TG-DISPENSE. 04 (sensibles, public, régalien) → TG-ACTE. 05 (sensibles, public, non régalien) → TG-AUTORISATION. 06 (sensibles, privé, art. 8) → TG-AUTORISATION. 07 (sensibles, privé, hors art. 8) → TG-DECLARATION. 08 (non sensibles) → TG-DECLARATION. 09 (Q1 non) → TG-DISPENSE.
- aipd_attendue vaut « oui » pour les cas 04, 05 et 06, et « selon critères » pour les autres.
- Les motifs attendus reprennent mot pour mot ceux de C06.

**Utile pour :** les tests automatisés du moteur et la simulation avant publication (C15, I01).

## referentiel-togo.json
*Chemin :* `01 Togo/01 Livrables Togo/_spécifications développeur/referentiel-togo.json`

**En une phrase :** référentiel machine de la juridiction Togo (v1.0 du 6 septembre 2026, « validé par AMELEGAL, à implémenter »), qui reprend les livrables C01 à C13. Avertissement : aucune valeur ne doit être codée en dur (art. 8.1 et 27.6 du cahier des charges).

**Contenu :**
- Clés de premier niveau : meta, juridiction (TG, CEDEAO, herite_du_socle true), sources (texte principal, textes d'application « non publiés », 20 articles clés), autorite, terminologie, regimes (5, avec famille de couleur et ordre), logigramme, feuilles_de_route, aipd, violations, correspondant, transferts, indice.
- logigramme : entrée TG-Q1, 8 questions et 5 sorties. Chaque question porte champ, type, aide, fondement et branches oui/non (type question ou sortie, cible, motif).
- TG-Q8 a 7 options : donnees_genetiques, recherche_sante, infractions_condamnations, interconnexion, numero_national_identification, donnees_biometriques, interet_public_historique_statistique_scientifique. Le libellé de la question ne cite ni la recherche en santé ni les infractions.
- aipd : 5 critères TG-AIPD-1 à 5 (seuil de 10 000 pour le volume), présomption pour TG-AUTORISATION et TG-ACTE, grille en 4 sections, 3 niveaux, source standard_international.
- violations : 72 heures, point de départ à la prise de connaissance, destinataire IPDCP, rappels à 0,25 / 0,5 / 0,75 / 0,9, arbre TG-V1/V2, consignation obligatoire.
- correspondant : désignation non obligatoire, 6 missions, correspondant_externe.admis = null (non tranché). transferts : pays_reconnus vide, formalite_associee TG-AVIS. indice : poids 0,35 / 0,35 / 0,2 / 0,1 et seuils 0-39 / 40-64 / 65-84 / 85-100, sensibilisation inactive.
- autorite : adresse, téléphone, courriel et site à null, alors que C03 les renseigne. Modalités de dépôt « à renseigner ». Délais : déclaration 1 mois prorogeable une fois, les autres régimes non chiffrés.
- Le fichier ne contient ni le registre, ni la sous-traitance, ni les bulles : ils sont dans les fichiers du dossier commun.

**Utile pour :** le chargement du référentiel Togo dans le back-office et l'exécution du moteur (qualification, AIPD, violations, indice).

# Partie 4 — Bénin : livrables AMELEGAL (02 Bénin/01 Livrables Bénin)

Remarques communes : chaque fiche .docx suit le même gabarit (juridiction Bénin, responsable AMELEGAL, version 1.0 du 6 septembre 2026, criticité, phase du chronogramme, statut), cite la loi n° 2017-20 portant code du numérique (Livre cinquième), le référentiel machine `referentiel-benin.json`, le jeu `cas-de-recette-benin.csv` et le cahier des charges Waɖɛ v1.0 du 12 août 2026. Le critère d'achèvement est partout le même : jeu de recette sans écart en simulation et contrôle de couverture des bulles sans lacune. Les articles cités « art. 8.3, 27, 29… » dans l'en-tête « Fondement » renvoient au cahier des charges ; les articles 380 à 490 renvoient à la loi béninoise.

## C01 - Identification de la juridiction.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C01 - Identification de la juridiction.docx`

**En une phrase :** fiche d'identité de la juridiction Bénin dans le référentiel.

**Contenu :**
- Nom : Bénin ; nom officiel : République du Bénin ; code pays BJ ; langue d'affichage fr.
- Rattachement au socle régional CEDEAO, « hérite du socle : oui », statut « à publier au lot 1 ».
- L'héritage du socle est déclaré mais sans effet : le socle n'étant pas renseigné, toutes les règles viennent du droit interne.
- Fondement : annexe 3 du cahier des charges ; phase 4 ; criticité Bloquant ; statut « Rempli et exploitable par le développeur ».

**Utile pour :** paramétrage de la juridiction (bloc `juridiction` du référentiel, back-office multi-juridictions).

## C02 - Sources.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C02 - Sources.docx`

**En une phrase :** liste des textes et documents de l'autorité sur lesquels repose le référentiel béninois.

**Contenu :**
- Texte principal : loi n° 2017-20 portant code du numérique, Livre cinquième.
- 17 articles clés cartographiés : 1er/380/381 (champ), 382 (exclusion domestique), 394 (données sensibles), 397 (régimes spéciaux), 405 (déclaration, droit commun), 406 (déclaration simplifiée), 407 (autorisation ; al. 2, obligation de consulter en cas de doute), 408 (exemption, fermée aux autorités publiques), 409 (dossier, 12 mentions minimales), 410 (dispenses), 411 (décret en Conseil des ministres après avis motivé), 412 (délais, silence valant acceptation), 413 (dépôt), 428 (AIPD), 429 (consultation préalable), 464 (composition APDP), 490 (pouvoirs d'investigation, délais doublés).
- Doctrine APDP versée : rapports annuels 2022, 2023, 2024 ; décisions n° 2019-020, 2022-0007, 2024-008, 2024-009 ; formulaire unique et annexes 1 à 4 ; modèle de registre ; modèle d'AIPD.
- Cite aussi le « Décisiomètre des formalités préalables Bénin, huit questions et huit sorties, AMELEGAL 2026 ».
- La numérotation saute de la section 1 à la section 3 (pas de section 2).

**Utile pour :** bloc `sources` du référentiel, références légales affichées dans les bulles et motifs.

## C03 - Autorité de contrôle.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C03 - Autorité de contrôle.docx`

**En une phrase :** paramètres de l'APDP (identité, dépôt, délais, effets du silence, validité des décisions).

**Contenu :**
- Autorité de protection des données à caractère personnel (APDP), art. 464 ; adresse, téléphone, courriel et site « à renseigner ».
- Dépôt : voie électronique, voie postale, guichet contre accusé de réception (art. 413).
- Délais : 60 jours, prorogeables une fois de 30 jours par décision motivée (art. 412) ; délais doublés quand l'APDP exerce ses pouvoirs d'investigation (art. 490) ; consultation préalable après AIPD : 8 semaines, prorogeables de 6 (art. 429).
- Silence valant acceptation (art. 412) : le logiciel doit produire un statut « Acceptation tacite » à l'échéance, distinct de « Acceptée ».
- Décisions de l'APDP valables 2 ans, avec alerte de renouvellement.
- Issues d'un dossier : récépissé, extrait de délibération d'autorisation, rejet, radiation, report pour complément, certificat de conformité sur demande (valable 2 ans).
- Statut : à valider par la gérance.

**Utile pour :** module de suivi des formalités (comptes à rebours, statuts, alertes de renouvellement), bloc `autorite` du référentiel.

## C04 - Terminologie.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C04 - Terminologie.docx`

**En une phrase :** libellés affichés propres au Bénin et intitulés officiels des 8 régimes.

**Contenu :**
- Clés de libellés : autorite = APDP ; correspondant = « délégué à la protection des données » (DPD) ; analyse_impact = « analyse d'impact relative à la protection des données » (AIPD) ; registre = « registre des activités de traitement » ; responsable = « responsable du traitement » ; personne concernée ; sous-traitant.
- Régimes et fondements : BJ-HORS-CHAMP (art. 1er, 380, 381), BJ-DOMESTIQUE (382 et 410, 1°), BJ-DISPENSE (410), BJ-DECRET (411), BJ-AUTORISATION (407), BJ-DECLARATION-SIMPLIFIEE (406), BJ-EXEMPTION (408), BJ-DECLARATION (405, 409, 412, 413).
- Chaque régime a un libellé court et un intitulé officiel (ex. « Décret en Conseil des ministres pris après avis motivé de l'APDP »).

**Utile pour :** couche de libellés par juridiction (bloc `terminologie`), affichage des résultats de qualification.

## C05 - Régimes de formalité.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C05 - Régimes de formalité.docx`

**En une phrase :** définition des 8 sorties du moteur béninois, de leur ordre, de leur famille de couleur et de leur portée.

**Contenu :**
- Ordre et familles de couleur (art. 23.2 du CDC) : 1 HORS-CHAMP neutre, 2 DOMESTIQUE neutre, 3 DISPENSE neutre, 4 DECRET critique, 5 AUTORISATION élevé, 6 DECLARATION-SIMPLIFIEE standard, 7 EXEMPTION neutre, 8 DECLARATION standard.
- Dispense : porte sur la formalité seule ; registre, information, sécurité, durées de conservation et rapport annuel restent dus.
- Décret : régime le plus lourd ; l'avis de l'APDP est publié avec le décret, favorable ou non.
- Autorisation : extrait de délibération ; décision unique possible pour des traitements de même finalité sur engagement de conformité.
- Exemption : suppose une décision de l'APDP sur des catégories de traitements, pas un droit acquis, fermée aux autorités publiques.
- Déclaration préalable = droit commun (récépissé) ; « la déclaration est la règle, les autres sorties sont des exceptions ».
- HORS-CHAMP et DOMESTIQUE sont des exclusions, pas des régimes : affichées à part, non comptées dans la répartition du tableau de bord, sans feuille de route de dépôt.
- Statut : validé par AMELEGAL le 6 septembre 2026.

**Utile pour :** moteur de qualification (sorties), code couleur, tableau de bord.

## C06 - Logigramme de qualification.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C06 - Logigramme de qualification.docx`

**En une phrase :** arbre de décision complet du Bénin, 8 questions et 8 sorties, avec champs, motifs et règles transverses.

**Contenu :**
- Enchaînement : Q1 données identifiantes ? non → HORS-CHAMP ; Q2 cadre domestique ? oui → DOMESTIQUE ; Q3 dispense art. 410 (registre privé, comptabilité générale, rémunérations, fournisseurs, membres d'un organisme à but non lucratif, archivage à long terme) ? oui → DISPENSE ; Q4 personne publique ou service public ? oui → Q5, non → Q6 ; Q5 l'un des 5 objets de l'art. 411 ? oui → DECRET ; Q6 catégories particulières ou caractéristique de l'art. 407 ? oui → AUTORISATION ; Q7 norme simplifiée publiée ? oui → DECLARATION-SIMPLIFIEE ; Q8 catégorie exemptée par décision APDP ? oui → EXEMPTION, non → DECLARATION.
- Les 5 objets de l'art. 411 : sûreté/défense/sécurité publique ; infractions pénales et condamnations ; recensement ; origines raciales/ethniques, opinions, syndicat, santé, vie sexuelle ; salaires, pensions, impôts.
- Champs : Q1 bloc2.nature_donnees_personnelles, Q2 bloc1.cadre_domestique, Q3 bloc1.dispense_article_410, Q4 bloc1.personne_publique_ou_mission_service_public, Q5 bloc3.objets_article_411, Q6 bloc2.caracteristiques_article_407, Q7 bloc1.norme_simplifiee_applicable, Q8 bloc3.exemption_article_408 (avec l'identifiant de bulle associé).
- Règle bloquante : si personne publique/service public = vrai, Q8 est forcée à faux (exemption fermée aux autorités publiques).
- Règles transverses : BJ-T1 AIPD si risque élevé (art. 428) ; BJ-T2 consultation APDP si risque résiduel élevé, 8 semaines + 6 (art. 429) ; BJ-T3 le doute oblige à consulter l'APDP, proposé quand l'utilisateur écarte le résultat (art. 407 al. 2) ; BJ-T4 toute modification d'une déclaration = nouvelle déclaration (art. 412) ; BJ-T5 décisions valables 2 ans (pratique APDP).
- Écart texte/pratique : sorties 6 et 7 (simplifiée, exemption) peu appliquées ; rapport APDP 2022 : les responsables déclarent systématiquement. Règle : tant qu'aucune norme ou décision d'exemption n'est publiée, afficher le régime légal en signalant que la pratique impose de déclarer, et proposer le dossier de déclaration.

**Utile pour :** cœur du moteur de qualification et assistant pas à pas, motifs restitués à l'utilisateur.

## C07 - Feuilles de route.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C07 - Feuilles de route.docx`

**En une phrase :** étapes à suivre et pièces attendues pour chaque sortie, plus le déclenchement des annexes du formulaire unique.

**Contenu :**
- HORS-CHAMP / DOMESTIQUE : documenter le motif et réévaluer (données identifiantes, communication à des tiers ou diffusion).
- DISPENSE : documenter le cas de l'art. 410, maintenir registre/information/sécurité/durées/rapport annuel, réévaluer si finalité ou destinataires changent.
- DECRET : projet de décret → dossier de saisine (formulaire unique) → avis motivé APDP → adoption en Conseil des ministres et publication avec l'avis.
- AUTORISATION : AIPD si risque élevé → dossier (formulaire unique, annexes 1 à 4) → dépôt électronique/postal/guichet → instruction 60 j + 30, doublée si investigation → extrait de délibération, validité 2 ans.
- DECLARATION-SIMPLIFIEE : vérifier la norme, déclarer par référence expresse, à défaut déclaration de droit commun. EXEMPTION : vérifier la décision, documenter, preuve de désignation du délégué, à défaut déclarer.
- DECLARATION : AIPD si besoin, dossier avec les 12 mentions de l'art. 409, dépôt, 60 j + 30 puis réponse réputée favorable, récépissé valable 2 ans.
- Annexes : annexe_1 Sous-traitance (bloc3.sous_traitance), annexe_2 Communication (bloc3.communication_tiers), annexe_3 Interconnexion (art. 407 contient interconnexion_fichiers), annexe_4 Transfert (bloc3.transfert_international).

**Utile pour :** feuilles de route post-qualification, tâches et pièces du module des formalités.

## C08 - Analyse d_impact.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C08 - Analyse d_impact.docx`

**En une phrase :** critères de déclenchement de l'AIPD, consultation préalable et grille en 4 sections pour le Bénin.

**Contenu :**
- Fondement : art. 428 (AIPD si risque élevé) et 429 (consultation préalable si risque résiduel élevé).
- AIPD requise dès qu'un critère est réuni : BJ-AIPD-1 risque élevé (aipd.score_risque, texte) ; -2 données sensibles art. 394 ; -3 biométrie, numéro national d'identification ou interconnexion ; -4 transfert vers un État tiers ; -5 décision automatisée excluant d'un droit/prestation/contrat (texte) ; -6 volume > 10 000 personnes. Les critères 2, 3, 4 et 6 sont de source standard_international.
- Présomption d'AIPD pour BJ-AUTORISATION et BJ-DECRET (aucune explication supplémentaire dans la fiche).
- Consultation préalable : 8 semaines prorogeables de 6, créée comme une formalité distincte avec son compte à rebours.
- Grille : 1 Description et finalité, 2 Nécessité et proportionnalité, 3 Risques pour les personnes, 4 Mesures de sécurité et de réduction ; niveaux faible / modéré / élevé.
- Statut : à valider par la gérance.

**Utile pour :** module AIPD (déclenchement automatique, consultation préalable).

## C09 - Violations de données.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C09 - Violations de données.docx`

**En une phrase :** paramètres de notification des violations, faute de texte béninois.

**Contenu :**
- Le Livre cinquième ne fixe aucun délai : paramètres tirés des standards internationaux (source=standard_international, réserve d'interprétation de l'art. 12 du CDC).
- Délai 72 heures à compter de la prise de connaissance par le responsable ; destinataire APDP ; rappels à 25 %, 50 %, 75 %, 90 % du délai ; consignation au registre interne obligatoire dans tous les cas.
- Arbre : BJ-V1 risque pour les droits et libertés ? non → ni notification ni information ; BJ-V2 risque élevé ? oui → notification APDP + information des personnes ; non → notification APDP seulement.
- Formulaire de signalement publié par l'APDP.

**Utile pour :** module de gestion des incidents (compte à rebours, arbre de décision, notifications).

## C10 - Correspondant.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C10 - Correspondant.docx`

**En une phrase :** statut du délégué à la protection des données au Bénin et son effet sur les formalités.

**Contenu :**
- Dénomination : délégué à la protection des données ; fondement art. 408 ; désignation non obligatoire.
- La désignation d'un délégué indépendant tenant le registre ouvre la voie de l'exemption de l'art. 408, qui suppose une décision de l'APDP, n'est pas un droit acquis et est fermée aux autorités publiques.
- Règle moteur : la désignation seule ne produit pas l'exemption ; Q8 exige une décision APDP couvrant la catégorie.
- Pièce : lettre d'engagement du DPD (modèle APDP).
- Sections numérotées 1, 5, 6, 7 : les sections 2 à 4 sont absentes du document.

**Utile pour :** gestion du correspondant/DPD, question Q8 du moteur.

## C11 - Transferts internationaux.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C11 - Transferts internationaux.docx`

**En une phrase :** règle béninoise sur les transferts vers un État tiers.

**Contenu :**
- Le transfert vers un État tiers est un cas d'autorisation préalable de l'art. 407 → régime BJ-AUTORISATION.
- Pays reconnus : liste vide, « à renseigner au vu des décisions de l'APDP ».
- Pièce : annexe 4 du formulaire unique (Transfert).
- Fiche courte (sections 1, 2 et 6 seulement) ; statut à valider par la gérance.

**Utile pour :** bloc `transferts` du référentiel, champ t.transfert_international, annexe 4.

## C12 - Registre.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C12 - Registre.docx`

**En une phrase :** correspondance entre le modèle de registre de l'APDP (12 sections) et les champs du registre Waɖɛ.

**Contenu :**
- Le registre Waɖɛ reprend intégralement le modèle APDP (12 sections, toutes colonnes) et y ajoute les champs du moteur.
- Champs propres au Bénin issus du modèle : N° IFU (identifiant fiscal unique), numéro RCCM.
- Sections APDP : 1 organisme, 2 responsable, 3 délégué, 4 activité (code, dénomination, date, finalités, fondement), 5 principes (consentement, droits), 6 données traitées, 7 cibles, 8 durées, 9 personnes ayant accès, 10 communications, 11 transferts, 12 mesures de sécurité.
- 70 champs au total dans registre-champs.csv (dossier commun), dont 66 applicables au Bénin ; table de 66 champs avec identifiant, bloc, type, obligatoire (O/R/C) et rattachement au moteur.
- Champs alimentant le moteur : org.pays_etablissement, org.nature_publique, org.mission_service_public, dpo.designe, dpo.statut, t.juridiction, t.cadre_domestique, t.dispense_article_410, t.norme_simplifiee_applicable, t.nature_donnees_personnelles, t.classification_donnees, t.donnees_sensibles, t.caracteristiques_article_407, t.volume_personnes, t.transfert_international, t.objets_article_411, t.exemption_article_408.
- En-tête : référence de la décision de l'autorité et validité de la décision.

**Utile pour :** modèle de données du registre et formulaire de fiche de traitement.

## C13 - Indice de conformité paramètres.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C13 - Indice de conformité paramètres.docx`

**En une phrase :** pondérations et seuils de l'indice de conformité pour le Bénin.

**Contenu :**
- Composantes : complétude du registre 35 %, formalités accomplies 35 %, AIPD réalisées 20 %, violations traitées 10 % (calcul renvoyé au livrable G01) ; poids administrables par juridiction.
- Seuils : Action requise 0-39, À surveiller 40-64, Bon, à consolider 65-84, Solide 85-100.
- Composante sensibilisation inactive jusqu'au lot 2 (repondération à ce moment).
- Restitution : jauge circulaire, valeur, libellé, détail du calcul, équivalent textuel pour l'accessibilité.

**Utile pour :** tableau de bord, calcul de l'indice de conformité.

## C14 - Sous-traitance.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C14 - Sous-traitance.docx`

**En une phrase :** mentions minimales du contrat de sous-traitance et effet dans le logiciel.

**Contenu :**
- Référence : annexe 1 du formulaire unique de l'APDP.
- 10 mentions : parties et qualités ; objet, durée, nature, finalité ; catégories de données et de personnes ; instruction documentée seule ; confidentialité ; mesures de sécurité ; sous-traitance ultérieure avec information préalable ; assistance (droits, AIPD, violations) ; restitution ou suppression en fin de prestation ; audit.
- t.sous_traitance impose de renseigner le contrat ; absence de contrat conforme → alerte de l'art. 25.5 du CDC ; déclenche aussi l'annexe 1.
- Réserve : mentions issues des standards internationaux, pas d'un texte. Criticité : Recommandé.

**Utile pour :** gestion des sous-traitants, alertes, annexe 1 du dossier.

## C15 - Version publiée du référentiel.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/C15 - Version publiée du référentiel.docx`

**En une phrase :** procédure de publication d'une version du référentiel béninois.

**Contenu :**
- Publication = acte explicite ; avant cela, statut Brouillon ou En simulation, sans effet sur les qualifications.
- 6 étapes : créer en brouillon (rubriques obligatoires de l'annexe 3) ; contrôle de couverture des bulles ; jeu de recette en simulation sans écart ; mesure d'impact sur les organisations rattachées ; publication horodatée, attribuée, irréversible ; information des organisations et revues de traitement confiées au correspondant, sans modification automatique des régimes arrêtés.
- Préalables à la première version : coordonnées de l'APDP, validation des familles de couleur, bulles des champs déterminants rédigées.
- Chaque qualification garde la juridiction et la version appliquée. Phase 17, criticité « Préalable à la mise en production ».

**Utile pour :** back-office de gestion des versions du référentiel.

## D01 - Liste arrêtée des notions appelant une bulle.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/D01 - Liste arrêtée des notions appelant une bulle.docx`

**En une phrase :** liste des notions qui reçoivent une bulle d'aide au Bénin, dont celles qui bloquent la publication.

**Contenu :**
- 61 notions, 60 servies au Bénin, 29 déterminantes pour le moteur (bulle obligatoire, son absence bloque la publication).
- Déterminantes : donnée personnelle, données sensibles, génétiques, biométriques, interconnexion, NNI, intérêt public/recherche, personne publique, mission de service public, mission régalienne, registre d'information du public, cadre domestique, 3 notions sur le correspondant, formalité préalable, transfert international, risque élevé, 4 notions sur les violations, juridiction applicable, volume de personnes, et 5 notions propres au Bénin : caracteristiques_autorisation_benin, dispense_benin, objets_411, norme_simplifiee, exemption_benin.
- 31 autres notions servies (traitement, finalité, bases juridiques, sécurité, AIPD, mandat…).
- Différence avec le Togo signalée : la notion `caracteristiques_autorisation` est « propre à une autre juridiction » et n'est pas servie ici ; elle reste dans le socle.
- Certains champs cités relèvent d'une autre juridiction ou n'apparaissent pas dans C12 (t.caracteristiques_article_8, t.mission_regalienne, t.registre_information_public, t.correspondant_designe).
- Statut : validé par AMELEGAL le 6 septembre 2026.

**Utile pour :** contrôle de couverture des bulles, aide contextuelle des formulaires.

## D02 - Contenu rédigé des bulles d_information.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/D02 - Contenu rédigé des bulles d_information.docx`

**En une phrase :** texte complet de chaque bulle d'aide (définition, exemples, contre-exemple, référence, conséquence) pour le Bénin.

**Contenu :**
- Règle de rédaction : définition de 2 ou 3 phrases, 1 ou 2 exemples, contre-exemple, référence citée, conséquence sur la qualification, réserve commune (« Cette aide est générale… ne se substitue pas à l'analyse d'un juriste ») ; aucun conseil personnalisé.
- Contenu en 11 domaines : objet du traitement, licéité, nature des données, qualité de l'organisme, correspondant, formalités, conservation et sécurité, transferts, AIPD, violations, cadre de l'intervention (mandat).
- Précisions béninoises : données génétiques non retenues comme cas distinct (rattachées à l'art. 394) ; biométrie, interconnexion, NNI, recherche/intérêt public et transfert → autorisation (art. 407) ; données sensibles → autorisation.
- « Registre destiné à l'information du public » : le droit béninois ne retient pas ce cas de dispense (notion non servie), alors que D01 la classe parmi les notions déterminantes servies.
- Norme simplifiée : l'APDP n'a publié aucune norme à ce jour, la déclaration ordinaire reste due ; exemption : pas de droit acquis, fermée aux autorités publiques.
- APDP présentée comme successeur de la Commission nationale de l'informatique et des libertés (art. 464). Instruction : 60 j + 30, doublée si investigation ; le silence vaut acceptation (statut Acceptation tacite), en notant qu'ailleurs le silence peut n'avoir aucun effet.
- Violations : 72 h dès la prise de connaissance (standard international), formulaire APDP ; seuil AIPD de 10 000 personnes issu des standards internationaux.
- Mandat : exprès, révocable sans préavis, sans effet sur la qualification ; le plus restrictif du rôle et du niveau de mandat l'emporte.
- 7 notions avec fiche développée : donnée personnelle, base juridique, données sensibles, correspondant, transfert international, AIPD, violation.

**Utile pour :** contenu de `bulles-information.json`, aide contextuelle, glossaire.

## D03 - Fiches d_explication développées.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/D03 - Fiches d_explication développées.docx`

**En une phrase :** cadrage des fiches d'explication longues, ouvertes depuis les bulles.

**Contenu :**
- 7 notions concernées : donnee_a_caractere_personnel, base_juridique, donnees_sensibles, correspondant, transfert_international, aipd, violation_donnees (déterminantes ou structurantes).
- Plan type : explication en 3 à 5 paragraphes, exemples sectoriels (F02), cas limites, texte cité, effet sur la qualification avec renvoi au logigramme, réserve.
- Statut : « Cadré, rédaction à venir » ; les fiches ne sont pas encore rédigées et ne conditionnent pas la publication. Criticité : Recommandé.

**Utile pour :** aide contextuelle approfondie (panneau ouvert depuis une bulle).

## D04 - Glossaire consolidé.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/D04 - Glossaire consolidé.docx`

**En une phrase :** glossaire alphabétique des 60 notions servies au Bénin, généré à partir des bulles.

**Contenu :**
- Une ligne par terme avec définition (identique à la bulle D02) et référence légale quand il y en a une (ex. Analyse d'impact art. 428/429 ; Autorité de contrôle art. 464 ; Instruction art. 412 et 490 ; Récépissé art. 405 et 412).
- Accessible depuis la recherche transverse, exportable, jamais rédigé séparément des bulles.
- Inclut « Registre destiné exclusivement à l'information du public », sans référence.
- Phase 10 ; statut à valider par la gérance.

**Utile pour :** écran Glossaire, recherche transverse, export.

## E01 - Fiche de registre.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/E01 - Fiche de registre.docx`

**En une phrase :** gabarit imprimable d'une fiche de registre béninoise.

**Contenu :**
- Reprend l'ordre des 12 sections du modèle APDP, plus les mentions Waɖɛ ; une fiche par page à l'identité Waɖɛ.
- En-tête : référence normalisée de la fiche, référence et validité de la décision de l'autorité, juridiction et texte appliqué, date et auteur, mention du cabinet si la fiche est produite sous mandat.
- Corps : 34 rubriques numérotées qui reprennent les lignes de correspondance de C12 ; l'extraction rend des libellés tronqués (« 2 », « 4 », « 3 (Statut) »…).
- Pied : régime, motifs et juridiction ; besoin d'AIPD et son fondement ; réserve de l'art. 12 du CDC ; signature du correspondant ; visa du responsable.

**Utile pour :** génération PDF de la fiche de registre.

## E02 - Registre complet.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/E02 - Registre complet.docx`

**En une phrase :** spécification des exports du registre complet.

**Contenu :**
- Formats : PDF (une fiche par page, gabarit E01), CSV et XLSX (une ligne par traitement), export structuré complet pour la réversibilité (art. 41 du CDC).
- 39 colonnes ordonnées de t.reference à t.validite_decision ; tableaux imbriqués (accès, communications, transferts, sous-traitants, droits) de préférence dans un onglet séparé lié par la référence.
- Champs export_registre=non exclus (ex. origine dans la cartographie AMELEGAL).
- Pied : date, auteur, cabinet si mandat, juridiction et version du référentiel ; chaque export est consigné au journal de conformité.

**Utile pour :** module d'export du registre.

## E03 - Dossiers de formalité.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/E03 - Dossiers de formalité.docx`

**En une phrase :** pièces attendues par régime et règles de constitution du dossier de formalité.

**Contenu :**
- Aucune pièce déposée pour hors champ, domestique, dispense et exemption.
- Décret : formulaire unique et pièces, avis motivé. Autorisation : rapport d'AIPD, formulaire unique et annexes 1 à 4, extrait de délibération. Simplifiée : référence de la norme. Déclaration : formulaire unique et liste des pièces, récépissé.
- Annexes déclenchées par champ (mêmes 4 annexes que C07).
- Pré-remplissage champ par champ via registre-champs.csv ; un champ sans correspondance donne lieu à un choix consigné.
- Le dossier ne peut pas passer à « Prêt à être transmis » tant qu'il manque une pièce ou un champ obligatoire ; la liste des manques est affichée.

**Utile pour :** module des formalités (constitution, pré-remplissage, contrôle de complétude).

## E04 - Rapport d_analyse d_impact.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/E04 - Rapport d_analyse d_impact.docx`

**En une phrase :** structure et mentions du rapport d'AIPD généré.

**Contenu :**
- 4 sections identiques à la grille de C08.
- Mentions : références du traitement et de la fiche, juridiction et version, critères de déclenchement et leur source, score et mode de calcul, risque résiduel et conclusion, avis signé du délégué, validation horodatée, réserve de l'art. 12.
- Reprend sans retrait les rubriques du modèle d'AIPD de l'APDP.
- Si le risque résiduel reste élevé : rapport joint à la consultation préalable, suivie comme une formalité distincte.

**Utile pour :** génération du rapport d'AIPD.

## E05 - Notifications de violation.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/E05 - Notifications de violation.docx`

**En une phrase :** modèles de notification à l'APDP et de communication aux personnes concernées.

**Contenu :**
- Deux modèles pré-remplis depuis la fiche d'incident.
- Notification à l'autorité : identités, dates et heures de survenance et de découverte, nature de la violation (fuite, perte, vol, accès non autorisé, altération, indisponibilité), personnes et données concernées (catégories, nombre approximatif), traitements et juridictions, conséquences, mesures, décision d'informer et son motif, pièces jointes.
- Communication aux personnes : nature en termes clairs, point de contact, conséquences, mesures et recommandations.
- Paramètres : 72 h à compter de la prise de connaissance, destinataire APDP, source standard_international ; formulaire de signalement APDP.

**Utile pour :** module incidents (génération des notifications).

## E06 - Rapport d_activité de cabinet.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/E06 - Rapport d_activité de cabinet.docx`

**En une phrase :** contenu du rapport d'activité d'un cabinet mandaté, par client et consolidé.

**Contenu :**
- Rapport par client (PDF et tableur) : en-tête du mandat, interventions, fiches traitées, qualifications et écarts, formalités, AIPD, incidents (respect du délai), sensibilisation (lot 2), réactivité, indice de conformité et échéances à la clôture, pied de page.
- Rapport consolidé interne : charge par consultant, échéances tous clients, clients sans intervention récente, mandats à échéance, suspendus ou expirés, décompte des mandats actifs servant à la facturation ; le dossier propre du cabinet est exclu.
- Règles : seule l'activité du cabinet, produit aussi après la fin du mandat (historique sans accès au contenu), consigné au journal, aucune donnée d'un autre client.
- Document non spécifique au Bénin (sources : CDC, référentiel, registre-champs.csv, bulles-information.json, alertes.json).

**Utile pour :** espace cabinet, gestion des mandats, facturation.

## F02 - Modèles sectoriels de traitement.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/F02 - Modèles sectoriels de traitement.docx`

**En une phrase :** modèles de fiches pré-remplies par secteur, à livrer au lot 1.

**Contenu :**
- Source : registre type béninois AMELEGAL de 139 fiches.
- 8 modèles : paie, clients et prospects, vidéosurveillance, contrôle d'accès (tous secteurs) ; dossier médical (santé) ; dossier scolaire (éducation) ; bénéficiaires (ONG et bailleurs) ; connaissance du client (finance inclusive et paiement), avec les champs pré-remplis et ceux laissés vides.
- Règles : un modèle ne pré-remplit jamais un champ déterminant ; il est rattaché à une ou plusieurs juridictions (alerte si utilisé hors de celles-ci) ; durées de conservation indicatives ; la fiche créée est un Brouillon.
- Criticité : Recommandé.

**Utile pour :** bibliothèque de modèles à la création d'une fiche.

## F03 - Grille d_analyse d_impact détaillée.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/F03 - Grille d_analyse d_impact détaillée.docx`

**En une phrase :** questionnaire détaillé de l'AIPD et méthode de calcul du score.

**Contenu :**
- 4 sections, chacune avec son état d'avancement ; un contributeur métier peut être invité sur une section.
- 20 questions numérotées de 1.1 à 4.4 : reprises automatiques (1.1 à 1.3), questions texte, questions oui/non/partiellement (2.4, 2.5, poids 2), gravité et vraisemblance pour accès non autorisé, modification et disparition (3.1 à 3.6, poids 4), réversibilité (3.7, poids 3), risque résiduel faible/modéré/élevé (4.3, poids 5).
- Score : somme pondérée des sections 2 et 3 ramenée sur 100 ; risque = gravité × vraisemblance (de 1 à 4 chacune) ; on retient le plus élevé des 3 événements, corrigé par la section 2. Niveaux : 0-33 faible, 34-66 modéré, 67-100 élevé.
- Déclenchement : les 6 critères de C08 ; un risque résiduel élevé crée une consultation préalable avec compte à rebours.
- Questions, poids et seuils administrables par juridiction.

**Utile pour :** formulaire AIPD et calcul du score de risque.

## I01 - Jeu de cas de recette du moteur.docx
*Chemin :* `02 Bénin/01 Livrables Bénin/I01 - Jeu de cas de recette du moteur.docx`

**En une phrase :** cas de test du moteur béninois (version lisible du CSV).

**Contenu :**
- 12 cas (CAS-BJ-01 à 12), un par chemin, couvrant les 8 sorties : 01 domestique, 02 dispense, 03 décret, 04 et 08 autorisation, 05 et 09 simplifiée, 06 et 10 exemption, 07 et 11 déclaration, 12 hors champ.
- Cas d'opposition : rôle Correspondant sans désignation → droit commun ; mandat de cabinet sans désignation → aucune dispense ; même traitement qualifié dans les deux juridictions → deux régimes côte à côte, sans primauté ; qualification ancienne restant explicable ; mêmes résultats en qualification continue et en assistant.
- Cas propres au Bénin : décision automatisée excluant d'un droit → autorisation et non déclaration ; autorité publique avec délégué → jamais Exemption ; délai expiré sans réponse → « Acceptation tacite », distinct de « Acceptée ».
- Incohérence : CAS-BJ-06 attend BJ-EXEMPTION avec BJ-Q4=oui (personne publique), ce que la condition bloquante de Q8 interdit.

**Utile pour :** tests automatisés et recette du moteur de qualification.

## cas-de-recette-benin.csv
*Chemin :* `02 Bénin/01 Livrables Bénin/_spécifications développeur/cas-de-recette-benin.csv`

**En une phrase :** jeu de recette exécutable du moteur béninois (même contenu que I01).

**Contenu :**
- UTF-8 avec BOM, séparateur « ; », 12 lignes plus l'en-tête.
- Colonnes : cas, reponses, BJ-Q1 à BJ-Q8 (oui/non/vide), regime_attendu, libelle_attendu, fondement, motif_attendu, aipd_attendue.
- aipd_attendue vaut « oui » pour CAS-BJ-03 (décret), 04 et 08 (autorisation), « selon critères » pour les 9 autres.
- Les motifs attendus reprennent mot pour mot ceux de C06/JSON ; certains contiennent un « ; » entre guillemets (cas 06 et 10), donc il faut un vrai parseur CSV.
- Même incohérence que I01 sur CAS-BJ-06 (Q4=oui → exemption).

**Utile pour :** tests automatisés du moteur (mode simulation avant publication).

## referentiel-benin.json
*Chemin :* `02 Bénin/01 Livrables Bénin/_spécifications développeur/referentiel-benin.json`

**En une phrase :** référentiel machine du Bénin, qui reprend sous forme exploitable tous les livrables C01 à C13.

**Contenu :**
- meta : version 1.0, 2026-09-06, AMELEGAL SARL, « validé, à implémenter » ; aucune valeur ne doit être codée en dur (CDC art. 8.1 et 27.6).
- juridiction (BJ, CEDEAO, herite_du_socle) ; sources : loi adoptée le 2017-06-13, publication null, avec une réserve : seule la version adoptée par l'Assemblée est au dossier, la version promulguée et sa référence au JO restent à obtenir avant publication ; 17 articles clés ; 5 documents de doctrine.
- autorite : APDP, coordonnées null, 3 canaux de dépôt, délais (60 j + 30, doublé, 8 sem + 6), silence_vaut_acceptation actif, validité 2 ans, 6 issues de dossier.
- terminologie ; regimes (8 objets : id, code, libellé, famille_couleur, ordre, fondement, est_un_regime_de_formalite false pour HORS-CHAMP et DOMESTIQUE).
- logigramme : 8 questions avec champ, type, aide, branches oui/non et motifs ; options de Q3 (6 dispenses), Q5 (5 objets), Q6 (10 caractéristiques : données sensibles, condamnations, biométrie, NNI, appréciations sur difficultés sociales, interconnexion, transfert État tiers, intérêt public/statistique/scientifique, décision automatisée excluante, catégorie à risque désignée par l'APDP) ; condition_bloquante sur Q8 ; 5 règles transverses ; ecart_texte_pratique.
- feuilles_de_route (8 régimes), annexes_formulaire (4), aipd (6 critères, seuil 10 000, présomption AUTORISATION et DECRET, grille, niveaux), violations (72 h, arbre V1/V2, rappels 0,25/0,5/0,75/0,9), correspondant (désignation non obligatoire), transferts (pays_reconnus vide, formalité BJ-AUTORISATION), indice (poids 0,35/0,35/0,2/0,1, 4 seuils, sensibilisation inactive).
- Les champs du logigramme sont nommés en bloc1/2/3.* (ex. bloc1.personne_publique_ou_mission_service_public, bloc3.communication_tiers), alors que le registre C12 utilise org.* et t.* ; la correspondance n'est pas donnée.

**Utile pour :** chargement direct dans le moteur de qualification et le back-office du référentiel.

# Partie 5 — Bénin : sources et référentiels (`02 Bénin/00 Sources et référentiels/`)

34 fichiers, 30 blocs (l'étude AMELEGAL en 3 versions et le registre type en pdf/xlsx sont regroupés). Ordre alphabétique des chemins, sans tenir compte de la casse ni des accents.

---

## Décisions et doctrine de l'autorité

## Decision-2019-N°020.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/Decision-2019-N°020.pdf`

**En une phrase :** décision de l'APDP n° 020/APDP/Pt/SG/DAFL/SA du 12 août 2019 qui fixe les frais du macaron de signalisation des systèmes de vidéosurveillance.

**Contenu :**
- PDF scanné de 2 pages, sans couche texte (lu à l'image). Signée par le président Étienne Marie FIFATIN, session du 7 mars 2019.
- Art. 1 : l'APDP fait payer l'acquisition d'un macaron qui signale une activité de vidéosurveillance.
- Art. 2 : 15 000 FCFA par activité pour les entreprises à usage commercial, 5 000 FCFA pour les particuliers. Le macaron est remis après paiement et étude du dossier.
- Art. 3 : les mêmes frais sont dus au renouvellement de la demande de traitement.
- Art. 4 : les structures publiques sont exemptées.
- Art. 5 : paiement en espèces sur le compte Trésor BJ66 01 001 000001 0426 94, ou par chèque certifié au Secrétariat général de l'APDP, contre quittance.
- Art. 6 : la décision abroge les dispositions antérieures contraires.

**Utile pour :** le module vidéosurveillance (coûts de signalisation affichés au responsable de traitement).

## decision_n_2022-0007.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/decision_n_2022-0007.pdf`

**En une phrase :** décision n° 2022-0007/APDP/Pt/SA du 24 février 2022 (président Yvon DETCHENOU) qui crée les pictogrammes, étiquettes et affiches des dispositifs de capture d'images et en fixe les prix.

**Contenu :**
- PDF scanné de 7 pages : 4 pages de décision et 3 bons de commande en annexe.
- Formats : pictogrammes ronds ou carrés de 10, 15 et 20 cm ; étiquettes de 3x3 ou 5x5 cm ; affiches rectangulaires portant le logo et le sceau ou tampon de l'APDP.
- Le pictogramme porte un QR code et le numéro de la décision. Il est renouvelé si le traitement change ou si le récépissé ou l'autorisation expire. Chaque dispositif utilisé hors du cadre domestique reçoit une étiquette à QR code.
- L'affiche doit indiquer : QR code ou numéro de délibération, données traitées, finalité, opérations, durée de conservation, nom du responsable de traitement, sous-traitants avec leurs références, partenaires en cas de transfert, modalités d'exercice des droits.
- Prix des pictogrammes (FCFA) : 10 cm de 10 000 (vinyle) à 50 000 (aluminium) ; 15 cm de 15 000 à 60 000 ; 20 cm de 18 500 à 70 000.
- Prix des étiquettes : vinyle 5x7 avec QR code 2 500 ; scellé plastique numéroté 15 000 ; plaque aluminium 5x5 15 000. Marquage d'affiches : gravure 30 000, scellés 15 000, tampon industriel 20 000. TVA de 18 % sur les bons de commande.
- Paiement sur le compte BJ660 01001 000001043824 74 au Trésor. Commande par formulaire avec la quittance. Remise à partir de la délivrance du récépissé ou de l'autorisation.

**Utile pour :** le module vidéosurveillance (check-list de signalisation, contenu obligatoire de l'affiche, estimation des coûts).

## Décision-n°2024-008-nouveau-1.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/Décision-n°2024-008-nouveau-1.pdf`

**En une phrase :** décision n° 2024-008/APDP/Pt/AP/CA/CTJ/SA du 13 juin 2024 (président Luciano HOUNKPONOU) qui crée la certification des compétences de délégué à la protection des données (DPD).

**Contenu :**
- PDF scanné de 3 pages. Elle vise la session plénière de régulation du 29 mai 2024.
- Art. 1 : certification réservée aux personnes physiques et aux personnes morales de droit privé qui veulent exercer comme DPD sous contrat de service (art. 430). L'APDP est seule compétente pour la délivrer.
- Art. 2 : en plus de l'art. 430 al. 5, le candidat doit maîtriser le droit du numérique. Pièces à fournir : Master en droit, diplôme ou attestation de formation en protection des données (un formateur « APDP approuvé » est un atout), pièce d'identité, casier judiciaire de moins de 3 mois, CV, quittance de 25 000 FCFA de frais d'étude.
- Art. 3 : examen QCM en présentiel sur une application web. Il faut au moins 70 % de bonnes réponses.
- Art. 4 : délivrance contre 250 000 FCFA.
- Art. 5 et 6 : validité de 2 ans, renouvellement aux mêmes conditions.
- L'art. 2 a été modifié en 2025 par la décision 2025-004 (voir `certification_c2.pdf`).

**Utile pour :** le module DPO (vérifier les qualifications d'un DPO externe, échéance de la certification).

## Décision-n°2024-009.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/Décision-n°2024-009.pdf`

**En une phrase :** décision n° 2024-009/APDP/Pt/AP/CA/CTJ/SA du 25 juin 2024 qui révise le prix de la labellisation des formateurs et des formations en protection des données.

**Contenu :**
- PDF scanné de 2 pages.
- Elle révise la délibération 2023-002/APDP/Pt/SA du 31 mars 2023, qui avait fixé le prix à 5 000 000 FCFA d'après le rapport 2024.
- Nouveau prix : 3 000 000 FCFA, label valable 2 ans.
- Paiement annuel en une seule fois au Trésor (DGTCP) : 1 000 000 pour le Trésor public et 2 000 000 pour l'APDP, destinés aux missions d'investigation et de contrôle sur site.
- Entrée en vigueur à la signature, publication au Journal officiel.

**Utile pour :** le référentiel des coûts et des acteurs agréés (formateurs « APDP approuvé », pièce n° 8 du dossier de formalités).

## rapport_activite_2022.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/rapport_activite_2022.pdf`

**En une phrase :** rapport annuel 2022 de l'APDP (président Yvon DETCHENOU, 3e mandature), prévu par l'art. 481.

**Contenu :**
- 100 pages en trois parties : activités (régulation, contrôle, contentieux, sensibilisation), fonctionnement (réformes, SI, finances), perspectives (identification et authentification, gouvernance des données, limites du Livre V, IA et big data).
- Plénière : 34 sessions en 2022 (24 ordinaires, 3 extraordinaires, 7 contentieuses). Exemples de dossiers rejetés, reportés ou ajournés : ANPE, NAUTILUS, MTN MoMo, FEDAPAY, SGB…
- Rapports annuels (art. 387) : 197 mises en demeure ont été envoyées et 56 rapports reçus. Les 77 communes et les 12 départements ont été formés et 44 DPO désignés par les préfectures et mairies.
- Procédure contentieuse : interpellation ou mise en demeure, rapport d'instruction (art. 457), 15 jours pour présenter des observations, audience devant la plénière contentieuse, décision. Les amendes se paient sous un mois. Un recours a été porté devant la chambre administrative de la Cour suprême.
- Procédure de désignation du DPO : notification à l'APDP (type interne ou externe, identité, CV), lettre d'engagement, organigramme, preuve de publication de la nomination, durée du mandat.
- Liste de 15 outils de conformité publiés : guide vidéosurveillance, modèle d'AIPD, formulaire de signalement, registres types vidéosurveillance et gestion du personnel, guide du rapport annuel, check-list de remplissage, cartographie pour préfectures et mairies…
- Critiques du texte : l'avertissement et la mise en demeure (art. 452) ne sont pas des sanctions ; les recours devraient aller à la chambre administrative de la Cour suprême ; l'APDP ne peut pas saisir le juge pénal ; le doublement des délais par l'art. 490 est jugé inutile ; les normes simplifiées (art. 406) ne sont pas effectives. L'APDP reconnaît aussi que les responsables déclarent systématiquement alors que le registre (art. 405) ou le DPO (art. 408) devraient les en dispenser.
- Budget : subvention de 488 277 000 FCFA, dont 408 492 538 exécutés.

**Utile pour :** la doctrine du moteur de qualification (écart entre le texte et la pratique sur la déclaration), le module DPO et le module rapport annuel.

## Rapport_Annuel_Activites_2023.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/Rapport_Annuel_Activites_2023.pdf`

**En une phrase :** rapport annuel 2023 de l'APDP. Il expose la doctrine de partage entre les régimes et les chiffres de régulation et de sanction.

**Contenu :**
- 85 pages. Composition : la loi 2020-35 a ramené l'APDP de 11 à 8 conseillers (art. 464 nouveau).
- Doctrine de la déclaration (art. 405) : données simples sans interconnexion ni transfert, récépissé avec interdiction d'étendre le traitement. Le NPI et l'IFU, identifiants nationaux uniques, font passer en autorisation (art. 407, 2°). Le numéro de pièce d'identité ou de passeport ne le fait pas, sauf si la copie de la pièce porte le NPI.
- Doctrine de l'autorisation : données sensibles, biométrie, NPI/IFU, difficultés sociales, intérêt public et recherche, journalisme, exclusion d'un droit, interconnexion, transfert hors CEDEAO. S'y ajoutent la vidéosurveillance avec accès à distance par internet ou smartphone et le site ou l'application hébergé dans un cloud hors CEDEAO.
- Demande d'avis (art. 411) pour les traitements publics sur cinq objets. L'avis est publié.
- Plaintes : 15 réclamations et plaintes (sextorsion, piratage, usurpation…). Les faits pénaux sont transmis au procureur de la CRIET, la cybercriminalité est renvoyée aux juridictions.
- 139 responsables de traitement saisis d'office (rapport annuel non remis, injonctions non respectées, formalités non accomplies). 15 dossiers contentieux, dont 14 jugés : avertissements ou amendes de 1 à 22 millions FCFA. 4 visites de contrôle. 39 sessions (22 ordinaires, 11 contentieuses, 5 extraordinaires, 1 de régulation). 8 décisions de vidéosurveillance avec pictogrammes.
- Pénalités à recouvrer : 181,5 M FCFA attendus, 83,7 M encaissés (MTN Spacetel 117 M, Orabank 25 M, Moov Africa 22,5 M, Capago 10 M, Nautilus 3 M…). Budget de 711 412 157 FCFA, consommé à 63,8 %. Pictogrammes : 6 517 500 FCFA de recettes.
- 3e formation des DPO du 18 au 20 décembre 2023, une centaine de participants. Perspectives : audit de sécurité, PSSIE, hygiène numérique, serveurs web open source, saisine du juge pénal.

**Utile pour :** les règles du moteur de qualification (déclencheurs d'autorisation propres à l'APDP : NPI, accès distant, cloud hors CEDEAO) et la mesure du risque de sanction.

## Rapport_annuel_activite_2024.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Décisions et doctrine de l_autorité/Rapport_annuel_activite_2024.pdf`

**En une phrase :** rapport annuel 2024 de l'APDP, sous la nouvelle présidence de Luciano HOUNKPONOU.

**Contenu :**
- 100 pages. Cinq nouveaux conseillers nommés par le décret 2024-740 du 31 janvier 2024, serment le 12 mars 2024. Bureau à deux membres (Président et Rapporteur, ce dernier au pouvoir précisé par le règlement intérieur du 29 mai 2024). Nouveau logo le 21 août 2024.
- Textes de 2024 : décision 2024-008 (certification DPD, reproduite en entier), modification de la labellisation (3e cycle), prix du label ramené de 5 M à 3 M FCFA. Un certificat de conformité a été créé le 8 avril 2024 : valable 2 ans, délivré après exécution des injonctions, 5 délivrés.
- Régulation : 560 dossiers soumis (412 en 2023), 476 validés (357 autorisations et 119 déclarations), 9 rejets, 27 radiations, 48 reports pour information insuffisante ou sécurité inadéquate. Le modèle d'extrait de délibération a été simplifié.
- Contrôles sur site : 52 structures (cliniques, pharmacies, mairies, hôtels). Constat : la plupart violent le code. 13 dossiers contentieux, amendes de 1 à 7,2 millions FCFA. Pénalités versées au Trésor : 196 850 000 FCFA.
- Budget de 773 431 628 FCFA (subvention 488 277 000, pictogrammes 23 868 000, formations 16 000 000). Tableau des subventions de 2015 à 2024. Effectif passé de 27 à 32 agents.
- Partie enjeux : IA et vie privée ; vidéosurveillance et vidéoprotection (régimes déclaration ou autorisation, obligations, dérives) ; obligations de sécurité des SI. Besoins : outils de cybersécurité et d'investigation, tests d'intrusion.

**Utile pour :** les tableaux de bord et la mesure du risque (volumes, taux de validation, motifs de report), le certificat de conformité et le module vidéosurveillance.

---

## Étude AMELEGAL et formation

## 2--FORMATION-DPO-2025-bn.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Etude Amelegal et formation/2--FORMATION-DPO-2025-bn.pdf`

**En une phrase :** diaporama de l'APDP (Delphin TAMADAHO, CTJ/APDP, Golden Tulip, 22 décembre 2025), module III de la formation des DPO : le DPO et la mise en place du registre.

**Contenu :**
- 27 diapositives, peu de texte (environ 1 000 mots). Aucune cartographie n'est jointe, seule la diapositive qui l'annonce figure.
- Bases citées : art. 430 al. 5 (profil du DPO) et art. 432, 2° (missions de contrôle). La cartographie, la classification et le registre font partie des missions du DPO.
- Cartographie des compétences : recenser les textes encadrant l'activité (lois, arrêtés, notes de service), maîtriser le Livre V, suivre le site de l'APDP. Cartographie des traitements : inventaire de toutes les opérations. L'APDP fournit une cartographie indicative à adapter.
- Politique de classification selon trois objectifs (confidentialité, intégrité, disponibilité) et trois niveaux d'impact (faible, modéré, élevé), avec une définition des effets limités, sérieux, sévères ou catastrophiques.
- Registre : reprise des 7 mentions de l'art. 435 pour le responsable de traitement et des 4 mentions pour le sous-traitant, remise à l'APDP sur demande, exemption PME sauf risque, traitement non occasionnel ou données sensibles ou pénales.
- Contacts : n° vert 150, +229 01 69 55 00 00, contact@apdp.bj.

**Utile pour :** le module registre et cartographie (niveaux de classification C/I/D) et l'aide contextuelle destinée au DPO.

## Pratique de la protection des données personnelles au Bénin : 3 versions (BON.docx, version finale.docx, version finale.pdf)
*Chemins :* `02 Bénin/00 Sources et référentiels/Etude Amelegal et formation/Pratique de la protection des données personnelles au Bénin BON.docx` ; `…/Pratique de la protection des données personnelles au Bénin (version finale).docx` ; `…/Pratique de la protection des données personnelles au Bénin (version finale).pdf`

**En une phrase :** étude pédagogique d'AMELEGAL SARL (2026, environ 76 pages, avec E. SIGNAN, Y. J. KOUMAKO et D. G. ALI) qui explique le Livre V et la pratique de l'APDP en suivant le parcours d'un responsable de traitement.

**Contenu :**
- Plan en 11 chapitres : vocabulaire, champ d'application, principes et cinq bases légales (art. 389), régimes particuliers, formalités préalables, obligations, droits, APDP, sanctions, cas de la vidéosurveillance, cas pratique de synthèse « AGBADO SANTÉ SA » (3 cliniques : dossier patient, biométrie, 18 caméras, cloud en France, recherche au Ghana, prospection).
- Cadre : loi 2009-09, puis code 2017-20 (7 livres, 647 articles, Livre V aux art. 379 à 490), loi 2020-35 sur la composition. Le PDF du code le plus diffusé en ligne n'est pas consolidé. Engagements internationaux : Acte additionnel CEDEAO de 2010, Malabo (loi 2024-05, dépôt le 26 novembre 2024), Budapest (20 juin 2024). L'APDP est observatrice de la Convention 108 depuis le 10 septembre 2021, le Bénin n'y est pas partie.
- Deux clefs de lecture : le régime est cumulatif (on accomplit les formalités et on documente la conformité) et le droit est appliqué. Chiffres 2024 et 2025 : 64 contrôles, 20 plaintes, 290 dossiers, 75 certificats, 14 contentieux en 2025.
- Formalités : tableau des 8 cas d'autorisation (art. 407) ; dispenses de l'art. 410 (la dispense ne vaut que pour la formalité) ; exemption de l'art. 408 fermée aux autorités publiques ; art. 411 à double condition, organique et matérielle ; 12 mentions de l'art. 409 ; annexes 1 à 4 ; délai de 60 jours plus 30, silence valant accord, mais le délai court à partir du dossier complet. Issues possibles : récépissé, extrait de délibération, rejet, radiation, report. Décisions valables 2 ans.
- Tarifs de l'APDP : macarons 15 000 et 5 000, pictogrammes de 10 000 à 70 000, certification DPD 25 000 puis 250 000, label à 3 M, TVA de 18 %. Pratique répressive : Orabank 25 M, UBA 3 M, JENY SAS 100 000 FCFA. La sanction naît du défaut de réponse à la mise en demeure de 8 jours.
- **Différences entre les versions :** le PDF « version finale » (export Word du 25 août 2026) reprend mot pour mot le texte du **BON.docx**, avec ses coquilles (« Une bémol la toutefois », « lointaine », « n'exclue ») et la citation « AMELEGAL SARL, … données à caractère personnel ». Ses tableaux sont des images. Le **docx « version finale »** est la version la plus aboutie : coquilles corrigées, citation abrégée (« AMELEGAL, Pratique de la protection des données personnelles au Bénin »), tableaux 1 (8 cas de l'art. 407) et 7 (3 cas d'AIPD de l'art. 428) en vrais tableaux de texte au lieu des repères « [TABLEAU n] », note Schrems remise en une seule note, 14 images contre 16 dans le BON. Le contenu de fond est le même dans les trois versions. Certaines légendes d'images restent visibles dans le docx final, par exemple « [CADRE INTERNATIONALE] » et « [LES CINQUE BASES LEGALES] ».

**Utile pour :** la conception du moteur de qualification et des contenus d'aide de Waɖɛ pour le Bénin (le docx final est la version de référence).

---

## Formalités préalables

## Decisiometre_Benin_A4_2pages.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formalités préalables/Decisiometre_Benin_A4_2pages.pdf`

**En une phrase :** logigramme AMELEGAL (2026) en 8 questions et 8 sorties qui fixe le régime de formalité préalable au Bénin (art. 405 à 411).

**Contenu :**
- Règle : on répond aux questions dans l'ordre et la première sortie atteinte fixe le régime.
- Q1, données personnelles ? Si non, sortie 1 : hors champ (art. 1, 380, 381). Q2, usage strictement personnel ou domestique ? Si oui, sortie 2 : exclusion domestique (art. 382, 410-1°).
- Q3, dispense de l'art. 410 (registre privé, comptabilité, paie, fournisseurs, membres d'un organisme sans but lucratif, archivage à long terme) ? Si oui, sortie 3 : dispense de la seule formalité.
- Q4, condition organique (État, établissement public, collectivité, gestionnaire de service public) ? Si non, renvoi à Q6. Q5, l'un des cinq objets de l'art. 411 ? Si oui, sortie 4 : décret en Conseil des ministres après avis motivé publié.
- Q6, données sensibles ou l'une des caractéristiques de l'art. 407 (sensibles, pénales, biométrie, NNI, difficultés sociales, interconnexion, transfert, intérêt public ou recherche, décision automatisée excluant d'un droit, catégorie désignée par l'APDP) ? Si oui, sortie 5 : autorisation, avec décision unique possible et engagement de conformité.
- Q7, norme simplifiée (art. 406) ? Sortie 6 : déclaration simplifiée. Q8, exemption par décision de l'APDP ou par désignation d'un DPO (art. 408, fermée aux autorités publiques) ? Sortie 7 : exemption. Sinon, sortie 8 : déclaration préalable avec récépissé (art. 405, 409, 412, 413).
- En amont, quelle que soit la sortie : AIPD si risque élevé (art. 428) ; consultation si le risque résiduel reste élevé (art. 429, 8 semaines plus 6) ; consultation en cas de doute (art. 407 al. 2) ; nouvelle déclaration à toute modification ; décisions valables 2 ans.
- Avertissement : les sorties 6 et 7 sont peu appliquées, il faut déclarer tant que l'APDP n'a publié ni norme ni décision d'exemption (rapport 2022).

**Utile pour :** le moteur `qualifier()` pour le Bénin (ordre des questions, clés de régime, drapeaux) et le parcours de formalités.

---

## Formulaires et modèles de l'autorité

## Analyse-dmpact-relative-a-la-protection-des-donnees.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Analyse-dmpact-relative-a-la-protection-des-donnees.pdf`

**En une phrase :** modèle d'AIPD de l'APDP (édition de septembre 2021, 27 pages, inspiré de la méthode PIA de la CNIL).

**Contenu :**
- I. Contexte : traitement, finalités, responsables, sous-traitants, mesures de sécurité, données (simples, sensibles), origine, durées, processus, supports et lieux de stockage.
- II. Principes : licéité (6 critères de l'art. 383), minimisation, qualité, durées par type (données courantes, archivées, traces, logs). Le document renvoie aux dispenses d'information (art. 417) et d'accès (art. 395).
- Mesures sur les droits : information, consentement (granularité, consentement parental sous 16 ans, réaffirmation), accès et portabilité, rectification, effacement et oubli, opposition (paramètres vie privée, contrôle parental, traceurs), sous-traitance, transferts.
- III. Sécurité : 8 mesures sur les données (chiffrement, anonymisation, cloisonnement, accès logiques, journalisation, intégrité, archivage, papier), 12 mesures générales et 8 mesures organisationnelles. Chacune est cotée « acceptable » ou « améliorable ».
- Risques : accès illégitime, modification non désirée, disparition. Gravité = facilité d'identification + dommages ; vraisemblance = vulnérabilité des supports + capacités des sources de risque.
- IV. Validation : synthèse avec légende (non applicable, insatisfaisant, amélioration prévue, satisfaisant), plan d'action (responsable, terme, coût, avancement), avis du DPO, avis des personnes concernées, validation formelle par le responsable de traitement. Un intitulé hérité mentionne encore les transferts « en dehors de l'Union européenne ».

**Utile pour :** le module AIPD (structure des écrans, référentiel des mesures, cotation des risques).

## ANNEXE-1-SOUS-TRAITANCE.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/ANNEXE-1-SOUS-TRAITANCE.pdf`

**En une phrase :** annexe 1 du formulaire unique (art. 407 et 409), à remplir en cas de recours à un sous-traitant.

**Contenu :**
- Tableau des intervenants : dénomination, contacts, représentant, rôle.
- Données accessibles à chaque intervenant et durée de l'accès. Opérations effectuées par le sous-traitant.
- Date du contrat de confidentialité et garanties offertes (responsabilité, sécurité, confidentialité, droits des personnes).
- Questions oui ou non : les intervenants sont-ils informés de la législation (comment) ? le sous-traitant a-t-il fait sa propre mise en conformité auprès de l'APDP (références) ?
- Sécurité du sous-traitant : PSSI communiquée, audits, mesures organisationnelles et physiques. Déclaration sur l'honneur.

**Utile pour :** la fiche sous-traitant et la génération du dossier de formalités.

## ANNEXE-2-COMMUNICATION.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/ANNEXE-2-COMMUNICATION.pdf`

**En une phrase :** annexe 2 du formulaire unique, pour la communication de données à des tiers au Bénin ou dans la CEDEAO.

**Contenu :**
- Deux listes de destinataires (au Bénin, dans un pays de la CEDEAO) : dénomination, contacts, représentant, données communiquées.
- Finalité, et texte légal qui prévoit la communication le cas échéant.
- Fondement : consentement préalable, ou exception (obligation légale, mission d'intérêt public, contrat), à justifier. Méthode de recueil du consentement : écrit, oral, électronique.
- Modalités : clé USB, transmission électronique. Sécurité : protection contre les intrusions, authentification, mesures cryptographiques.
- Information préalable (affichage, mentions écrites, entretien) et preuve.

**Utile pour :** la fiche destinataires du registre et le dossier de formalités.

## ANNEXE-3-INTERCONNEXION.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/ANNEXE-3-INTERCONNEXION.pdf`

**En une phrase :** annexe 3 du formulaire unique, pour l'interconnexion de fichiers ou de traitements, avec une check-list de sécurité pour l'interconnexion à internet.

**Contenu :**
- Jusqu'à trois fichiers ou traitements mis en relation : références APDP et finalité de chacun. Modalités : API, services web.
- Nature de l'automatisation : fusion, transfert d'informations, assemblage, consultation de bases par internet. Services exposés : navigation, DNS, hébergement, VPN, messagerie, visioconférence…
- Données concernées, texte qui prévoit l'interconnexion, raisons, durée.
- Risques : exfiltration, intrusion, usurpation, sites interdits, facteur humain. Architecture : DMZ, pare-feux, rupture protocolaire, cloisonnement, journalisation, interception TLS, poste de rebond.
- Page 3 : check-list de 33 mesures inspirée de l'ANSSI (passerelle internet sécurisée, pare-feux, mandataire web authentifié, journaux centralisés, routage statique, protection contre le déni de service…). L'extraction texte de cette page a perdu les caractères accentués.

**Utile pour :** le dossier de formalités (cas de l'interconnexion) et le référentiel des mesures de sécurité.

## ANNEXE-4-TRANSFERT.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/ANNEXE-4-TRANSFERT.pdf`

**En une phrase :** annexe 4 du formulaire unique, pour la demande d'autorisation de transfert de données à l'étranger.

**Contenu :**
- Fondement et méthode de recueil du consentement au transfert, comme dans l'annexe 2.
- Destinataires et lien avec le responsable de traitement : groupe ou filiale, client, sous-traitant, fournisseur.
- Pays, existence d'une autorité de protection (nom, contacts), niveau de protection de la loi étrangère.
- Données transférées, finalité, base légale ou réglementaire, nombre de personnes, volume du fichier, opérations du destinataire (liste de 25 opérations).
- Mode (électronique ou physique), support (clé USB, mail, service web), contrat de confidentialité et garanties, mise en conformité du destinataire, sécurité organisée par le destinataire.

**Utile pour :** le module transferts (art. 391 et 392) et la génération du dossier.

## certification_c2.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/certification_c2.pdf`

**En une phrase :** décision n° 2025-004/APDP/Pt/AP/CA/CTJ/SA du 31 mars 2025 qui modifie l'art. 2 de la décision 2024-008 sur la certification des DPD.

**Contenu :**
- PDF scanné de 2 pages, sans couche texte. Elle vise la réunion du Bureau du 26 mars 2025.
- Art. 2 nouveau : le candidat doit justifier d'un diplôme universitaire Bac+5 en droit ou en informatique. Le Master en droit n'est plus exigé seul et la condition de « maîtrise du droit du numérique » disparaît.
- Pièces : diplôme Bac+5 en droit ou en informatique reconnu par l'État, attestation de formation en protection des données (formateur labellisé en atout), pièce d'état civil, casier judiciaire de moins de 3 mois, CV, quittance de 25 000 FCFA (compte BJ 660 01001 00000104382474).
- Abroge les décisions antérieures contraires, publication au Journal officiel.

**Utile pour :** le module DPO (critères de qualification à jour).

## Fiche.Pratique.Mise-en-conformite_Pt_OK_Validee.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Fiche.Pratique.Mise-en-conformite_Pt_OK_Validee.pdf`

**En une phrase :** fiche pratique officielle de l'APDP (12 pages) qui résume la mise en conformité au Livre V (loi 2017-20 modifiée par la loi 2020-35).

**Contenu :**
- Définitions : donnée personnelle, traitement, responsable de traitement, sous-traitant (soumis aux mêmes obligations), personne concernée.
- « Les 10 points de la conformité » : 1 inventaire des traitements et registre ; 2 intervenants et prestataires ; 3 mesures de sécurité et PSSI ; 4 formalités auprès de l'APDP (« gratuit mais obligatoire ») ; 5 sensibilisation ; 6 information et consentement ; 7 désignation d'un DPO ; 8 droits et processus de notification des violations ; 9 sécurité permanente (droits d'accès, mots de passe, journaux, sauvegardes, MDM, antivirus, audits) ; 10 rapports périodiques et certificat de conformité.
- Formalités possibles : demande d'avis par lettre au Président, formulaire d'autorisation, formulaire de déclaration (trois types), fiche de plainte ou de signalement.
- Obligations et articles : déclaration (405, 407, sauf 410), principes (383 à 390), information (415), confidentialité et sécurité (425, 426), droits (415, 437, 440, 441), registre (435), rapport annuel (387).
- Droits, chacun avec « en quoi il consiste » et « comment le garantir » : information (415), accès (437), opposition (440), rectification et suppression (441), oubli (443), portabilité (438), interrogation (439), réparation (451).
- Le document s'arrête à l'art. 451. Il n'y a pas de section consacrée aux sanctions, bien que l'introduction en annonce une.

**Utile pour :** le parcours d'accompagnement et la check-list de conformité (les 10 étapes), ainsi que les textes d'aide sur les droits.

## FORMULAIRE-ENGAGEMENT-DE-CONFORMITE.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/FORMULAIRE-ENGAGEMENT-DE-CONFORMITE.pdf`

**En une phrase :** formulaire d'engagement de conformité (6 pages) pour faire évoluer un traitement déjà connu de l'APDP, ou pour le rattacher à une décision unique (art. 407 dernier alinéa).

**Contenu :**
- I. Identification du responsable de traitement (NPI ou RCCM, secteur privé, public ou institution étrangère, représentant légal).
- II. Traitement antérieur : référence APDP, date de mise en œuvre, nature (vidéosurveillance, site ou application, photo ou vidéo).
- III. Traitement envisagé : extension, réduction, modification ou renouvellement. Pour chaque paramètre (données, personnes, opérations, type, conservation, stockage, sous-traitance, communication, interconnexion, transfert), la question « y a-t-il un changement ? » appelle un oui ou un non avec précisions.
- IV. Sécurité : même question pour la sécurité technique, physique, organisationnelle, le facteur humain, les mesures juridiques, la confidentialité, l'intégrité, la disponibilité et la traçabilité.
- Engagement à respecter le cadre fixé antérieurement et le régime béninois. Mentions d'information de l'APDP : réponse en 1 mois aux demandes de rectification, suppression et oubli.

**Utile pour :** le cycle de vie des formalités (renouvellement au bout de 2 ans, modification d'un traitement déjà déclaré).

## Formulaire-complementaire-capture.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Formulaire-complementaire-capture.pdf`

**En une phrase :** formulaire complémentaire (art. 406) pour les traitements par capteurs (image, voix, biométrie), à joindre au formulaire unique.

**Contenu :**
- Données : images et vidéos, empreintes, voix, température corporelle, géolocalisation, métadonnées, écriture manuscrite.
- Finalités possibles : sécurité des personnes ou des biens, abords, trafic routier, bâtiments publics, risques naturels, âge osseux, jeux, rayonnement thermique, gestion d'accès.
- Opérations : IA, reconnaissance faciale, vocale ou d'empreinte, IRM, retouche, segmentation…
- Dispositif : équipements, fabricant, origine ; technologie analogique ou numérique (IR, RX…) ; architecture ; connexions (câble, wifi, internet, LAN, VPN) ; accès en temps réel ou à distance ; terminaux.
- Localisation fixe ou mobile, espace privé ou ouvert au public, nombre de capteurs, volume. Sécurité physique (art. 387, 7°). Nombre d'affiches et de pictogrammes.
- 10 pièces à joindre : caractéristiques techniques, preuve du consentement en cas de transfert, engagements de confidentialité, contrats sous-traitant et hébergeur, PSSI, NPI ou pièce d'identité, RCCM ou IFU, preuve de l'information préalable, plan d'installation et champs de vision.

**Utile pour :** le module vidéosurveillance et biométrie (champs à collecter, déclencheurs d'autorisation comme l'accès distant).

## Formulaire-de-signalement.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Formulaire-de-signalement.pdf`

**En une phrase :** formulaire de l'APDP (4 pages) pour signaler une violation relative à des données personnelles.

**Contenu :**
- Envoi à contact@apdp.bj, rue 6.076 immeuble El Marzouk Joël, 01 BP 04837 Cotonou.
- Identification du déclarant.
- 10 types de violation : traitement non autorisé, changement ou détournement de finalité, prospection irrégulière, transfert sans autorisation, droits non garantis (information, accès, opposition, rectification, oubli, portabilité), conservation excessive, violation de sécurité (disponibilité, intégrité, confidentialité), refus de traiter une réclamation, autre.
- Auteur présumé, date et heure de la violation et de sa constatation, lieu, résumé de l'incident, données concernées.
- 8 conséquences potentielles à cocher (utilisation illicite, diffusion, corrélation, détournement, altération en données invalides ou valides, indisponibilité totale ou partielle), avec exemples.
- Observations techniques, jusqu'à 4 pièces jointes.

**Utile pour :** le module plaintes et incidents (typologie des violations et des impacts, modèle de notification).

## Formulaire-du-consentement-a-la-transmission-electronique-des-courriers.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Formulaire-du-consentement-a-la-transmission-electronique-des-courriers.pdf`

**En une phrase :** formulaire facultatif par lequel un déclarant accepte que l'APDP lui transmette ses courriers par voie électronique.

**Contenu :**
- Identité du déclarant et de son représentant : raison sociale, RCCM, IFU, adresse, deux numéros de portable, e-mail.
- Canal choisi : adresse électronique ou messagerie instantanée avec numéro.
- Mentions : consentement retirable à tout moment, les frais d'expédition sont alors à la charge du déclarant ; obligation de signaler tout changement de coordonnées ; réception en ligne, alertes et rappels de convocation par SMS ou appel.
- Portée : tous les documents de la procédure (actes, pièces, avis, accusés de réception, convocations, PV, notifications et copies de décisions).
- Référence du dossier, date, signature, certification sur l'honneur. Renvoi à la loi 2020-35 pour les droits d'accès et de rectification.

**Utile pour :** le dossier de formalités (pièce optionnelle) et le paramétrage des notifications.

## FORMULAIRE-UNIQUE.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/FORMULAIRE-UNIQUE.pdf`

**En une phrase :** formulaire unique de formalités préalables de l'APDP (10 pages, art. 407 et 409), qui sert à la fois de déclaration et de demande d'autorisation.

**Contenu :**
- I. Responsable de traitement : nom ou raison sociale, NPI ou RCCM, adresse, secteur (privé, public, institution étrangère), représentant légal.
- II. Traitement : données et origine ; personnes (salariés, adhérents, usagers, visiteurs, patients, clients, élèves) et nombre ; opérations (liste de 25) ; type (vidéosurveillance, site ou application, biométrie, qui renvoie au formulaire complémentaire) ; traitement manuel ou automatisé ; finalité ; fondement ; conservation (art. 383, 6°) ; stockage (disque, cloud, NAS, LVM, art. 433) ; partage (sous-traitance art. 386, communication art. 409, interconnexion art. 393, transfert art. 391 et 392, qui renvoient aux annexes) ; date de mise en œuvre.
- III. Principes : base légale (consentement, contrat, obligation légale, intérêt légitime, mission d'intérêt public, intérêts vitaux) ; information (exceptions, modalités, contenu, preuve) ; consentement (exclusions, méthode) ; pertinence et minimisation.
- IV. Sécurité (art. 387, 424, 426) : personnes habilitées, protection contre les intervenants non autorisés, accès physique, incendie, inondation, surtension, sécurité logique, tests, certification, journalisation, authentification forte ou chiffrement, facteur humain, PSSI, charte ; confidentialité, intégrité (hachage, blockchain, logs), disponibilité (sauvegardes, architecture).
- V. Droits : modalités, responsables et délais pour l'accès (437), la portabilité (438), l'opposition (440), l'interrogation (439), la rectification et suppression (441), l'oubli (443).
- VI. Antériorité : enregistrement antérieur, registre tenu (art. 435), DPO désigné (art. 430 et 431). Mentions APDP : décisions publiées sans le NPI, droit d'accès par QR code, réponse en 1 mois.
- La base « intérêt légitime » figure dans le formulaire alors que l'art. 389 ne la retient pas.

**Utile pour :** la fiche traitement de Waɖɛ et la génération automatique du dossier de déclaration ou d'autorisation.

## GUIDE-PRATIQUE-VIDEOSURVEILLANCE-COMPLETE_Pt_YD.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/GUIDE-PRATIQUE-VIDEOSURVEILLANCE-COMPLETE_Pt_YD.pdf`

**En une phrase :** guide pratique complet de l'APDP sur la vidéosurveillance (17 pages) : obligations, droits, vérification d'une installation et sanctions.

**Contenu :**
- Textes : loi 2017-20, décret 2017-077 du 10 février 2017, délibération 2016-008/RE/CNIL du 9 novembre 2016. Exigences connexes : loi 90-005 sur le commerce, loi 2007-021 sur la consommation, décrets 2020-281 et 2021-051, décision ARCEP 2021-360 (agrément des équipements).
- La vidéosurveillance concerne les lieux privés. La vidéoprotection concerne la voie publique pour le compte de l'État et suit un régime particulier.
- Emplacements autorisés : entrées et sorties, couloirs, salles techniques, stocks, parkings. Emplacements interdits : salles de réunion, vestiaires, réfectoires, infirmeries, dortoirs, bureaux, sanitaires. On ne filme ni les postes de travail (sauf la caisse), ni la voie publique, ni le voisinage, ni les salles de cours, ni les locaux syndicaux.
- Formalité préalable avant la mise en service, sauf caméra dans une habitation privée à usage personnel sans diffusion. Le particulier, le commerçant, l'entreprise et l'administration (hors fins régaliennes) sont concernés. L'installateur n'est pas responsable de la déclaration mais ne doit pas mettre en service sans avis favorable.
- Avis dans un délai maximal de 60 jours après dépôt du dossier complet. Récépissé pour des caméras analogiques en réseau fermé, sans accès distant ni communication. Extrait de délibération d'autorisation dans les autres cas. Toute modification (caméras ajoutées, plan modifié) se déclare.
- Obligations : signalisation par pictogramme APDP et affiche (accès, données, durée), posée à l'installation ; registre dès la mise en service (modèle APDP) ; information ; droits d'accès, d'effacement, d'opposition et de recours. Une installation se vérifie par son pictogramme et son QR code renvoyant au site de l'APDP.
- Sanctions : administratives (injonction, retrait, verrouillage, amende), civiles, pénales (6 mois à 10 ans, 10 à 50 M FCFA, 5 à 50 M FCFA pour une négligence sur les formalités). Saisine de l'APDP : délibération en 60 jours après mise en état, plaintes traitées en 45 jours.

**Utile pour :** le module vidéosurveillance (règles d'implantation, critère récépissé ou autorisation, signalisation, registre).

## Guide-delaboration-du-rapport-annuel.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Guide-delaboration-du-rapport-annuel.pdf`

**En une phrase :** modèle de l'APDP (13 pages) pour le rapport annuel que tout responsable de traitement doit lui remettre (art. 387).

**Contenu :**
- Page de garde : structure et période couverte (de MM/AAAA à MM/AAAA).
- I. Préambule : structure (secteur, RCCM ou IFU, effectif, agences) ; responsable de traitement ; personnes impliquées par traitement ; DPO (date de désignation, durée du mandat, statut) ; gouvernance (positionnement et moyens du DPO).
- II. Registre : traitements réguliers, autres traitements, tableau par traitement (nature, finalités, services, données, sous-traitants, contact pour les droits, durée, transfert, hébergement, sécurité, décision APDP avec la mention oui avec référence, non ou en cours).
- III. Faits marquants : traitements nouveaux ou mis à jour ; procédures (formalités, formulaire de consentement, AIPD, procédure de notification des failles, procédure des droits) ; transferts (destinataire, pays, catégories, garanties).
- Culture de la protection des données : nombre de sessions, cibles (DRH, DSI, juristes, IT…), heures, fréquence.
- Incidents : nombre de demandes de droits, délai moyen, plaintes transmises par l'APDP, failles et signalements.
- Relations avec l'APDP (contrôles, saisines, conseils, notifications, ateliers) ; audits (constats, recommandations) ; remédiations par traitement (formalités, sous-traitance, transfert, politique, sécurité, droits). La numérotation du plan est incohérente après la partie E.

**Utile pour :** le module rapport annuel (génération automatique à partir du registre et des journaux d'incidents et de demandes).

## guide-videosurveillance.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/guide-videosurveillance.pdf`

**En une phrase :** dépliant de l'APDP (5 pages) « Comment procéder à la déclaration de votre système de vidéosurveillance ».

**Contenu :**
- Formulaires à télécharger sur service.apdp.bj : formulaire unique, formulaire complémentaire capteurs, annexe 1 en cas de sous-traitance, autres annexes si nécessaire. Le Service Conformité de l'APDP peut aider à les remplir.
- Pièces : pièce d'identité du responsable de traitement, RCCM ou IFU, plan d'installation et champs de vision, caractéristiques techniques (IP ou analogique, application mobile), engagements de confidentialité, contrat avec le sous-traitant ou l'installateur, preuves de sécurité (charte, politique), preuve que le personnel a été informé (personnes morales).
- Le dossier est envoyé par lettre officielle au Président de l'APDP, avec pour objet « demande d'autorisation de traitement des données personnelles par système de vidéosurveillance ».
- Chemin sur le site : « Vos démarches », puis « Les outils de la conformité », puis « Formulaires ».
- Contacts : n° vert 150, +229 01 21 32 57 88 et 01 69 55 00 00, siège à Aïdjèdo.

**Utile pour :** le module vidéosurveillance (check-list des pièces, lettre d'accompagnement).

## labellisation_c2.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/labellisation_c2.pdf`

**En une phrase :** décision n° 2025-005/APDP/Pt/AP/CA/CTJ/SA du 31 mars 2025 qui modifie les art. 3 et 4 de la délibération 2022-001 du 27 avril 2022 sur la labellisation des formateurs et des formations.

**Contenu :**
- PDF scanné de 2 pages, sans couche texte. Signée par le président L. HOUNKPONOU.
- Art. 3 nouveau : peuvent être candidats au label « APDP approuvé » les personnes et organismes dont les formateurs justifient d'attestations de bonne exécution de formations en protection des données sur les 3 dernières années et d'un diplôme Bac+5 en droit ou en informatique.
- Candidature individuelle ou en réseau. Une demande conjointe doit inclure l'engagement de rester ensemble pendant la durée du label, sinon une nouvelle demande est nécessaire.
- Art. 4 nouveau : demande écrite au Président contenant les types de formation, le programme et les compétences, les preuves de 3 ans d'activité ou les attestations, le reçu de 50 000 FCFA de frais d'étude (compte BJ660 01001 000001043824 74).
- Abroge les dispositions contraires, publication au Journal officiel.

**Utile pour :** le référentiel des formateurs agréés et les justificatifs de formation demandés par le dossier.

## Lettre.Engagement.DPO_-valide_OK.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/Lettre.Engagement.DPO_-valide_OK.pdf`

**En une phrase :** modèle de lettre d'engagement que le DPO désigné signe et remet à l'APDP (4 pages).

**Contenu :**
- Identité du DPO, organisme (RCCM, IFU), référence du courrier de désignation, rattachement à la direction, publication de ses coordonnées, récépissé de l'APDP et date d'effet.
- 15 missions : informer et conseiller ; signaler les manquements ; contrôler le respect du Livre V ; démontrer la conformité ; auditer ; piloter les politiques ; gérer les demandes de droits et les réclamations ; conseiller sur l'AIPD ; veiller à la protection dès la conception ; être l'interlocuteur et le point focal de l'APDP ; préparer la notification des violations ; tenir l'inventaire des traitements ; tenir compte du risque ; présenter un bilan annuel à l'APDP.
- Engagements du responsable de traitement : associer le DPO, lui donner moyens, accès et formation, garantir son indépendance (aucune instruction, aucune sanction), lui permettre de rapporter au plus haut niveau, éviter les conflits d'intérêts, documenter les avis non suivis, recueillir son avis avant toute mise en production.
- Le DPO s'engage à transmettre ses dossiers en fin de mission. Il est tenu au secret professionnel.

**Utile pour :** le module DPO (générer la lettre, suivre les missions et l'indépendance).

## LISTE.PIECES-A-JOINDRE_FORMULAIRE-UNIQUE.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/LISTE.PIECES-A-JOINDRE_FORMULAIRE-UNIQUE.pdf`

**En une phrase :** liste officielle des pièces à joindre au formulaire unique (4 pages).

**Contenu :**
- 9 pièces ordinaires : pièce d'identité avec NPI ; selon le cas RCCM, IFU, agrément, accord de siège, récépissé d'association ou décret de création ; projet d'annonce d'information (art. 415, modèle de politique de confidentialité sur le site) ; textes rendant le traitement obligatoire ; preuves de sécurité (charte, PSSI, politique de gestion des incidents) ; spécifications techniques ; modèle de preuve du consentement ; engagements de confidentialité ; preuve d'une formation par un formateur agréé par l'APDP ; contrat commercial type.
- Pièces spécifiques : sous-traitance (contrat de confidentialité, preuve de conformité du destinataire) ; transfert (contrat conforme aux clauses types de l'APDP, loi étrangère, preuve de conformité) ; interconnexion (contrat de clauses types) ; NNI, traitements massifs, profilage ou données sensibles (AIPD) ; recherche en santé (note au ministre et réponse, protocole) ; site ou application (mentions légales, politique cookies, CGU, architecture, comportement sur le terminal) ; vidéosurveillance (information du personnel, caractéristiques, plan, application d'accès distant).
- Pièces authentiques et traduites. Dépôt par mail ou au guichet avec lettre au Président. Bordereau recommandé. Récépissé immédiat avec numéro de dossier.
- Incohérence : la liste associe le transfert à l'« annexe 3 » et l'interconnexion à l'« annexe 4 », alors que les annexes réelles sont numérotées dans l'autre sens. Certaines adresses de modèles sont laissées en blanc (« … »).

**Utile pour :** la check-list des pièces générée par Waɖɛ selon les drapeaux du traitement.

---

## Registre

## Modèle de registre des activités de traitement (APDP).pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Registre/Modèle de registre des activités de traitement (APDP).pdf`

**En une phrase :** modèle officiel de fiche de registre de l'APDP (4 pages, « Fiche n° 001 : nom du traitement »).

**Contenu :**
- En-tête : référence de la décision APDP et validité.
- 1 organisme (dénomination, IFU, RCCM) ; 2 responsable de traitement ; 3 DPO (fonction, statut).
- 4 activité : code, dénomination, date de création, finalités, catégories de personnes, fondement juridique. 5 principes : modalités du consentement et des droits (délai, disponibilité, mode, service, recours).
- 6 données en 9 classifications (identification, vie personnelle, vie professionnelle, économique et financière, sociale, connectivité, localisation, internet et navigation, sensibles), réparties en simples, sensibles ou à régime spécial.
- 7 cibles ; 8 durées de conservation (conventionnelles ou légales) ; 9 personnes ayant accès (nature du lien, référence du contrat de confidentialité) ; 10 communications au Bénin ; 11 transferts vers un pays tiers.
- 12 sécurité : procédures, environnement, contrôle d'accès, traçabilité, protection des logiciels, sauvegarde, chiffrement, contrôle des sous-traitants.

**Utile pour :** le modèle de données de la fiche registre de Waɖɛ (les 9 classifications de l'APDP).

## Modele-de-Registre-des-activites-de-Videosurveillance.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Registre/Modele-de-Registre-des-activites-de-Videosurveillance.pdf`

**En une phrase :** modèle officiel de registre propre à la vidéosurveillance (5 pages, « Fiche n° 001 : vidéo surveillance »).

**Contenu :**
- Rubriques 1 à 6 identiques au registre général, avec en plus un bloc sous-traitant (IFU ou RCCM, NIP).
- 7 lieu de traitement des images (sur place ou ailleurs) ; 8 visionnage continu (qui, quand, où) ou à distance (qui, comment, où).
- 9 journal des sauvegardes et suppressions : date, caméra, heure de début et de fin, NIP et signature.
- 10 consultation par des tiers (droit d'accès) : référence d'autorisation, date et heure, caméra, service compétent, identité, pièce, finalité, visualisation ou copie.
- 11 sécurité avec des exemples de réponses : enregistreur sous clé, journalisation des connexions, mises à jour annuelles, accès https, main courante de maintenance, accompagnement des prestataires, clause de sécurité, destruction des disques.

**Utile pour :** le module vidéosurveillance (journaux d'extraction, d'accès et d'effacement).

## Registre_type_Benin.xlsx / Registre_type_Benin.pdf
*Chemins :* `02 Bénin/00 Sources et référentiels/Registre/Registre_type_Benin.xlsx` ; `02 Bénin/00 Sources et référentiels/Registre/Registre_type_Benin.pdf`

**En une phrase :** registre type pour le Bénin (version 4.0, septembre 2026, AMELEGAL Conseils pour « Warê ») : 139 fiches de traitement préqualifiées et prêtes à charger dans l'application. Le PDF de 185 pages est un export du classeur.

**Contenu :**
- 10 onglets : Notice, Registre (une ligne par fiche, colonnes A à AV), Finalités (599 lignes), Personnes publiques, Bases légales (15 textes), Durées, Référentiels, Injection Waɖɛ, Synthèse, Fiches imprimables.
- Répartition : 49 fiches du socle générique (SG-REC, RH, SSI, CLI, NUM…), 60 sectorielles (SE-SAN, BQE, TEL, EME, EDU, LOG, OSC, SFD, ASS, ASO), 8 de communes béninoises (CB-COM), 22 de personnes publiques (PP-RHP, IDE, FIN, SEC, SAN, SOC, STA, REG…).
- Régime calculé sans DPO : 57 déclarations (art. 405), 52 autorisations (art. 407), 24 décrets (art. 411), 6 dispenses (art. 410). Avec un DPO désigné, les 57 déclarations deviennent des exemptions (art. 408). AIPD requise pour 77 fiches.
- Bases : liste fermée de 5 valeurs de l'art. 389 (obligation légale 50, contrat 37, mission d'intérêt public 19, consentement 18, sauvegarde des intérêts 15). « Intérêt légitime » est écarté et une colonne de repli est prévue pour la maquette.
- Durées en deux couches : ancrages contraignants (OHADA AUDCIF art. 24, 10 ans ; LBC-FT UMOA art. 35, 10 ans ; art. 383, 6°) et repères indicatifs CNIL et APD belge (candidats 2 ans, paie, registre du personnel 5 ans, prospection 3 ans, vidéo 1 mois, logs 6 mois à 1 an, traceurs 13 et 25 mois…).
- Référentiels : environ 90 clés de catégories de données (ID_NNI, SEN_BIO, SEN_PENAL, CNX_LOG…) rattachées aux 9 classifications de l'APDP, 32 catégories de personnes, 8 clés de régime (horschamp, domestique, dispense, decret, autorisation, simplifiee, exemption, declaration), 25 drapeaux (perso, dispPaie…, nni, interconnexion, transfert, correspondant…), modèles de sécurité (STD, RENF, SANTE, PUB, VIDEO). 24 fiches déclenchent le décret de l'art. 411.
- Onglet d'injection : correspondance entre colonnes et champs de la fiche (ref, nom, finalite multivaluée, base, dataClasses, dureeIndicative…). Les colonnes de contrôle doivent redonner les résultats de `qualifier()` et `besoinAIPD()`.
- **Différences xlsx/pdf :** le PDF garde une notice commune Togo et Bénin (176 mentions du Togo, « collectivités togolaises retirées », art. 14 et 16 de la loi togolaise). Le xlsx est épuré pour le Bénin seul (aucune mention du Togo). Dans le xlsx, les comptages de l'onglet Synthèse sont des formules sans valeur en cache (cellules vides à la lecture avec openpyxl). Le PDF affiche ces comptages (49/60/8/22, total 139 ; 52/6/57/0/24/0/0/0).

**Utile pour :** le chargement initial du registre Waɖɛ pour le Bénin, les tests du moteur de qualification et de `besoinAIPD()`, et les durées par défaut.

---

## Textes

## Benin-Loi-2017-20-Portant-code-du-numerique-en-Republique-du-Benin.pdf
*Chemin :* `02 Bénin/00 Sources et référentiels/Textes/Benin-Loi-2017-20-Portant-code-du-numerique-en-Republique-du-Benin.pdf`

**En une phrase :** texte intégral de la loi n° 2017-20 portant code du numérique (adoptée le 13 juin 2017, datée du 20 avril 2018, 201 pages, 7 livres, 647 articles). Le Livre cinquième (art. 379 à 490) porte sur la protection des données personnelles.

**Contenu :**
- Version d'origine non consolidée : l'art. 464 y fixe encore 11 membres, alors que la loi 2020-35 les a ramenés à 8. Le texte contient des renvois erronés (art. 461 renvoie à « l'article 445 » au lieu de 460 ; art. 432 renvoie à l'art. 412 pour la consultation préalable au lieu de 429 ; art. 417 renvoie aux art. 445 et 446). Livres : préliminaire (définitions), I réseaux, II écrits électroniques, III prestataires de confiance, IV commerce électronique, V données personnelles, VI cybercriminalité, VII dispositions transitoires (art. 647 qui abroge la loi 2009-09).
- Champ et principes : application à tous, publics et privés (art. 380) ; territoire du Bénin, ciblage des personnes au Bénin et traitement dans la CEDEAO (art. 381) ; exclusion domestique (art. 382) ; 7 conditions de licéité, dont la durée limitée (art. 383, 6°) ; sous-traitant avec contrat écrit (art. 386) ; 14 obligations de sécurité et rapport annuel (art. 387) ; responsables conjoints (art. 388) ; consentement et 4 dérogations (art. 389) ; conditions du consentement (art. 390).
- Transferts : niveau équivalent constaté par l'APDP et autorisation préalable (art. 391) ; 6 exceptions, ou décret après avis conforme (art. 392) ; interconnexion (art. 393). Données sensibles interdites sauf 15 exceptions (art. 394) ; données pénales (art. 395) ; recherche (art. 396) ; prospection directe interdite au sens de l'art. 332 (art. 400) ; pas de décision fondée uniquement sur un profilage (art. 401) ; mesures supplémentaires (art. 402) ; consentement de l'employé non valable (art. 404).
- Formalités : déclaration ou inscription au registre (art. 405) ; normes simplifiées (art. 406) ; 8 cas d'autorisation, décision unique et engagement de conformité (art. 407) ; exemptions, dont le DPO, fermées aux autorités publiques (art. 408) ; 12 mentions du dossier (art. 409) ; 6 dispenses (art. 410) ; décret en Conseil des ministres sur 5 objets (art. 411) ; délai de 60 jours plus 30, silence valant accord (art. 412) ; dépôt (art. 413).
- Obligations : information en 14 points à la collecte (art. 415) ou dans les 30 jours (art. 416) ; réponse aux demandes en 30 jours, prolongeable de 60 (art. 420) ; gratuité (art. 421) ; protection dès la conception et par défaut (art. 424) ; sécurité (art. 426) ; notification « sans délai » à l'APDP et aux personnes, avec 4 mentions et 3 dispenses (art. 427) ; AIPD dans 3 cas (art. 428) ; consultation en 8 semaines plus 6 (art. 429) ; DPO obligatoire pour les autorités publiques, le suivi à grande échelle et les données sensibles à grande échelle (art. 430 à 432) ; registre en 7 mentions pour le responsable et 4 pour le sous-traitant, exemption PME sauf risque (art. 435).
- Droits : accès avec copie en 60 jours (art. 437) ; portabilité (art. 438) ; interrogation (art. 439) ; opposition avec réponse en 30 jours (art. 440) ; rectification en 45 jours (art. 441) ; oubli (art. 443) ; accès indirect pour la sûreté de l'État (art. 445) ; mineur de 16 ans (art. 446) ; réclamation, recours après 90 jours sans réponse de l'APDP, réparation solidaire (art. 448 à 451).
- Sanctions : avertissement, mise en demeure de 8 jours au plus (art. 452) ; 5 manquements graves (art. 453) ; amende (pas contre l'État), injonction, retrait, verrouillage (art. 454) ; jusqu'à 50 M FCFA, puis 100 M ou 5 % du chiffre d'affaires en cas de récidive sous 5 ans (art. 455) ; contradictoire avec 15 jours pour répondre (art. 457) ; 15 infractions pénales (art. 460) ; 6 mois à 10 ans et 10 à 50 M FCFA, 5 à 50 M pour négligence, interdiction de gérer pendant 2 ans, récidive jusqu'à 100 M (art. 461).
- APDP (art. 462 à 490) : autorité administrative indépendante ; 11 membres dans ce texte ; mandat de 5 ans renouvelable une fois ; 26 missions (art. 483) ; pouvoir réglementaire (art. 485) ; contrôle sur place de 6 h à 21 h, avec information du procureur et droit d'opposition levé par le juge (art. 489) ; délais doublés en cas d'investigation (art. 490).

**Utile pour :** la base juridique de tout le volet Bénin (moteur de qualification, délais, sanctions, aide contextuelle). Il faut le compléter par la loi 2020-35, absente du dépôt, pour la composition de l'APDP.

# Partie 6 — Anomalies relevées pendant la lecture

Ces points sont à soumettre à AMELEGAL. Ils s'ajoutent aux écarts déjà listés dans `_modélisation/README.md`.

## Communs

- **Cartographie v3** : l'annexe annoncée sur les compétences « hors traitement » manque. Le texte s'arrête sur un fragment tronqué.
- **Deux versions de registre commun** : *Registre_type* est en v3.0 (142 fiches, 593 finalités), *Registre_original* en v4.0 (164 fiches, 709 finalités, avec en plus une partie « personne morale de droit public »).
- **Registres PDF** : le nom Waɖɛ s'affiche « Warê » et des lignes sont coupées. Les xlsx sont complets.
- **registre-champs.csv et bulles-information.json** :
  - les bulles `categorie_donnees` et `droits_personnes` sont citées dans le CSV mais n'existent pas dans le JSON ;
  - la notice annonce 11 types de champ alors que le CSV en utilise 12 (`fichiers` en plus) ;
  - `org.nature_publique` renvoie à la bulle `mission_service_public`.
- **H06 (CGV)** : il manque les prix, les formules et les taxes, qui dépendent de G06, absent du dépôt.
- **Champs [●]** : de nombreux éléments restent à compléter dans H02, H03 et H04 (RCCM, NIF, hébergement, durées).
- **H04** : la référence à la loi togolaise n° 2017-07, art. 40, est signalée comme non vérifiée par le document lui-même.

## Togo

- **Coordonnées de l'IPDCP** : C03 les donne, mais `referentiel-togo.json` les laisse à `null`.
- **Bulles D02 en contradiction avec la loi ou le moteur** :
  - « données sensibles » : la bulle dit que leur présence écarte la déclaration, alors que CAS-TG-07 aboutit à une déclaration ;
  - « instruction » : la bulle dit que le silence de l'IPDCP ne vaut pas acceptation, alors que l'art. 11 dit qu'il vaut avis favorable ;
  - « cadre domestique » : la bulle dit que la loi ne prévoit pas d'exclusion domestique, alors que l'art. 3, 1° la prévoit.
- **Logigramme C06 et loi** :
  - C06 ne reprend pas l'art. 9, 2°, 4° et 5° ;
  - C06 n'examine les cas de l'art. 8 qu'après un « oui » sur les données sensibles (TG-Q5), condition que la loi ne pose pas ;
  - le libellé de TG-Q8 ne cite pas deux de ses sept options.
- **Registre type Togo** : le PDF est une version plus ancienne que le xlsx (sa notice mentionne encore le Bénin).
- **Défauts de forme** : numérotation sautée dans C08 et E03, libellés manquants dans E01, D03 pas encore rédigé, K01 et K02 restés à « À renseigner ».

## Bénin

- **CAS-BJ-06** : il attend BJ-EXEMPTION avec BJ-Q4 = oui (personne publique), ce que la condition bloquante de BJ-Q8 interdit.
- **D01** : la notion « registre destiné à l'information du public » y est déterminante, alors que la bulle D02 la dit non retenue en droit béninois.
- **Noms de champs** :
  - `bloc1.*`, `bloc2.*` et `bloc3.*` d'un côté, `org.*` et `t.*` de l'autre, sans table de correspondance ;
  - D01 cite `t.caracteristiques_article_8`, un champ propre au Togo.
- **Sections manquantes et éléments à renseigner** :
  - sections absentes dans C02, C10 et C11 ;
  - D03 n'est que cadré ;
  - les coordonnées de l'APDP, les pays reconnus et la référence au JO de la loi restent à renseigner.
- **Loi 2017-20** : le texte fourni n'est pas consolidé. L'art. 464 y fixe encore 11 membres, ramenés à 8 par la loi 2020-35, qui manque au dépôt. Il contient aussi des renvois erronés (art. 461 vers 445, art. 432 vers 412).
- **LISTE.PIECES-A-JOINDRE** : la liste inverse les annexes 3 (interconnexion) et 4 (transfert).
- **Formulaire unique** : il propose la base « intérêt légitime », que l'art. 389 ne prévoit pas.
- **Fichiers mal nommés** : *labellisation_c2.pdf* est en réalité la décision 2025-005 (labellisation des formateurs) et *certification_c2.pdf* la décision 2025-004 (certification des DPD).
- **Étude « Pratique… »** : le PDF « version finale » reprend le texte de *BON.docx*. Le docx « version finale » est la version la plus corrigée.
- **Registre type Bénin** : le PDF est un export plus ancien qui mentionne encore le Togo. Dans le xlsx, les formules de l'onglet Synthèse n'ont pas de valeur enregistrée.
