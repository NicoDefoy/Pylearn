exercises = [
    {
        "id": "files_intro",
        "title": "📘 Lire un fichier texte",
        "instruction": "En Python, on lit un fichier avec open(). Exemple :\n\nwith open('monfichier.txt', 'r') as f:\n    contenu = f.read()\n    print(contenu)",
        "initial_code": "with open('monfichier.txt', 'r') as f:\n    contenu = f.read()\n    print(contenu)",
        "expected_output": "",
        "level": 0,
        "theme": "files_exceptions"
    },
    {
        "id": "files_write",
        "title": "Écrire dans un fichier",
        "instruction": "Utilise open() avec le mode 'w' pour écrire 'Bonjour' dans un fichier texte.",
        "initial_code": "# Écris dans un fichier",
        "expected_output": "",
        "level": 1,
        "theme": "files_exceptions"
    },
    {
        "id": "files_append",
        "title": "Ajouter à un fichier",
        "instruction": "Ajoute une ligne 'Nouvelle ligne' dans un fichier texte sans supprimer le contenu précédent.",
        "initial_code": "# Ajoute au fichier",
        "expected_output": "",
        "level": 2,
        "theme": "files_exceptions"
    },
    {
        "id": "files_readlines",
        "title": "Lire ligne par ligne",
        "instruction": "Lis un fichier et affiche chaque ligne séparément avec une boucle.",
        "initial_code": "# Affiche les lignes une à une",
        "expected_output": "",
        "level": 2,
        "theme": "files_exceptions"
    },
    {
        "id": "exceptions_intro",
        "title": "📘 Gérer une erreur",
        "instruction": "Une erreur peut être interceptée avec try/except. Exemple :\n\ntry:\n    print(1/0)\nexcept ZeroDivisionError:\n    print(\"Erreur\")",
        "initial_code": "try:\n    print(1/0)\nexcept ZeroDivisionError:\n    print(\"Erreur\")",
        "expected_output": "Erreur",
        "level": 2,
        "theme": "files_exceptions"
    },
    {
        "id": "exceptions_file",
        "title": "Fichier manquant",
        "instruction": "Lis un fichier 'absent.txt'. Si le fichier n'existe pas, affiche 'Introuvable'.",
        "initial_code": "# Gère l'erreur fichier",
        "expected_output": "Introuvable",
        "level": 3,
        "theme": "files_exceptions"
    },
    {
        "id": "exceptions_value",
        "title": "Erreur de conversion",
        "instruction": "Demande à Python de convertir 'abc' en entier avec int(). Gère l’erreur avec ValueError et affiche 'Invalide'.",
        "initial_code": "# Conversion invalide",
        "expected_output": "Invalide",
        "level": 3,
        "theme": "files_exceptions"
    },
    {
        "id": "exceptions_finally",
        "title": "🔁 Bonus : finally",
        "instruction": "Utilise try/except/finally. Affiche 'Toujours là' dans le bloc finally.",
        "initial_code": "try:\n    x = 1 / 0\nexcept:\n    print('Erreur')\nfinally:\n    print('Toujours là')",
        "expected_output": "Erreur\nToujours là",
        "level": 4,
        "theme": "files_exceptions"
    },
    {
        "id": "exceptions_multiple",
        "title": "🔁 Bonus : plusieurs exceptions",
        "instruction": "Gère ZeroDivisionError ET ValueError. Affiche 'Erreur de calcul' dans les deux cas.",
        "initial_code": "# Plusieurs exceptions",
        "expected_output": "Erreur de calcul",
        "level": 5,
        "theme": "files_exceptions"
    }
]
