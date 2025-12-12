# Prix Goncourt - Application de gestion

Une application Python pour gérer le processus de sélection et de vote du Prix Goncourt.

## Description

Ce projet permet de :

- Gérer les différentes sélections de livres pour le Prix Goncourt
- Enregistrer les votes pour la sélection finale
- Déterminer le lauréat du prix

## Installation

1. Clonez le dépôt :

   ```bash
   git clone [url-du-depot]
   cd eval_prix_goncourt
   ```

2. Créez la base de données.

3. Configurez les identifiants de connexion à la base de données dans `daos/dao.py`.

4. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

Lancez l'application :

```bash
python main.py
```
