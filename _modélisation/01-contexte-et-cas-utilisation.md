# 1. Contexte et cas d'utilisation

## 1.1 Diagramme de contexte

Waɖɛ au centre, ses utilisateurs et les systèmes externes avec lesquels il échange.

```mermaid
flowchart TB
    subgraph ORG["Organisation cliente"]
        ADM["Administrateur<br/>d'organisation"]
        COR["Correspondant"]
        RT["Responsable<br/>de traitement"]
        CM["Contributeur<br/>métier"]
        LA["Lecteur-auditeur"]
    end
    subgraph CAB["Cabinet (sous mandat)"]
        ACAB["Administrateur<br/>de cabinet"]
        CREF["Consultant<br/>référent"]
        CCON["Consultant<br/>contributeur / lecteur"]
    end
    subgraph AME["AMELEGAL (éditeur)"]
        JUR["Juriste<br/>référentiels"]
        BO["Administrateur<br/>back-office"]
        SUP["Support"]
    end
    VIS["Visiteur<br/>du site public"]

    W(("<b>Waɖɛ</b><br/>plateforme SaaS"))

    ADM & COR & RT & CM & LA --> W
    ACAB & CREF & CCON --> W
    JUR & BO & SUP --> W
    VIS --> W

    W -- "courriels transactionnels<br/>(alertes, invitations)" --> MAIL["Service SMTP"]
    W -- "pièces jointes,<br/>documents produits" --> S3["Stockage objet<br/>chiffré (S3)"]
    W -- "conversion Word → PDF" --> GOT["Gotenberg"]
    W -- "paiement abonnements<br/>(G06, à arbitrer)" --> PAY["Prestataire<br/>de paiement"]
    W -. "dossiers imprimés ou<br/>envoyés hors plateforme" .-> AUT["Autorités de contrôle<br/>IPDCP (TG) · APDP (BJ)"]

    classDef sys fill:#00370B,color:#fff,stroke:#00370B
    classDef ext fill:#f4f4f4,stroke:#888,color:#333
    class W sys
    class MAIL,S3,GOT,PAY,AUT ext
```

> Il n'existe **pas d'interface électronique** avec les autorités : le dépôt se fait par voie
> électronique (courriel), postale ou au guichet (art. 413 BJ ; à renseigner pour l'IPDCP).
> Waɖɛ produit le dossier, l'utilisateur le dépose, puis enregistre les jalons (accusé, décision).

## 1.2 Cas d'utilisation par acteur

Les droits détaillés sont ceux de la matrice G04. P = limité au périmètre de services de l'utilisateur. Un consultant de cabinet exerce, chez le client, les prérogatives du rôle d'organisation correspondant à son rôle de cabinet, dans la limite du mandat (G04 §2).

### Registre

```mermaid
flowchart LR
    CM["Contributeur métier (P)"]
    COR["Correspondant"]
    RT["Responsable de traitement"]
    ADM["Administrateur d'organisation"]
    LA["Lecteur-auditeur"]
    subgraph S[" "]
        direction TB
        U1(["Créer / modifier une fiche"])
        U2(["Soumettre à qualification"])
        U3(["Qualifier et arrêter le régime"])
        U4(["Retenir un autre régime (motivé)"])
        U5(["Viser avant dépôt"])
        U6(["Publier au registre"])
        U7(["Archiver une fiche"])
        U8(["Consulter / exporter le registre"])
    end
    CM --> U1 & U2 & U8
    COR --> U1 & U2 & U3 & U4 & U6 & U7 & U8
    RT --> U1 & U2 & U3 & U4 & U5 & U8
    ADM --> U1 & U2 & U7 & U8
    LA --> U8
    classDef act fill:#00370B,color:#fff,stroke:#00370B
    class CM,COR,RT,ADM,LA act
```

### Formalités et analyses d'impact

```mermaid
flowchart LR
    CM["Contributeur métier (P)"]
    COR["Correspondant"]
    RT["Responsable de traitement"]
    subgraph S[" "]
        direction TB
        F1(["Créer un dossier de formalité"])
        F2(["Déposer un dossier auprès de l'autorité"])
        F3(["Enregistrer la décision de l'autorité"])
        F4(["Lancer une AIPD"])
        F5(["Contribuer à une section d'AIPD (sur invitation)"])
        F6(["Valider une AIPD"])
    end
    COR --> F1 & F2 & F3 & F4 & F5 & F6
    RT --> F1 & F2 & F3 & F4 & F5 & F6
    CM --> F5
    classDef act fill:#00370B,color:#fff,stroke:#00370B
    class CM,COR,RT act
```

### Violations de données

```mermaid
flowchart LR
    TOUS["Admin, Correspondant, RT,<br/>Contributeur métier"]
    COR["Correspondant"]
    RT["Responsable de traitement"]
    subgraph S[" "]
        direction TB
        V1(["Déclarer une violation (y compris sur mobile)"])
        V2(["Qualifier le risque"])
        V3(["Notifier l'autorité"])
        V4(["Informer les personnes concernées"])
        V5(["Clore la violation"])
    end
    TOUS --> V1
    COR --> V2 & V3 & V4 & V5
    RT --> V2 & V3 & V4 & V5
    classDef act fill:#00370B,color:#fff,stroke:#00370B
    class TOUS,COR,RT act
```

### Gouvernance et traçabilité

```mermaid
flowchart LR
    ADM["Administrateur d'organisation"]
    COR["Correspondant"]
    RT["Responsable de traitement"]
    LA["Lecteur-auditeur"]
    subgraph S[" "]
        direction TB
        G1(["Inviter un utilisateur, modifier rôle ou périmètre"])
        G2(["Paramétrer circuit et alertes"])
        G3(["Renseigner la désignation légale du correspondant"])
        G4(["Octroyer / suspendre / révoquer un mandat"])
        G5(["S'opposer à l'affectation d'un consultant"])
        G6(["Consulter le journal de conformité"])
        G7(["Exporter le journal"])
        G8(["Créer et affecter une tâche"])
    end
    ADM --> G1 & G2 & G3 & G4 & G5 & G6 & G7 & G8
    RT --> G3 & G6 & G8
    COR --> G6 & G7 & G8
    LA --> G6 & G7
    classDef act fill:#00370B,color:#fff,stroke:#00370B
    class ADM,COR,RT,LA act
```

### Espace cabinet

```mermaid
flowchart LR
    ACAB["Administrateur de cabinet"]
    CREF["Consultant référent"]
    CCON["Consultant contributeur / lecteur"]
    subgraph S[" "]
        direction TB
        C1(["Demander un mandat"])
        C2(["Affecter nominativement un consultant"])
        C3(["Piloter le portefeuille de clients"])
        C4(["Agir chez un client, dans la limite du mandat"])
        C5(["Produire le rapport d'activité (E06)"])
        C6(["Tenir la conformité propre du cabinet"])
    end
    ACAB --> C1 & C2 & C3 & C4 & C5 & C6
    CREF --> C3 & C4 & C5
    CCON --> C4
    classDef act fill:#00370B,color:#fff,stroke:#00370B
    class ACAB,CREF,CCON act
```

### Back-office AMELEGAL et site public

```mermaid
flowchart LR
    JUR["Juriste AMELEGAL"]
    BO["Administrateur back-office"]
    SUP["Support"]
    VIS["Visiteur"]
    subgraph S[" "]
        direction TB
        B1(["Importer / éditer un référentiel"])
        B2(["Simuler une version sur les cas de recette"])
        B3(["Publier une version de référentiel"])
        B4(["Créer une juridiction"])
        B5(["Gérer contenus publics, bulles, glossaire"])
        B6(["Gérer les paramètres globaux et par juridiction"])
        B7(["Intervenir chez un client (tracé et notifié)"])
        P1(["Consulter offres, actualités, FAQ"])
        P2(["Créer un espace / souscrire"])
        P3(["Demander une démonstration"])
    end
    JUR --> B1 & B2 & B3 & B4 & B5
    BO --> B4 & B5 & B6
    SUP --> B7
    VIS --> P1 & P2 & P3
    classDef act fill:#00370B,color:#fff,stroke:#00370B
    class JUR,BO,SUP,VIS act
```
