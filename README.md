# 🐍 Python Learning App

Une application web pour apprendre Python de façon progressive, interactive et fun !  
Développée avec ❤️ en React (frontend) et Flask (backend).

---

## 🗂️ Structure de l’app

```
h-9928-main/
│
├── server.py              # Backend Flask : exécution & vérification du code
├── exercises/             # Dossier contenant tous les fichiers d’exercices
│   ├── __init__.py
│   ├── variables.py
│   ├── functions.py
│   ├── conditions.py
│   ├── loops.py
│   ├── strings.py
│   ├── lists.py
│   ├── dictionaries.py
│   ├── sets_tuples.py
│   ├── pandas_basics.py
│   ├── numpy_basics.py
│   ├── scikit_learn.py
│   ├── env_imports.py
│   └── classes.py
│
├── lessons/               # Dossier contenant toutes les leçons théoriques (format ultra-débutant)
│   ├── variables.py
│   ├── affichage_commentaires.py
│   ├── operations_de_base.py
│   ├── conditions.py
│   ├── boucles.py
│   └── ...
│
├── src/                   # Frontend React (TypeScript + Vite)
│   ├── components/
│   │   ├── App.tsx
│   │   ├── Header.tsx
│   │   ├── Home.tsx
│   │   ├── ExerciseList.tsx
│   │   ├── ThemeExercises.tsx
│   │   ├── Exercise.tsx
│   │   ├── CodeEditor.tsx
│   │   └── ProgressTracker.tsx
│   └── ...
└── README.md              # Ce fichier
```

---

## 🧠 Contenu pédagogique

Chaque **fichier `.py` dans le dossier `exercises/`** correspond à un **thème**.  
Chaque thème contient :
- 📘 **Définitions claires** (niveau 0)
- 🧪 **Exemples interactifs**
- 🧩 **Exercices progressifs** (niveau 1 à 5)
- 🧠 **Bonus pour les plus chauds**

---

## 📚 Leçons théoriques (ultra-débutant)

Chaque **fichier `.py` dans le dossier `lessons/`** correspond à une **leçon** (notion, concept, ou bibliothèque).  
Chaque leçon contient :
- 🧩 **Blocs pédagogiques colorés** (définition, règle, astuce, erreur fréquente...)
- 📝 **Exemples de code** avec vrais noms Python (int, str, etc.)
- 💡 **Astuces et erreurs fréquentes**
- 🧑‍🎓 **Explications étape par étape, sans jargon**

**Pour ajouter ou modifier une leçon :**
- Crée/modifie un fichier dans `lessons/` (ex : `boucles.py`)
- Respecte la structure :
  - `title` : titre de la leçon
  - `description` : texte pédagogique découpé en blocs (utilise ### pour chaque bloc)
  - `examples` : liste d'exemples de code (avec explication)
  - `tips` : astuces (optionnel)
  - `common_mistakes` : erreurs fréquentes (optionnel)

Les leçons sont affichées dans l'interface avec la même UX que les exercices, adaptées à un vrai débutant.

---

## 🚀 Lancer le projet localement

### 1. Lancer le backend (Flask)
```bash
source venv/bin/activate
./venv/bin/python server.py
```

### 2. Lancer le frontend (React + Vite)
```bash
npm install
npm run dev
```

### 📍 Accès à l'application :
> http://localhost:8080

---

## ✨ Fonctionnalités

- Interface propre et responsive
- Exécution du code Python en temps réel
- Feedback interactif ✅ 🟡 ❌
- Suivi de progression
- Thèmes clairs et bien séparés

---

## 📦 Tech stack

- 🧠 Python 3 + Flask
- ⚛️ React + TypeScript + Vite
- 🎨 Tailwind CSS + shadcn/ui
- 🧪 CodeMirror (ou Monaco) pour l'éditeur de code

---

## 🙌 Projet perso en cours de perfectionnement

Conçu pour s'auto-former efficacement à Python et passer en 3e année avec les bases bien solides 💪  
> Tu veux contribuer, m'encourager ou poser une question ? N'hésite pas !

---
