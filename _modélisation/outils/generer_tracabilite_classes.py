"""Génère « Traçabilité du diagramme de classes » : pour chaque classe et chaque champ, le
fichier AMELEGAL d'où il vient.

Usage : python3 _modélisation/outils/generer_tracabilite_classes.py

Les références sont relevées dans les explications (dossier explications/), qui citent leurs
sources (G04, C08, AL-03, t.volume_personnes, TG-Q6…). Chaque référence est rattachée au fichier
du dépôt qui la contient. Une classe sans aucune référence est un choix de conception, signalé
comme tel. Le script échoue si une référence ne correspond à aucun fichier du dépôt.
"""
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

OUTILS = Path(__file__).resolve().parent
DOSSIER = OUTILS.parent
DEPOT = DOSSIER.parent
sys.path.insert(0, str(OUTILS))

import generer_classes_complet as g  # noqa: E402
import generer_explication_classes as e  # noqa: E402

SORTIE_MD = DOSSIER / "13-tracabilite-classes.md"
SORTIE_PDF = DOSSIER / "Waɖɛ_Tracabilite_diagramme_de_classes.pdf"
COMMUN = "00 Commun aux deux pays/02 Livrables communs"
SPEC = f"{COMMUN}/_spécifications développeur"

# Référence → (libellé, fichiers). Les livrables C, D, E, F02, F03, I01 existent dans chaque pays.
FICHIERS_FIXES = {
    "CSV": ("Champs du registre", [f"{SPEC}/registre-champs.csv"]),
    "ALERTES": ("Types d'alerte AL-01 à AL-13", [f"{SPEC}/alertes.json"]),
    "BULLES": ("Bulles d'information", [f"{SPEC}/bulles-information.json"]),
    "NOTICE": ("Notice d'implémentation du référentiel", [f"{SPEC}/00 Notice d_implémentation du référentiel.docx"]),
    "JSON": ("Référentiels machine", ["01 Togo/01 Livrables Togo/_spécifications développeur/referentiel-togo.json",
                                     "02 Bénin/01 Livrables Bénin/_spécifications développeur/referentiel-benin.json"]),
    "RECETTE": ("Cas de recette du moteur", ["01 Togo/01 Livrables Togo/_spécifications développeur/cas-de-recette-togo.csv",
                                            "02 Bénin/01 Livrables Bénin/_spécifications développeur/cas-de-recette-benin.csv"]),
    "LOI_TG": ("Loi togolaise n° 2019-014", ["01 Togo/00 Sources et référentiels/Textes/Loi n° 2019-014 du 29 octobre 2019 - JO 64e année n° 26 ter.pdf"]),
    "LOI_BJ": ("Loi béninoise n° 2017-20, Livre cinquième", ["02 Bénin/00 Sources et référentiels/Textes/Benin-Loi-2017-20-Portant-code-du-numerique-en-Republique-du-Benin.pdf"]),
    "FORMULAIRE_BJ": ("Formulaire unique de l'APDP et annexes", ["02 Bénin/00 Sources et référentiels/Formulaires et modèles de l_autorité/FORMULAIRE-UNIQUE.pdf"]),
    "CDC": ("Cahier des charges (absent du dépôt)", []),
}


def fichiers_livrable(code):
    motif = f"{code} - *"
    trouves = sorted(str(p.relative_to(DEPOT)) for p in DEPOT.glob(f"0[012]*/**/{motif}"))
    return trouves


def references(texte):
    """Rend l'ensemble des références citées dans un texte d'explication."""
    refs = set()
    for code in re.findall(r"\b([CDEFGHIK]0\d|C1[0-5])\b", texte):
        refs.add(code)
    if re.search(r"\bAL-\d\d\b|alerte", texte, re.I):
        refs.add("ALERTES") if re.search(r"\bAL-\d\d\b", texte) else None
    if re.search(r"\b(org|t|aipd|bloc\d)\.[a-z_]+", texte) or re.search(r"\bCSV\b|registre-champs|[Rr]ubrique \d", texte):
        refs.add("CSV")
    if re.search(r"\b(TG|BJ)-(Q\d|AIPD|[A-Z]{3,})", texte) or re.search(r"référentiel JSON|\bJSON\b|logigramme|condition bloquante", texte, re.I):
        refs.add("JSON")
    if re.search(r"cas de recette|CAS-(TG|BJ)", texte, re.I):
        refs.add("RECETTE")
    if re.search(r"\bnotice\b", texte, re.I):
        refs.add("NOTICE")
    if re.search(r"\bbulle", texte, re.I):
        refs.add("BULLES")
    if re.search(r"\bart\. ?(4\d\d|3[89]\d)\b|Bénin.{0,40}art\.|silence vaut", texte):
        refs.add("LOI_BJ")
    if re.search(r"\bart\. ?([1-9]|[1-8]\d|9[0-7])\b(?! ?du cahier)", texte) and "Togo" in texte:
        refs.add("LOI_TG")
    if re.search(r"formulaire unique|annexe [1-4]", texte, re.I):
        refs.add("FORMULAIRE_BJ")
    if re.search(r"cahier des charges", texte, re.I):
        refs.add("CDC")
    return refs


def libelle_ref(ref):
    if ref in FICHIERS_FIXES:
        return FICHIERS_FIXES[ref]
    fichiers = fichiers_livrable(ref)
    if not fichiers:
        return (f"{ref} (absent du dépôt)", [])
    nom = Path(fichiers[0]).stem
    return (nom, fichiers)


ORDRE_REF = ["G01", "G02", "G03", "G04", "G05", "G06", "G07"]


def cle_tri(ref):
    return (0 if re.match(r"^[A-K]\d\d$", ref) else 1, ref)


# Source principale de chaque classe : le livrable d'où elle est tirée. Complète les références
# relevées automatiquement dans les explications. Une classe absente de cette table fait échouer
# la génération : toute nouvelle classe doit recevoir sa source.
SOURCE_PRINCIPALE = {
    # Accès
    "Utilisateur": ["G04", "H01"], "Organisation": ["C12", "CSV", "G04"], "ServiceDirection": ["G04", "G05"],
    "MembreOrganisation": ["G04"], "RoleOrganisation": ["G04"], "ResponsableTraitementLegal": ["C12", "CSV"],
    "DesignationCorrespondant": ["C10", "CSV"], "Cabinet": ["H05", "G04"], "MembreCabinet": ["G04"],
    "RoleCabinet": ["G04"], "Mandat": ["G05"], "NiveauMandat": ["G05", "G04"], "ActionReservable": ["G05"],
    "AffectationConsultant": ["G04", "G05"], "StatutMandat": ["G03", "G05"], "PorteeMandat": ["G05"],
    "StatutCorrespondant": ["C10", "CSV"],
    # Référentiels
    "Juridiction": ["C01", "NOTICE"], "ReferentielVersion": ["C15", "NOTICE"], "StatutReferentiel": ["C15", "G03"],
    "Referentiel": ["JSON", "NOTICE"], "Regime": ["C05", "JSON"], "Logigramme": ["C06", "JSON"],
    "Question": ["C06", "JSON"], "Branche": ["C06", "JSON"], "TypeBranche": ["C06", "JSON"],
    "ConditionBloquante": ["C06", "JSON"], "RegleTransverse": ["NOTICE", "JSON"], "EtapeFeuilleDeRoute": ["C07"],
    "ParametresAutorite": ["C03"], "DelaiInstruction": ["C03", "C05"], "ConfigAipd": ["C08"],
    "CritereAipd": ["C08", "JSON"], "ConfigViolation": ["C09"], "NoeudViolation": ["C09", "JSON"],
    "ConfigIndice": ["C13", "G01"], "DefinitionChamp": ["CSV", "C12"], "ExigenceChamp": ["CSV"], "Exigence": ["CSV"],
    "BulleInformation": ["D01", "D02", "D03", "BULLES"], "TypeQuestion": ["C06", "JSON"], "NiveauChamp": ["CSV"],
    "TypeChamp": ["CSV"], "Sources": ["C02"], "ArticleCle": ["C02"], "ModaliteDepot": ["C03"],
    "EcartTextePratique": ["C02", "JSON"], "ConfigCorrespondant": ["C10"], "ConfigTransferts": ["C11"],
    "ConsultationPrealable": ["C08", "LOI_BJ"], "SectionGrille": ["F03"], "BrancheViolation": ["C09", "JSON"],
    "ComposanteIndice": ["C13", "G01"], "SeuilIndice": ["C13", "G01"],
    # Moteur
    "ResultatQualification": ["C06", "D05", "NOTICE"], "MoteurQualification": ["NOTICE", "JSON", "I01", "RECETTE"],
    # Registre
    "FicheTraitement": ["C12", "E01", "CSV", "G03"], "StatutFiche": ["G03"], "VersionFichePubliee": ["G04", "G03"],
    "Qualification": ["C06", "NOTICE"], "VoieQualification": ["NOTICE"], "EtapeChemin": ["C06", "JSON"],
    "Prestataire": ["C14", "CSV"], "SousTraitanceFiche": ["C14", "CSV"], "TransfertFiche": ["C11", "CSV"],
    "PieceJointe": ["CSV", "E03"],
    # Formalités
    "DossierFormalite": ["E03", "C07", "G03"], "TypeDossier": ["C05", "E03"], "StatutDossier": ["G03"],
    "JalonDossier": ["G03", "C03"], "DocumentProduit": ["E01", "E02", "E03", "E04", "E05", "E06", "E07"],
    # AIPD
    "AnalyseImpact": ["C08", "F03", "E04"], "SectionAipd": ["F03"], "RisqueAipd": ["F03"],
    "InvitationAipd": ["F03", "G04"], "StatutAipd": ["G03"],
    # Violations
    "Violation": ["C09", "E05"], "NatureViolation": ["C09", "E05"], "StatutViolation": ["G03"],
    # Pilotage
    "DefinitionAlerte": ["G02", "ALERTES"], "OccurrenceAlerte": ["G02", "ALERTES"], "Tache": ["G02", "C07", "G03"],
    "StatutTache": ["G03"], "Notification": ["G02"], "Parametre": ["G07"], "PorteeParametre": ["G07"],
    "InstantaneIndice": ["G01", "C13"], "EntreeJournal": ["E07", "G05"], "CanalAlerte": ["G02", "ALERTES"],
    "OrigineTache": ["G02", "C07", "NOTICE"],
}

NOMS_COURTS = {"CSV": "registre-champs.csv", "JSON": "référentiels JSON", "ALERTES": "alertes.json",
               "BULLES": "bulles-information.json", "NOTICE": "Notice d'implémentation", "RECETTE": "cas de recette",
               "LOI_TG": "loi TG 2019-014", "LOI_BJ": "loi BJ 2017-20", "FORMULAIRE_BJ": "formulaire unique APDP",
               "CDC": "cahier des charges"}


def court(refs):
    return ", ".join(NOMS_COURTS.get(r, r) for r in sorted(refs, key=cle_tri))


def construire():
    modules, relations = e.charger_modele()
    enumerations = {n for cls in modules.values() for n, c in cls.items() if c and c[0] == "<<enumeration>>"}
    absentes = set()
    lignes = [
        "# 13. Traçabilité du diagramme de classes",
        "",
        "Pour chaque classe du diagramme, ce document indique **le fichier AMELEGAL d'où elle vient**,",
        "puis, champ par champ, la source citée. Il est **généré** par `outils/generer_tracabilite_classes.py`",
        "à partir des explications du diagramme (`explications/`), qui citent leurs sources.",
        "",
        "## 1. Les fichiers du diagramme de classes",
        "",
        "| Fichier | Ce qu'il contient |",
        "|---|---|",
        "| `02-diagrammes-de-classes.md` | **Source unique du modèle** : les classes par paquet (2.1 à 2.6), en Mermaid. Toute modification se fait ici. |",
        "| `09-diagramme-classes-complet.md` | Les 90 classes sur une seule vue, générée depuis le fichier 02. |",
        "| `planches/Waɖɛ_Diagramme_de_classes_complet.pdf` / `.svg` / `.png` / `.dot` | La vue complète en grand format (Graphviz), à zoomer. |",
        "| `Waɖɛ_Diagramme_de_classes_explique.pdf` | Chaque classe, champ et relation expliqué, avec la raison de sa présence. |",
        "| `Waɖɛ_Modélisation.drawio` (page 1) | Le diagramme de classes modifiable dans draw.io. |",
        "| `Waɖɛ_Modélisation.pdf` | Le dossier de modélisation complet, dont le chapitre 2. |",
        "| `07-modele-physique-donnees.md` | La traduction des classes en tables PostgreSQL. |",
        "| `explications/acces.py`, `referentiels.py`, `metier.py` | Les explications des classes et des champs. |",
        "| `explications/relations.py` | Les explications des relations. |",
        "| `outils/generer_classes_complet.py`, `generer_explication_classes.py`, `generer_tracabilite_classes.py` | Les générateurs. |",
        "| `13-tracabilite-classes.md` / `Waɖɛ_Tracabilite_diagramme_de_classes.pdf` | Le présent document. |",
        "",
    ]

    par_classe = {}
    index = defaultdict(list)
    for module in g.ORDRE_MODULES:
        for nom, corps in modules[module].items():
            ex = e.EXPLICATIONS[nom]
            if nom not in SOURCE_PRINCIPALE:
                raise SystemExit(f"Classe sans source principale : {nom}")
            principale = set(SOURCE_PRINCIPALE[nom])
            refs_classe = references(ex.get("role", ""))
            champs = []
            for cle, texte in {**ex.get("champs", {}), **ex.get("valeurs", {})}.items():
                r = references(texte)
                champs.append((cle, r, texte))
                refs_classe |= r
            for r in list(relations):
                if re.match(rf"^{nom}\b|.*\b{nom}(\s*:|$)", r) and r in e.RELATIONS:
                    refs_classe |= references(e.RELATIONS[r])
            refs_classe -= principale
            par_classe[nom] = (module, principale, refs_classe, champs)
            for ref in principale | refs_classe:
                index[ref].append(nom)

    # 2. Vue d'ensemble : une ligne par classe
    lignes += ["## 2. Vue d'ensemble : la source de chaque classe", "",
               "| Module | Classe | Source principale | Autres sources citées |", "|---|---|---|---|"]
    for module in g.ORDRE_MODULES:
        for nom in modules[module]:
            _, principale, citees, _ = par_classe[nom]
            lignes.append(f"| {g.LIBELLE_MODULE[module].split(' :')[0]} | {nom} | {court(principale)} | {court(citees)} |")
    lignes.append("")

    # 3. Index par fichier source
    lignes += ["## 3. Index : quel fichier AMELEGAL alimente quelles classes", "",
               "| Source | Fichier(s) dans le dépôt | Classes concernées |", "|---|---|---|"]
    for ref in sorted(index, key=cle_tri):
        libelle, fichiers = libelle_ref(ref)
        if not fichiers:
            absentes.add(ref)
        chemins = "<br>".join(f"`{f}`" for f in fichiers) or "*absent du dépôt*"
        titre = ref if ref not in FICHIERS_FIXES else libelle
        if ref not in FICHIERS_FIXES:
            titre = f"**{ref}** {libelle.split(' - ', 1)[-1]}" if fichiers else f"**{ref}**"
        lignes.append(f"| {titre} | {chemins} | {', '.join(sorted(set(index[ref])))} |")
    sans = [n for n in SOURCE_PRINCIPALE if n not in par_classe]
    if sans:
        raise SystemExit(f"Source donnée pour une classe absente du modèle : {sans}")
    lignes.append("")

    # 3. Détail par classe
    lignes += ["## 4. Détail par classe et par champ", "",
               "Pour chaque classe : la source principale, puis les champs et valeurs qui citent une source. "
               "Un champ absent du tableau est technique (identifiant, date de création…) ou découle de la classe.", ""]
    for module in g.ORDRE_MODULES:
        lignes += [f"### {g.LIBELLE_MODULE[module]}", ""]
        for nom in modules[module]:
            _, principale, citees, champs = par_classe[nom]
            genre = "énumération" if nom in enumerations else "classe"
            lignes += [f"#### {nom} ({genre})", "", f"**Source principale :** {court(principale)}"]
            if citees:
                lignes.append(f"<br>**Sources citées par ses champs :** {court(citees)}")
            lignes.append("")
            avec = [(c, r, t) for c, r, t in champs if r]
            if avec:
                lignes += ["| Champ | Source | Explication du champ |", "|---|---|---|"]
                for c, r, t in avec:
                    src = court(r)
                    lignes.append(f"| `{c}` | {src} | {t.replace('|', '/')} |")
                lignes.append("")

    lignes += ["## 5. Légende des sources", "",
               "| Code | Fichier |", "|---|---|"]
    for ref in sorted(index, key=cle_tri):
        libelle, fichiers = libelle_ref(ref)
        lignes.append(f"| {ref} | {libelle}{' — ' + fichiers[0] if fichiers else ''} |")
    SORTIE_MD.write_text("\n".join(lignes) + "\n", encoding="utf-8")
    print(f"{len(par_classe)} classes, références absentes : {sorted(absentes)}")
    return SORTIE_MD


def pdf():
    css = OUTILS / "vendor" / "tracabilite.css"
    css.write_text("""body{font-family:Arial,sans-serif;font-size:8.8pt;line-height:1.4;color:#1d2b22}
h1{color:#00370B;font-size:18pt;border-bottom:2px solid #00370B}h2{color:#00370B;font-size:14pt;page-break-before:always}
h2:first-of-type{page-break-before:avoid}h3{background:#00370B;color:#fff;padding:4px 8px;font-size:11pt;margin-top:20px}
h4{color:#00370B;font-size:10pt;margin:14px 0 3px;border-left:4px solid #c9a227;padding-left:6px;page-break-after:avoid}
table{border-collapse:collapse;width:100%;margin:4px 0 8px}td,th{border:1px solid #b9c8bd;padding:3px 5px;vertical-align:top}
th{background:#e4ece6;text-align:left}code{font-size:7.8pt;background:#eef3ef}tr{page-break-inside:avoid}""", encoding="utf-8")
    html = OUTILS / "vendor" / "tracabilite.html"
    subprocess.run(["pandoc", str(SORTIE_MD), "-f", "gfm", "-t", "html5", "-s", "--metadata",
                    "title=Traçabilité du diagramme de classes", "--css", str(css), "--embed-resources", "-o", str(html)], check=True)
    subprocess.run(["node", str(OUTILS / "html_vers_pdf.js"), str(html), str(SORTIE_PDF),
                    "Waɖɛ — Traçabilité du diagramme de classes"], check=True)


if __name__ == "__main__":
    construire()
    pdf()
