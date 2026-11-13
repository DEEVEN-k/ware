"""Explications des classes des modules Référentiels et Moteur."""

CLASSES = {
    "Juridiction": {
        "role": "Un pays couvert (Togo, Bénin). La juridiction est un paramètre : chaque traitement est qualifié selon le droit du pays dont il relève.",
        "champs": {
            "Code": "Code stable (TG, BJ), clé de rattachement des référentiels, des fiches et des exigences.",
            "Nom": "Nom court affiché en permanence dans l'interface (exigence de visibilité de la juridiction).",
            "NomOfficiel": "Repris dans les documents (« République du Bénin »).",
            "Langue": "Langue des documents produits.",
            "SocleRegional": "Rattachement au socle CEDEAO, en vue d'ouvrir d'autres pays.",
            "HeriteDuSocle": "Indique que la juridiction reprend les éléments communs du socle.",
        },
    },
    "ReferentielVersion": {
        "role": "Une version du référentiel juridique d'un pays, stockée en base. Règle cardinale de la notice : aucune valeur juridique dans le code ; tout est chargé, versionné et rattaché à une juridiction.",
        "champs": {
            "Id": "Référencé par chaque qualification : une qualification ancienne reste explicable avec la version qui l'a produite.",
            "JuridictionCode": "Le pays concerné.",
            "Numero": "Numéro de version (1.0, 1.1…), affiché avec chaque résultat.",
            "Statut": "Seule la version Publiée est utilisée pour les nouvelles qualifications.",
            "DateVersion": "Date du référentiel (meta.date du JSON).",
            "PublieLe": "Date de mise en vigueur dans l'application.",
            "Avertissement": "Mention reprise du JSON (« aucune valeur codée en dur »).",
            "Contenu": "Le référentiel complet en JSON, tel qu'importé et validé par schéma.",
            "Empreinte": "Empreinte SHA-256 du contenu : prouve qu'une version publiée n'a jamais été modifiée.",
        },
    },
    "StatutReferentiel": {
        "role": "Cycle de vie d'une version de référentiel (G03).",
        "valeurs": {
            "Brouillon": "Importé ou en cours d'édition.",
            "EnSimulation": "Rejoué sur les cas de recette et les fiches existantes avant publication.",
            "Publie": "En vigueur ; immuable.",
            "Remplace": "Remplacé par une version postérieure ; toujours lisible.",
        },
    },
    "Referentiel": {
        "role": "La forme typée, en lecture seule, du contenu JSON. Elle reprend exactement les clés du fichier referentiel-*.json décrites par la notice §3.",
        "champs": {
            "Sources": "Textes et articles qui fondent chaque résultat (clé sources).",
            "Autorite": "Autorité de contrôle et règles de procédure (clé autorite).",
            "Terminologie": "Libellés propres au pays : « correspondant » au Togo, « délégué » au Bénin (clé terminologie).",
            "Regimes": "Les sorties possibles du logigramme (clé regimes).",
            "Logigramme": "L'arbre de qualification (clé logigramme).",
            "FeuillesDeRoute": "Étapes et pièces à fournir, par régime (clé feuilles_de_route).",
            "Aipd": "Critères et grille d'analyse d'impact (clé aipd).",
            "Violations": "Délai et arbre de qualification d'une violation (clé violations).",
            "Correspondant": "Statut et effets du correspondant ou délégué (clé correspondant).",
            "Transferts": "Règles des transferts hors du pays (clé transferts).",
            "Indice": "Composantes, poids et seuils de l'indice (clé indice).",
        },
    },
    "Regime": {
        "role": "Une sortie du logigramme : régime de formalité (déclaration, autorisation…) ou exclusion (hors champ, domestique).",
        "champs": {
            "Id": "Code stable (TG-DECLARATION, BJ-EXEMPTION…), clé de rattachement des qualifications et des dossiers.",
            "Libelle": "Nom court affiché dans le badge du résultat.",
            "IntituleOfficiel": "Intitulé repris dans les documents officiels.",
            "FamilleCouleur": "Couleur du badge : même famille de régime, même couleur, quel que soit le pays.",
            "Ordre": "Ordre d'affichage dans les listes.",
            "Fondement": "Article de loi qui fonde le régime, affiché avec le résultat.",
            "EstUnRegimeDeFormalite": "Faux pour les exclusions béninoises : aucun dossier n'est alors créé.",
        },
    },
    "Logigramme": {
        "role": "L'arbre de décision qui détermine le régime (livrable C06).",
        "champs": {
            "Entree": "La première question posée.",
            "Principe": "Règle de lecture : « la première sortie atteinte fixe le régime ».",
            "Questions": "Les huit questions du pays.",
            "ReglesTransverses": "Obligations ajoutées quelle que soit la sortie (AIPD, consultation préalable…).",
            "Ecart": "Signale un écart entre le texte et la pratique de l'autorité.",
        },
    },
    "Question": {
        "role": "Une question du logigramme.",
        "champs": {
            "Id": "Code stable (TG-Q3, BJ-Q8), conservé dans le chemin de chaque qualification.",
            "Ordre": "Ordre d'affichage dans l'assistant pas à pas.",
            "Libelle": "Texte de la question.",
            "Champ": "Le code du champ de fiche qui fournit la réponse : la qualification se fait en continu pendant la saisie.",
            "Type": "Booléen ou choix multiple.",
            "Options": "Pour un choix multiple : les codes de valeurs attendus.",
            "AideId": "Bulle d'information obligatoire pour toute notion juridique utilisée.",
            "Fondement": "Article de loi affiché avec la question et dans les motifs.",
            "ConditionBloquante": "Force la réponse à « non » dans certains cas (exemption béninoise fermée aux autorités publiques).",
            "Oui": "La suite si la réponse est oui.",
            "Non": "La suite si la réponse est non.",
        },
    },
    "Branche": {
        "role": "La suite d'une réponse : une autre question ou un régime.",
        "champs": {
            "Type": "Question ou sortie.",
            "Cible": "L'identifiant de la question suivante ou du régime.",
            "Motif": "Pour une sortie : la phrase qui explique le résultat à l'utilisateur.",
        },
    },
    "TypeBranche": {
        "role": "Nature d'une branche.",
        "valeurs": {
            "Question": "Passer à une autre question.",
            "Sortie": "Fin du parcours : un régime est déterminé.",
        },
    },
    "ConditionBloquante": {
        "role": "Une condition qui force une réponse à « non » (notice §4).",
        "champs": {
            "Champ": "Le champ testé (nature publique ou mission de service public).",
            "Valeur": "La valeur qui déclenche le forçage.",
            "Effet": "Explication affichée dans les motifs.",
        },
    },
    "RegleTransverse": {
        "role": "Une règle qui ajoute des obligations ou des tâches sans changer le régime (notice §4).",
        "champs": {
            "Id": "Code stable (BJ-T1 à BJ-T5).",
            "Libelle": "Titre affiché.",
            "Fondement": "Article de loi ou pratique de l'autorité.",
            "Regle": "Ce que l'application doit faire.",
        },
    },
    "EtapeFeuilleDeRoute": {
        "role": "Une étape de la marche à suivre après la qualification (livrable C07).",
        "champs": {
            "Ordre": "Ordre des étapes.",
            "Etape": "Ce qu'il faut faire.",
            "Pieces": "Pièces à joindre au dossier.",
        },
    },
    "ParametresAutorite": {
        "role": "L'autorité de contrôle et ses règles de procédure (livrable C03).",
        "champs": {
            "Denomination": "Nom complet de l'autorité, repris dans les documents.",
            "Sigle": "IPDCP ou APDP, affiché dans le résultat.",
            "ModalitesDepot": "Comment déposer un dossier (voie électronique, postale, guichet).",
            "DelaisInstruction": "Délais par régime, utilisés pour calculer l'échéance des dossiers.",
            "SilenceVautAcceptation": "Vrai au Bénin : le dossier passe en « Acceptation tacite » à l'échéance.",
            "ValiditeDecisionMois": "24 au Bénin : déclenche l'alerte de renouvellement (AL-12).",
        },
    },
    "DelaiInstruction": {
        "role": "Un délai d'instruction de l'autorité.",
        "champs": {
            "Regime": "Le régime concerné (ou « toutes formalités »).",
            "Delai": "La durée (60 jours, 1 mois…), absente quand la loi ne la chiffre pas.",
            "Prorogeable": "Possibilité et durée de prorogation.",
            "Condition": "Cas particulier (délai doublé en cas d'investigation).",
            "Fondement": "Article de loi.",
        },
    },
    "ConfigAipd": {
        "role": "Les règles de l'analyse d'impact du pays (livrable C08).",
        "champs": {
            "Criteres": "Les critères qui rendent l'AIPD obligatoire ; un seul suffit.",
            "PresomptionRegimes": "Régimes pour lesquels l'AIPD est présumée requise (autorisation, décret).",
            "Consultation": "Consultation préalable de l'autorité si le risque résiduel reste élevé.",
            "Grille": "Les quatre sections de la grille d'analyse.",
        },
    },
    "CritereAipd": {
        "role": "Un critère qui déclenche l'analyse d'impact.",
        "champs": {
            "Id": "Code stable, conservé dans la qualification.",
            "Libelle": "Texte affiché.",
            "Champ": "Le champ de fiche testé.",
            "Seuil": "Seuil numérique éventuel (10 000 personnes).",
            "Source": "Texte de loi ou standard international.",
        },
    },
    "ConfigViolation": {
        "role": "Les règles de traitement d'une violation de données (livrable C09).",
        "champs": {
            "DelaiNotificationHeures": "72 heures, issues des standards internationaux.",
            "PointDeDepart": "Point de départ du délai : la prise de connaissance par le responsable.",
            "Destinataire": "Autorité destinataire de la notification.",
            "Arbre": "Les deux questions qui décident de la notification.",
            "RappelsProportionDelai": "Rappels à 25, 50, 75 et 90 % du délai.",
        },
    },
    "NoeudViolation": {
        "role": "Une question de l'arbre de qualification d'une violation.",
        "champs": {
            "Id": "Code stable (BJ-V1, BJ-V2).",
            "Libelle": "Texte de la question.",
            "Oui": "La suite si oui.",
            "Non": "La suite si non.",
        },
    },
    "ConfigIndice": {
        "role": "Le paramétrage de l'indice de conformité (G01, C13).",
        "champs": {
            "Composantes": "Les quatre composantes et leurs poids.",
            "Seuils": "Les libellés selon la valeur (Action requise, À surveiller…).",
        },
    },
    "BulleInformation": {
        "role": "Une aide contextuelle sur une notion juridique (livrables D01, D02).",
        "champs": {
            "Id": "Code stable cité par les champs et les questions.",
            "JuridictionCode": "Vide si commune aux deux pays, sinon propre à un pays.",
            "Titre": "Titre de la bulle.",
            "Texte": "Explication courte.",
            "LienFiche": "Lien vers une fiche d'explication développée (D03).",
        },
    },
    "TypeQuestion": {
        "role": "Les deux types de question du logigramme.",
        "valeurs": {
            "Booleen": "Oui ou non.",
            "Multiple": "Vrai dès qu'une option au moins est cochée (notice §4).",
        },
    },
    "Sources": {
        "role": "Les sources juridiques du pays (livrable C02).",
        "champs": {
            "TextePrincipal": "La loi de référence (loi 2019-014, Code du numérique).",
            "EtatTextesApplication": "Décrets d'application parus ou attendus.",
            "ArticlesCles": "Les articles cités par les motifs.",
            "DoctrineAutorite": "Décisions et rapports de l'autorité.",
        },
    },
    "ArticleCle": {
        "role": "Un article de loi et son objet.",
        "champs": {
            "Art": "Numéro de l'article.",
            "Objet": "Ce qu'il régit.",
        },
    },
    "ModaliteDepot": {
        "role": "Un moyen de déposer un dossier auprès de l'autorité.",
        "champs": {
            "Canal": "Voie électronique, postale, guichet.",
            "Fondement": "Article ou pratique de l'autorité.",
        },
    },
    "EcartTextePratique": {
        "role": "Un écart entre la loi et la pratique de l'autorité (exemple béninois : déclaration simplifiée et exemption peu appliquées).",
        "champs": {
            "SortiesConcernees": "Les régimes concernés.",
            "Constat": "Ce qu'on observe.",
            "RegleAffichage": "Ce que l'application affiche à côté du résultat.",
        },
    },
    "ConfigCorrespondant": {
        "role": "Le statut juridique du correspondant ou délégué dans le pays (livrable C10).",
        "champs": {
            "Denomination": "Correspondant (Togo) ou délégué (Bénin).",
            "DesignationObligatoire": "Si la désignation est imposée par la loi.",
            "Fondement": "Article de loi.",
            "EffetSurFormalites": "Effet de la désignation : dispense au Togo, voie de l'exemption au Bénin.",
            "Piece": "Justificatif attendu.",
            "RegleMoteur": "Comment le moteur en tient compte.",
        },
    },
    "ConfigTransferts": {
        "role": "Les règles des transferts hors du pays (livrable C11).",
        "champs": {
            "Principe": "Règle générale.",
            "PaysReconnus": "Pays offrant une protection reconnue, qui allègent la formalité.",
            "Piece": "Annexe à joindre (annexe 4 du formulaire unique au Bénin).",
            "FormaliteAssociee": "Le régime qu'implique un transfert.",
        },
    },
    "ConsultationPrealable": {
        "role": "La consultation de l'autorité après une AIPD à risque résiduel élevé (art. 429 au Bénin).",
        "champs": {
            "Fondement": "Article de loi.",
            "Declencheur": "Risque résiduel élevé.",
            "DelaiReponse": "8 semaines, prorogeables de 6.",
            "EffetMoteur": "Crée un dossier de consultation avec son propre compte à rebours.",
        },
    },
    "SectionGrille": {
        "role": "Une section de la grille d'AIPD.",
        "champs": {
            "Section": "Numéro (1 à 4).",
            "Titre": "Description, nécessité, risques, mesures.",
            "Contenu": "Ce qu'il faut renseigner.",
        },
    },
    "BrancheViolation": {
        "role": "La suite d'une réponse dans l'arbre des violations : autre question ou décision.",
        "champs": {
            "Type": "Question ou décision.",
            "Cible": "La question suivante.",
            "NotificationAutorite": "Décision : faut-il notifier l'autorité ?",
            "InformationPersonnes": "Décision : faut-il informer les personnes concernées ?",
            "Motif": "Explication affichée.",
        },
    },
    "ComposanteIndice": {
        "role": "Une composante de l'indice de conformité.",
        "champs": {
            "Code": "Code stable (completude_registre…).",
            "Libelle": "Libellé affiché dans le détail du calcul.",
            "Poids": "Pondération (0,35, 0,35, 0,20, 0,10).",
        },
    },
    "SeuilIndice": {
        "role": "Une plage de valeurs de l'indice et son libellé.",
        "champs": {
            "Libelle": "Action requise, À surveiller, Bon à consolider, Solide.",
            "Min": "Borne basse.",
            "Max": "Borne haute.",
        },
    },
    # ----------------------------------------------------------------- MOTEUR
    "ResultatQualification": {
        "role": "Ce que restitue le moteur. La notice §4 impose que le résultat contienne toujours ces éléments.",
        "champs": {
            "JuridictionCode": "Juridiction appliquée.",
            "VersionReferentiel": "Version du référentiel utilisée.",
            "RegimeId": "Régime déterminé.",
            "Motifs": "Phrases qui expliquent le résultat.",
            "Chemin": "Les questions parcourues et leurs réponses.",
            "AipdRequise": "Besoin d'analyse d'impact.",
            "CriteresAipdReunis": "Les critères qui l'imposent.",
            "ReglesTransverses": "Les obligations transverses déclenchées.",
            "AutoriteSigle": "Autorité compétente.",
            "FeuilleDeRoute": "Les étapes à suivre.",
            "ReserveInterpretation": "Mention du livrable D05 : le résultat est indicatif.",
        },
    },
    "MoteurQualification": {
        "role": "Le moteur de règles, en C# pur sans dépendance : il ne fait que lire un référentiel et des valeurs. Il est donc testable avec les seuls fichiers CSV de recette.",
        "champs": {
            "Qualifier()": "Exécute le logigramme et renvoie le résultat complet.",
            "EvaluerViolation()": "Parcourt l'arbre des violations.",
            "CalculerIndice()": "Calcule l'indice à partir des mesures.",
        },
    },
}
