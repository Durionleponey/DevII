# Fonctionnalités du Programme

# Objectif Principal

Le programme permet de gérer des fichiers CSV, effectuer des recherches rapides, générer des rapports statistiques détaillés, et faciliter la fusion de multiples fichiers CSV dans un format unique. Les fonctionnalités sont définies selon le modèle SMART (Spécifique, Mesurable, Atteignable, Réaliste, Temporel).

---

# Fonctionnalités Principales

# 1. Lecture des Fichiers CSV

- **Description** : Importer et lire des fichiers CSV en ligne par ligne dans un format exploitable (liste de listes).
- **SMART** :
  - *Spécifique* : Supporter uniquement les fichiers CSV avec encodage UTF-8.
  - *Mesurable* : Lecture complète d’un fichier CSV en moins de 2 secondes pour des fichiers jusqu’à 1000 lignes.
  - *Atteignable* : Utilisation de la bibliothèque Python `csv` pour une gestion simplifiée.
  - *Réaliste* : Compatible avec les formats CSV courants.
  - *Temporel* : Fonctionnalité prête à l’utilisation dès le lancement du programme.

# 2. Fusion de Fichiers CSV

- **Description** : Combiner plusieurs fichiers CSV d’un répertoire en un fichier unique, tout en évitant la duplication des en-têtes.
- **SMART** :
  - *Spécifique* : Fusionner tous les fichiers avec une structure compatible dans un répertoire donné.
  - *Mesurable* : Réussir la fusion pour 10 fichiers CSV (chacun de 500 lignes) en moins de 5 secondes.
  - *Atteignable* : Utilisation des structures Python optimisées pour la gestion de données.
  - *Réaliste* : Gérer les fichiers avec en-têtes différents en ajoutant une logique pour signaler les incohérences.
  - *Temporel* : Génération du fichier fusionné après une seule exécution.

# 3. Recherche dans un Fichier CSV

- **Description** : Rechercher des données dans une colonne spécifique, en affichant toutes les lignes correspondantes.
- **SMART** :
  - *Spécifique* : Recherche par mot-clé insensible à la casse.
  - *Mesurable* : Retourner les résultats pour une colonne de 1000 lignes en moins de 3 secondes.
  - *Atteignable* : Utilisation de boucles optimisées et gestion de colonnes dynamiques.
  - *Réaliste* : Interface utilisateur simple pour sélectionner la colonne et saisir les mots-clés.
  - *Temporel* : Recherche opérationnelle via un menu interactif.

# 4. Génération de Rapports Statistiques

- **Description** : Créer un rapport détaillé (texte) avec des statistiques calculées pour chaque colonne numérique.
- **SMART** :
  - *Spécifique* : Statistiques générées incluent : somme, moyenne, minimum, maximum, nombre d'entrées, écart-type.
  - *Mesurable* : Générer un rapport complet pour un fichier de 10 colonnes et 1000 lignes en moins de 5 secondes.
  - *Atteignable* : Stockage des statistiques dans une structure Python adaptée pour un accès rapide.
  - *Réaliste* : Exportation dans un fichier texte lisible (`summary_report.txt`).
  - *Temporel* : Rapport exporté immédiatement après génération.

# 5. Interface Utilisateur Interactive

- **Description** : Fournir un menu interactif pour accéder aux fonctionnalités du programme.
- **SMART** :
  - *Spécifique* : Menu interactif avec des options claires : lecture, fusion, recherche, génération de rapports.
  - *Mesurable* : Navigation intuitive avec un maximum de 3 interactions utilisateur pour accéder à une fonctionnalité.
  - *Atteignable* : Utilisation des entrées/sorties Python pour la gestion du menu.
  - *Réaliste* : Permettre à l’utilisateur de quitter le menu à tout moment.
  - *Temporel* : Menu opérationnel dès le démarrage du programme.

# 6. Gestion des Erreurs

- **Description** : Gérer les erreurs courantes, telles que les fichiers manquants ou mal formatés, avec des messages explicites.
- **SMART** :
  - *Spécifique* : Détecter et signaler les erreurs comme les fichiers introuvables ou incompatibles.
  - *Mesurable* : Identifier les erreurs immédiatement après leur occurrence.
  - *Atteignable* : Utilisation des blocs `try-except` Python.
  - *Réaliste* : Messages d’erreur adaptés à l’utilisateur final.
  - *Temporel* : Gestion des erreurs intégrée dans toutes les fonctionnalités principales.

---

# Fonctionnalités Avancées (Extensions Futures)

- Export des rapports en formats alternatifs (Excel, JSON).
- Analyse de corrélation entre colonnes numériques.
- Implémentation d’un moteur de recherche plus avancé (expressions régulières).
- Support multilingue pour le programme et les rapports.

---

# Notes Techniques

- **Bibliothèques utilisées** : `csv`, `os`.
- **Compatibilité** : Testé sous Python 3.9 et versions ultérieures.
- **Documentation** : Chaque module et fonction est documenté pour garantir une maintenance aisée.

### Rapport sur l’utilisation des outils d’IA

Dans ce projet, **ChatGPT** a été l’outil principal d’assistance.
Il a été utilisé pour générer du code Python, expliquer certains concepts, et fournir des idées pour structurer le projet.
ChatGPT s’est montré particulièrement efficace pour produire rapidement des solutions fonctionnelles
et fournir des recommandations adaptées au langage Python.

Par exemple, lors de la création d’une fonctionnalité pour trier des données ou gérer des exceptions,
ChatGPT a proposé des implémentations claires et concises.
De plus, son expertise en Python, un langage qu’il maîtrise très bien,
a permis d’aboutir à des solutions exploitables sans trop de corrections.

Cependant, certaines **limites** ont été rencontrées :
- ChatGPT propose souvent des solutions génériques qui nécessitent des ajustements pour coller parfaitement aux spécificités du projet.
- Lorsqu’il s’agit de configurations plus complexes ou de choix de design détaillés, l’IA manque parfois de profondeur et nécessite une validation humaine.

Il est aussi important de noter que ce projet, étant **relativement petit**,
se situe encore dans une échelle où ChatGPT reste performant et pertinent. Pour des projets plus vastes,
cette approche pourrait atteindre ses limites,
notamment pour la gestion des dépendances complexes ou la coordination entre plusieurs modules.
En revanche, pour un projet Python, la qualité des suggestions montre que l’outil est bien optimisé pour ce langage.

En résumé, ChatGPT a été un excellent assistant pour un projet de cette taille,
mais son utilisation requiert toujours une **supervision et un ajustement humains**
pour garantir des résultats de qualité.