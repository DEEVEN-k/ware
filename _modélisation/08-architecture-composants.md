# 8. Architecture des composants (.NET)

## 8.1 Vue de déploiement

```mermaid
flowchart LR
    subgraph CLIENT["Navigateurs (poste, mobile)"]
        B["Front React / Next.js<br/>site public + applications"]
    end
    subgraph HOST["Hébergement (choix A06)"]
        RP["Reverse proxy TLS<br/>(Nginx / Traefik)"]
        subgraph APP["Conteneurs applicatifs"]
            API["Wade.Api<br/>ASP.NET Core .NET 10"]
            WK["Wade.Worker<br/>serveur Hangfire"]
            GOT["Gotenberg<br/>(Word → PDF)"]
        end
        PG[("PostgreSQL 16+<br/>RLS, JSONB")]
        S3[("Stockage objet<br/>S3 / MinIO chiffré")]
        OBS["OpenTelemetry → Grafana<br/>(logs, traces, métriques)"]
    end
    SMTP["SMTP transactionnel"]

    B -- HTTPS --> RP --> API
    API --> PG
    WK --> PG
    API --> S3
    WK --> S3
    API --> GOT
    WK --> GOT
    WK --> SMTP
    API -.-> OBS
    WK -.-> OBS
```

`Wade.Api` et `Wade.Worker` partagent les mêmes assemblies de modules. Seul l'hôte change :
l'un sert l'API HTTP, l'autre exécute les tâches Hangfire (alertes, échéances, vérification du
journal, conversions lourdes).

## 8.2 Dépendances entre projets de la solution

```mermaid
flowchart TD
    API["Wade.Api<br/>(hôte HTTP)"]
    WK["Wade.Worker<br/>(hôte Hangfire)"]
    subgraph MODS["Modules (chacun : Domaine · Application · Endpoints)"]
        M1["Wade.Modules.Acces<br/>identité, organisations, mandats, autorisation"]
        M10["Wade.Modules.Formulaires<br/>types, listes, champs, versions,<br/>validateur dynamique"]
        M2["Wade.Modules.Referentiels"]
        M3["Wade.Modules.Registre"]
        M4["Wade.Modules.Formalites"]
        M5["Wade.Modules.Aipd"]
        M6["Wade.Modules.Violations"]
        M7["Wade.Modules.Pilotage<br/>tâches, alertes, indice, paramètres"]
        M8["Wade.Modules.Documents"]
        M9["Wade.Modules.Contenus<br/>site public, bulles, glossaire"]
    end
    MOT["Wade.Moteur<br/>(C# pur, sans dépendance)"]
    SK["Wade.SharedKernel<br/>types communs, événements, Result"]
    INF["Wade.Infrastructure<br/>EF Core, RLS, journal chaîné, S3, SMTP, Gotenberg"]

    API --> MODS
    WK --> MODS
    M2 --> MOT
    M3 --> MOT
    M3 --> M2
    M3 --> M10
    M2 --> M10
    M4 --> M3
    M5 --> M3
    M4 & M5 & M6 --> M8
    MODS --> SK
    MODS --> INF
    INF --> SK
```

Règles de dépendance, vérifiées par un test d'architecture (NetArchTest) :

- `Wade.Moteur` ne référence **rien** : ni EF Core, ni ASP.NET. Il reste ainsi testable avec les seuls fichiers CSV de recette.
- Un module n'accède jamais aux tables d'un autre module. Il passe par son interface publique (`IRegistreLecture`…) ou par un **événement de domaine** (`FichePubliee`, `ReferentielPublie`, `ViolationDeclaree`…) diffusé en mémoire, avec une table outbox pour les effets asynchrones.
- Toute écriture passe par `DbContext.SaveChanges`. Un intercepteur y produit l'entrée de journal chaînée. Aucune écriture SQL directe hors migrations.

## 8.3 Pile technique retenue

| Besoin | Choix |
|---|---|
| API | ASP.NET Core Minimal APIs (ou contrôleurs), OpenAPI |
| Persistance | EF Core + Npgsql (JSONB, tableaux, RLS) |
| Identité | ASP.NET Core Identity, TOTP + codes de récupération, verrouillage après 5 essais (G07) |
| Autorisation | Policies + `IAuthorizationHandler` « droits effectifs » (flux 4.3) |
| Tâches planifiées | Hangfire (stockage PostgreSQL) |
| Validation des référentiels | JsonSchema.Net + contrôles de graphe |
| Formulaires dynamiques | Validateur générique piloté par la configuration (C#), même règles en TypeScript côté front ; expressions régulières avec délai maximal |
| Documents | Open XML SDK (modèles Word E01 à E07) + Gotenberg |
| Courriels | MailKit |
| Tests | xUnit, Testcontainers (PostgreSQL), recette du moteur sur les CSV, NetArchTest |
| Observabilité | OpenTelemetry, .NET Aspire en local |
| Client front | Client TypeScript généré depuis l'OpenAPI (NSwag ou Kiota) |
