# Contexte et Objectifs

## Application : Gestion des sélections et du vote pour le prix Goncourt 2025.

### Public cible :

---
Utilisateurs lambda (consultation des sélections).
Président du jury (gestion des sélections et des votes).
Futurs membres du jury (vote authentifié).
Objectifs :

Afficher les livres des sélections (1ère, 2ème, 3ème).
Permettre au président du jury de gérer les sélections et les votes.
Préparer l’extension future (authentification, vote automatisé).

### Fonctionnalités Principales

---

#### Fonctionnalité 1 :

Afficher les livres d’une sélection

#### Description :

Permettre à tout utilisateur de consulter les livres d’une sélection (1ère, 2ème ou 3ème), avec leurs détails.

#### Entrées :

Numéro de la sélection (1, 2 ou 3).

#### Sorties :

Liste des livres avec :

Titre, résumé, auteur, éditeur, personnages principaux, date de parution, nombre de pages, ISBN, prix éditeur.
Pour les auteurs : biographie (si disponible).

### Règles métiers :

---

Les données sont extraites de la base MySQL.
Seuls les 8 premiers auteurs (par ordre alphabétique) ont une biographie détaillée.
Les autres livres n’affichent que titre, auteur et éditeur.

### Exemple d’affichage :

```
Sélection 1 (15 romans) :
1. Titre : [Titre], Auteur : [Auteur], Éditeur : [Éditeur], Résumé : [Résumé], Personnages : [Personnages], Date : [Date], Pages : [Pages], ISBN : [ISBN], Prix : [Prix]
   Biographie : [Biographie si disponible]
...
```
