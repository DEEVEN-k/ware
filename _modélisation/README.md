# Modélisation de Waɖɛ

Dossier de conception établi à partir des livrables d'AMELEGAL (version 1.0, septembre 2026)
et de l'architecture retenue : **backend ASP.NET Core (.NET 10)**, PostgreSQL et front React.
Les diagrammes sont écrits en **Mermaid**. GitHub les affiche directement dans les fichiers `.md`.
Une version PDF consolidée est générée dans `Waɖɛ_Modélisation.pdf`.

| Fichier | Contenu |
|---|---|
| [01-contexte-et-cas-utilisation.md](01-contexte-et-cas-utilisation.md) | Diagramme de contexte, cas d'utilisation par acteur |
| [02-diagrammes-de-classes.md](02-diagrammes-de-classes.md) | Classes du domaine en 5 paquets : accès et mandats, référentiels, registre et qualification, formalités, AIPD et violations, pilotage |
| [03-diagrammes-etats.md](03-diagrammes-etats.md) | Cycles de vie (G03) : fiche, dossier, AIPD, violation, mandat, référentiel, tâche |
| [04-flux-et-activites.md](04-flux-et-activites.md) | Parcours global, algorithme du moteur, droits effectifs, violations, déclenchement de l'AIPD, indice |
| [05-logigrammes.md](05-logigrammes.md) | Logigrammes Togo et Bénin, **générés** depuis les référentiels JSON |
| [06-diagrammes-de-sequence.md](06-diagrammes-de-sequence.md) | Qualification, circuit de validation, dossier et acceptation tacite, violation, mandat, publication d'un référentiel |
| [07-modele-physique-donnees.md](07-modele-physique-donnees.md) | Schéma PostgreSQL (un schéma par module), isolement par organisation (RLS), index |
| [08-architecture-composants.md](08-architecture-composants.md) | Déploiement, dépendances entre projets .NET, pile technique |

## Outils

```bash
python3 _modélisation/outils/generer_logigrammes.py
```

```bash
node _modélisation/outils/construire_pdf.js
```

Le premier script régénère `05-logigrammes.md` après toute modification d'un référentiel JSON.
Le second reconstruit le PDF. Il nécessite Playwright et Chromium, et télécharge Mermaid
(version 11.4.1) depuis jsDelivr s'il n'est pas déjà présent dans `outils/vendor/`.

## Écarts relevés dans les livrables (à arbitrer par AMELEGAL)

Ces écarts ont été relevés par un contrôle croisé automatique entre les référentiels JSON,
`registre-champs.csv` et les règles de gestion. Ils ne bloquent pas la conception, mais chacun
appelle une décision avant l'implémentation.

| # | Écart | Où | Proposition retenue dans la modélisation |
|---|---|---|---|
| 1 | Les questions citent leurs champs sous la forme `bloc1.x`, `bloc2.x`, `bloc3.x`, alors que le CSV les identifie par `t.x` ou `org.x`. | référentiels JSON, CSV | Une table de correspondance explicite, chargée avec le référentiel. À terme, aligner les référentiels sur les `id` du CSV, qui sont stables. |
| 2 | `bloc1.personne_publique_ou_mission_service_public` (TG-Q6, BJ-Q4, condition bloquante de BJ-Q8) **n'existe pas** dans le CSV. | référentiels JSON | Champ **dérivé** : `org.nature_publique OU org.mission_service_public`, comme l'indiquent les notes du CSV. À confirmer. |
| 3 | Le critère d'AIPD `BJ-AIPD-1` porte sur `aipd.score_risque`, une valeur produite par l'AIPD elle-même. Le raisonnement est circulaire au moment de la qualification. | referentiel-benin.json | Évaluer ce critère **après** l'AIPD, au titre de la consultation préalable (art. 429). À la qualification, seuls les autres critères s'appliquent. À confirmer. |
| 4 | L'indice (G01) compte les formalités au statut « Récépissé reçu » ou « Dispense documentée ». Ces statuts n'existent pas dans le cycle du dossier (G03). | G01, G03 | « Récépissé reçu » est rattaché à `Acceptée` (décision expresse ou récépissé). « Dispense documentée » correspond à une fiche publiée dont le régime n'est pas une formalité. |
| 5 | `t.volume_personnes` est une **tranche** (« 1 000 à 9 999 »…), alors que le seuil d'AIPD est un **nombre** (10 000). | CSV, référentiels | Critère réuni si la borne basse de la tranche est ≥ au seuil. Les seuils administrables doivent coïncider avec une borne de tranche, ce qui est vérifié à la publication. |
| 6 | `t.juridiction` : « un traitement peut relever de plusieurs juridictions », mais le champ est typé `liste` et non `liste multiple`. | CSV | Modélisé en **liste multiple**, avec une qualification courante par juridiction. |
| 7 | Les transitions entre états ne sont pas décrites par G03, qui ne fixe que les états. | G03 | Transitions déduites de G04 et des référentiels. Celles qui sont propres à la modélisation sont marquées *(proposée)*. |
