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

## 🚀 Lancer le projet localement

### 1. Lancer le backend (Flask)
```bash
python3 server.py
```

### 2. Lancer le frontend (React + Vite)
```bash
npm install
npm run dev
```

### 📍 Accès à l’application :
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

Conçu pour s’auto-former efficacement à Python et passer en 3e année avec les bases bien solides 💪  
> Tu veux contribuer, m’encourager ou poser une question ? N'hésite pas !

---
