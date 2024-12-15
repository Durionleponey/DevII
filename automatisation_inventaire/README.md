# README

## [Lien vers la vidéo](https://ephec-my.sharepoint.com/:v:/g/personal/he201721_students_ephec_be/ERRrJoHX99tNinB8BemZpiEBjNRsQZ15ffdGFnL7zEy7Fg?e=bbSx2d)



## Description du Programme

Ce programme permet de gérer et manipuler facilement des fichiers CSV grâce à des fonctionnalités telles que la fusion de fichiers, la recherche, et la génération de rapports statistiques détaillés. Il est conçu pour être simple d'utilisation, rapide et efficace.

---

## Fonctionnalités Principales

- Lecture des fichiers CSV.
- Fusion de multiples fichiers CSV en un seul fichier unique.
- Recherche interactive dans les fichiers CSV.
- Génération de rapports statistiques (somme, moyenne, minimum, maximum, écart-type).
- Gestion des erreurs avec des messages explicites.

---

## Installation

### Prérequis

- Python 3.9 ou version ultérieure.
- Système d'exploitation compatible avec Python (Windows, macOS, Linux).

### Étapes d'installation

1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   ```

2. Naviguez dans le dossier du projet :
   ```bash
   cd votre-repo
   ```

3. Installez un environnement virtuel (optionnel mais recommandé) :
   ```bash
   python -m venv env
   source env/bin/activate  # Sur Windows : env\Scripts\activate
   ```

4. Installez les dépendances nécessaires (s'il y en a) :
   ```bash
   pip install -r requirements.txt
   ```

---

## Utilisation

### Lancer le Programme

Exécutez le fichier principal du programme :
```bash
python main.py
```

1. Placez vos fichiers CSV dans un répertoire dédié (par exemple `csv_files/`).
2. Recherchez des données spécifiques dans ce fichier fusionné.
3. Générez un rapport pour analyser les données.

---

## Notes Techniques

- Le programme gère automatiquement les erreurs courantes (fichiers manquants, mauvais format, etc.).
- Les rapports sont exportés sous forme de fichiers texte (`summary_report.txt`).

---
