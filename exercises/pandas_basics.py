exercises = [
    {
        "id": "pandas_intro",
        "title": "📘 Introduction à Pandas",
        "instruction": "Pandas permet de manipuler des données sous forme de tableau. On commence par importer :\n\nimport pandas as pd",
        "initial_code": "import pandas as pd\nprint('Pandas prêt !')",
        "expected_output": "Pandas prêt !",
        "level": 0,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_df_create",
        "title": "Créer un DataFrame",
        "instruction": "Crée un DataFrame avec les données suivantes : noms = ['Alice', 'Bob'], âges = [25, 30]",
        "initial_code": "# Crée un DataFrame",
        "expected_output": "",
        "level": 1,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_read_csv",
        "title": "📘 Lire un fichier CSV",
        "instruction": "On peut lire un CSV avec read_csv. Exemple :\n\ndf = pd.read_csv('fichier.csv')",
        "initial_code": "import pandas as pd\ndf = pd.read_csv('data.csv')\nprint(df.head())",
        "expected_output": "",
        "level": 1,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_select_column",
        "title": "Accéder à une colonne",
        "instruction": "Accède à la colonne 'nom' dans un DataFrame et affiche-la.",
        "initial_code": "# Sélection de colonne",
        "expected_output": "",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_filter_rows",
        "title": "Filtrer les lignes",
        "instruction": "Affiche les lignes du DataFrame où l'âge est supérieur à 25.",
        "initial_code": "# Filtrage de lignes",
        "expected_output": "",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_mean",
        "title": "📘 Moyenne d'une colonne",
        "instruction": "La méthode .mean() permet de calculer la moyenne d'une colonne numérique.",
        "initial_code": "import pandas as pd\ndf = pd.DataFrame({'valeurs': [10, 20, 30]})\nprint(df['valeurs'].mean())",
        "expected_output": "20.0",
        "level": 2,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_new_column",
        "title": "Ajouter une colonne",
        "instruction": "Ajoute une colonne 'statut' avec la valeur 'ok' pour chaque ligne.",
        "initial_code": "# Nouvelle colonne",
        "expected_output": "",
        "level": 3,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_groupby",
        "title": "🔁 Bonus : groupby",
        "instruction": "Groupe les données par 'catégorie' et affiche la moyenne d'une colonne numérique.",
        "initial_code": "# Group by",
        "expected_output": "",
        "level": 4,
        "theme": "pandas_basics"
    },
    {
        "id": "pandas_sort",
        "title": "🔁 Bonus : Trier les lignes",
        "instruction": "Trie un DataFrame par la colonne 'score' de manière décroissante.",
        "initial_code": "# Tri décroissant",
        "expected_output": "",
        "level": 4,
        "theme": "pandas_basics"
    }
]
