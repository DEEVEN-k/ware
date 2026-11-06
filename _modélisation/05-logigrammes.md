# 5. Logigrammes de qualification

> Fichier **généré** par `outils/generer_logigrammes.py` à partir des référentiels JSON. Ne pas modifier à la main : corriger le référentiel puis relancer le script.

Lecture : rectangle vert arrondi = question, rectangle sombre = régime de formalité, rectangle gris arrondi = exclusion (sans formalité), parallélogramme = condition bloquante.

## Togo — référentiel v1.0 du 2026-09-06

Autorité : **IPDCP**. Entrée : `TG-Q1`. 8 questions, 5 sorties.

```mermaid
flowchart LR
    START(["Entrée : nouvelle qualification"]) --> TG_Q1
    TG_Q1("<b>TG-Q1</b><br/>Le traitement porte-t-il sur des données à caractère personnel ?<br/><i>art. 2 et 4</i>")
    TG_Q2("<b>TG-Q2</b><br/>A-t-il pour objet un registre destiné exclusivement à l'information du public ?<br/><i>art. 5, 2°</i>")
    TG_Q3("<b>TG-Q3</b><br/>Un correspondant à la protection des données a-t-il été désigné ?<br/><i>art. 5, 3° et art. 77</i>")
    TG_Q4("<b>TG-Q4</b><br/>Le traitement implique-t-il un transfert de données hors du Togo ?<br/><i>art. 5, 3°, in fine, et art. 28, alinéa 2</i>")
    TG_Q5("<b>TG-Q5</b><br/>Le traitement porte-t-il sur des données sensibles ?<br/><i>art. 4, art. 21 et art. 6</i>")
    TG_Q6("<b>TG-Q6</b><br/>Est-il mis en oeuvre par l'État, une collectivité locale ou une entité privée chargée d'une mission de service public ?<br/><i>art. 9</i>")
    TG_Q7("<b>TG-Q7</b><br/>Concerne-t-il la sûreté de l'État, la sécurité publique, la Défense nationale ou le recensement ?<br/><i>art. 9, 1° et 3°</i>")
    TG_Q8("<b>TG-Q8</b><br/>Porte-t-il sur des données génétiques ou biométriques, une interconnexion de fichiers, un numéro national d'identification, ou relève-t-il de statistiques, de recherche scientifique ou d'un motif d'intérêt public ? (choix multiple)<br/><i>art. 8, 1° à 6°</i>")
    TG_Q1 -- OUI --> TG_Q2
    TG_Q1 -- NON --> TG_DISPENSE
    TG_Q2 -- OUI --> TG_DISPENSE
    TG_Q2 -- NON --> TG_Q3
    TG_Q3 -- OUI --> TG_Q4
    TG_Q3 -- NON --> TG_Q5
    TG_Q4 -- OUI --> TG_AVIS
    TG_Q4 -- NON --> TG_DISPENSE
    TG_Q5 -- OUI --> TG_Q6
    TG_Q5 -- NON --> TG_DECLARATION
    TG_Q6 -- OUI --> TG_Q7
    TG_Q6 -- NON --> TG_Q8
    TG_Q7 -- OUI --> TG_ACTE
    TG_Q7 -- NON --> TG_AUTORISATION
    TG_Q8 -- OUI --> TG_AUTORISATION
    TG_Q8 -- NON --> TG_DECLARATION
    TG_DISPENSE["<b>Pas de formalité</b><br/>TG-DISPENSE"]
    TG_DECLARATION["<b>Déclaration</b><br/>TG-DECLARATION"]
    TG_AVIS["<b>Avis motivé</b><br/>TG-AVIS"]
    TG_AUTORISATION["<b>Autorisation</b><br/>TG-AUTORISATION"]
    TG_ACTE["<b>Acte réglementaire après avis</b><br/>TG-ACTE"]
    classDef q fill:#EAF5EC,stroke:#00901D,color:#00370B
    classDef r fill:#00370B,stroke:#00370B,color:#ffffff
    classDef x fill:#f1f1f1,stroke:#888,color:#333
    class TG_Q1,TG_Q2,TG_Q3,TG_Q4,TG_Q5,TG_Q6,TG_Q7,TG_Q8 q
    class TG_DISPENSE,TG_DECLARATION,TG_AVIS,TG_AUTORISATION,TG_ACTE r
```

### Motifs par branche — Togo

| Question | Réponse | Issue | Motif affiché |
|---|---|---|---|
| TG-Q1 | OUI | → TG-Q2 |  |
| TG-Q1 | NON | **TG-DISPENSE** | Le traitement ne porte pas sur des données à caractère personnel : il échappe au champ de la loi. |
| TG-Q2 | OUI | **TG-DISPENSE** | Le traitement a pour seul objet la tenue d'un registre destiné exclusivement à l'information du public : il est dispensé de formalités. |
| TG-Q2 | NON | → TG-Q3 |  |
| TG-Q3 | OUI | → TG-Q4 |  |
| TG-Q3 | NON | → TG-Q5 |  |
| TG-Q4 | OUI | **TG-AVIS** | La désignation d'un correspondant dispense des formalités, sauf lorsqu'un transfert vers un pays tiers est envisagé. Le transfert appelle l'avis motivé préalable de l'IPDCP. |
| TG-Q4 | NON | **TG-DISPENSE** | Un correspondant a été désigné et aucun transfert hors du Togo n'est envisagé : le traitement est dispensé de formalités préalables. |
| TG-Q5 | OUI | → TG-Q6 |  |
| TG-Q5 | NON | **TG-DECLARATION** | Le traitement ne relève d'aucun régime dérogatoire : il suit le régime de droit commun de la déclaration. |
| TG-Q6 | OUI | → TG-Q7 |  |
| TG-Q6 | NON | → TG-Q8 |  |
| TG-Q7 | OUI | **TG-ACTE** | Traitement opéré pour le compte d'une personne publique et portant sur une mission régalienne ou le recensement : il est décidé par acte réglementaire pris après avis motivé de l'IPDCP. |
| TG-Q7 | NON | **TG-AUTORISATION** | Traitement de données sensibles opéré pour le compte d'une personne publique, hors mission régalienne : il est soumis à l'autorisation préalable de l'IPDCP. |
| TG-Q8 | OUI | **TG-AUTORISATION** | Le traitement relève de l'un des cas de l'article 8 : il est soumis à l'autorisation préalable de l'IPDCP. |
| TG-Q8 | NON | **TG-DECLARATION** | Le traitement porte sur des données sensibles sans relever d'un cas d'autorisation : il suit le régime de la déclaration. |

## Bénin — référentiel v1.0 du 2026-09-06

Autorité : **APDP**. Entrée : `BJ-Q1`. 8 questions, 8 sorties.

```mermaid
flowchart LR
    START(["Entrée : nouvelle qualification"]) --> BJ_Q1
    BJ_Q1("<b>BJ-Q1</b><br/>Le fichier contient-il des données à caractère personnel permettant d'identifier une personne physique : identité, adresse, numéro de téléphone, image, voix, identifiant en ligne ?<br/><i>art. 1er, 380 et 381</i>")
    BJ_Q2("<b>BJ-Q2</b><br/>Le traitement relève-t-il du cadre exclusivement personnel ou domestique d'une personne physique, sans communication à des tiers ni diffusion ?<br/><i>art. 382 et 410, 1°</i>")
    BJ_Q3("<b>BJ-Q3</b><br/>Relève-t-il de l'une des dispenses de l'article 410 ? (choix multiple)<br/><i>art. 410</i>")
    BJ_Q4("<b>BJ-Q4</b><br/>Est-il mis en oeuvre pour le compte de l'État, d'un établissement public, d'une collectivité locale, ou d'une personne morale de droit privé gérant un service public ?<br/><i>art. 411, alinéa 1er</i>")
    BJ_Q5("<b>BJ-Q5</b><br/>Porte-t-il sur l'un des cinq objets de l'article 411 ? (choix multiple)<br/><i>art. 411</i>")
    BJ_Q6("<b>BJ-Q6</b><br/>Porte-t-il sur des catégories particulières de données, ou présente-t-il l'une des caractéristiques de l'article 407 ? (choix multiple)<br/><i>art. 407, et art. 394 pour les données sensibles</i>")
    BJ_Q7("<b>BJ-Q7</b><br/>Le traitement entre-t-il dans une norme simplifiée publiée par l'APDP pour les catégories les plus courantes de traitements non susceptibles de porter atteinte à la vie privée ?<br/><i>art. 406</i>")
    BJ_Q8("<b>BJ-Q8</b><br/>Le traitement relève-t-il d'une catégorie exemptée par décision de l'APDP, parce qu'il est manifestement sans risque et documenté (finalités, catégories de données, de personnes concernées et de destinataires, durée de conservation), ou parce qu'un délégué à la protection des données a été désigné, chargé d'assurer de manière indépendante l'application de la loi et de tenir le registre des traitements ?<br/><i>art. 408</i>")
    CB_BJ_Q8[/"Condition bloquante : si bloc1.personne_publique_ou_mission_service_public = true, réponse forcée à NON"/]
    CB_BJ_Q8 -.-> BJ_Q8
    BJ_Q1 -- OUI --> BJ_Q2
    BJ_Q1 -- NON --> BJ_HORS_CHAMP
    BJ_Q2 -- OUI --> BJ_DOMESTIQUE
    BJ_Q2 -- NON --> BJ_Q3
    BJ_Q3 -- OUI --> BJ_DISPENSE
    BJ_Q3 -- NON --> BJ_Q4
    BJ_Q4 -- OUI --> BJ_Q5
    BJ_Q4 -- NON --> BJ_Q6
    BJ_Q5 -- OUI --> BJ_DECRET
    BJ_Q5 -- NON --> BJ_Q6
    BJ_Q6 -- OUI --> BJ_AUTORISATION
    BJ_Q6 -- NON --> BJ_Q7
    BJ_Q7 -- OUI --> BJ_DECLARATION_SIMPLIFIEE
    BJ_Q7 -- NON --> BJ_Q8
    BJ_Q8 -- OUI --> BJ_EXEMPTION
    BJ_Q8 -- NON --> BJ_DECLARATION
    BJ_HORS_CHAMP(["<b>Hors du champ d'application</b><br/>BJ-HORS-CHAMP"])
    BJ_DOMESTIQUE(["<b>Exclusion domestique</b><br/>BJ-DOMESTIQUE"])
    BJ_DISPENSE["<b>Dispense de formalité</b><br/>BJ-DISPENSE"]
    BJ_DECRET["<b>Décret en Conseil des ministres</b><br/>BJ-DECRET"]
    BJ_AUTORISATION["<b>Autorisation préalable</b><br/>BJ-AUTORISATION"]
    BJ_DECLARATION_SIMPLIFIEE["<b>Déclaration simplifiée</b><br/>BJ-DECLARATION-SIMPLIFIEE"]
    BJ_EXEMPTION["<b>Exemption de déclaration</b><br/>BJ-EXEMPTION"]
    BJ_DECLARATION["<b>Déclaration préalable</b><br/>BJ-DECLARATION"]
    classDef q fill:#EAF5EC,stroke:#00901D,color:#00370B
    classDef r fill:#00370B,stroke:#00370B,color:#ffffff
    classDef x fill:#f1f1f1,stroke:#888,color:#333
    class BJ_Q1,BJ_Q2,BJ_Q3,BJ_Q4,BJ_Q5,BJ_Q6,BJ_Q7,BJ_Q8 q
    class BJ_DISPENSE,BJ_DECRET,BJ_AUTORISATION,BJ_DECLARATION_SIMPLIFIEE,BJ_EXEMPTION,BJ_DECLARATION r
    class BJ_HORS_CHAMP,BJ_DOMESTIQUE x
```

### Règles transverses (ne modifient pas la sortie)

| Id | Règle | Fondement |
|---|---|---|
| BJ-T1 | **Analyse d'impact préalable** : Si le traitement présente un risque élevé pour les droits et libertés, réaliser une analyse d'impact avant le traitement, quelle que soit la sortie. | art. 428 |
| BJ-T2 | **Consultation préalable** : Si le risque résiduel demeure élevé après l'analyse, consulter l'APDP, qui répond dans un délai maximum de huit semaines, prorogeable de six. | art. 429 |
| BJ-T3 | **Le doute oblige à consulter** : Le responsable du traitement ou le délégué qui hésite sur le régime applicable doit consulter l'Autorité. Waɖɛ propose cette action lorsque l'utilisateur écarte le résultat du moteur. | art. 407, alinéa 2 |
| BJ-T4 | **Modification d'une déclaration** : Toute modification affectant une déclaration initiale donne lieu à une nouvelle déclaration. Une modification substantielle de la fiche déclenche une tâche de nouvelle déclaration. | art. 412 |
| BJ-T5 | **Validité des décisions** : Les décisions de l'APDP sont valables deux ans. Alerte de renouvellement à l'approche du terme. | pratique de l'APDP |

### Motifs par branche — Bénin

| Question | Réponse | Issue | Motif affiché |
|---|---|---|---|
| BJ-Q1 | OUI | → BJ-Q2 |  |
| BJ-Q1 | NON | **BJ-HORS-CHAMP** | Le fichier ne contient pas de données permettant d'identifier une personne physique : il est hors du champ du Livre cinquième. |
| BJ-Q2 | OUI | **BJ-DOMESTIQUE** | Le traitement relève du cadre exclusivement personnel ou domestique, sans communication à des tiers ni diffusion. Les conditions sont cumulatives et strictes. |
| BJ-Q2 | NON | → BJ-Q3 |  |
| BJ-Q3 | OUI | **BJ-DISPENSE** | Le traitement figure dans la liste des dispenses de l'article 410. La dispense porte sur la formalité seule : registre, information, sécurité, durées et rapport annuel demeurent. |
| BJ-Q3 | NON | → BJ-Q4 |  |
| BJ-Q4 | OUI | → BJ-Q5 |  |
| BJ-Q4 | NON | → BJ-Q6 |  |
| BJ-Q5 | OUI | **BJ-DECRET** | Traitement mis en oeuvre pour le compte d'une personne publique et portant sur l'un des cinq objets de l'article 411 : il est décidé par décret en Conseil des ministres pris après avis motivé de l'APDP, publié avec le décret. |
| BJ-Q5 | NON | → BJ-Q6 |  |
| BJ-Q6 | OUI | **BJ-AUTORISATION** | Le traitement relève de l'article 407 : il est soumis à l'autorisation préalable de l'APDP, matérialisée par un extrait de délibération. |
| BJ-Q6 | NON | → BJ-Q7 |  |
| BJ-Q7 | OUI | **BJ-DECLARATION-SIMPLIFIEE** | Le traitement entre dans une norme simplifiée publiée par l'APDP : la déclaration est simplifiée, par référence expresse à la norme. |
| BJ-Q7 | NON | → BJ-Q8 |  |
| BJ-Q8 | OUI | **BJ-EXEMPTION** | Le traitement relève d'une catégorie exemptée par décision de l'APDP. L'exemption suppose une décision de l'Autorité portant sur des catégories de traitements ; elle n'est pas un droit acquis. |
| BJ-Q8 | NON | **BJ-DECLARATION** | Le traitement ne relève d'aucune exception : il suit le régime de droit commun de la déclaration préalable à l'APDP. |
