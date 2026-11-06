"""Génère 05-logigrammes.md à partir des référentiels JSON de chaque juridiction.

Usage : python3 _modélisation/outils/generer_logigrammes.py
À relancer à chaque nouvelle version d'un référentiel : le diagramme reste ainsi
le reflet exact des données validées, jamais une recopie manuelle.
"""
import json
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
SORTIE = RACINE / "_modélisation" / "05-logigrammes.md"
REFERENTIELS = [
    ("Togo", RACINE / "01 Togo/01 Livrables Togo/_spécifications développeur/referentiel-togo.json"),
    ("Bénin", RACINE / "02 Bénin/01 Livrables Bénin/_spécifications développeur/referentiel-benin.json"),
]


def nid(code: str) -> str:
    return code.replace("-", "_")


def esc(texte: str) -> str:
    return texte.replace('"', "#quot;")


def libelle_court(q: dict) -> str:
    lib = q["libelle"]
    if q["type"] == "multiple" and ":" in lib:
        lib = lib.split(":")[0].strip() + " ?"
    return lib


def diagramme(ref: dict) -> str:
    lg = ref["logigramme"]
    regimes = {r["id"]: r for r in ref["regimes"]}
    lignes = ["flowchart LR"]
    lignes.append(f'    START(["Entrée : nouvelle qualification"]) --> {nid(lg["entree"])}')
    for q in lg["questions"]:
        suffixe = " (choix multiple)" if q["type"] == "multiple" else ""
        lignes.append(
            f'    {nid(q["id"])}("<b>{q["id"]}</b><br/>{esc(libelle_court(q))}{suffixe}<br/><i>{esc(q.get("fondement", ""))}</i>")'
        )
        cb = q.get("condition_bloquante")
        if cb:
            lignes.append(
                f'    CB_{nid(q["id"])}[/"Condition bloquante : si {esc(cb["champ"])} = {str(cb["valeur"]).lower()}, réponse forcée à NON"/]'
            )
            lignes.append(f"    CB_{nid(q['id'])} -.-> {nid(q['id'])}")
    for q in lg["questions"]:
        for rep in ("oui", "non"):
            b = q[rep]
            lignes.append(f'    {nid(q["id"])} -- {rep.upper()} --> {nid(b["cible"])}')
    for code, r in regimes.items():
        forme = '(["{}"])' if r.get("est_un_regime_de_formalite") is False else '["{}"]'
        lignes.append(f"    {nid(code)}" + forme.format(f"<b>{esc(r['libelle'])}</b><br/>{code}"))
    lignes.append("    classDef q fill:#EAF5EC,stroke:#00901D,color:#00370B")
    lignes.append("    classDef r fill:#00370B,stroke:#00370B,color:#ffffff")
    lignes.append("    classDef x fill:#f1f1f1,stroke:#888,color:#333")
    lignes.append("    class " + ",".join(nid(q["id"]) for q in lg["questions"]) + " q")
    formalites = [nid(c) for c, r in regimes.items() if r.get("est_un_regime_de_formalite") is not False]
    exclusions = [nid(c) for c, r in regimes.items() if r.get("est_un_regime_de_formalite") is False]
    lignes.append("    class " + ",".join(formalites) + " r")
    if exclusions:
        lignes.append("    class " + ",".join(exclusions) + " x")
    return "\n".join(lignes)


def tableau_motifs(ref: dict) -> str:
    out = ["| Question | Réponse | Issue | Motif affiché |", "|---|---|---|---|"]
    for q in ref["logigramme"]["questions"]:
        for rep in ("oui", "non"):
            b = q[rep]
            issue = f"→ {b['cible']}" if b["type"] == "question" else f"**{b['cible']}**"
            out.append(f"| {q['id']} | {rep.upper()} | {issue} | {b.get('motif', '')} |")
    return "\n".join(out)


def main() -> None:
    parties = [
        "# 5. Logigrammes de qualification",
        "",
        "> Fichier **généré** par `outils/generer_logigrammes.py` à partir des référentiels JSON. "
        "Ne pas modifier à la main : corriger le référentiel puis relancer le script.",
        "",
        "Lecture : rectangle vert arrondi = question, rectangle sombre = régime de formalité, "
        "rectangle gris arrondi = exclusion (sans formalité), parallélogramme = condition bloquante.",
        "",
    ]
    for nom, chemin in REFERENTIELS:
        ref = json.loads(chemin.read_text(encoding="utf-8-sig"))
        meta = ref["meta"]
        parties += [
            f"## {nom} — référentiel v{meta['version']} du {meta['date']}",
            "",
            f"Autorité : **{ref['autorite']['sigle']}**. Entrée : `{ref['logigramme']['entree']}`. "
            f"{ref['logigramme']['nb_questions']} questions, {ref['logigramme']['nb_sorties']} sorties.",
            "",
            "```mermaid",
            diagramme(ref),
            "```",
            "",
        ]
        rt = ref["logigramme"].get("regles_transverses")
        if rt:
            parties += ["### Règles transverses (ne modifient pas la sortie)", "", "| Id | Règle | Fondement |", "|---|---|---|"]
            parties += [f"| {r['id']} | **{r['libelle']}** : {r['regle']} | {r['fondement']} |" for r in rt]
            parties.append("")
        parties += [f"### Motifs par branche — {nom}", "", tableau_motifs(ref), ""]
    SORTIE.write_text("\n".join(parties), encoding="utf-8")
    print(f"Écrit : {SORTIE}")


if __name__ == "__main__":
    main()
