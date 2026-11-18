"""Génère le PDF « Diagramme de flux expliqué » : chaque phase, chaque étape, chaque décision
et chaque passage entre phases, avec sa raison d'être et sa source.

Usage : python3 _modélisation/outils/generer_explication_flux.py

Le flux est lu dans 10-flux-complet.md (source unique) et les explications dans
explications/flux.py. Le script échoue si une étape ou un passage entre phases n'est pas
expliqué, ou si une explication ne correspond plus à rien. Nécessite Graphviz (dot) et
Playwright (via html_vers_pdf.js).
"""
import base64
import html
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

OUTILS = Path(__file__).resolve().parent
DOSSIER = OUTILS.parent
sys.path.insert(0, str(OUTILS))
sys.path.insert(0, str(DOSSIER / "explications"))

import generer_flux_complet as gf  # noqa: E402
from flux import ACTEURS, ETAPES, LIENS, PHASES, POINTS  # noqa: E402

SORTIE_HTML = OUTILS / "vendor" / "explication_flux.html"
SORTIE_PDF = DOSSIER / "Waɖɛ_Diagramme_de_flux_explique.pdf"
LOGO = DOSSIER.parent / "00 Commun aux deux pays" / "01 Ware identité visuelle" / "LOGOTYPE HORIZONTALE.png"


def texte_brut(label: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<br\s*/?>", " · ", label)).strip()


def titre_court(label: str) -> str:
    return re.split(r"<br\s*/?>", label)[0].strip()


def charger():
    code = re.search(r"```mermaid\n(.*?)```", (DOSSIER / "10-flux-complet.md").read_text(encoding="utf-8"), flags=re.S).group(1)
    return gf.analyser(code)


def verifier(noeuds, aretes, groupes):
    erreurs = []
    for i in noeuds:
        if i not in ETAPES:
            erreurs.append(f"Étape non expliquée : {i} ({texte_brut(noeuds[i]['label'])})")
    for i in ETAPES:
        if i not in noeuds:
            erreurs.append(f"Explication d'une étape absente du diagramme : {i}")
    ids_phases = {g for g, _ in groupes}
    for g in ids_phases:
        if g not in PHASES:
            erreurs.append(f"Phase non expliquée : {g}")
    croisees = {(a, b) for a, b, _ in aretes if noeuds[a]["groupe"] != noeuds[b]["groupe"]}
    for c in sorted(croisees):
        if c not in LIENS:
            erreurs.append(f"Passage entre phases non expliqué : {c[0]} → {c[1]}")
    for c in LIENS:
        if c not in croisees:
            erreurs.append(f"Explication d'un passage absent du diagramme : {c[0]} → {c[1]}")
    if erreurs:
        raise SystemExit("Document incomplet :\n  " + "\n  ".join(erreurs))
    return croisees


def svg(dot_lignes):
    sortie = subprocess.run(["dot", "-Tsvg"], input="\n".join(dot_lignes), capture_output=True, text=True, check=True).stdout
    return sortie[sortie.index("<svg"):]


def schema_phase(gid, noeuds, aretes, styles):
    dot = [
        "digraph P {",
        f'  graph [rankdir=TB, fontname="DejaVu Sans", pad=0.15, nodesep=0.25, ranksep=0.35, bgcolor="transparent"];',
        '  node [fontname="DejaVu Sans", fontsize=10, margin="0.12,0.06", penwidth=1.1];',
        '  edge [fontname="DejaVu Sans", fontsize=9, color="#3f5a47", fontcolor="#00370B", arrowsize=0.7];',
    ]
    for i, n in noeuds.items():
        if n["groupe"] == gid:
            dot.append(f"  {i} [{gf.attributs_noeud(n, styles)}, xlabel=<<FONT POINT-SIZE=\"8\" COLOR=\"#616d49\">{i}</FONT>>];")
    for a, b, l in aretes:
        if noeuds[a]["groupe"] == gid and noeuds[b]["groupe"] == gid:
            attrs = []
            if l["texte"]:
                attrs.append(f"label=<{gf.libelle_html(l['texte'])}>")
            if l["type"] == "<-->":
                attrs.append("dir=both")
            elif l["type"] == "-.->":
                attrs.append("style=dashed")
            elif l["type"] == "---":
                attrs.append("dir=none")
            dot.append(f"  {a} -> {b} [{', '.join(attrs)}];")
    dot.append("}")
    return svg(dot)


def schema_ensemble(noeuds, aretes, groupes):
    titres = dict(groupes)
    paires = {}
    for a, b, _ in aretes:
        ga, gb = noeuds[a]["groupe"] or ("DEBUT" if a == "START" else "FIN"), noeuds[b]["groupe"] or ("DEBUT" if b == "START" else "FIN")
        if ga != gb:
            paires[(ga, gb)] = paires.get((ga, gb), 0) + 1
    dot = [
        "digraph E {",
        '  graph [rankdir=LR, fontname="DejaVu Sans", pad=0.2, nodesep=0.45, ranksep=0.55, bgcolor="transparent"];',
        '  node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize=11, fillcolor="#EAF5EC", color="#00901D", fontcolor="#00370B", margin="0.18,0.1"];',
        '  edge [color="#3f5a47", arrowsize=0.8, fontname="DejaVu Sans", fontsize=9, fontcolor="#616d49"];',
        '  DEBUT [label="Début", shape=oval, fillcolor="#ffffff"]; FIN [label="Pilotage dans la durée", shape=oval, fillcolor="#ffffff"];',
    ]
    for gid, t in groupes:
        dot.append(f'  {gid} [label=<<B>{html.escape(t)}</B>>];')
    for (a, b), n in paires.items():
        dot.append(f'  {a} -> {b} [label="{n}"];' if n > 1 else f"  {a} -> {b};")
    dot.append("}")
    return svg(dot)


def construire():
    noeuds, aretes, groupes, styles = charger()
    croisees = verifier(noeuds, aretes, groupes)
    sortantes = {}
    for a, b, l in aretes:
        sortantes.setdefault(a, []).append((b, l))
    titres_phases = dict(groupes)
    nb_dec = sum(1 for n in noeuds.values() if n["classe"] == "dec")

    def puce(classe):
        st = styles.get(classe, {"fill": "#ffffff", "stroke": "#888888", "color": "#333333"})
        bord = "dashed" if "stroke-dasharray" in st else "solid"
        return f'<span class="acteur" style="background:{st["fill"]};color:{st["color"]};border:1px {bord} {st["stroke"]}">{html.escape(ACTEURS.get(classe, ""))}</span>'

    corps, sommaire = [], []
    for k, (gid, titre) in enumerate(groupes):
        ids = [i for i, n in noeuds.items() if n["groupe"] == gid]
        sommaire.append(f"<li>{html.escape(titre)} <span class='muted'>({len(ids)} étapes)</span></li>")
        corps.append(f"<section class='phase'><h1>{html.escape(titre)}</h1><p class='intro'>{html.escape(PHASES[gid])}</p>")
        corps.append(f"<div class='schema schema-phase'>{schema_phase(gid, noeuds, aretes, styles)}</div>")
        corps.append("<h2>Étapes</h2><table><thead><tr><th style='width:6%'>N°</th><th style='width:23%'>Étape</th><th style='width:15%'>Acteur</th><th>Ce qui se passe</th><th style='width:30%'>Pourquoi, et source</th></tr></thead><tbody>")
        for i in ids:
            n = noeuds[i]
            quoi, pourquoi = ETAPES[i]
            issues = ""
            if n["classe"] == "dec" or len(sortantes.get(i, [])) > 1:
                items = []
                for b, l in sortantes.get(i, []):
                    cible = noeuds[b]
                    hors = f" <span class='muted'>({html.escape(titres_phases.get(cible['groupe'], 'fin'))})</span>" if cible["groupe"] != gid else ""
                    etiquette = html.escape(texte_brut(l["texte"])) if l["texte"] else "ensuite"
                    items.append(f"<li><b>{etiquette}</b> → {b} · {html.escape(texte_brut(titre_court(cible['label'])))}{hors}</li>")
                issues = f"<ul class='issues'>{''.join(items)}</ul>"
            corps.append(f"<tr><td class='n'>{i}</td><td><b>{html.escape(texte_brut(n['label']))}</b></td><td>{puce(n['classe'])}</td><td>{html.escape(quoi)}{issues}</td><td class='src'>{html.escape(pourquoi)}</td></tr>")
        corps.append("</tbody></table>")
        liens = [(a, b) for (a, b) in sorted(croisees) if noeuds[a]["groupe"] == gid]
        if liens:
            corps.append("<h2>Passages vers une autre phase</h2><table><thead><tr><th style='width:34%'>Passage</th><th>Pourquoi</th></tr></thead><tbody>")
            for a, b in liens:
                cible = noeuds[b]
                dest = titres_phases.get(cible["groupe"], "Fin du parcours")
                corps.append(f"<tr><td><b>{a}</b> → <b>{b}</b><br><span class='muted'>vers « {html.escape(dest)} » · {html.escape(texte_brut(titre_court(cible['label'])))}</span></td><td>{html.escape(LIENS[(a, b)])}</td></tr>")
            corps.append("</tbody></table>")
        corps.append("</section>")

    legende = "".join(f"<tr><td>{puce(c)}</td><td>{d}</td></tr>" for c, d in [
        ("con", "Agent d'un service : décrit les traitements de son périmètre."),
        ("cor", "Juriste ou référent : qualifie, publie, conduit formalités, AIPD et violations."),
        ("rt", "Personne qui répond du traitement : vise avant dépôt."),
        ("adm", "Gère l'espace, les utilisateurs, les paramètres et les mandats."),
        ("cab", "Prestataire qui intervient sous mandat."),
        ("sys", "Ce que Waɖɛ fait seul : calculs, contrôles, alertes, documents."),
        ("aut", "IPDCP ou APDP : agit hors de la plateforme."),
        ("dec", "Point de décision : le chemin dépend de la réponse."),
    ])
    logo = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode() if LOGO.exists() else ""
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Waɖɛ – Diagramme de flux expliqué</title>
<style>
@page {{ size: A4 landscape; margin: 14mm 14mm 16mm 14mm; }}
:root {{ --dark:#00370B; --green:#00901D; --light:#EAF5EC; --ink:#1d2a20; --muted:#5b6b5f; --line:#cfdcd2; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color: var(--ink); font-size: 8.8pt; line-height: 1.42; margin: 0; background:#fff; }}
h1 {{ color: var(--dark); font-size: 17pt; border-bottom: 2px solid var(--green); padding-bottom: 4px; margin: 0 0 6px; }}
h2 {{ color: var(--dark); font-size: 12pt; margin: 14px 0 6px; break-after: avoid; }}
.phase, .page {{ break-before: page; }}
.intro {{ font-size: 9.6pt; background: var(--light); border-left: 3px solid var(--green); padding: 6px 10px; margin: 6px 0 8px; }}
.schema {{ text-align: center; margin: 6px 0; break-inside: avoid; }}
.schema svg {{ max-width: 100%; max-height: 150mm; width: auto; height: auto; }}
.schema-phase {{ break-after: page; }}
.schema-phase svg {{ max-height: 140mm; height: 140mm; }}
table {{ width: 100%; border-collapse: collapse; font-size: 8.2pt; margin: 2px 0 8px; }}
th {{ background: var(--dark); color: #fff; text-align: left; padding: 4px 6px; }}
td {{ border-bottom: 1px solid var(--line); padding: 4px 6px; vertical-align: top; }}
tr {{ break-inside: avoid; }}
td.n {{ font-family: "DejaVu Sans Mono", monospace; font-weight: 700; color: var(--dark); }}
td.src {{ color: #3a4a3e; }}
.acteur {{ display: inline-block; font-size: 7.6pt; font-weight: 600; padding: 2px 7px; border-radius: 6px; white-space: nowrap; }}
.issues {{ margin: 4px 0 0; padding-left: 14px; }}
.issues li {{ margin: 1px 0; }}
.muted {{ color: var(--muted); font-size: 7.8pt; }}
.note {{ background: var(--light); border-left: 3px solid var(--green); padding: 6px 10px; margin: 6px 0; }}
.cover {{ height: 175mm; display: flex; flex-direction: column; justify-content: space-between; }}
.cover img {{ width: 70mm; }}
.cover .k {{ color: var(--green); font-weight: 700; letter-spacing: .14em; text-transform: uppercase; font-size: 9pt; }}
.cover h1 {{ border: 0; font-size: 28pt; margin: 6px 0 10px; }}
.cover .lead {{ font-size: 12pt; color: var(--muted); max-width: 210mm; }}
.chiffres {{ display: flex; gap: 10px; margin-top: 10mm; }}
.chiffres div {{ border: 1px solid var(--line); border-radius: 6px; padding: 8px 12px; min-width: 32mm; }}
.chiffres b {{ display: block; font-size: 18pt; color: var(--dark); }}
.meta {{ font-size: 8.4pt; color: var(--muted); border-top: 1px solid var(--line); padding-top: 6px; }}
code {{ font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; background: #f1f4f2; padding: 0 3px; border-radius: 3px; }}
</style></head><body>
<div class="cover"><div>{f'<img src="{logo}">' if logo else ''}</div>
<div><div class="k">Dossier de conception</div><h1>Le diagramme de flux expliqué</h1>
<p class="lead">Le parcours complet d'une organisation dans Waɖɛ, de la création de son espace au pilotage continu : chaque étape, chaque décision et chaque passage d'une phase à l'autre, avec sa raison d'être et la source qui le justifie.</p>
<div class="chiffres"><div><b>{len(groupes)}</b>phases</div><div><b>{len(noeuds)}</b>étapes</div><div><b>{nb_dec}</b>décisions</div><div><b>{len(aretes)}</b>transitions</div></div></div>
<div class="meta">Établi d'après les livrables AMELEGAL v1.0 (septembre 2026). Généré le {date.today().strftime('%d/%m/%Y')} à partir de <code>_modélisation/10-flux-complet.md</code> ; la génération échoue si une étape ou un passage n'est pas expliqué. La planche à zoomer est <code>planches/Waɖɛ_Flux_complet.pdf</code>.</div></div>

<div class="page"><h1>Comment lire ce document</h1>
<p>Le flux est découpé en {len(groupes)} phases. Pour chacune : son rôle, son schéma, le tableau de ses étapes, puis les passages vers les autres phases. Chaque étape porte un numéro (A1, B7, E14…) qui est le même que sur la planche complète.</p>
<h2>Les acteurs (couleurs)</h2><table><thead><tr><th style="width:24%">Couleur</th><th>Rôle dans le flux</th></tr></thead><tbody>{legende}</tbody></table>
<h2>Les formes</h2>
<table><tbody><tr><td style="width:24%"><b>Rectangle</b></td><td>Une étape : une action d'un acteur, ou un traitement automatique de Waɖɛ.</td></tr>
<tr><td><b>Losange</b></td><td>Une décision : les flèches qui en partent portent la réponse (oui, non, rejet…). Dans les tableaux, les issues sont listées sous l'étape.</td></tr>
<tr><td><b>Flèche pleine</b></td><td>L'enchaînement normal.</td></tr><tr><td><b>Flèche pointillée</b></td><td>Un déclenchement conditionnel, par exemple une alerte quand un délai est dépassé.</td></tr>
<tr><td><b>Codes AL-xx</b></td><td>Les 13 alertes du fichier <code>alertes.json</code>.</td></tr></tbody></table>
<h2>Vue d'ensemble des phases</h2>
<div class="schema">{schema_ensemble(noeuds, aretes, groupes)}</div>
<p class="muted">Le chiffre sur une flèche indique le nombre de passages entre deux phases. La phase 6 (violation) peut survenir à tout moment ; la phase 5 renvoie vers les phases 1 et 4 quand une fiche doit être revue.</p>
<h2>Sommaire</h2><ol>{''.join(sommaire)}<li>Points d'attention</li></ol></div>

{''.join(corps)}

<section class="phase"><h1>Points d'attention</h1>
<p>Points du flux qui reposent sur un choix de modélisation ou sur un écart dans les livrables, à confirmer par AMELEGAL.</p>
<table><thead><tr><th style="width:24%">Point</th><th>Explication</th></tr></thead><tbody>
{''.join(f'<tr><td><b>{html.escape(t)}</b></td><td>{html.escape(x)}</td></tr>' for t, x in POINTS)}
</tbody></table></section>
</body></html>"""
    SORTIE_HTML.parent.mkdir(exist_ok=True)
    SORTIE_HTML.write_text(page, encoding="utf-8")
    subprocess.run(["node", str(OUTILS / "html_vers_pdf.js"), str(SORTIE_HTML), str(SORTIE_PDF), "Waɖɛ · Diagramme de flux expliqué", "paysage"], check=True)
    print(f"{len(groupes)} phases, {len(noeuds)} étapes, {len(croisees)} passages entre phases : tout est expliqué.")
    print(f"PDF écrit : {SORTIE_PDF}")


if __name__ == "__main__":
    construire()
