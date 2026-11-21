"""Exporte le diagramme d'activité UML complet en un seul fichier draw.io d'une page.

Usage : python3 _modélisation/outils/generer_activite_drawio.py

Sortie : _modélisation/Waɖɛ_Diagramme_activite.drawio

Mise en page :
  - un « pool » UML avec un couloir horizontal par acteur, sur toute la largeur ; chaque forme est
    enfant de son couloir (déplacer un couloir déplace ses formes) ;
  - les 7 phases se suivent de gauche à droite, avec un bandeau de titre et un séparateur ;
  - l'ordre des formes dans une phase vient de Graphviz (dot -Tjson, flux de gauche à droite) ;
    la hauteur de chaque forme est fixée par son couloir, sur plusieurs lignes si nécessaire ;
  - tous les flots sont directs (pas de connecteurs), routés par draw.io (orthogonal).
Source unique : outils/activite_donnees.py.
"""
import html
import json
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

OUTILS = Path(__file__).resolve().parent
sys.path.insert(0, str(OUTILS))
from activite_donnees import COULOIRS, FLOTS, NOEUDS, PHASES, phase_de  # noqa: E402

SORTIE = OUTILS.parent / "Waɖɛ_Diagramme_activite.drawio"
EN_TETE_COULOIR = 40      # largeur du titre vertical d'un couloir
LIGNE = 96                # hauteur d'une ligne dans un couloir
MARGE_COULOIR = 22        # marge haute et basse dans un couloir
ECART_PHASE = 90          # espace entre deux phases
X0, Y_BANDEAU, Y_POOL = 40, 90, 150

TAILLES = {"debut": (26, 26), "fin": (28, 28), "finflux": (26, 26), "decision": (36, 36),
           "fourche": (8, 64), "temps": (26, 34)}


def taille_action(libelle):
    lignes = libelle.split("\n")
    largeur = max(len(l) for l in lignes) * 6.6 + 26
    return max(110, min(230, largeur)), 22 + 15 * len(lignes)


def taille(noeud):
    _, _, t, lib = noeud
    if t in TAILLES:
        return TAILLES[t]
    w, h = taille_action(lib)
    return (w + 18, h) if t in ("envoi", "reception") else (w, h)


def ordre_horizontal(pid):
    """Position horizontale de chaque forme de la phase, d'après une mise en page Graphviz de gauche à droite."""
    membres = [n for n in NOEUDS if phase_de(n[0]) == pid]
    ids = {n[0] for n in membres}
    dot = ['digraph P { graph [rankdir=LR, nodesep=0.25, ranksep=0.55]; node [shape=box, fixedsize=true];']
    for n in membres:
        w, h = taille(n)
        dot.append(f'  {n[0]} [width={w / 72:.2f}, height={h / 72:.2f}, label=""];')
    for a, b, _, _ in FLOTS:
        if a in ids and b in ids:
            dot.append(f"  {a} -> {b};")
    dot.append("}")
    sortie = subprocess.run(["dot", "-Tjson"], input="\n".join(dot), capture_output=True, text=True, check=True)
    d = json.loads(sortie.stdout)
    positions = {o["name"]: float(o["pos"].split(",")[0]) for o in d["objects"] if "pos" in o}
    gauche = min(positions[i] - taille(NOEUD[i])[0] / 2 for i in positions)
    droite = max(positions[i] + taille(NOEUD[i])[0] / 2 for i in positions)
    return {i: x - gauche for i, x in positions.items()}, droite - gauche


NOEUD = {n[0]: n for n in NOEUDS}


def style(noeud, trait, fond_couloir):
    _, _, t, _ = noeud
    if t == "debut":
        return "ellipse;html=1;aspect=fixed;fillColor=#12180E;strokeColor=#12180E;"
    if t == "fin":
        return "ellipse;html=1;shape=endState;aspect=fixed;fillColor=#12180E;strokeColor=#12180E;"
    if t == "finflux":
        return "shape=mxgraph.sysml.flowFinal;html=1;aspect=fixed;fillColor=#FFFFFF;strokeColor=#12180E;"
    if t == "decision":
        return f"rhombus;html=1;fillColor=#FFFFFF;strokeColor={trait};"
    if t == "fourche":
        return "rounded=0;html=1;fillColor=#12180E;strokeColor=none;"
    if t == "envoi":
        return "shape=mxgraph.sysml.sendSigAct;html=1;whiteSpace=wrap;fillColor=#FFF6E0;strokeColor=#B7791F;fontColor=#12180E;fontSize=11;"
    if t == "reception":
        return "shape=mxgraph.sysml.accEvent;html=1;whiteSpace=wrap;fillColor=#E4F1F4;strokeColor=#0E5F73;fontColor=#12180E;fontSize=11;"
    if t == "temps":
        return "shape=mxgraph.sysml.timeEvent;html=1;fillColor=#FFF9E0;strokeColor=#B7791F;verticalLabelPosition=bottom;verticalAlign=top;labelPosition=center;align=center;fontSize=10;fontColor=#00370B;"
    return f"rounded=1;arcSize=20;html=1;whiteSpace=wrap;fillColor=#FFFFFF;strokeColor={trait};fontColor=#12180E;fontSize=11;"


def construire():
    cellules = []

    def cellule(cid, valeur, st, x, y, w, h, parent="1", sommet=True):
        a = f"id={quoteattr(cid)} value={quoteattr(valeur)} style={quoteattr(st)} parent={quoteattr(parent)}" + (' vertex="1"' if sommet else "")
        cellules.append(f'<mxCell {a}><mxGeometry x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" as="geometry"/></mxCell>')

    # 1. Position horizontale : phases successives de gauche à droite.
    x_global, bornes_phases, curseur = {}, [], X0 + 2 * EN_TETE_COULOIR + 30
    for pid, titre, _ in PHASES:
        xs, largeur = ordre_horizontal(pid)
        for i, x in xs.items():
            x_global[i] = curseur + x
        bornes_phases.append((pid, titre, curseur, curseur + largeur))
        curseur += largeur + ECART_PHASE
    largeur_pool = curseur - X0 - ECART_PHASE + 40

    # 2. Hauteur : lignes par couloir, sans chevauchement horizontal.
    ligne_de, lignes_couloir = {}, {}
    for c, *_ in COULOIRS:
        occupees = []
        for n in sorted((n for n in NOEUDS if n[1] == c), key=lambda n: x_global[n[0]]):
            w, _ = taille(n)
            debut, fin = x_global[n[0]] - w / 2, x_global[n[0]] + w / 2
            for k, fin_ligne in enumerate(occupees):
                if debut > fin_ligne + 24:
                    occupees[k] = fin
                    ligne_de[n[0]] = k
                    break
            else:
                occupees.append(fin)
                ligne_de[n[0]] = len(occupees) - 1
        lignes_couloir[c] = max(1, len(occupees))

    # 3. Pool et couloirs (conteneurs UML), formes enfants de leur couloir.
    hauteur_pool = sum(2 * MARGE_COULOIR + LIGNE * lignes_couloir[c] for c, *_ in COULOIRS)
    cellule("titre", "<b>Waɖɛ · Diagramme d'activité UML complet</b><br><span style=\"font-size:13px;color:#5b6b5f\">Parcours complet d'une organisation · un couloir par acteur · d'après les livrables AMELEGAL v1.0</span>",
            "text;html=1;align=left;verticalAlign=top;strokeColor=none;fillColor=none;fontSize=24;fontColor=#00370B;", X0, 10, 1200, 70)
    cellule("pool", "", f"swimlane;html=1;horizontal=0;startSize={EN_TETE_COULOIR};childLayout=stackLayout;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=0;fillColor=#12180E;strokeColor=#12180E;fontColor=#FFFFFF;",
            X0, Y_POOL, largeur_pool, hauteur_pool)
    y_couloir = {}
    y = 0
    for c, nom, fond, trait in COULOIRS:
        h = 2 * MARGE_COULOIR + LIGNE * lignes_couloir[c]
        y_couloir[c] = Y_POOL + y
        cellule(f"L_{c}", f"<b>{escape(nom)}</b>",
                f"swimlane;html=1;horizontal=0;startSize={EN_TETE_COULOIR};collapsible=0;fontSize=12;fillColor={trait};swimlaneFillColor={fond};strokeColor={trait};fontColor=#FFFFFF;",
                EN_TETE_COULOIR, y, largeur_pool - EN_TETE_COULOIR, h, parent="pool")
        for n in NOEUDS:
            if n[1] != c:
                continue
            w, hn = taille(n)
            cx = x_global[n[0]] - X0 - EN_TETE_COULOIR      # relatif au couloir
            cy = MARGE_COULOIR + LIGNE * ligne_de[n[0]] + LIGNE / 2
            valeur = "<br>".join(escape(l) for l in n[3].split("\n")) if n[2] != "finflux" else ""
            cellule(f"n_{n[0]}", valeur, style(n, trait, fond), cx - w / 2, cy - hn / 2, w, hn, parent=f"L_{c}")
        y += h

    # 4. Bandeau des phases et séparateurs verticaux.
    for k, (pid, titre, g, d) in enumerate(bornes_phases):
        cellule(f"phase_{pid}", f"<b>{escape(titre)}</b>", "rounded=1;arcSize=12;html=1;fillColor=#00370B;strokeColor=#00370B;fontColor=#FFFFFF;fontSize=14;",
                g - 20, Y_BANDEAU, d - g + 40, 40)
        if k:
            xsep = g - ECART_PHASE / 2
            cellule(f"sep_{pid}", "", "line;html=1;direction=south;dashed=1;dashPattern=8 6;strokeColor=#5b6b5f;strokeWidth=1.5;",
                    xsep - 5, Y_BANDEAU, 10, Y_POOL - Y_BANDEAU + hauteur_pool)

    # 5. Flots (tous directs, routage orthogonal par draw.io).
    for k, (a, b, garde, s) in enumerate(FLOTS):
        st = "html=1;rounded=1;edgeStyle=orthogonalEdgeStyle;orthogonalLoop=1;jettySize=auto;endArrow=block;endFill=1;fontSize=10;fontColor=#00370B;labelBackgroundColor=#FFFFFF;"
        st += "dashed=1;strokeColor=#B7791F;" if s == "signal" else "strokeColor=#3f5a47;"
        valeur = "[" + "<br>".join(escape(l) for l in garde.split("\n")) + "]" if garde else ""
        cellules.append(f'<mxCell id="e_{k}" value={quoteattr(valeur)} style={quoteattr(st)} edge="1" parent="1" source="n_{a}" target="n_{b}"><mxGeometry relative="1" as="geometry"/></mxCell>')

    # 6. Légende sous le pool.
    yl = Y_POOL + hauteur_pool + 50
    cellule("leg", "<b>Notation UML</b>", "swimlane;html=1;startSize=28;fillColor=#00370B;fontColor=#FFFFFF;strokeColor=#00370B;swimlaneFillColor=#FFFFFF;rounded=1;arcSize=4;", X0, yl, 760, 330)
    elements = [("debut", "", "Début de l'activité"), ("fin", "", "Fin de l'activité"), ("finflux", "", "Fin de flot : ce chemin s'arrête"),
                ("action", "Action", "Action d'un acteur ou de Waɖɛ"), ("decision", "", "Décision ou fusion ; [garde] sur chaque flèche"),
                ("fourche", "", "Fourche / jonction : chemins en parallèle"), ("envoi", "Signal", "Envoi de signal (alerte, notification, dépôt)"),
                ("reception", "Signal", "Réception d'un signal externe"), ("temps", "", "Événement temporel (échéance, délai)")]
    for k, (t, lib, texte) in enumerate(elements):
        colonne, rang = divmod(k, 5)
        bx, by = 20 + colonne * 380, 44 + rang * 56
        n = ("L", "SYS", t, lib)
        w, h = taille(n) if t != "action" else (90, 34)
        if t in ("envoi", "reception"):
            w = 90
        cellule(f"leg_f{k}", lib, style(n, "#555555", "#FFFFFF"), bx + (100 - w) / 2, by + (40 - h) / 2, w, h, parent="leg")
        cellule(f"leg_t{k}", escape(texte), "text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=12;", bx + 110, by, 250, 40, parent="leg")
    cellule("leg_sig", "<span style=\"color:#B7791F\">- - - -&gt;</span>&nbsp; flot de signal (pointillé)", "text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=12;", 400, 44 + 4 * 56, 340, 40, parent="leg")

    largeur_page = int(largeur_pool + 2 * X0)
    hauteur_page = int(yl + 380)
    contenu = (f'<mxfile host="Waɖɛ" type="device"><diagram id="activite_complete" name="Diagramme d\'activité complet">'
               f'<mxGraphModel dx="1600" dy="1000" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
               f'pageWidth="{largeur_page}" pageHeight="{hauteur_page}" math="0" shadow="0"><root><mxCell id="0"/><mxCell id="1" parent="0"/>'
               + "".join(cellules) + "</root></mxGraphModel></diagram></mxfile>")
    SORTIE.write_text(contenu, encoding="utf-8")
    verifier(contenu)
    print(f"{len(NOEUDS)} formes, {len(FLOTS)} flots, {len(COULOIRS)} couloirs, {len(PHASES)} phases sur une page de {largeur_page} × {hauteur_page} px.")
    print(f"Fichier draw.io écrit : {SORTIE}")


def verifier(contenu):
    import xml.etree.ElementTree as ET
    from collections import Counter
    racine = ET.fromstring(contenu)
    cellules = racine.findall(".//mxCell")
    ids = [c.get("id") for c in cellules]
    connus = set(ids)
    erreurs = [f"identifiant en double : {i}" for i, n in Counter(ids).items() if n > 1]
    erreurs += [f"parent absent pour {c.get('id')}" for c in cellules if c.get("parent") and c.get("parent") not in connus]
    erreurs += [f"lien orphelin {c.get('id')}" for c in cellules if c.get("edge") == "1" and (c.get("source") not in connus or c.get("target") not in connus)]
    formes = sum(1 for c in cellules if (c.get("id") or "").startswith("n_"))
    liens = sum(1 for c in cellules if c.get("edge") == "1")
    if formes != len(NOEUDS):
        erreurs.append(f"{formes} formes au lieu de {len(NOEUDS)}")
    if liens != len(FLOTS):
        erreurs.append(f"{liens} liens au lieu de {len(FLOTS)}")
    if erreurs:
        raise SystemExit("Fichier incohérent :\n  " + "\n  ".join(erreurs))


if __name__ == "__main__":
    construire()
