"""Diagramme d'activité UML de Waɖɛ : source unique (données).

Le générateur (generer_activite.py) en tire la planche Graphviz. Les identifiants reprennent
ceux du diagramme de flux (A1, B7, E14…) quand l'étape est la même, pour garder la traçabilité.

Types de nœuds (notation UML 2) :
  debut      nœud initial (disque plein)
  fin        nœud final d'activité (œil de bœuf)
  finflux    fin de flot (cercle barré) : ce chemin s'arrête, l'activité continue
  action     action
  decision   décision ou fusion (losange) ; les gardes sont portées par les flèches
  fourche    fourche ou jonction (barre noire) : chemins parallèles
  envoi      envoi de signal (pentagone sortant) : alerte, notification, courriel
  reception  réception d'un signal externe (pentagone rentrant)
  temps      événement temporel (sablier) : échéance, délai
"""

COULOIRS = [
    ("ADM", "Administrateur d'organisation", "#F3ECFA", "#6B3FA0"),
    ("CAB", "Cabinet (sous mandat)", "#FDEBD3", "#C97A12"),
    ("CON", "Contributeur métier", "#EAF5EC", "#00901D"),
    ("COR", "Correspondant", "#E6F0E8", "#00370B"),
    ("RT", "Responsable de traitement", "#E6EEFB", "#2A5DB0"),
    ("SYS", "Système Waɖɛ", "#F1F3F2", "#7b857e"),
    ("AUT", "Autorité de contrôle (IPDCP, APDP)", "#FFFFFF", "#555555"),
]

PHASES = [
    ("PH0", "0 · Mise en place", "S0"),
    ("PH1", "1 · Recensement", "B1"),
    ("PH2", "2 · Qualification et publication", "C1"),
    ("PH3", "3 · Analyse d'impact", "D1"),
    ("PH4", "4 · Formalité", "E1"),
    ("PH5", "5 · Pilotage continu", "MF"),
    ("PH6", "6 · Violation de données", "G0"),
]

# (identifiant, couloir, type, libellé)
NOEUDS = [
    # 0 · Mise en place
    ("S0", "ADM", "debut", ""),
    ("A1", "ADM", "action", "Créer l'espace,\naccepter les CGU"),
    ("A1E", "SYS", "envoi", "Courriel de\nvérification"),
    ("A1C", "ADM", "action", "Confirmer l'adresse,\nactiver la double\nauthentification"),
    ("A2", "ADM", "action", "Décrire l'organisation"),
    ("A3", "ADM", "action", "Renseigner la désignation\nlégale du correspondant"),
    ("F0", "ADM", "fourche", ""),
    ("A4", "ADM", "action", "Inviter les utilisateurs\n(rôles, périmètres)"),
    ("A5", "ADM", "decision", ""),
    ("A6", "CAB", "action", "Demander un mandat\n(niveau, périmètre, durée)"),
    ("A7", "ADM", "decision", ""),
    ("A8", "CAB", "action", "Affecter nominativement\nles consultants"),
    ("MA", "ADM", "decision", ""),
    ("J0", "ADM", "fourche", ""),

    # 1 · Recensement
    ("B1", "CON", "decision", ""),
    ("B2", "CON", "action", "Répondre au diagnostic\nguidé (F01)"),
    ("B3", "CON", "action", "Importer un registre\nexistant"),
    ("B4", "CON", "action", "Partir d'un modèle\nsectoriel (F02)"),
    ("B5", "CON", "action", "Remplir la trame\nde collecte (F04)"),
    ("MB", "CON", "decision", ""),
    ("B6", "SYS", "action", "Créer les fiches\nen Brouillon"),
    ("B7", "CON", "action", "Saisir les 3 blocs\nde la fiche"),
    ("B8", "SYS", "action", "Qualifier en direct\n(résultat provisoire)"),
    ("B9", "CON", "action", "Soumettre à\nqualification"),
    ("B10", "SYS", "decision", ""),
    ("B11", "SYS", "envoi", "AL-05 : champs\nobligatoires manquants"),
    ("B12", "SYS", "envoi", "Notifier le\ncorrespondant"),

    # 2 · Qualification et publication
    ("C1", "SYS", "action", "Exécuter le logigramme\nde chaque juridiction"),
    ("C2", "SYS", "action", "Présenter régime, motifs,\nfondement, feuille de route"),
    ("C6", "COR", "decision", ""),
    ("C7", "COR", "action", "Renvoyer au contributeur\n(motif)"),
    ("C3", "COR", "decision", ""),
    ("C4", "COR", "action", "Retenir un autre régime\n(motif obligatoire)"),
    ("C5", "SYS", "action", "Créer la tâche\n« consulter l'autorité »\n(BJ-T3)"),
    ("MC", "COR", "decision", ""),
    ("C8", "COR", "action", "Arrêter le régime :\nfiche Qualifiée"),
    ("C9", "SYS", "decision", ""),
    ("MC2", "SYS", "decision", ""),
    ("C10", "SYS", "decision", ""),
    ("C11", "RT", "action", "Viser la fiche"),
    ("MC3", "COR", "decision", ""),
    ("C12", "COR", "action", "Publier au registre"),
    ("C13", "SYS", "action", "Créer l'instantané,\nrecalculer l'indice"),
    ("F2", "SYS", "fourche", ""),
    ("F5P", "SYS", "action", "Planifier la revue\n(12 ou 6 mois)"),

    # 3 · Analyse d'impact
    ("D1", "SYS", "envoi", "Ouvrir l'AIPD,\nalerte AL-02"),
    ("D2", "COR", "action", "Lancer l'analyse,\ninviter des contributeurs"),
    ("FD", "COR", "fourche", ""),
    ("D3A", "CON", "action", "Rédiger les sections\nauxquelles il est invité"),
    ("D3B", "COR", "action", "Rédiger description,\nnécessité, mesures"),
    ("JD", "COR", "fourche", ""),
    ("D4", "COR", "action", "Coter les risques\n(initial, résiduel)"),
    ("D5", "COR", "action", "Soumettre à validation"),
    ("D6", "RT", "decision", ""),
    ("D7", "SYS", "action", "Générer le rapport\nd'AIPD (E04)"),
    ("D8", "SYS", "decision", ""),
    ("D9", "SYS", "action", "Ouvrir un dossier de\nconsultation préalable\n(8 semaines)"),

    # 4 · Formalité
    ("E1", "SYS", "decision", ""),
    ("E2", "SYS", "action", "Documenter la dispense\nau registre"),
    ("E3", "COR", "action", "Créer le dossier\nprérempli"),
    ("E4", "SYS", "action", "Générer les documents\n(E03)"),
    ("E5", "COR", "action", "Joindre les pièces\nde la feuille de route"),
    ("T1", "SYS", "temps", "30 jours sans dépôt"),
    ("E20", "SYS", "envoi", "AL-03 : formalité\nnon déposée"),
    ("X1", "SYS", "finflux", ""),
    ("E6", "COR", "action", "Valider le dossier"),
    ("E7", "COR", "envoi", "Déposer auprès\nde l'autorité"),
    ("E8", "SYS", "action", "Enregistrer le dépôt,\ncalculer l'échéance"),
    ("E9", "AUT", "action", "Instruire le dossier"),
    ("E10", "AUT", "decision", ""),
    ("E11", "COR", "action", "Répondre aux\nobservations"),
    ("E13", "COR", "action", "Régulariser\nle dossier"),
    ("E12", "COR", "reception", "Enregistrer récépissé\nou décision"),
    ("T2", "SYS", "temps", "Échéance d'instruction\natteinte"),
    ("E14", "SYS", "decision", ""),
    ("E15", "SYS", "action", "Passer en\nAcceptation tacite"),
    ("E16", "SYS", "envoi", "AL-04 : dossier\nsans suite (+15 j)"),
    ("E16R", "COR", "action", "Relancer l'autorité"),
    ("ME", "SYS", "decision", ""),
    ("E17", "SYS", "decision", ""),
    ("T3", "SYS", "temps", "J-60 puis J-15\navant expiration"),
    ("E18", "SYS", "envoi", "AL-12 : décision\nà renouveler"),
    ("E19", "COR", "action", "Préparer le\nrenouvellement"),

    # 5 · Pilotage continu
    ("MF", "SYS", "decision", ""),
    ("P1", "SYS", "action", "Mettre à jour l'indice\net le tableau de bord"),
    ("P7", "COR", "decision", ""),
    ("ARCH", "COR", "action", "Archiver la fiche"),
    ("FIN", "COR", "fin", ""),
    ("P8", "SYS", "action", "Attendre un événement\nde révision"),
    ("T4", "SYS", "temps", "Échéance de revue\n(AL-08)"),
    ("R1", "SYS", "reception", "Nouvelle version\ndu référentiel (AL-09)"),
    ("MOD", "CON", "action", "Modifier substantiellement\nla fiche publiée"),
    ("MP", "SYS", "decision", ""),
    ("P4", "SYS", "action", "Passer la fiche\n« À réviser »"),
    ("P5", "SYS", "decision", ""),
    ("P6", "SYS", "envoi", "AL-13 : nouvelle\ndéclaration requise"),

    # 6 · Violation de données
    ("G0", "CON", "reception", "Incident constaté"),
    ("G1", "CON", "action", "Déclarer la violation\n(y compris sur mobile)"),
    ("G2", "SYS", "action", "Fixer l'échéance\nà 72 heures"),
    ("FG", "SYS", "fourche", ""),
    ("G2A", "SYS", "envoi", "AL-01 au\ncorrespondant"),
    ("T5", "SYS", "temps", "25, 50, 75 et 90 %\ndu délai"),
    ("G2B", "SYS", "envoi", "Rappels tant que\nnon notifiée"),
    ("X2", "SYS", "finflux", ""),
    ("G3", "COR", "decision", ""),
    ("G4", "COR", "action", "Consigner au\nregistre interne"),
    ("G5", "COR", "decision", ""),
    ("G6", "COR", "envoi", "Notifier l'autorité\n(E05)"),
    ("FG2", "COR", "fourche", ""),
    ("G6B", "COR", "envoi", "Notifier l'autorité"),
    ("G7", "COR", "envoi", "Informer les personnes\nconcernées"),
    ("JG", "COR", "fourche", ""),
    ("GA", "AUT", "reception", "Recevoir la\nnotification"),
    ("MG", "COR", "decision", ""),
    ("G9", "COR", "action", "Mettre en œuvre les\nmesures correctives"),
    ("G10", "COR", "action", "Clore la violation"),
    ("G11", "SYS", "action", "Mettre à jour l'indice\n(traitement des violations)"),
    ("FIN2", "SYS", "fin", ""),
]

# (source, cible, garde ou libellé, style) ; style « signal » = flot d'objet ou de signal (pointillé)
FLOTS = [
    ("S0", "A1", "", ""), ("A1", "A1E", "", ""), ("A1E", "A1C", "", ""), ("A1C", "A2", "", ""),
    ("A2", "A3", "", ""), ("A3", "F0", "", ""),
    ("F0", "A4", "", ""), ("F0", "A5", "", ""),
    ("A5", "A6", "recours à un cabinet", ""), ("A5", "MA", "sans cabinet", ""),
    ("A6", "A7", "", ""), ("A7", "A8", "mandat accepté (2FA)", ""), ("A7", "MA", "refusé", ""),
    ("A8", "MA", "", ""), ("A4", "J0", "", ""), ("MA", "J0", "", ""), ("J0", "B1", "", ""),

    ("B1", "B2", "diagnostic", ""), ("B1", "B3", "import", ""), ("B1", "B4", "modèle", ""), ("B1", "B5", "trame", ""),
    ("B2", "MB", "", ""), ("B3", "MB", "", ""), ("B4", "MB", "", ""), ("B5", "MB", "", ""),
    ("MB", "B6", "", ""), ("B6", "B7", "", ""), ("B7", "B8", "à chaque saisie", ""), ("B8", "B9", "", ""),
    ("B9", "B10", "", ""), ("B10", "B11", "incomplète", ""), ("B11", "B7", "", ""),
    ("B10", "B12", "complète", ""), ("B12", "C1", "", ""),

    ("C1", "C2", "", ""), ("C2", "C6", "", ""),
    ("C6", "C7", "à compléter", ""), ("C7", "B7", "", ""),
    ("C6", "C3", "complète", ""),
    ("C3", "MC", "régime du moteur retenu", ""), ("C3", "C4", "autre régime", ""),
    ("C4", "C5", "", ""), ("C5", "MC", "", ""), ("MC", "C8", "", ""),
    ("C8", "C9", "", ""), ("C9", "D1", "AIPD requise", ""), ("C9", "MC2", "non requise", ""),
    ("MC2", "C10", "", ""), ("C10", "C11", "visa activé", ""), ("C10", "MC3", "visa désactivé", ""),
    ("C11", "MC3", "", ""), ("MC3", "C12", "", ""), ("C12", "C13", "", ""), ("C13", "F2", "", ""),
    ("F2", "E1", "", ""), ("F2", "F5P", "", ""), ("F5P", "MF", "", ""),

    ("D1", "D2", "", ""), ("D2", "FD", "", ""), ("FD", "D3A", "", ""), ("FD", "D3B", "", ""),
    ("D3A", "JD", "", ""), ("D3B", "JD", "", ""), ("JD", "D4", "", ""), ("D4", "D5", "", ""),
    ("D5", "D6", "", ""), ("D6", "D3B", "renvoi", ""), ("D6", "D7", "validée", ""),
    ("D7", "D8", "", ""), ("D8", "D9", "risque résiduel élevé\n(Bénin, art. 429)", ""), ("D8", "MC2", "sinon", ""),
    ("D9", "MC2", "", ""),

    ("E1", "E2", "dispense ou exclusion", ""), ("E1", "E3", "formalité due", ""),
    ("E2", "MF", "", ""),
    ("E3", "E4", "", ""), ("E4", "E5", "", ""), ("E5", "E6", "", ""),
    ("E3", "T1", "", "signal"), ("T1", "E20", "", ""), ("E20", "X1", "", ""),
    ("E6", "E7", "", ""), ("E7", "E8", "", ""), ("E8", "E9", "", ""), ("E9", "E10", "", ""),
    ("E10", "E11", "observations", ""), ("E11", "E9", "", ""),
    ("E10", "E13", "rejet", ""), ("E13", "E5", "", ""),
    ("E10", "E12", "acceptation", ""), ("E12", "ME", "", ""),
    ("E10", "T2", "pas de réponse", ""), ("T2", "E14", "", ""),
    ("E14", "E15", "silence vaut acceptation\n(Bénin)", ""), ("E15", "ME", "", ""),
    ("E14", "E16", "sans effet (Togo)", ""), ("E16", "E16R", "", ""), ("E16R", "E9", "", ""),
    ("ME", "E17", "", ""),
    ("E17", "T3", "validité limitée\n(Bénin : 2 ans)", ""), ("T3", "E18", "", ""), ("E18", "E19", "", ""), ("E19", "E3", "", ""),
    ("E17", "MF", "sans limite", ""),

    ("MF", "P1", "", ""), ("P1", "P7", "", ""),
    ("P7", "ARCH", "traitement abandonné", ""), ("ARCH", "FIN", "", ""),
    ("P7", "P8", "toujours en œuvre", ""),
    ("P8", "T4", "", ""), ("P8", "R1", "", ""), ("P8", "MOD", "", ""),
    ("T4", "MP", "", ""), ("R1", "MP", "", ""), ("MOD", "MP", "", ""), ("MP", "P4", "", ""),
    ("P4", "P5", "", ""),
    ("P5", "P6", "déjà déclarée et\nmodification substantielle", ""), ("P6", "E3", "", ""),
    ("P5", "B9", "sinon : resoumettre", ""),

    ("G0", "G1", "", ""), ("G1", "G2", "", ""), ("G2", "FG", "", ""),
    ("FG", "G2A", "", ""), ("FG", "T5", "", ""), ("FG", "G3", "", ""),
    ("T5", "G2B", "", ""), ("G2B", "X2", "", ""),
    ("G2A", "G3", "", "signal"),
    ("G3", "G4", "V1 : aucun risque", ""), ("G3", "G5", "V1 : risque", ""),
    ("G5", "G6", "V2 : risque non élevé", ""), ("G5", "FG2", "V2 : risque élevé", ""),
    ("FG2", "G6B", "", ""), ("FG2", "G7", "", ""), ("G6B", "JG", "", ""), ("G7", "JG", "", ""),
    ("G6", "GA", "", "signal"), ("G6B", "GA", "", "signal"),
    ("G4", "MG", "", ""), ("G6", "MG", "", ""), ("JG", "MG", "", ""),
    ("MG", "G9", "", ""), ("G9", "G10", "", ""), ("G10", "G11", "", ""), ("G11", "FIN2", "", ""),
]


def phase_de(identifiant: str) -> str:
    """Phase à laquelle appartient un nœud (sert au découpage en un diagramme par phase)."""
    explicites = {
        "S0": "PH0", "MA": "PH0", "J0": "PH0", "F0": "PH0",
        "MB": "PH1",
        "MC": "PH2", "MC2": "PH2", "MC3": "PH2", "F2": "PH2", "F5P": "PH2",
        "FD": "PH3", "JD": "PH3",
        "T1": "PH4", "T2": "PH4", "T3": "PH4", "X1": "PH4", "ME": "PH4",
        "MF": "PH5", "ARCH": "PH5", "FIN": "PH5", "T4": "PH5", "R1": "PH5", "MOD": "PH5", "MP": "PH5",
        "FG": "PH6", "FG2": "PH6", "JG": "PH6", "MG": "PH6", "T5": "PH6", "X2": "PH6", "FIN2": "PH6",
    }
    if identifiant in explicites:
        return explicites[identifiant]
    return {"A": "PH0", "B": "PH1", "C": "PH2", "D": "PH3", "E": "PH4", "P": "PH5", "G": "PH6"}[identifiant[0]]
