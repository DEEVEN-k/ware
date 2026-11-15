"""Explications des classes du module Accès."""

CLASSES = {
    # ------------------------------------------------------------------ ACCÈS
    "Utilisateur": {
        "role": "La personne physique qui se connecte. Elle ne porte ni rôle ni organisation : ses droits dépendent de l'endroit où elle travaille (MembreOrganisation ou MembreCabinet).",
        "champs": {
            "Id": "Identifiant technique stable. Le journal de conformité désigne l'auteur de chaque action par cet identifiant, même si la personne change de nom ou de courriel.",
            "Courriel": "Identifiant de connexion et adresse d'envoi des alertes (AL-01, AL-03…). Unique sur la plateforme.",
            "NomComplet": "Affiché dans le journal, les jalons de dossier et les documents produits.",
            "DoubleAuthActive": "La double authentification est obligatoire pour les administrateurs, les correspondants et les cabinets (H01, section Confiance). Ce champ permet de bloquer l'accès tant qu'elle n'est pas activée pour ces profils.",
            "Actif": "Permet de désactiver un compte (départ d'un salarié) sans le supprimer : le journal doit continuer à désigner une personne identifiable.",
            "DerniereConnexion": "Repérage des comptes dormants et audits de sécurité.",
        },
    },
    "Organisation": {
        "role": "Le client qui tient son registre : entreprise, administration, association… C'est l'unité de cloisonnement : toutes les données métier portent l'identifiant de l'organisation.",
        "champs": {
            "Id": "Clé de cloisonnement. Elle figure sur chaque ligne métier et sert au filtre d'isolement par organisation (RLS PostgreSQL).",
            "Denomination": "Rubrique 1 du registre (« Informations sur l'organisme », champ org.denomination). Saisie une fois, reprise dans chaque fiche et chaque export.",
            "FormeJuridique": "Rubrique 1 du registre (org.forme_juridique) ; figure sur les formulaires de l'autorité.",
            "IdentifiantFiscal": "Rubrique 1 du registre (org.identifiant_fiscal) ; identifie l'organisme auprès de l'autorité.",
            "Rccm": "Numéro au registre du commerce (org.rccm), demandé par les formulaires de déclaration.",
            "Adresse": "Coordonnées de l'organisme (org.adresse), reprises dans les dossiers de formalité.",
            "Secteur": "Secteur d'activité (org.secteur). Sert à proposer les modèles sectoriels de traitements (F02).",
            "TrancheEffectif": "Effectif par tranche (org.effectif). Sert à adapter l'accompagnement, par exemple le circuit fusionné pour les petites structures.",
            "PaysEtablissement": "Alimente le moteur : il détermine la juridiction proposée par défaut pour chaque traitement (Togo ou Bénin).",
            "NaturePublique": "Alimente le moteur : répond à TG-Q6 et BJ-Q4 (traitement pour le compte de l'État ou d'une collectivité). Typé en booléen parce que la logique juridique en dépend.",
            "MissionServicePublic": "Alimente le moteur : complète TG-Q6 et BJ-Q4, et ferme l'exemption béninoise BJ-Q8 aux autorités publiques (condition bloquante).",
            "VisaActive": "Le visa du responsable de traitement avant dépôt est une étape désactivable par l'organisation (G04 §4).",
            "CircuitFusionne": "Une petite structure peut fusionner soumission, qualification et visa en une seule validation (G04 §4).",
            "GroupeParentId": "Rattache une entité à son groupe. Permet le mandat « limité à certaines entités du groupe » (G05) et la vision consolidée d'un groupe présent dans plusieurs pays.",
        },
    },
    "ServiceDirection": {
        "role": "Un service ou une direction de l'organisation. C'est l'unité de périmètre : elle limite ce que voit un contributeur métier et ce que couvre un mandat.",
        "champs": {
            "Id": "Référencé par les fiches, les périmètres d'utilisateurs et les mandats.",
            "Libelle": "Nom affiché, par exemple « Ressources humaines ».",
            "ParentId": "Les services s'imbriquent (direction, service, cellule). Restreindre l'accès à une direction couvre aussi ses sous-services.",
        },
    },
    "MembreOrganisation": {
        "role": "Le lien entre une personne et une organisation, avec ses rôles. Le rôle appartient à la place occupée dans l'organisation, pas à la personne.",
        "champs": {
            "UtilisateurId": "La personne.",
            "OrganisationId": "L'organisation à laquelle elle est rattachée.",
            "Roles": "Un ensemble, pas un seul rôle : G04 prévoit le cumul (« le droit le plus favorable s'applique »). Dans une PME, une même personne peut être administrateur et correspondant.",
            "PerimetreServices": "Les services auxquels le rôle est limité, pour le contributeur métier (le « P » de la matrice G04).",
        },
    },
    "RoleOrganisation": {
        "role": "Les cinq rôles de la matrice G04. Liste fermée, car chaque rôle correspond à des règles d'accès vérifiées par le serveur.",
        "valeurs": {
            "AdministrateurOrganisation": "Gère les utilisateurs, les paramètres et les mandats. Ne qualifie pas.",
            "Correspondant": "Qualifie, publie au registre, conduit formalités, AIPD et violations.",
            "ResponsableTraitement": "Qualifie, vise avant dépôt, conduit formalités, AIPD et violations.",
            "ContributeurMetier": "Saisit les fiches de son périmètre, sans qualifier ni publier.",
            "LecteurAuditeur": "Consulte et exporte, y compris le journal.",
        },
    },
    "ResponsableTraitementLegal": {
        "role": "Le responsable du traitement au sens de la loi (champs rt.*). Il figure sur le registre et les formulaires de l'autorité ; il n'a pas forcément de compte dans Waɖɛ.",
        "champs": {
            "Nom": "Identité exigée par le registre et les formulaires officiels.",
            "Fonction": "Qualité du signataire (directeur général, maire…).",
            "Adresse": "Coordonnées exigées par l'autorité.",
            "Telephone": "Coordonnées exigées par l'autorité.",
            "Courriel": "Coordonnées exigées par l'autorité.",
        },
    },
    "DesignationCorrespondant": {
        "role": "La désignation légale du correspondant (Togo) ou du délégué (Bénin), champs dpo.*. Elle est distincte du rôle applicatif « Correspondant » : seule cette désignation alimente le moteur (FAQ H01).",
        "champs": {
            "Designe": "Répond à TG-Q3 (désignation qui dispense de formalités au Togo) et ouvre la voie de l'exemption au Bénin. À défaut, réputé faux.",
            "Nom": "Identité du correspondant ou délégué, exigée par l'autorité.",
            "Fonction": "Sa position dans l'organisation, utile pour apprécier son indépendance.",
            "Statut": "Interne ou externe : un cabinet peut être délégué externe.",
            "DateDesignation": "Date d'effet, reprise dans les dossiers.",
            "JustificatifId": "Preuve de la désignation, par exemple la lettre d'engagement publiée par l'APDP.",
        },
    },
    "Cabinet": {
        "role": "Le cabinet de conseil ou correspondant externe qui gère plusieurs clients, uniquement sous mandat.",
        "champs": {
            "Id": "Référencé par les mandats, les membres et le journal.",
            "Denomination": "Affichée au client, dans le journal et sur le rapport d'activité E06.",
            "OrganisationPropreId": "Le cabinet tient sa propre conformité (H01). Son registre est une Organisation ordinaire, ce qui évite tout développement spécifique.",
            "AccesDossierPropreOuvert": "L'administrateur de cabinet décide si les consultants accèdent au dossier interne du cabinet (G04 §2).",
        },
    },
    "MembreCabinet": {
        "role": "Le lien entre une personne et un cabinet.",
        "champs": {
            "UtilisateurId": "La personne.",
            "CabinetId": "Son cabinet.",
            "Role": "Un seul rôle de cabinet par personne (G04 §2).",
        },
    },
    "RoleCabinet": {
        "role": "Les quatre rôles de cabinet de G04 §2. Le rôle régit ce qu'un consultant peut faire ; le mandat régit sur quoi.",
        "valeurs": {
            "AdministrateurCabinet": "Gère l'équipe, les affectations, la facturation ; prérogatives de correspondant chez le client, dans la limite du mandat.",
            "ConsultantReferent": "Pilote un portefeuille de clients ; prérogatives de correspondant, dans la limite du mandat.",
            "ConsultantContributeur": "Saisit et modifie, sans qualifier, valider ni déposer.",
            "ConsultantLecteur": "Lit et exporte.",
        },
    },
    "Mandat": {
        "role": "L'autorisation expresse donnée par un client à un cabinet (G05). Classe à part entière car le lien client-cabinet a ses propres caractéristiques : niveau, périmètre, durée, statut.",
        "champs": {
            "Id": "Référencé par le journal : chaque action d'un consultant cite le mandat en vigueur, et cette mention subsiste après la fin du mandat (G05 §4).",
            "OrganisationId": "Le client, seul à pouvoir consentir, étendre ou révoquer le mandat.",
            "CabinetId": "Le cabinet bénéficiaire.",
            "Niveau": "Ce que le cabinet peut faire. Plafonne les droits du consultant, quel que soit son rôle de cabinet.",
            "Portee": "Sur quoi porte le mandat : toute l'organisation, certains services ou certaines entités du groupe.",
            "ServicesOuEntites": "La liste précise des services ou entités, quand la portée est restreinte. Un mandat limité aux RH ne donne aucun accès aux traitements commerciaux.",
            "DateDebut": "Date d'effet : le mandat accepté devient Actif à cette date.",
            "DateFin": "Facultative. Si elle est renseignée, le mandat expire automatiquement et les alertes partent à J-30 puis J-7 (AL-10).",
            "Statut": "Cycle de vie du mandat (G03) ; seul le statut Actif ouvre l'accès.",
            "ActionsReservees": "Actions que le client garde pour lui même sous mandat de pilotage complet (G05 §3).",
            "AccepteParId": "Preuve du caractère exprès : qui a accepté (un administrateur authentifié).",
            "AccepteLe": "Preuve du caractère exprès : quand.",
        },
    },
    "NiveauMandat": {
        "role": "Les trois niveaux de mandat, qui plafonnent les droits des consultants (G04 §3).",
        "valeurs": {
            "Consultation": "Lecture et export seuls.",
            "Contribution": "Création et modification de fiches, sans qualifier, viser, publier ni déposer.",
            "PilotageComplet": "Prérogatives du correspondant, sauf actions réservées.",
        },
    },
    "ActionReservable": {
        "role": "Les actions que l'organisation peut garder pour son équipe interne (G05 §3).",
        "valeurs": {
            "VisaAvantDepot": "Le visa engage la responsabilité du responsable de traitement.",
            "NotificationViolation": "La notification à l'autorité engage l'organisation.",
            "RevocationMandat": "Évite qu'un cabinet puisse agir sur son propre mandat.",
        },
    },
    "AffectationConsultant": {
        "role": "Désigne nominativement les consultants qui travaillent pour un client. Un consultant n'accède à un client qu'avec un mandat actif ET une affectation (G05).",
        "champs": {
            "MandatId": "Le mandat dans le cadre duquel le consultant intervient.",
            "UtilisateurId": "Le consultant affecté.",
            "OpposeeParOrganisation": "Le client peut s'opposer à l'affectation d'un consultant (G04).",
            "AffecteLe": "Traçabilité.",
        },
    },
    "StatutMandat": {
        "role": "Le cycle de vie d'un mandat (G03).",
        "valeurs": {
            "Demande": "Demande du cabinet, sans effet.",
            "Accepte": "Accepté par le client, en attente de la date de début.",
            "Refuse": "Refusé par le client.",
            "Actif": "Seul statut qui ouvre l'accès.",
            "Suspendu": "Accès coupé sans fin du mandat ; levée par le client seul.",
            "Revoque": "Fin immédiate décidée par le client, sessions coupées.",
            "Expire": "Fin automatique à la date de fin.",
        },
    },
    "PorteeMandat": {
        "role": "L'étendue d'un mandat (G05, dimension « Périmètre »).",
        "valeurs": {
            "TouteLOrganisation": "Aucune restriction.",
            "ServicesOuDirections": "Restreint aux services listés.",
            "EntitesDuGroupe": "Restreint à certaines entités d'un groupe.",
        },
    },
    "StatutCorrespondant": {
        "role": "Nature du correspondant ou délégué désigné.",
        "valeurs": {
            "Interne": "Salarié de l'organisation.",
            "Externe": "Prestataire, par exemple un cabinet ou AMELEGAL.",
        },
    },
}
