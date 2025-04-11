exercises = [
    {
        "id": "env_intro",
        "title": "📘 Introduction aux imports",
        "instruction": "On peut importer un module standard avec `import`. Exemple :\n\nimport math",
        "initial_code": "import math\nprint(math.sqrt(16))",
        "expected_output": "4.0",
        "level": 0,
        "theme": "env_imports"
    },
    {
        "id": "env_import_math",
        "title": "Importer un module standard",
        "instruction": "Importe le module `math` et affiche `math.pi`.",
        "initial_code": "# Import ici",
        "expected_output": "3.141592653589793",
        "level": 1,
        "theme": "env_imports"
    },
    {
        "id": "env_from_import",
        "title": "Importer une fonction spécifique",
        "instruction": "Importe seulement `sqrt` depuis `math`. Affiche la racine carrée de 25.",
        "initial_code": "# from ... import ...",
        "expected_output": "5.0",
        "level": 1,
        "theme": "env_imports"
    },
    {
        "id": "env_import_alias",
        "title": "Donner un alias à un module",
        "instruction": "Importe `math` sous le nom `m`. Affiche `m.floor(3.7)`.",
        "initial_code": "# Alias d'import",
        "expected_output": "3",
        "level": 2,
        "theme": "env_imports"
    },
    {
        "id": "env_pip_theory",
        "title": "📘 Installer un package avec pip",
        "instruction": "`pip install nom_du_package` permet d’installer un package externe. Cela ne s'écrit **pas** dans le code Python, mais dans le terminal.",
        "initial_code": "# Juste un exemple\n# pip install requests",
        "expected_output": "",
        "level": 2,
        "theme": "env_imports"
    },
    {
        "id": "env_pip_question",
        "title": "Commande pip théorique",
        "instruction": "Quelle commande te permet d’installer le package `requests` avec pip ?",
        "initial_code": "# Commande ici (commentée)",
        "expected_output": "# pip install requests",
        "level": 2,
        "theme": "env_imports"
    },
    {
        "id": "env_import_requests",
        "title": "Utiliser un module externe",
        "instruction": "Importe `requests` et fais une requête GET sur `https://httpbin.org/get`. Affiche le code de réponse.",
        "initial_code": "# Requête GET ici",
        "expected_output": "200",
        "level": 3,
        "theme": "env_imports"
    },
    {
        "id": "env_virtualenv",
        "title": "📘 Créer un virtualenv (théorie)",
        "instruction": "On crée un environnement virtuel avec :\n\n`python -m venv env`\n\nOn l’active avec : `source env/bin/activate` (Linux/Mac)",
        "initial_code": "# Environnement virtuel",
        "expected_output": "",
        "level": 3,
        "theme": "env_imports"
    },
    {
        "id": "env_virtualenv_cmd",
        "title": "Commande virtualenv",
        "instruction": "Écris la commande pour créer un environnement `mon_env`.",
        "initial_code": "# Commande",
        "expected_output": "# python -m venv mon_env",
        "level": 3,
        "theme": "env_imports"
    },
    {
        "id": "env_requirements",
        "title": "📘 Fichier requirements.txt",
        "instruction": "On sauvegarde les packages avec :\n\n`pip freeze > requirements.txt`\n\nEt on les installe avec :\n\n`pip install -r requirements.txt`",
        "initial_code": "# Extrait du terminal",
        "expected_output": "",
        "level": 3,
        "theme": "env_imports"
    },
    {
        "id": "env_custom_module",
        "title": "🔁 Bonus : Créer son propre module",
        "instruction": "Crée un fichier `utils.py` avec une fonction bonjour(). Importe-la dans un autre fichier et appelle-la.",
        "initial_code": "# Exemple multi-fichier",
        "expected_output": "Bonjour",
        "level": 4,
        "theme": "env_imports"
    }
]
