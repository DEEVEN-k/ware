"""Produit la planche grand format du flux complet avec Graphviz.

Usage : python3 _modélisation/outils/generer_flux_complet.py

La source reste le diagramme Mermaid de 10-flux-complet.md (affiché par GitHub). Ce script
le convertit en DOT, car Graphviz donne une mise en page bien plus compacte sur un diagramme
de cette taille. Écrit planches/Waɖɛ_Flux_complet.(dot|svg|pdf|png).
"""
import html
import re
import subprocess
from pathlib import Path

DOSSIER = Path(__file__).resolve().parents[1]
SOURCE = DOSSIER / "10-flux-complet.md"
PLANCHES = DOSSIER / "planches"
NOM = "Waɖɛ_Flux_complet"

NOEUD = re.compile(r'(\w+)(\(\[".*?"\]\)|\[".*?"\]|\{".*?"\})?(?::::(\w+))?')
LIEN = re.compile(r'\s*(<-->|-\.->|---|-->|--\s*(?:"[^"]*"|[^-">]+?)\s*-->)\s*')
LEGENDE = [
    ("con", "Contributeur métier"), ("cor", "Correspondant"), ("rt", "Responsable de traitement"),
    ("adm", "Administrateur d'organisation"), ("cab", "Cabinet"), ("sys", "Système Waɖɛ"),
    ("aut", "Autorité de contrôle"), ("dec", "Décision"),
]


def libelle_html(texte: str) -> str:
    return "<BR/>".join(html.escape(p) for p in re.split(r"<br\s*/?>", texte))


def analyser(code: str):
    noeuds, aretes, groupes, styles = {}, [], [], {}
    groupe = None
    for brute in code.split("\n"):
        ligne = brute.strip()
        if not ligne or ligne.startswith(("flowchart", "direction")):
            continue
        if ligne.startswith("classDef"):
            _, nom, regles = ligne.split(" ", 2)
            styles[nom] = dict(r.split(":", 1) for r in regles.replace(" ", "").split(",") if ":" in r)
            continue
        m = re.match(r'subgraph (\w+)\["(.*)"\]', ligne)
        if m:
            groupe = m.group(1)
            groupes.append((groupe, m.group(2)))
            continue
        if ligne == "end":
            groupe = None
            continue
        pos, precedents, lien = 0, None, None
        while pos < len(ligne):
            courants = []
            while True:
                m = NOEUD.match(ligne, pos)
                if not m:
                    raise SystemExit(f"Ligne non comprise : {ligne!r} (position {pos})")
                ident, forme, classe = m.groups()
                n = noeuds.setdefault(ident, {"label": ident, "forme": "box", "classe": None, "groupe": None})
                if forme:
                    n["label"] = forme.strip('([{}])')[1:-1]
                    n["forme"] = "diamond" if forme[0] == "{" else ("stade" if forme[:2] == "([" else "box")
                    n["groupe"] = groupe
                if classe:
                    n["classe"] = classe
                courants.append(ident)
                pos = m.end()
                esperluette = re.match(r"\s*&\s*", ligne[pos:])
                if not esperluette:
                    break
                pos += esperluette.end()
            if precedents:
                for a in precedents:
                    for b in courants:
                        aretes.append((a, b, lien))
            m = LIEN.match(ligne, pos)
            if not m:
                break
            brut = m.group(1)
            texte = None
            if brut.startswith("--") and brut.endswith("-->") and len(brut) > 3:
                texte = brut[2:-3].strip().strip('"') or None
            lien = {"type": "<-->" if brut == "<-->" else "-.->" if brut == "-.->" else "---" if brut == "---" else "-->", "texte": texte}
            precedents, pos = courants, m.end()
    return noeuds, aretes, groupes, styles


def attributs_noeud(n: dict, styles: dict) -> str:
    st = styles.get(n["classe"], {"fill": "#EAF5EC", "stroke": "#00901D", "color": "#00370B"})
    style = "filled"
    forme = n["forme"]
    if forme == "stade":
        forme, style = "box", "filled,rounded"
    if "stroke-dasharray" in st:
        style += ",dashed"
    return (f'label=<{libelle_html(n["label"])}>, shape={forme}, style="{style}", fillcolor="{st["fill"]}", '
            f'color="{st["stroke"]}", fontcolor="{st["color"]}"')


def main() -> None:
    code = re.search(r"```mermaid\n(.*?)```", SOURCE.read_text(encoding="utf-8"), flags=re.S).group(1)
    noeuds, aretes, groupes, styles = analyser(code)
    dot = [
        "digraph Flux {",
        '    graph [rankdir=TB, fontname="DejaVu Sans", fontsize=24, labelloc=t, pad=0.4, nodesep=0.3, ranksep=0.45, newrank=true,',
        '           label=<<B>Waɖɛ · Diagramme de flux complet</B>>];',
        '    node [fontname="DejaVu Sans", fontsize=11, margin="0.14,0.08", penwidth=1.2];',
        '    edge [fontname="DejaVu Sans", fontsize=10, color="#3f5a47", fontcolor="#00370B", arrowsize=0.8];',
    ]
    for ident, titre in groupes:
        dot.append(f"    subgraph cluster_{ident} {{")
        dot.append(f'        label=<<B>{html.escape(titre)}</B>>; fontsize=17; fontcolor="#00370B"; style="rounded,filled"; fillcolor="#FAFCFA"; color="#8fa596"; margin=16;')
        dot += [f"        {i} [{attributs_noeud(n, styles)}];" for i, n in noeuds.items() if n["groupe"] == ident]
        dot.append("    }")
    dot += [f"    {i} [{attributs_noeud(n, styles)}];" for i, n in noeuds.items() if n["groupe"] is None]
    for a, b, lien in aretes:
        attrs = []
        if lien["texte"]:
            attrs.append(f'label=<{libelle_html(lien["texte"])}>')
        if lien["type"] == "<-->":
            attrs.append("dir=both")
        elif lien["type"] == "-.->":
            attrs.append("style=dashed")
        elif lien["type"] == "---":
            attrs.append("dir=none")
        dot.append(f"    {a} -> {b} [{', '.join(attrs)}];")
    # Légende des couleurs par acteur.
    dot.append('    subgraph cluster_legende { label=<<B>Légende</B>>; fontsize=15; style="rounded"; color="#8fa596"; margin=12;')
    for classe, texte in LEGENDE:
        n = {"label": texte, "forme": "diamond" if classe == "dec" else "box", "classe": classe}
        dot.append(f"        L_{classe} [{attributs_noeud(n, styles)}];")
    dot.append("        " + " -> ".join(f"L_{c}" for c, _ in LEGENDE) + " [style=invis];")
    dot.append("    }")
    dot.append("}")
    PLANCHES.mkdir(exist_ok=True)
    source = PLANCHES / f"{NOM}.dot"
    source.write_text("\n".join(dot), encoding="utf-8")
    for fmt, options in (("svg", []), ("pdf", []), ("png", ["-Gdpi=110"])):
        subprocess.run(["dot", f"-T{fmt}", *options, str(source), "-o", str(PLANCHES / f"{NOM}.{fmt}")], check=True)
    print(f"{len(noeuds)} étapes, {len(aretes)} transitions. Planche écrite : {PLANCHES / NOM}.(svg|pdf|png)")


if __name__ == "__main__":
    main()
