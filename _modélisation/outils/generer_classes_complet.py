"""Assemble le diagramme de classes complet à partir de 02-diagrammes-de-classes.md.

Usage : python3 _modélisation/outils/generer_classes_complet.py

Les diagrammes par module (02) restent la source unique : ce script les fusionne en une
seule planche, range chaque classe dans l'espace de noms de son module et ajoute les
associations entre modules. Écrit 09-diagramme-classes-complet.md.
"""
import html
import re
import subprocess
from pathlib import Path

DOSSIER = Path(__file__).resolve().parents[1]
SOURCE = DOSSIER / "02-diagrammes-de-classes.md"
SORTIE = DOSSIER / "09-diagramme-classes-complet.md"
PLANCHES = DOSSIER / "planches"
NOM_PLANCHE = "Waɖɛ_Diagramme_de_classes_complet"

LIBELLE_MODULE = {
    "Acces": "Accès : organisations, cabinets, utilisateurs, mandats",
    "Formulaires": "Formulaires configurables : types et champs créés dans l'application",
    "Referentiels": "Référentiels de juridiction",
    "Moteur": "Moteur de qualification",
    "Registre": "Registre et qualification",
    "Formalites": "Formalités",
    "Aipd": "Analyses d'impact",
    "Violations": "Violations de données",
    "Pilotage": "Pilotage : tâches, alertes, paramètres, indice, journal",
}
COULEUR_MODULE = {
    "Acces": "#F3ECFA", "Formulaires": "#E3F4F4", "Referentiels": "#EAF5EC", "Moteur": "#FFF9E0", "Registre": "#E6F0FB",
    "Formalites": "#FDF1E1", "Aipd": "#FBE9EC", "Violations": "#FDE8E0", "Pilotage": "#EEF0EF",
}

# Module (espace de noms) de chaque section de 02.
MODULE_PAR_SECTION = {
    "2.1": "Acces",
    "2.2": "Referentiels",
    "2.3": "Registre",
    "2.5": "Pilotage",
    "2.7": "Formulaires",
}
# Sections dont les classes se répartissent entre plusieurs modules.
MODULE_PAR_CLASSE = {
    # 2.4
    "DossierFormalite": "Formalites", "TypeDossier": "Formalites", "StatutDossier": "Formalites",
    "JalonDossier": "Formalites", "DocumentProduit": "Formalites",
    "AnalyseImpact": "Aipd", "SectionAipd": "Aipd", "RisqueAipd": "Aipd",
    "InvitationAipd": "Aipd", "StatutAipd": "Aipd",
    "Violation": "Violations", "NatureViolation": "Violations", "StatutViolation": "Violations",
    # 2.6
    "StatutMandat": "Acces", "PorteeMandat": "Acces", "StatutCorrespondant": "Acces",
    "TypeQuestion": "Referentiels",
    "Sources": "Referentiels", "ArticleCle": "Referentiels", "ModaliteDepot": "Referentiels",
    "EcartTextePratique": "Referentiels", "ConfigCorrespondant": "Referentiels",
    "ConfigTransferts": "Referentiels", "ConsultationPrealable": "Referentiels",
    "SectionGrille": "Referentiels", "BrancheViolation": "Referentiels",
    "ComposanteIndice": "Referentiels", "SeuilIndice": "Referentiels",
    "ResultatQualification": "Moteur", "MoteurQualification": "Moteur",
    "CanalAlerte": "Pilotage", "OrigineTache": "Pilotage",
}
ORDRE_MODULES = ["Acces", "Formulaires", "Referentiels", "Moteur", "Registre", "Formalites", "Aipd", "Violations", "Pilotage"]

# Associations entre modules, absentes des diagrammes par module.
LIENS_INTER_MODULES = """
    Organisation "1" -- "*" FicheTraitement : tient le registre
    ServiceDirection "0..1" -- "*" FicheTraitement : rattachée à
    Juridiction "1..*" -- "*" FicheTraitement : relève de
    Organisation "1" -- "*" Prestataire
    Organisation "1" -- "*" PieceJointe
    Organisation "1" -- "*" Violation : subit
    Juridiction "1" -- "*" Violation
    Organisation "1" -- "*" Tache
    Organisation "1" -- "*" OccurrenceAlerte
    Organisation "1" -- "*" InstantaneIndice
    Organisation "1" -- "*" EntreeJournal : une chaîne par organisation
    Utilisateur "1" -- "*" EntreeJournal : acteur
    Mandat "0..1" -- "*" EntreeJournal : au titre de
    Mandat "0..1" -- "*" Qualification : au titre de
    Utilisateur "1" -- "*" Qualification : auteur
    Utilisateur "0..1" -- "*" Tache : assignée à
    Utilisateur "1" -- "*" Notification : destinataire
    Utilisateur "1" -- "*" InvitationAipd
    Qualification ..> Regime : régime moteur et régime retenu
    FicheTraitement "*" --> "1" VersionFormulaire : saisie avec
    Organisation "*" --> "1" VersionFormulaire : saisie avec
    Formulaire "*" -- "0..1" Organisation : champs propres (portée Organisation)
    CritereAipd ..> DefinitionChamp : Champ
    UsageChamp ..> Question : consommateur
    ControleurPublication ..> ReferentielVersion : croise
    ValeurListe ..> BulleInformation : AideCode
    DocumentProduit ..> DefinitionChamp : champs exportés
    Qualification ..> ResultatQualification : enregistre
    DossierFormalite ..> Regime : régime du dossier
    DossierFormalite ..> ParametresAutorite : délais, silence, validité
    DocumentProduit "*" --> "1" ReferentielVersion : terminologie figée
    DocumentProduit "1" --> "1" PieceJointe : fichier
    JalonDossier "0..1" --> "0..1" PieceJointe
    DesignationCorrespondant "0..1" --> "0..1" PieceJointe : justificatif
    SousTraitanceFiche "0..1" --> "0..1" PieceJointe : contrat
    AnalyseImpact ..> ConfigAipd : critères et grille
    Violation ..> ConfigViolation : délai et arbre
    InstantaneIndice ..> ConfigIndice : poids et seuils
    Parametre ..> Juridiction : cible
    Parametre ..> Organisation : cible
    OccurrenceAlerte ..> FicheTraitement : objet
    OccurrenceAlerte ..> DossierFormalite : objet
    OccurrenceAlerte ..> Violation : objet
    OccurrenceAlerte ..> Mandat : objet
""".strip("\n").split("\n")


def blocs_par_section(md: str):
    """Rend (numéro de section, contenu du bloc classDiagram) pour chaque section 2.x."""
    for section in re.split(r"^## ", md, flags=re.M)[1:]:
        numero = section.split(" ", 1)[0]
        m = re.search(r"```mermaid\n(classDiagram.*?)```", section, flags=re.S)
        if m:
            yield numero, m.group(1)


def decouper(bloc: str):
    """Sépare les définitions de classes (avec corps) des relations."""
    classes, relations = {}, []
    lignes = bloc.split("\n")
    i = 0
    while i < len(lignes):
        ligne = lignes[i].strip()
        m = re.match(r"class (\w+) \{$", ligne)
        if m:
            corps = []
            i += 1
            while lignes[i].strip() != "}":
                corps.append(lignes[i].strip())
                i += 1
            classes[m.group(1)] = corps
        elif ligne and not ligne.startswith(("classDiagram", "direction")):
            relations.append(ligne)
        i += 1
    return classes, relations


def noeud_dot(nom: str, corps: list[str]) -> str:
    """Nœud UML : nom (et stéréotype), attributs, méthodes."""
    stereo = next((c for c in corps if c.startswith("<<")), None)
    membres = [c for c in corps if not c.startswith("<<")]
    attributs = [m for m in membres if "(" not in m]
    methodes = [m for m in membres if "(" in m]
    def texte(m: str) -> str:
        # Mermaid note les génériques List~T~ : on les rend en List<T>, de l'intérieur vers l'extérieur.
        precedent = None
        while precedent != m:
            precedent = m
            m = re.sub(r"(\w+)~([^~]*)~(?!\w)", r"\1<\2>", m)
        return html.escape(m)
    entete = f'<FONT POINT-SIZE="9">{html.escape(stereo)}</FONT><BR/>' if stereo else ""
    fond = "#00370B" if not stereo else ("#5b6b5f" if "enumeration" in stereo else "#B7791F")
    lignes = [f'<TR><TD BGCOLOR="{fond}"><FONT COLOR="white">{entete}<B>{nom}</B></FONT></TD></TR>']
    def bloc(items):
        if not items:
            return '<TR><TD></TD></TR>'
        contenu = "".join(f'{texte(i)}<BR ALIGN="LEFT"/>' for i in items)
        return f'<TR><TD ALIGN="LEFT" BALIGN="LEFT">{contenu}</TD></TR>'
    lignes.append(bloc(attributs))
    if methodes:
        lignes.append(bloc(methodes))
    table = f'<TABLE BORDER="0" CELLBORDER="1" CELLSPACING="0" CELLPADDING="4" BGCOLOR="white">{"".join(lignes)}</TABLE>'
    return f'    {nom} [label=<{table}>];'


MOTIF_RELATION = re.compile(
    r'^(\w+)\s*(?:"([^"]*)")?\s*(\*--|o--|-->|\.\.>|--)\s*(?:"([^"]*)")?\s*(\w+)\s*(?::\s*(.*))?$'
)


def arete_dot(relation: str, enumerations: set[str]) -> str:
    m = MOTIF_RELATION.match(relation)
    if not m:
        raise SystemExit(f"Relation non comprise : {relation}")
    a, mult_a, type_rel, mult_b, b, libelle = m.groups()
    attrs = {
        "*--": 'dir=back, arrowtail=diamond',
        "o--": 'dir=back, arrowtail=odiamond',
        "--": 'dir=none',
        "-->": 'arrowhead=vee',
        "..>": 'style=dashed, arrowhead=vee',
    }[type_rel]
    extra = []
    if mult_a:
        extra.append(f'taillabel="{mult_a}"')
    if mult_b:
        extra.append(f'headlabel="{mult_b}"')
    if libelle:
        extra.append(f'label="{libelle}"')
    if b in enumerations or a in enumerations:
        extra.append('color="#9aa59d", constraint=true')
    return f'    {a} -> {b} [{", ".join([attrs] + extra)}];'


def ecrire_planche(modules: dict, relations: list[str]) -> None:
    enumerations = {n for cls in modules.values() for n, corps in cls.items() if "<<enumeration>>" in corps}
    dot = [
        "digraph Wade {",
        '    graph [rankdir=LR, fontname="DejaVu Sans", fontsize=22, labelloc=t, pad=0.4, nodesep=0.35, ranksep=1.1,',
        '           splines=true, compound=true, newrank=true,',
        '           label=<<B>Waɖɛ · Diagramme de classes complet</B>>];',
        '    node [shape=plain, fontname="DejaVu Sans", fontsize=10];',
        '    edge [fontname="DejaVu Sans", fontsize=9, color="#3f5a47", fontcolor="#3f5a47", arrowsize=0.8, labeldistance=1.6];',
    ]
    for module in ORDRE_MODULES:
        dot.append(f"    subgraph cluster_{module} {{")
        dot.append(f'        label=<<B>{html.escape(LIBELLE_MODULE[module])}</B>>; fontsize=16; fontcolor="#00370B";')
        dot.append(f'        style="rounded,filled"; fillcolor="{COULEUR_MODULE[module]}"; color="#8fa596"; margin=18;')
        for nom, corps in modules[module].items():
            dot.append("    " + noeud_dot(nom, corps))
        dot.append("    }")
    dot += [arete_dot(r, enumerations) for r in relations]
    dot.append("}")
    PLANCHES.mkdir(exist_ok=True)
    source = PLANCHES / f"{NOM_PLANCHE}.dot"
    source.write_text("\n".join(dot), encoding="utf-8")
    for fmt, options in (("svg", []), ("pdf", []), ("png", ["-Gdpi=110"])):
        subprocess.run(["dot", f"-T{fmt}", *options, str(source), "-o", str(PLANCHES / f"{NOM_PLANCHE}.{fmt}")], check=True)
    print(f"Planche Graphviz écrite : {PLANCHES / NOM_PLANCHE}.(svg|pdf|png)")


def main() -> None:
    modules = {m: {} for m in ORDRE_MODULES}
    relations = []
    for numero, bloc in blocs_par_section(SOURCE.read_text(encoding="utf-8")):
        classes, rels = decouper(bloc)
        for nom, corps in classes.items():
            module = MODULE_PAR_CLASSE.get(nom) or MODULE_PAR_SECTION.get(numero)
            if module is None:
                raise SystemExit(f"Classe sans module : {nom} (section {numero})")
            modules[module][nom] = corps
        relations += rels
    relations += [r.strip() for r in LIENS_INTER_MODULES]
    relations = list(dict.fromkeys(relations))  # dédoublonnage en conservant l'ordre

    connues = {n for cls in modules.values() for n in cls}
    for r in relations:
        for nom in re.findall(r"\b[A-Z]\w+\b", re.sub(r'"[^"]*"|:.*$', "", r)):
            if nom not in connues:
                raise SystemExit(f"Relation vers une classe inconnue : {nom} dans « {r} »")

    d = ["classDiagram", "    direction TB"]
    for module in ORDRE_MODULES:
        d.append(f"    namespace {module} {{")
        for nom, corps in modules[module].items():
            d.append(f"        class {nom} {{")
            d += [f"            {c}" for c in corps]
            d.append("        }")
        d.append("    }")
    d += [f"    {r}" for r in relations]

    nb = len(connues)
    md = [
        "# 9. Diagramme de classes complet",
        "",
        "> Fichier **généré** par `outils/generer_classes_complet.py` à partir de "
        "`02-diagrammes-de-classes.md`. Ne pas modifier à la main.",
        "",
        f"Vue d'ensemble du domaine : **{nb} classes et énumérations** réparties en "
        f"{len(ORDRE_MODULES)} modules, et {len(relations)} relations, dont les associations entre modules. "
        "La planche est grande : la version à zoomer se trouve dans `planches/` (PDF vectoriel, SVG, PNG).",
        "",
        "| Module | Classes |",
        "|---|---|",
    ]
    md += [f"| {m} | {', '.join(modules[m])} |" for m in ORDRE_MODULES]
    md += ["", "```mermaid", *d, "```", ""]
    SORTIE.write_text("\n".join(md), encoding="utf-8")
    print(f"Écrit : {SORTIE} ({nb} classes, {len(relations)} relations)")
    ecrire_planche(modules, relations)


if __name__ == "__main__":
    main()
