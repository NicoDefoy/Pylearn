
# PyLearn - Application d'apprentissage Python

Une application locale pour apprendre Python avec un éditeur de code intégré et un suivi de progression.

## Fonctionnalités

- Éditeur de code Python avec coloration syntaxique
- Exercices progressifs
- Retour immédiat sur le code
- Suivi de progression
- Sauvegarde locale des exercices et solutions

## Installation

1. Clonez ce dépôt
2. Installez les dépendances frontend:
   ```
   npm install
   ```
3. Installez les dépendances Python:
   ```
   pip install flask
   ```

## Démarrage

1. Construisez l'application React:
   ```
   npm run build
   ```
2. Démarrez le serveur Flask:
   ```
   python server.py
   ```
3. Accédez à l'application dans votre navigateur:
   ```
   http://localhost:5000
   ```

## Développement

Pour le développement, vous pouvez exécuter:

1. Serveur de développement React:
   ```
   npm run dev
   ```
2. Serveur Flask:
   ```
   python server.py
   ```

## Stockage local

L'application utilise localStorage pour sauvegarder:
- Les exercices et leur état (terminé ou non)
- Le code des solutions
- La progression globale

## Personnalisation

Vous pouvez ajouter de nouveaux exercices en modifiant le tableau `defaultExercises` dans le composant `ExerciseList.tsx`.
