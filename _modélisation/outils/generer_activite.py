"""Génère le diagramme d'activité UML complet de Waɖɛ : un diagramme par phase, avec un couloir
horizontal par acteur (le flux se lit de gauche à droite), reliés entre eux par des connecteurs, plus une vue d'ensemble.

Usage : python3 _modélisation/outils/generer_activite.py

Source : outils/activite_donnees.py. Sorties :
  planches/activite/<phase>.svg, .pdf et .dot   un diagramme par phase, à sa taille réelle
  Waɖɛ_Diagramme_activite.pdf             couverture, notation et vue d'ensemble (A4), puis une page par phase
Nécessite Graphviz (dot) et Playwright (html_vers_pdf.js).

Le script vérifie la cohérence du modèle (flots vers des nœuds existants, nœuds reliés, gardes
sur chaque issue de décision, fourches réelles) et que chaque nœud apparaît dans un diagramme
de phase.
"""
import base64
import html
import subprocess
import sys
from datetime import date
from pathlib import Path

OUTILS = Path(__file__).resolve().parent
DOSSIER = OUTILS.parent
sys.path.insert(0, str(OUTILS))
from activite_donnees import COULOIRS, FLOTS, NOEUDS, PHASES, phase_de  # noqa: E402

PLANCHES = DOSSIER / "planches" / "activite"
SORTIE_PDF = DOSSIER / "Waɖɛ_Diagramme_activite.pdf"
SORTIE_HTML = OUTILS / "vendor" / "activite.html"
LOGO = DOSSIER.parent / "00 Commun aux deux pays" / "01 Ware identité visuelle" / "LOGOTYPE HORIZONTALE.png"
NOEUD = {n[0]: n for n in NOEUDS}
TITRE_PHASE = {p[0]: p[1] for p in PHASES}


def verifier():
    ids = [n[0] for n in NOEUDS]
    erreurs = [f"Identifiant en double : {i}" for i in set(ids) if ids.count(i) > 1]
    couloirs = {c[0] for c in COULOIRS}
    erreurs += [f"Couloir inconnu pour {n[0]} : {n[1]}" for n in NOEUDS if n[1] not in couloirs]
    entrants = {i: 0 for i in ids}
    sortants = {i: 0 for i in ids}
    gardes = {i: 0 for i in ids}
    for a, b, g, _ in FLOTS:
        for x in (a, b):
            if x not in NOEUD:
                erreurs.append(f"Flot vers un nœud inconnu : {a} → {b}")
        if a in NOEUD and b in NOEUD:
            sortants[a] += 1
            entrants[b] += 1
            gardes[a] += 1 if g else 0
    for i, _, t, _ in NOEUDS:
        if t not in ("debut", "reception") and entrants[i] == 0:
            erreurs.append(f"Nœud sans entrée : {i}")
        if t not in ("fin", "finflux", "reception") and sortants[i] == 0:
            erreurs.append(f"Nœud sans sortie : {i}")
        if t == "decision" and sortants[i] > 1 and gardes[i] < sortants[i]:
            erreurs.append(f"Décision {i} : chaque issue doit porter une garde")
        if t == "fourche" and sortants[i] < 2 and entrants[i] < 2:
            erreurs.append(f"Fourche {i} : ni plusieurs sorties ni plusieurs entrées")
    for i in ids:
        try:
            phase_de(i)
        except KeyError:
            erreurs.append(f"Nœud sans phase : {i}")
    if erreurs:
        raise SystemExit("Modèle incohérent :\n  " + "\n  ".join(erreurs))


def libelle(texte):
    return "<" + "<BR/>".join(html.escape(x) for x in texte.split("\n")) + ">" if texte else '""'


def attributs(noeud, trait):
    _, _, t, lib = noeud
    if t == "debut":
        return 'shape=circle, style=filled, fillcolor="#12180E", color="#12180E", width=0.3, fixedsize=true, label=""'
    if t == "fin":
        return 'shape=doublecircle, style=filled, fillcolor="#12180E", color="#12180E", width=0.24, fixedsize=true, label=""'
    if t == "finflux":
        return 'shape=circle, style=filled, fillcolor="white", color="#12180E", width=0.3, fixedsize=true, fontsize=14, label="×"'
    if t == "decision":
        return f'shape=diamond, style=filled, fillcolor="white", color="{trait}", width=0.42, height=0.42, fixedsize=true, label=""'
    if t == "fourche":
        return 'shape=box, style=filled, fillcolor="#12180E", color="#12180E", width=1.7, height=0.07, fixedsize=true, label=""'
    if t == "envoi":
        return f'shape=cds, style=filled, fillcolor="#FFF6E0", color="#B7791F", label={libelle(lib)}'
    if t == "reception":
        return f'shape=larrow, style=filled, fillcolor="#E4F1F4", color="#0E5F73", label={libelle(lib)}'
    if t == "temps":
        x = f", xlabel={libelle(lib)}" if lib else ""
        return f'shape=invtriangle, style=filled, fillcolor="#FFF9E0", color="#B7791F", width=0.42, height=0.36, fixedsize=true, label=""{x}'
    return f'shape=box, style="rounded,filled", fillcolor="white", color="{trait}", label={libelle(lib)}'


def attributs_flot(garde, style):
    attrs = []
    if garde:
        texte = "<BR/>".join(html.escape(x) for x in garde.split("\n"))
        attrs.append(f"label=<[{texte}]>")
    if style == "signal":
        attrs.append('style=dashed, color="#B7791F"')
    return attrs


def dessiner(dot, fmt="svg"):
    sortie = subprocess.run(["dot", "-Tsvg"], input="\n".join(dot), capture_output=True, text=True)
    if sortie.returncode != 0 and any("newrank=true" in ligne for ligne in dot):
        # Graphviz 2.43 perd parfois une arête avec newrank (« lost edge ») : on relance sans.
        dot = [ligne.replace("newrank=true, ", "") for ligne in dot]
        sortie = subprocess.run(["dot", "-Tsvg"], input="\n".join(dot), capture_output=True, text=True)
    if sortie.returncode != 0:
        raise SystemExit("Graphviz a échoué :\n" + sortie.stderr)
    return sortie.stdout[sortie.stdout.index("<svg"):]


def diagramme_phase(pid, titre=""):
    """Un diagramme de phase : ses nœuds, ses couloirs, et un connecteur pour chaque flot qui sort de la phase ou y entre."""
    membres = [n for n in NOEUDS if phase_de(n[0]) == pid]
    ids = {n[0] for n in membres}
    connecteurs = {}  # identifiant -> (couloir, libellé)
    flots = []
    for a, b, g, s in FLOTS:
        dedans_a, dedans_b = a in ids, b in ids
        if dedans_a and dedans_b:
            flots.append((a, b, g, s))
        elif dedans_a:
            cid = f"VERS_{b}"
            connecteurs[cid] = (NOEUD[a][1], f"vers phase {TITRE_PHASE[phase_de(b)].split(' · ')[0]} · {b}")
            flots.append((a, cid, g, s))
        elif dedans_b:
            cid = f"DEPUIS_{a}"
            connecteurs[cid] = (NOEUD[b][1], f"depuis phase {TITRE_PHASE[phase_de(a)].split(' · ')[0]} · {a}")
            flots.append((cid, b, g, s))
    couloirs = [c for c in COULOIRS if any(n[1] == c[0] for n in membres) or any(v[0] == c[0] for v in connecteurs.values())]
    dot = [
        "digraph Phase {",
        '  graph [rankdir=LR, newrank=true, fontname="DejaVu Sans", pad=0.35, nodesep=0.3, ranksep=0.4, forcelabels=true, bgcolor="white", labelloc=t, labeljust=l, fontsize=22,',
        f'         label=<<B>{html.escape(titre)}</B>  <FONT POINT-SIZE="12" COLOR="#5b6b5f">Waɖɛ · diagramme d\'activité UML · couloirs horizontaux, lecture de gauche à droite</FONT>>];',
        '  node [fontname="DejaVu Sans", fontsize=11, margin="0.12,0.06", penwidth=1.2];',
        '  edge [fontname="DejaVu Sans", fontsize=9, color="#3f5a47", fontcolor="#00370B", arrowsize=0.75];',
    ]
    for c, nom, fond, trait in couloirs:
        dot.append(f'  subgraph cluster_{c} {{ label=<<B>{html.escape(nom)}</B>>; fontsize=14; fontcolor="{trait}"; style="filled"; fillcolor="{fond}"; color="{trait}"; penwidth=1.3; margin=14;')
        dot.append(f"    H_{c} [shape=point, width=0.01, style=invis];")
        for n in membres:
            if n[1] == c:
                dot.append(f"    {n[0]} [{attributs(n, trait)}];")
        for cid, (couloir, texte) in connecteurs.items():
            if couloir == c:
                dot.append(f'    {cid} [shape=circle, style=filled, fillcolor="#EAF5EC", color="#00901D", fixedsize=true, width=0.32, label="", xlabel=<<FONT COLOR="#00370B" POINT-SIZE="10"><B>{html.escape(texte)}</B></FONT>>];')
        dot.append("  }")
    for c in couloirs:
        premiers = [n[0] for n in membres if n[1] == c[0]] + [cid for cid, v in connecteurs.items() if v[0] == c[0]]
        dot.append(f"  H_{c[0]} -> {premiers[0]} [style=invis];")
    for a, b, g, s in flots:
        dot.append(f"  {a} -> {b} [{', '.join(attributs_flot(g, s))}];")
    dot.append("}")
    return dot, len(membres), len(flots), len(connecteurs)


def vue_ensemble():
    paires = {}
    for a, b, _, _ in FLOTS:
        pa, pb = phase_de(a), phase_de(b)
        if pa != pb:
            paires[(pa, pb)] = paires.get((pa, pb), 0) + 1
    dot = [
        "digraph E {",
        '  graph [rankdir=LR, fontname="DejaVu Sans", pad=0.2, nodesep=0.5, ranksep=0.6, bgcolor="transparent"];',
        '  node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize=12, fillcolor="#00370B", color="#00370B", fontcolor="white", margin="0.2,0.12"];',
        '  edge [color="#3f5a47", arrowsize=0.8, fontname="DejaVu Sans", fontsize=10, fontcolor="#616d49"];',
        '  DEBUT [shape=circle, style=filled, fillcolor="#12180E", width=0.3, fixedsize=true, label=""];',
        '  INC [shape=larrow, style=filled, fillcolor="#E4F1F4", color="#0E5F73", fontcolor="#0b4553", label="Incident constaté"];',
    ]
    for pid, titre, _ in PHASES:
        dot.append(f"  {pid} [label=<<B>{html.escape(titre)}</B>>];")
    dot.append("  DEBUT -> PH0; INC -> PH6;")
    for (a, b), n in paires.items():
        dot.append(f'  {a} -> {b} [label="{n} flot{"s" if n > 1 else ""}"];')
    dot.append("}")
    return dessiner(dot)


def legende_svg():
    dot = ['digraph L { graph [rankdir=TB, bgcolor="transparent", nodesep=0.2, ranksep=0.18]; node [fontname="DejaVu Sans", fontsize=11];']
    elements = [
        ("debut", "", "Début de l'activité"),
        ("fin", "", "Fin de l'activité"),
        ("finflux", "", "Fin de flot : ce chemin s'arrête, l'activité continue"),
        ("action", "Action", "Action d'un acteur ou de Waɖɛ"),
        ("decision", "", "Décision ou fusion ; la condition [garde] est sur chaque flèche"),
        ("fourche", "", "Fourche ou jonction : chemins menés en parallèle"),
        ("envoi", "Signal", "Envoi de signal : alerte, notification, courriel, dépôt"),
        ("reception", "Signal", "Réception d'un signal externe : incident, décision, nouvelle version"),
        ("temps", "", "Événement temporel : échéance ou délai écoulé"),
    ]
    for k, (t, lib, texte) in enumerate(elements):
        dot.append(f"  L{k} [{attributs(('L', 'SYS', t, lib), '#555555')}];")
        dot.append(f'  T{k} [shape=plaintext, label="{texte}"]; {{ rank=same; L{k}; T{k}; }} L{k} -> T{k} [style=invis];')
    dot.append('  C [shape=circle, style=filled, fillcolor="#EAF5EC", color="#00901D", fixedsize=true, width=0.32, label=""];')
    dot.append('  CT [shape=plaintext, label="Connecteur : le flot continue dans une autre phase"]; { rank=same; C; CT; } C -> CT [style=invis];')
    dot.append('  SA [shape=point, width=0.05]; SB [shape=point, width=0.05]; SA -> SB [style=dashed, color="#B7791F"];')
    dot.append('  ST [shape=plaintext, label="Flot de signal (pointillé)"]; { rank=same; SB; ST; } SB -> ST [style=invis];')
    dot.append("  " + " -> ".join([f"L{k}" for k in range(len(elements))] + ["C", "SA"]) + " [style=invis];")
    dot.append("}")
    return dessiner(dot)


def construire():
    verifier()
    PLANCHES.mkdir(parents=True, exist_ok=True)
    pages, total_noeuds = [], 0
    for pid, titre, _ in PHASES:
        dot, nn, nf, nc = diagramme_phase(pid, titre)
        contenu = dessiner(dot)
        (PLANCHES / f"{pid}.dot").write_text("\n".join(dot), encoding="utf-8")
        texte_dot = "\n".join(dot)
        rendu = subprocess.run(["dot", "-Tpdf", "-o", str(PLANCHES / f"{pid}.pdf")], input=texte_dot, capture_output=True, text=True)
        if rendu.returncode != 0:
            subprocess.run(["dot", "-Tpdf", "-o", str(PLANCHES / f"{pid}.pdf")], input=texte_dot.replace("newrank=true, ", ""), check=True, text=True)
        (PLANCHES / f"{pid}.svg").write_text(contenu, encoding="utf-8")
        total_noeuds += nn
        pages.append((titre, contenu, nn, nf, nc))  # contenu : SVG, aussi écrit dans planches/activite
    if total_noeuds != len(NOEUDS):
        raise SystemExit(f"{len(NOEUDS) - total_noeuds} nœud(s) absent(s) des diagrammes de phase")

    nb = {t: sum(1 for n in NOEUDS if n[2] == t) for t in ("action", "decision", "fourche", "envoi", "reception", "temps")}
    logo = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode() if LOGO.exists() else ""
    couloirs_html = "".join(
        f'<tr><td style="width:14px;background:{f};border-left:4px solid {t}"></td><td><b>{html.escape(n)}</b></td></tr>' for _, n, f, t in COULOIRS
    )
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Waɖɛ – Diagramme d'activité</title>
<style>
@page {{ size: A4 landscape; margin: 12mm 12mm 14mm 12mm; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color: #1d2a20; font-size: 9pt; line-height: 1.42; margin: 0; background: #fff; }}
h1 {{ color: #00370B; font-size: 16pt; border-bottom: 2px solid #00901D; padding-bottom: 3px; margin: 0 0 4px; }}
h2 {{ color: #00370B; font-size: 12pt; margin: 10px 0 6px; }}
.phase, .page {{ break-before: page; }}
.schema {{ text-align: center; }}
.phase .schema svg {{ width: 100%; max-height: 165mm; height: auto; }}
.page .schema svg {{ max-width: 100%; height: auto; }}
.muted {{ color: #5b6b5f; font-size: 8.5pt; margin: 0 0 4px; }}
.cover {{ height: 178mm; display: flex; flex-direction: column; justify-content: space-between; }}
.cover img {{ width: 70mm; }}
.k {{ color: #00901D; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; font-size: 9pt; }}
.cover h1 {{ border: 0; font-size: 28pt; margin: 6px 0 10px; }}
.lead {{ font-size: 12pt; color: #5b6b5f; max-width: 220mm; }}
.chiffres {{ display: flex; gap: 10px; margin-top: 8mm; flex-wrap: wrap; }}
.chiffres div {{ border: 1px solid #cfdcd2; border-radius: 6px; padding: 8px 12px; min-width: 28mm; }}
.chiffres b {{ display: block; font-size: 17pt; color: #00370B; }}
.meta {{ font-size: 8.4pt; color: #5b6b5f; border-top: 1px solid #cfdcd2; padding-top: 6px; }}
.cols {{ display: flex; gap: 18px; align-items: flex-start; }}
.cols > div {{ flex: 1; }}
table {{ border-collapse: collapse; font-size: 8.6pt; width: 100%; }}
td {{ border-bottom: 1px solid #cfdcd2; padding: 4px 6px; vertical-align: top; }}
code {{ font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; }}
</style></head><body>
<div class="cover"><div>{f'<img src="{logo}">' if logo else ''}</div>
<div><div class="k">Dossier de conception</div><h1>Diagramme d'activité UML</h1>
<p class="lead">Le parcours complet d'une organisation dans Waɖɛ, en notation UML : un couloir par acteur, décisions gardées, chemins parallèles, signaux d'alerte et échéances. Un diagramme par phase, reliés par des connecteurs.</p>
<div class="chiffres"><div><b>{len(PHASES)}</b>phases</div><div><b>{len(COULOIRS)}</b>couloirs</div><div><b>{nb['action']}</b>actions</div><div><b>{nb['decision']}</b>décisions et fusions</div><div><b>{nb['fourche']}</b>fourches et jonctions</div><div><b>{nb['envoi'] + nb['reception']}</b>signaux</div><div><b>{nb['temps']}</b>événements temporels</div><div><b>{len(FLOTS)}</b>flots</div></div></div>
<div class="meta">Établi d'après les livrables AMELEGAL v1.0. Généré le {date.today().strftime('%d/%m/%Y')} à partir de <code>_modélisation/outils/activite_donnees.py</code>. Les identifiants (A1, B7, E14…) sont ceux du diagramme de flux et de son document explicatif.</div></div>

<div class="page"><h1>Lire le diagramme</h1>
<div class="cols"><div><h2>Notation</h2><div class="schema">{legende_svg()}</div></div>
<div><h2>Couloirs</h2><table>{couloirs_html}</table>
<p class="muted" style="margin-top:8px">Un consultant de cabinet agit dans les couloirs « Contributeur métier » ou « Correspondant » selon son rôle et le niveau de son mandat. Le couloir « Cabinet » ne montre que ce qui lui est propre : demander un mandat, affecter ses consultants.</p>
<h2>Vue d'ensemble</h2><div class="schema">{vue_ensemble()}</div>
<p class="muted">Chaque flèche indique combien de flots passent d'une phase à l'autre. La phase 6 démarre sur un signal externe (incident) et peut survenir à tout moment.</p></div></div></div>
<div class="page"><h1>Diagrammes de phase</h1><p>Les pages suivantes présentent un diagramme par phase, chacun à sa taille réelle (page vectorielle, à agrandir à l'écran) :</p><ol>{''.join(f'<li><b>{html.escape(t)}</b> · {nn} nœuds, {nf} flots, {nc} connecteur{"s" if nc > 1 else ""}</li>' for t, _, nn, nf, nc in pages)}</ol><p class="muted">Les mêmes diagrammes existent en SVG et en PDF dans <code>_modélisation/planches/activite/</code>.</p></div>
</body></html>"""
    SORTIE_HTML.parent.mkdir(exist_ok=True)
    SORTIE_HTML.write_text(page, encoding="utf-8")
    intro = OUTILS / "vendor" / "activite_intro.pdf"
    subprocess.run(["node", str(OUTILS / "html_vers_pdf.js"), str(SORTIE_HTML), str(intro), "Waɖɛ · Diagramme d'activité UML", "paysage"], check=True)
    from pypdf import PdfReader, PdfWriter
    ecrivain = PdfWriter()
    for page_pdf in PdfReader(str(intro)).pages:
        ecrivain.add_page(page_pdf)
    for pid, titre, _ in PHASES:
        ecrivain.add_page(PdfReader(str(PLANCHES / f"{pid}.pdf")).pages[0])
        ecrivain.add_outline_item(titre, len(ecrivain.pages) - 1)
    with open(SORTIE_PDF, "wb") as f:
        ecrivain.write(f)
    print(f"{len(NOEUDS)} nœuds ({nb['action']} actions, {nb['decision']} décisions ou fusions, {nb['fourche']} fourches, "
          f"{nb['envoi']} envois, {nb['reception']} réceptions, {nb['temps']} événements temporels), {len(FLOTS)} flots, {len(COULOIRS)} couloirs.")
    print(f"Diagrammes de phase : {PLANCHES} (PH0 à PH6, .dot et .svg). PDF : {SORTIE_PDF}")


if __name__ == "__main__":
    construire()
