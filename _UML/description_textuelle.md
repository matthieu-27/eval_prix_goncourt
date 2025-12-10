# Description textuelle des cas d'utilisations

## Acteurs

- User (Utilisateur) : Toute personne souhaitant consulter les informations publiques sur les sélections.
- President (Président du jury) : Responsable de la gestion des sélections et des votes finaux.
- Member (Membre du jury) : Personne autorisée à voter pour les sélections et le lauréat (fonctionnalité future).

## Cas d'utilisations :

### Cas d'utilisation 1 :

---

| Elément                       | Description                                                                                                                                             |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| __Nom des cas d’utilisation__ | Cas 1 : Afficher les livres de chaque sélection                                                                                                         |
| __But / Objectif__            | L’utilisateur peut consulter la liste des livres pour chaque sélection (1ère, 2ème ou 3ème), avec leurs détails (titre, auteur, éditeur, résumé, etc.). |
| __Acteur principal__          | User                                                                                                                                                    |
| __Préconditions__             | Les sélections sont enregistrées dans la base de données.                                                                                               |
| __Scénario principal__        | 1. L’utilisateur choisit une sélection (1, 2 ou 3).<br/>2. Le système affiche les livres de cette sélection avec leurs informations.                    |
| __Scénario alternatif__       | Si la sélection n’existe pas, le système affiche un message d’erreur.                                                                                   |
| __Postconditions__            | Aucune.                                                                                                                                                 |

### Cas d'utilisation 2 :

---


| Elément                       | Description                                                                                                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| __Nom des cas d’utilisation__ | Cas 2 : Indiquer les livres faisant partie de la 2ème et 3ème sélection                                                                                                                                                   |
| __But / Objectif__            | Le président du jury sélectionne les livres qui passeront en 2ème ou 3ème sélection.                                                                                                                                      |
| __Acteur principal__          | President                                                                                                                                                                                                                 |
| __Préconditions__             | La sélection précédente doit être validée (ex : la 1ère sélection doit exister pour créer la 2ème).                                                                                                                       |
| __Scénario principal__        | 1. Le président choisit la sélection à mettre à jour (2ème ou 3ème). <br/> 2. Le président sélectionne les livres (par ISBN) parmi ceux de la sélection précédente. <br/> 3. Le système enregistre la nouvelle sélection. |
| __Scénario alternatif__       | Si la sélection n’existe pas, le système affiche un message d’erreur.                                                                                                                                                     |
| __Postconditions__            | - La 2ème sélection doit contenir 8 livres (issus de la 1ère).<br/> - La 3ème sélection doit contenir 4 livres (issus de la 2ème).                                                                                        |


### Cas d'utilisation 3 :

---

| Elément                       | Description                                                                                                                                                               |
|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| __Nom des cas d’utilisation__ | Cas 3 : Indiquer le nombre de votes pour chaque livre présent au dernier tour du scrutin                                                                                  |
| __But / Objectif__            | Le président saisit le nombre de votes obtenus par chaque livre finaliste (3ème sélection).                                                                               |
| __Acteur principal__          | President                                                                                                                                                                 |
| __Préconditions__             | La 3ème sélection doit être validée.                                                                                                                                      |
| __Scénario principal__        | 1.Le président accède à la liste des finalistes. <br/> 2. Pour chaque livre, il saisit le nombre de votes. <br/> Le système enregistre les votes et détermine le lauréat. |
| __Scénario alternatif__       | Si le nombre de votes est invalide (négatif ou non entier), le système demande une nouvelle saisie.                                                                       |
| __Postconditions__            | Aucune.                                                                                                                                                                   |


[//]: # (### Cas d'utilisation 4 :)

[//]: # ()
[//]: # (---)

[//]: # ()
[//]: # (| Elément                       | Description                                                                                                                                                                              |)

[//]: # (|-------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|)

[//]: # (| __Nom des cas d’utilisation__ | Cas 4 : Voter pour les 2ème et 3ème sélections                                                                                                                                           |)

[//]: # (| __But / Objectif__            | Un membre du jury s’identifie et vote pour un livre dans les 2ème ou 3ème sélections.                                                                                                    |)

[//]: # (| __Acteur principal__          | Member                                                                                                                                                                                   |)

[//]: # (| __Préconditions__             | - Le membre doit être authentifié. <br/> - La sélection concernée doit être ouverte aux votes.                                                                                           |)

[//]: # (| __Scénario principal__        | 1. Le membre s’identifie. <br/> 2. Le système affiche les livres de la sélection concernée. <br/> Le membre choisit un livre et valide son vote. <br/> 4. Le système enregistre le vote. |)

[//]: # (| __Scénario alternatif__       | - Si le membre a déjà voté, le système l’en informe et refuse le vote. <br/> - Si la sélection n’est pas ouverte aux votes, le système affiche un message d’erreur.                      |)

[//]: # (| __Postconditions__            | Aucune.                                                                                                                                                                                  |)
