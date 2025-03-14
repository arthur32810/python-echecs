# Gestionnaire de tournois d'échec

## 1. Créer votre environnement dédié au projet
Pour créer votre environnemenet dédié au projet, nous vous recommandons d'executer la commande suivante : `python -m venv env`

## 2. Activation de l'environnement virtuel
Pour activer l'environnement virtuel, que nous venons de créer.
Par exemple pour linux, entrer la commander suivante : `source env/bin/activate`

## 3. Installer les dépendances du projet
Une fois l'environnement activé, pour installer les dépendances du projet il faut executer la commande suivante : 
`pip install -r requirements.txt`

## 4. Executer le module Eches
Une fois positionné dans l'environnement, vous pouvez executer le module grâce à la commande : `python -m echecs`

## Générer un rapport flake8
Flake8 est un outil qui permet d'écrire du code propre et qualité en vérifiant qu'il respecte les bonnes pratiques ( PEP8 ) et en signalant les erreurs courantes.

### Générer le rapport

Vous avez la possibilité de générer un rapport via l'outil flake 8 pour ce faire, utiliser la commande:
`flake8 --format=html --htmldir=flake-report`

### Consulter le rapport
Pour consulter le rapport, veuillez vous rendre dans le dossier flake-report qui vient d'être généré et ouvrez la page index.html.