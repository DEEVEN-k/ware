"""Exporte les diagrammes de Waɖɛ au format draw.io (diagrams.net), en formes modifiables.

Usage : python3 _modélisation/outils/generer_drawio.py

Produit _modélisation/Waɖɛ_Modélisation.drawio, un fichier de plusieurs pages :
  1. Diagramme de classes complet (formes « classe UML », un champ par ligne)
  2. Diagramme de flux complet
  3 à 9. Diagramme d'activité UML, une page par phase (couloirs, formes UML/SysML natives)

Les positions viennent de la mise en page Graphviz (dot -Tjson) des fichiers .dot déjà
produits par les autres générateurs : lancer ceux-ci d'abord. Dans draw.io : Fichier > Ouvrir,
ou glisser le fichier dans la fenêtre ; chaque page est un onglet en bas de l'écran.
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from xml.sax.saxutils import escape, quoteattr

OUTILS = Path(__file__).resolve().parent
DOSSIER = OUTILS.parent
PLANCHES = DOSSIER / "planches"
SORTIE = DOSSIER / "Waɖɛ_Modélisation.drawio"
sys.path.insert(0, str(OUTILS))

import generer_classes_complet as gc  # noqa: E402
from activite_donnees import PHASES  # noqa: E402

PAGES = [("Classes (complet)", PLANCHES / "Waɖɛ_Diagramme_de_classes_complet.dot", "classes"),
         ("Flux complet", PLANCHES / "Waɖɛ_Flux_complet.dot", "flux")] + [
    (f"Activité · {titre}", PLANCHES / "activite" / f"{pid}.dot", "activite") for pid, titre, _ in PHASES]


def mise_en_page(fichier: Path) -> dict:
    texte = fichier.read_text(encoding="utf-8")
    sortie = subprocess.run(["dot", "-Tjson"], input=texte, capture_output=True, text=True)
    if sortie.returncode != 0:  # même contournement que les générateurs (bug « newrank » de Graphviz 2.43)
        sortie = subprocess.run(["dot", "-Tjson"], input=texte.replace("newrank=true, ", ""), capture_output=True, text=True, check=True)
    return json.loads(sortie.stdout)


def html_drawio(label: str) -> str:
    """Libellé Graphviz (pseudo-HTML) vers HTML draw.io."""
    t = label or ""
    t = re.sub(r"<BR\s*/?>", "<br>", t, flags=re.I)
    t = re.sub(r"</?(B|I)>", lambda m: m.group(0).lower(), t)
    t = re.sub(r"<FONT[^>]*>|</FONT>", "", t, flags=re.I)
    return t.replace("\\n", "<br>")


def generiques(m: str) -> str:
    precedent = None
    while precedent != m:
        precedent = m
        m = re.sub(r"(\w+)~([^~]*)~(?!\w)", r"\1<\2>", m)
    return m


def pt(valeur: str):
    x, y = valeur.split(",")[:2]
    return float(x), float(y)


class Page:
    def __init__(self, nom, donnees):
        self.nom = nom
        self.d = donnees
        x1, y1, x2, y2 = (float(v) for v in donnees["bb"].split(","))
        self.hauteur = y2
        self.largeur = x2
        self.cellules = []
        self.ids = {}

    def y(self, y):
        return self.hauteur - y

    def cellule(self, cid, valeur, style, x, y, w, h, parent="1", sommet=True):
        attrs = f'id={quoteattr(cid)} value={quoteattr(valeur)} style={quoteattr(style)} parent={quoteattr(parent)}'
        attrs += ' vertex="1"' if sommet else ""
        self.cellules.append(f'<mxCell {attrs}><mxGeometry x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" as="geometry"/></mxCell>')

    def xml(self):
        corps = "".join(self.cellules)
        return (f'<diagram id={quoteattr(re.sub(r"[^A-Za-z0-9]", "_", self.nom))} name={quoteattr(self.nom)}>'
                f'<mxGraphModel dx="1400" dy="900" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" '
                f'pageWidth="{int(self.largeur) + 40}" pageHeight="{int(self.hauteur) + 40}" math="0" shadow="0">'
                f'<root><mxCell id="0"/><mxCell id="1" parent="0"/>{corps}</root></mxGraphModel></diagram>')


def style_noeud(o, famille):
    forme = o.get("shape", "ellipse")
    remplissage = o.get("fillcolor", "#FFFFFF")
    trait = o.get("color", "#333333")
    police = o.get("fontcolor", "#12180E")
    commun = f"html=1;whiteSpace=wrap;fillColor={remplissage};strokeColor={trait};fontColor={police};fontSize={o.get('fontsize', '11')};"
    tirets = "dashed=1;" if "dashed" in o.get("style", "") else ""
    if forme == "box":
        arrondi = "rounded=1;arcSize=18;" if "rounded" in o.get("style", "") else "rounded=0;"
        if remplissage.upper() == "#12180E" and float(o.get("height", "1")) < 0.15:  # fourche / jonction
            return "rounded=0;html=1;fillColor=#12180E;strokeColor=none;", ""
        return arrondi + commun + tirets, None
    if forme == "diamond":
        return "rhombus;" + commun, None
    if forme == "circle":
        if o.get("label") == "×":
            return "shape=mxgraph.sysml.flowFinal;html=1;fillColor=#FFFFFF;strokeColor=#12180E;", ""
        if famille == "activite" and "#00901D" in trait:  # connecteur
            return "ellipse;aspect=fixed;html=1;fillColor=#EAF5EC;strokeColor=#00901D;", ""
        return "ellipse;aspect=fixed;html=1;fillColor=#12180E;strokeColor=#12180E;", ""
    if forme == "doublecircle":
        return "ellipse;shape=endState;aspect=fixed;html=1;fillColor=#12180E;strokeColor=#12180E;", ""
    if forme == "oval":
        return "ellipse;" + commun, None
    if forme == "cds":
        return "shape=mxgraph.sysml.sendSigAct;" + commun, None
    if forme == "larrow":
        return "shape=mxgraph.sysml.accEvent;" + commun, None
    if forme == "invtriangle":
        return "shape=mxgraph.sysml.timeEvent;html=1;fillColor=#FFF9E0;strokeColor=#B7791F;", ""
    if forme in ("plaintext", "plain", "none"):
        return "text;html=1;align=center;verticalAlign=middle;strokeColor=none;fillColor=none;", None
    return "rounded=1;" + commun, None


def ajouter_grappes(page, famille):
    """Couloirs (activité), phases (flux) ou modules (classes) : des conteneurs derrière les formes."""
    for o in page.d.get("objects", []):
        if not o.get("name", "").startswith("cluster_") or "bb" not in o:
            continue
        x1, y1, x2, y2 = (float(v) for v in o["bb"].split(","))
        cid = "c_" + o["name"][8:]
        titre = html_drawio(o.get("label", ""))
        if famille == "activite":
            style = (f"swimlane;horizontal=0;startSize=30;html=1;fontStyle=1;fontSize=13;swimlaneLine=1;"
                     f"fillColor={o.get('color', '#888888')};swimlaneFillColor={o.get('fillcolor', '#FFFFFF')};"
                     f"strokeColor={o.get('color', '#888888')};fontColor=#FFFFFF;")
        else:
            style = (f"swimlane;startSize=28;html=1;fontStyle=1;fontSize=14;rounded=1;arcSize=2;"
                     f"fillColor={o.get('color', '#8fa596')};swimlaneFillColor={o.get('fillcolor', '#FAFCFA')};"
                     f"strokeColor={o.get('color', '#8fa596')};fontColor=#FFFFFF;")
        page.cellule(cid, titre, style, x1, page.y(y2), x2 - x1, y2 - y1)


def classe_uml(page, o, membres):
    """Une classe UML draw.io : en-tête, puis un champ par ligne, séparateur avant les méthodes."""
    nom = o["name"]
    w = float(o["width"]) * 72
    cx, cy = pt(o["pos"])
    stereo = next((m for m in membres if m.startswith("<<")), None)
    corps = [m for m in membres if not m.startswith("<<")]
    attributs = [m for m in corps if "(" not in m]
    methodes = [m for m in corps if "(" in m]
    entete = 40 if stereo else 26
    hauteur = entete + 18 * max(1, len(attributs)) + (8 + 18 * len(methodes) if methodes else 0)
    x, y = cx - w / 2, page.y(cy) - hauteur / 2
    fond = "#5b6b5f" if stereo and "enumeration" in stereo else ("#B7791F" if stereo else "#00370B")
    titre = (f"«{escape(stereo.strip('<>'))}»<br>" if stereo else "") + f"<b>{escape(nom)}</b>"
    page.cellule(f"n_{nom}", titre, f"swimlane;fontStyle=0;childLayout=stackLayout;horizontal=1;startSize={entete};horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;html=1;fillColor={fond};fontColor=#FFFFFF;strokeColor={fond};swimlaneFillColor=#FFFFFF;", x, y, w, hauteur)
    ligne = "text;strokeColor=none;fillColor=none;align=left;verticalAlign=middle;spacingLeft=6;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;html=1;fontSize=11;"
    yy = entete
    for k, m in enumerate(attributs or [""]):
        page.cellule(f"n_{nom}_a{k}", escape(generiques(m)), ligne, 0, yy, w, 18, parent=f"n_{nom}")
        yy += 18
    if methodes:
        page.cellule(f"n_{nom}_sep", "", "line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;", 0, yy, w, 8, parent=f"n_{nom}")
        yy += 8
        for k, m in enumerate(methodes):
            page.cellule(f"n_{nom}_m{k}", escape(generiques(m)), ligne, 0, yy, w, 18, parent=f"n_{nom}")
            yy += 18


def ajouter_noeuds(page, famille, membres_classes):
    for o in page.d.get("objects", []):
        nom = o.get("name", "")
        if nom.startswith("cluster_") or "pos" not in o:
            continue
        if "invis" in o.get("style", "") or (o.get("shape") == "point" and float(o.get("width", "1")) < 0.05):
            continue
        page.ids[o["_gvid"]] = f"n_{nom}"
        if famille == "classes" and nom in membres_classes:
            classe_uml(page, o, membres_classes[nom])
            continue
        w, h = float(o["width"]) * 72, float(o["height"]) * 72
        cx, cy = pt(o["pos"])
        style, valeur_forcee = style_noeud(o, famille)
        valeur = valeur_forcee if valeur_forcee is not None else html_drawio(o.get("label", ""))
        if valeur == "\\N":
            valeur = ""
        page.cellule(f"n_{nom}", valeur, style, cx - w / 2, page.y(cy) - h / 2, w, h)
        if o.get("xlabel") and o.get("xlp"):
            lx, ly = pt(o["xlp"])
            page.cellule(f"x_{nom}", html_drawio(o["xlabel"]), "text;html=1;align=center;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=10;fontColor=#00370B;", lx - 70, page.y(ly) - 14, 140, 28)


def ajouter_aretes(page, famille):
    for k, e in enumerate(page.d.get("edges", [])):
        if "invis" in e.get("style", ""):
            continue
        source, cible = page.ids.get(e["tail"]), page.ids.get(e["head"])
        if not source or not cible:
            continue
        style = "html=1;rounded=1;endArrow=block;endFill=1;fontSize=9;fontColor=#00370B;"
        couleur = e.get("color", "#3f5a47")
        style += f"strokeColor={couleur};"
        if "dashed" in e.get("style", ""):
            style += "dashed=1;"
        if e.get("dir") == "none":
            style += "endArrow=none;"
        elif e.get("dir") == "both":
            style += "startArrow=block;startFill=1;"
        elif e.get("dir") == "back":
            fleche = e.get("arrowtail", "normal")
            style += "endArrow=none;" + {"diamond": "startArrow=diamondThin;startFill=1;startSize=14;", "odiamond": "startArrow=diamondThin;startFill=0;startSize=14;"}.get(fleche, "startArrow=block;startFill=1;")
        if e.get("arrowhead") == "vee":
            style += "endArrow=open;endFill=0;"
        points = []
        if e.get("pos"):
            morceaux = [m for m in e["pos"].split() if not m.startswith(("e,", "s,"))]
            interieurs = morceaux[1:-1]
            points = [pt(p) for p in interieurs[2::3]] if len(interieurs) > 2 else []
        style += "curved=1;" if points else "edgeStyle=orthogonalEdgeStyle;"
        geo = '<mxGeometry relative="1" as="geometry">'
        if points:
            geo += "<Array as=\"points\">" + "".join(f'<mxPoint x="{x:.1f}" y="{page.y(y):.1f}"/>' for x, y in points) + "</Array>"
        geo += "</mxGeometry>"
        valeur = html_drawio(e.get("label", ""))
        eid = f"e_{k}"
        page.cellules.append(f'<mxCell id="{eid}" value={quoteattr(valeur)} style={quoteattr(style)} edge="1" parent="1" source={quoteattr(source)} target={quoteattr(cible)}>{geo}</mxCell>')
        for cle, position in (("taillabel", -0.85), ("headlabel", 0.85)):
            if e.get(cle):
                page.cellules.append(
                    f'<mxCell id="{eid}_{cle}" value={quoteattr(escape(e[cle]))} style="edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontStyle=1;" vertex="1" connectable="0" parent="{eid}">'
                    f'<mxGeometry x="{position}" relative="1" as="geometry"><mxPoint as="offset"/></mxGeometry></mxCell>')


def titre_page(page):
    titre = html_drawio(page.d.get("label", ""))
    if titre and page.d.get("lp"):
        lx, ly = pt(page.d["lp"])
        page.cellule("titre", titre, "text;html=1;align=left;verticalAlign=middle;strokeColor=none;fillColor=none;fontSize=20;fontColor=#00370B;", 20, page.y(ly) - 20, max(600, page.largeur * 0.6), 40)


def membres_des_classes():
    md = (DOSSIER / "02-diagrammes-de-classes.md").read_text(encoding="utf-8")
    membres = {}
    for _, bloc in gc.blocs_par_section(md):
        classes, _ = gc.decouper(bloc)
        membres.update(classes)
    return membres


def main():
    manquants = [str(f) for _, f, _ in PAGES if not f.exists()]
    if manquants:
        raise SystemExit("Fichiers .dot manquants (lancer d'abord les autres générateurs) :\n  " + "\n  ".join(manquants))
    membres = membres_des_classes()
    pages = []
    for nom, fichier, famille in PAGES:
        page = Page(nom, mise_en_page(fichier))
        ajouter_grappes(page, famille)
        ajouter_noeuds(page, famille, membres)
        ajouter_aretes(page, famille)
        titre_page(page)
        pages.append(page)
    contenu = '<mxfile host="Waɖɛ" type="device">' + "".join(p.xml() for p in pages) + "</mxfile>"
    SORTIE.write_text(contenu, encoding="utf-8")
    from xml.dom import minidom
    minidom.parseString(contenu.encode("utf-8"))  # échoue si le XML est mal formé
    for p in pages:
        sommets = sum(1 for c in p.cellules if 'vertex="1"' in c)
        aretes = sum(1 for c in p.cellules if 'edge="1"' in c)
        print(f"  {p.nom} : {sommets} formes, {aretes} liens")
    print(f"Fichier draw.io écrit : {SORTIE}")


if __name__ == "__main__":
    main()
