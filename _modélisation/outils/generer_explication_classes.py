"""Génère le PDF « Diagramme de classes expliqué » : chaque classe, chaque champ et chaque
relation, avec la raison de leur présence.

Usage : python3 _modélisation/outils/generer_explication_classes.py

Les classes, champs et relations sont lus dans 02-diagrammes-de-classes.md (source unique).
Les explications sont dans _modélisation/explications/. Le script échoue si un élément du
modèle n'est pas expliqué, ou si une explication ne correspond plus à rien : le document
reste ainsi complet et synchronisé avec le modèle.
"""
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

import generer_classes_complet as g  # noqa: E402
from acces import CLASSES as C1  # noqa: E402
from metier import CLASSES as C3  # noqa: E402
from referentiels import CLASSES as C2  # noqa: E402
from relations import RELATIONS  # noqa: E402

EXPLICATIONS = {**C1, **C2, **C3}
SORTIE_HTML = OUTILS / "vendor" / "explication_classes.html"
SORTIE_PDF = DOSSIER / "Waɖɛ_Diagramme_de_classes_explique.pdf"
LOGO = DOSSIER.parent / "00 Commun aux deux pays" / "01 Ware identité visuelle" / "LOGOTYPE HORIZONTALE.png"

INTRO_MODULE = {
    "Acces": "Qui se connecte, pour quelle structure, avec quels droits, et dans quelles limites un cabinet peut agir chez un client. Sources : G04 (habilitations) et G05 (mandats).",
    "Referentiels": "Le droit de chaque pays, sous forme de données versionnées : régimes, logigramme, autorité, AIPD, violations, indice. Règle cardinale de la notice : aucune valeur juridique dans le code.",
    "Moteur": "Le moteur de qualification et son résultat. Il ne fait que lire un référentiel et des valeurs, ce qui le rend testable avec les cas de recette.",
    "Registre": "Le registre des traitements : fiches, qualifications, sous-traitance, transferts, pièces jointes.",
    "Formalites": "Les dossiers déposés auprès de l'autorité et les documents produits.",
    "Aipd": "Les analyses d'impact sur la protection des données.",
    "Violations": "Les violations de données, de la déclaration à la clôture.",
    "Pilotage": "Alertes, tâches, notifications, paramètres, indice de conformité et journal.",
}
NOTATION = {
    "*--": ("Composition", "◆"),
    "o--": ("Agrégation", "◇"),
    "--": ("Association", "—"),
    "-->": ("Association orientée", "→"),
    "..>": ("Dépendance", "⇢"),
}


def generiques(t: str) -> str:
    precedent = None
    while precedent != t:
        precedent = t
        t = re.sub(r"(\w+)~([^~]*)~(?!\w)", r"\1<\2>", t)
    return t


def analyser_membre(m: str):
    """Rend (clé principale, clé de secours, type affiché) pour un membre Mermaid."""
    m = m.lstrip("+")
    if "(" in m:
        signature = m[: m.index(")") + 1]
        nom = m[: m.index("(")]
        retour = m[m.index(")") + 1:].strip()
        return signature, f"{nom}()", ("méthode" + (f" → {generiques(retour)}" if retour else ""))
    type_, _, nom = m.rpartition(" ")
    return nom, nom, generiques(type_)


def charger_modele():
    modules = {m: {} for m in g.ORDRE_MODULES}
    relations = []
    for numero, bloc in g.blocs_par_section((DOSSIER / "02-diagrammes-de-classes.md").read_text(encoding="utf-8")):
        classes, rels = g.decouper(bloc)
        for nom, corps in classes.items():
            module = g.MODULE_PAR_CLASSE.get(nom) or g.MODULE_PAR_SECTION.get(numero)
            modules[module][nom] = corps
        relations += rels
    relations += [r.strip() for r in g.LIENS_INTER_MODULES]
    return modules, list(dict.fromkeys(relations))


def verifier(modules, relations, enumerations):
    erreurs = []
    toutes = {n: c for cls in modules.values() for n, c in cls.items()}
    for nom, corps in toutes.items():
        e = EXPLICATIONS.get(nom)
        if not e:
            erreurs.append(f"Classe non expliquée : {nom}")
            continue
        if nom in enumerations:
            for v in corps[1:]:
                if v not in e.get("valeurs", {}):
                    erreurs.append(f"Valeur non expliquée : {nom}.{v}")
            for v in e.get("valeurs", {}):
                if v not in corps:
                    erreurs.append(f"Explication sans valeur : {nom}.{v}")
        else:
            membres = [c for c in corps if not c.startswith("<<")]
            cles = set()
            for m in membres:
                principale, secours, _ = analyser_membre(m)
                cles |= {principale, secours}
                if principale not in e.get("champs", {}) and secours not in e.get("champs", {}):
                    erreurs.append(f"Champ non expliqué : {nom}.{principale}")
            for c in e.get("champs", {}):
                if c not in cles:
                    erreurs.append(f"Explication sans champ : {nom}.{c}")
    for nom in EXPLICATIONS:
        if nom not in toutes:
            erreurs.append(f"Explication d'une classe absente du modèle : {nom}")
    for r in relations:
        if r not in RELATIONS and not relation_auto(r, enumerations, toutes):
            erreurs.append(f"Relation non expliquée : {r}")
    for r in RELATIONS:
        if r not in relations:
            erreurs.append(f"Explication d'une relation absente du modèle : {r}")
    if erreurs:
        raise SystemExit("Document incomplet :\n  " + "\n  ".join(erreurs))


def relation_auto(r, enumerations, toutes):
    m = g.MOTIF_RELATION.match(r)
    a, _, type_rel, _, b, libelle = m.groups()
    if type_rel != "..>" or libelle or b not in enumerations:
        return None
    champs = [analyser_membre(c)[0] for c in toutes[a] if not c.startswith("<<") and re.search(rf"\b{b}\b", c)]
    cible = f"du champ {', '.join(champs)}" if champs else "de ses champs"
    return f"{a} utilise l'énumération {b} comme type {cible} : les valeurs possibles sont fixées et contrôlées."


def lire_relation(r):
    a, mult_a, type_rel, mult_b, b, libelle = g.MOTIF_RELATION.match(r).groups()
    nom_type, symbole = NOTATION[type_rel]
    texte = f"<b>{a}</b>"
    if mult_a:
        texte += f" <span class='m'>{mult_a}</span>"
    texte += f" <span class='s'>{symbole}</span> "
    if mult_b:
        texte += f"<span class='m'>{mult_b}</span> "
    texte += f"<b>{b}</b>"
    if libelle:
        texte += f"<br><i>{html.escape(libelle)}</i>"
    return a, b, nom_type, texte


def svg_module(module, classes, relations, enumerations):
    """Schéma compact d'un module : noms de classes et relations internes."""
    services = {n for n, c in classes.items() if "<<service>>" in c}
    dot = [
        "digraph M {",
        '  graph [rankdir=LR, fontname="DejaVu Sans", pad=0.2, nodesep=0.25, ranksep=0.5, bgcolor="transparent"];',
        '  node [shape=box, style="rounded,filled", fontname="DejaVu Sans", fontsize=11, margin="0.12,0.06"];',
        '  edge [fontname="DejaVu Sans", fontsize=8, color="#3f5a47", fontcolor="#3f5a47", arrowsize=0.7];',
    ]
    for n in classes:
        if n in enumerations:
            dot.append(f'  {n} [fillcolor="#e9ecea", color="#7b857e", fontcolor="#26302a", label=<<FONT POINT-SIZE="8">«énumération»</FONT><BR/>{n}>];')
        elif n in services:
            dot.append(f'  {n} [fillcolor="#FFF1D6", color="#B7791F", fontcolor="#5a3d0a", label=<<FONT POINT-SIZE="8">«service»</FONT><BR/><B>{n}</B>>];')
        else:
            dot.append(f'  {n} [fillcolor="#00370B", color="#00370B", fontcolor="white", label=<<B>{n}</B>>];')
    for r in relations:
        a, *_ , b, _ = g.MOTIF_RELATION.match(r).groups()
        if a in classes and b in classes:
            dot.append(g.arete_dot(r, enumerations).replace("    ", "  ", 1))
    dot.append("}")
    svg = subprocess.run(["dot", "-Tsvg"], input="\n".join(dot), capture_output=True, text=True, check=True).stdout
    return svg[svg.index("<svg"):]


def construire():
    modules, relations = charger_modele()
    enumerations = {n for cls in modules.values() for n, c in cls.items() if "<<enumeration>>" in c}
    verifier(modules, relations, enumerations)
    toutes = {n: c for cls in modules.values() for n, c in cls.items()}
    module_de = {n: m for m, cls in modules.items() for n in cls}

    nb_classes = len(toutes)
    nb_enums = len(enumerations)
    nb_champs = sum(len([c for c in corps if not c.startswith("<<")]) for n, corps in toutes.items() if n not in enumerations)

    corps = []
    sommaire = []
    for i, module in enumerate(g.ORDRE_MODULES, start=1):
        classes = modules[module]
        rels = [r for r in relations if module_de[g.MOTIF_RELATION.match(r).group(1)] == module]
        sommaire.append(f"<li>{html.escape(g.LIBELLE_MODULE[module])} <span class='muted'>({len(classes)} classes, {len(rels)} relations)</span></li>")
        corps.append(f"<section class='module'><h1>{i}. {html.escape(g.LIBELLE_MODULE[module])}</h1>")
        corps.append(f"<p class='intro'>{html.escape(INTRO_MODULE[module])}</p>")
        corps.append(f"<div class='schema'>{svg_module(module, classes, relations, enumerations)}</div>")
        corps.append("<p class='legende'>Schéma du module : vert foncé = classe, gris = énumération, orangé = service. Seules les relations internes au module sont dessinées ; les liens vers d'autres modules sont listés dans le tableau des relations.</p>")
        corps.append("<h2>Classes</h2>")
        for nom, membres in classes.items():
            e = EXPLICATIONS[nom]
            stereo = "énumération" if nom in enumerations else ("service" if "<<service>>" in membres else "classe")
            corps.append(f"<div class='classe'><h3>{nom} <span class='badge {stereo}'>{stereo}</span></h3>")
            corps.append(f"<p class='role'>{html.escape(e['role'])}</p>")
            if nom in enumerations:
                lignes = "".join(f"<tr><td class='n'>{v}</td><td>{html.escape(t)}</td></tr>" for v, t in e["valeurs"].items())
                corps.append(f"<table><thead><tr><th style='width:28%'>Valeur</th><th>Signification</th></tr></thead><tbody>{lignes}</tbody></table>")
            else:
                lignes = []
                for m in membres:
                    if m.startswith("<<"):
                        continue
                    principale, secours, type_ = analyser_membre(m)
                    texte = e["champs"].get(principale) or e["champs"][secours]
                    nom_aff = principale if "(" not in principale else secours
                    lignes.append(f"<tr><td class='n'>{html.escape(nom_aff)}</td><td class='t'>{html.escape(type_)}</td><td>{html.escape(texte)}</td></tr>")
                corps.append(f"<table><thead><tr><th style='width:22%'>Champ</th><th style='width:20%'>Type</th><th>Pourquoi</th></tr></thead><tbody>{''.join(lignes)}</tbody></table>")
            corps.append("</div>")
        corps.append("<h2>Relations</h2>")
        lignes = []
        for r in rels:
            a, b, nom_type, texte = lire_relation(r)
            pourquoi = RELATIONS.get(r) or relation_auto(r, enumerations, toutes)
            autre = module_de[b]
            note = f"<br><span class='muted'>vers le module {html.escape(g.LIBELLE_MODULE[autre].split(' :')[0])}</span>" if autre != module else ""
            lignes.append(f"<tr><td>{texte}{note}</td><td>{nom_type}</td><td>{html.escape(pourquoi)}</td></tr>")
        corps.append(f"<table class='rel'><thead><tr><th style='width:34%'>Relation</th><th style='width:14%'>Nature</th><th>Pourquoi</th></tr></thead><tbody>{''.join(lignes)}</tbody></table>")
        corps.append("</section>")

    logo = ""
    if LOGO.exists():
        import base64
        logo = "data:image/png;base64," + base64.b64encode(LOGO.read_bytes()).decode()
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Waɖɛ – Diagramme de classes expliqué</title>
<style>
@page {{ size: A4; margin: 16mm 14mm 16mm 14mm; }}
:root {{ --dark:#00370B; --green:#00901D; --light:#EAF5EC; --ink:#1d2a20; --muted:#5b6b5f; --line:#cfdcd2; }}
body {{ font-family: "DejaVu Sans", Arial, sans-serif; color: var(--ink); font-size: 8.8pt; line-height: 1.42; margin: 0; background: #fff; }}
h1 {{ color: var(--dark); font-size: 17pt; border-bottom: 2px solid var(--green); padding-bottom: 4px; margin: 0 0 6px; }}
h2 {{ color: var(--dark); font-size: 12.5pt; margin: 14px 0 6px; break-after: avoid; }}
h3 {{ color: var(--dark); font-size: 10.5pt; margin: 0 0 3px; break-after: avoid; }}
.module {{ break-before: page; }}
.intro {{ font-size: 9.6pt; background: var(--light); border-left: 3px solid var(--green); padding: 6px 10px; margin: 6px 0 8px; }}
.schema {{ text-align: center; margin: 4px 0; break-inside: avoid; }}
.schema svg {{ max-width: 100%; max-height: 200mm; height: auto; width: auto; }}
.legende, .muted {{ color: var(--muted); font-size: 7.8pt; }}
.classe {{ margin: 10px 0 12px; }}
.role {{ margin: 0 0 4px; }}
.badge {{ font-size: 7pt; font-weight: 600; padding: 1px 6px; border-radius: 8px; vertical-align: middle; }}
.badge.classe {{ background: #dff0e3; color: #0b6b22; }} .badge.énumération {{ background: #e9ecea; color: #3b463f; }} .badge.service {{ background: #FFF1D6; color: #8a5a10; }}
table {{ width: 100%; border-collapse: collapse; font-size: 8.2pt; margin: 2px 0 6px; }}
th {{ background: var(--dark); color: #fff; text-align: left; padding: 3px 6px; font-weight: 600; }}
td {{ border-bottom: 1px solid var(--line); padding: 3px 6px; vertical-align: top; }}
tr {{ break-inside: avoid; }}
td.n {{ font-family: "DejaVu Sans Mono", monospace; font-size: 7.8pt; font-weight: 600; color: var(--dark); }}
td.t {{ font-family: "DejaVu Sans Mono", monospace; font-size: 7.4pt; color: #345; }}
table.rel td {{ font-size: 8pt; }}
.m {{ font-family: "DejaVu Sans Mono", monospace; font-size: 7.4pt; background: #f1f4f2; padding: 0 3px; border-radius: 3px; }}
.s {{ color: var(--green); font-weight: 700; }}
.cover {{ height: 255mm; display: flex; flex-direction: column; justify-content: space-between; }}
.cover img {{ width: 70mm; }}
.cover .k {{ color: var(--green); font-weight: 700; letter-spacing: .14em; text-transform: uppercase; font-size: 9pt; }}
.cover h1 {{ border: 0; font-size: 26pt; margin: 6px 0 10px; }}
.cover .lead {{ font-size: 11.5pt; color: var(--muted); }}
.cover .chiffres {{ display: flex; gap: 10px; margin-top: 12mm; }}
.cover .chiffres div {{ border: 1px solid var(--line); border-radius: 6px; padding: 8px 12px; min-width: 32mm; }}
.cover .chiffres b {{ display: block; font-size: 18pt; color: var(--dark); }}
.cover .meta {{ font-size: 8.4pt; color: var(--muted); border-top: 1px solid var(--line); padding-top: 6px; }}
.page {{ break-before: page; }}
.note {{ background: var(--light); border-left: 3px solid var(--green); padding: 6px 10px; margin: 6px 0; break-inside: avoid; }}
code {{ font-family: "DejaVu Sans Mono", monospace; font-size: 8pt; background: #f1f4f2; padding: 0 3px; border-radius: 3px; }}
</style></head><body>
<div class="cover"><div>{f'<img src="{logo}">' if logo else ''}</div>
<div><div class="k">Dossier de conception</div><h1>Le diagramme de classes expliqué</h1>
<p class="lead">Chaque classe, chaque champ et chaque relation du modèle de Waɖɛ, avec la raison de sa présence : la règle de gestion, le livrable ou l'exigence qui le justifie.</p>
<div class="chiffres"><div><b>{nb_classes}</b>classes et énumérations</div><div><b>{nb_champs}</b>champs et méthodes</div><div><b>{len(relations)}</b>relations</div><div><b>{len(g.ORDRE_MODULES)}</b>modules</div></div></div>
<div class="meta">Établi d'après les livrables AMELEGAL v1.0 (septembre 2026) et la modélisation du dossier <code>_modélisation/</code>. Backend ASP.NET Core (.NET 10), PostgreSQL. Généré le {date.today().strftime('%d/%m/%Y')} : le contenu est lu directement dans le modèle, et la génération échoue si un élément n'est pas expliqué.</div></div>

<div class="page"><h1>Comment lire ce document</h1>
<p>Le modèle est découpé en {len(g.ORDRE_MODULES)} modules, qui correspondent aux modules de la solution .NET. Pour chaque module : un schéma, puis chaque classe avec le rôle de la classe et le tableau de ses champs, puis le tableau des relations.</p>
<h2>Notation des relations</h2>
<table><thead><tr><th style="width:8%">Signe</th><th style="width:22%">Nature</th><th>Signification</th></tr></thead><tbody>
<tr><td class="s">◆</td><td>Composition</td><td>La partie n'existe pas sans le tout et disparaît avec lui (exemple : les sections d'une AIPD).</td></tr>
<tr><td class="s">◇</td><td>Agrégation</td><td>Le tout regroupe des parties qui gardent leur propre existence (exemple : les pièces jointes d'une fiche).</td></tr>
<tr><td class="s">—</td><td>Association</td><td>Lien entre deux objets indépendants (exemple : une organisation et ses mandats).</td></tr>
<tr><td class="s">→</td><td>Association orientée</td><td>Le premier objet connaît le second, pas l'inverse (exemple : une qualification connaît sa version de référentiel).</td></tr>
<tr><td class="s">⇢</td><td>Dépendance</td><td>Le premier utilise le second sans le posséder (un type énuméré, un service qui lit une configuration).</td></tr>
</tbody></table>
<h2>Multiplicités</h2>
<table><thead><tr><th style="width:12%">Notation</th><th>Signification</th></tr></thead><tbody>
<tr><td class="n">1</td><td>Exactement un.</td></tr><tr><td class="n">0..1</td><td>Zéro ou un (facultatif).</td></tr>
<tr><td class="n">*</td><td>Zéro, un ou plusieurs.</td></tr><tr><td class="n">1..*</td><td>Au moins un.</td></tr>
<tr><td class="n">2, 4</td><td>Nombre exact (deux branches par question, quatre sections par AIPD).</td></tr></tbody></table>
<h2>Types</h2>
<p>Les types sont ceux de C# : <code>Guid</code> (identifiant technique), <code>string</code>, <code>int</code>, <code>decimal</code>, <code>bool</code>, <code>DateOnly</code> (date), <code>DateTimeOffset</code> (date et heure avec fuseau), <code>List&lt;T&gt;</code> et <code>Set&lt;T&gt;</code> (listes), <code>JsonDocument</code> (données JSON, stockées en JSONB dans PostgreSQL). Un <code>?</code> signale un champ facultatif.</p>
<div class="note"><b>Trois principes reviennent dans tout le modèle.</b> (1) <b>Aucune règle juridique dans le code</b> : elles vivent dans les référentiels versionnés. (2) <b>Rien n'est modifié en place quand cela doit rester prouvable</b> : qualifications, versions de référentiel et de formulaire, journal. (3) <b>Toute donnée métier porte l'organisation</b>, pour un cloisonnement strict entre clients.</div>
<h2>Sommaire</h2><ol>{''.join(sommaire)}<li>Points ouverts</li></ol></div>

{''.join(corps)}

<section class="module"><h1>{len(g.ORDRE_MODULES) + 1}. Points ouverts</h1>
<p>Relevés en relisant le modèle ; à trancher avant l'implémentation.</p>
<table><thead><tr><th style="width:4%">#</th><th style="width:36%">Point</th><th>Proposition</th></tr></thead><tbody>
<tr><td>1</td><td><code>Cabinet.OrganisationPropreId</code> double la relation « dossier propre ».</td><td>Sans conséquence ; on peut ne garder que la relation.</td></tr>
<tr><td>2</td><td><code>DesignationCorrespondant</code> ne garde que la désignation en cours.</td><td>Historiser les désignations (date de début et de fin) pour prouver qui était désigné à la date d'une qualification ancienne.</td></tr>
<tr><td>3</td><td>Les écarts relevés dans les livrables (README, n° 1 à 7).</td><td>Voir l'annexe du dossier de modélisation.</td></tr>
</tbody></table></section>
</body></html>"""
    SORTIE_HTML.parent.mkdir(exist_ok=True)
    SORTIE_HTML.write_text(page, encoding="utf-8")
    subprocess.run(["node", str(OUTILS / "html_vers_pdf.js"), str(SORTIE_HTML), str(SORTIE_PDF), "Waɖɛ · Diagramme de classes expliqué"], check=True)
    print(f"{nb_classes} classes, {nb_champs} champs et méthodes, {len(relations)} relations : tout est expliqué.")
    print(f"PDF écrit : {SORTIE_PDF}")


if __name__ == "__main__":
    construire()
