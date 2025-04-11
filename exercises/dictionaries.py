exercises = [
    {
        "id": "dict_intro",
        "title": "📘 Introduction aux dictionnaires",
        "instruction": "Un dictionnaire associe des clés à des valeurs. Exemple :\n\nage = {'Alice': 25, 'Bob': 30}\nprint(age['Alice'])",
        "initial_code": "age = {'Alice': 25, 'Bob': 30}\nprint(age['Alice'])",
        "expected_output": "25",
        "level": 0,
        "theme": "dictionaries"
    },
    {
        "id": "dict_create",
        "title": "Créer un dictionnaire",
        "instruction": "Crée un dictionnaire infos avec les paires : 'nom': 'Jean', 'age': 28. Affiche-le.",
        "initial_code": "# Dico ici",
        "expected_output": "{'nom': 'Jean', 'age': 28}",
        "level": 1,
        "theme": "dictionaries"
    },
    {
        "id": "dict_access",
        "title": "Accéder à une valeur",
        "instruction": "Crée un dictionnaire capitales = {'France': 'Paris', 'Italie': 'Rome'} et affiche la capitale de l'Italie.",
        "initial_code": "# Accès par clé",
        "expected_output": "Rome",
        "level": 1,
        "theme": "dictionaries"
    },
    {
        "id": "dict_modify",
        "title": "Modifier une valeur",
        "instruction": "Crée un dico stock = {'pommes': 10}. Change le nombre de pommes à 15 et affiche le dico.",
        "initial_code": "# Modification ici",
        "expected_output": "{'pommes': 15}",
        "level": 1,
        "theme": "dictionaries"
    },
    {
        "id": "dict_add",
        "title": "Ajouter une entrée",
        "instruction": "Crée un dictionnaire vide, puis ajoute une paire 'clé': 'valeur'. Affiche le résultat.",
        "initial_code": "# Ajout d'une entrée",
        "expected_output": "{'clé': 'valeur'}",
        "level": 2,
        "theme": "dictionaries"
    },
    {
        "id": "dict_delete",
        "title": "📘 Supprimer une clé",
        "instruction": "On peut supprimer une entrée avec del. Exemple :\n\npersonne = {'nom': 'Luc'}\ndel personne['nom']",
        "initial_code": "personne = {'nom': 'Luc'}\ndel personne['nom']\nprint(personne)",
        "expected_output": "{}",
        "level": 2,
        "theme": "dictionaries"
    },
    {
        "id": "dict_loop",
        "title": "Parcourir un dictionnaire",
        "instruction": "Parcours ce dictionnaire et affiche chaque clé et valeur :\n\ncouleurs = {'rouge': '#FF0000', 'bleu': '#0000FF'}",
        "initial_code": "couleurs = {'rouge': '#FF0000', 'bleu': '#0000FF'}\n# Boucle ici",
        "expected_output": "rouge #FF0000\nbleu #0000FF",
        "level": 3,
        "theme": "dictionaries"
    },
    {
        "id": "dict_keys",
        "title": "Afficher les clés",
        "instruction": "Crée un dictionnaire et affiche uniquement ses clés avec .keys().",
        "initial_code": "d = {'x': 1, 'y': 2}\n# Affiche les clés",
        "expected_output": "dict_keys(['x', 'y'])",
        "level": 3,
        "theme": "dictionaries"
    },
    {
        "id": "dict_values",
        "title": "Afficher les valeurs",
        "instruction": "Affiche les valeurs du dico suivant : d = {'a': 10, 'b': 20}",
        "initial_code": "d = {'a': 10, 'b': 20}\n# Affiche les valeurs",
        "expected_output": "dict_values([10, 20])",
        "level": 3,
        "theme": "dictionaries"
    },
    {
        "id": "dict_get",
        "title": "📘 Utiliser get()",
        "instruction": "La méthode get() retourne la valeur associée à une clé, ou None si elle n'existe pas.\n\nexemple : age.get('Luc')",
        "initial_code": "age = {'Luc': 29}\nprint(age.get('Luc'))",
        "expected_output": "29",
        "level": 3,
        "theme": "dictionaries"
    },
    {
        "id": "dict_in",
        "title": "Vérifier l'existence d'une clé",
        "instruction": "Crée un dico animaux = {'chien': 4}. Si 'chien' est une clé, affiche 'ok'.",
        "initial_code": "# Vérifie si 'chien' existe",
        "expected_output": "ok",
        "level": 3,
        "theme": "dictionaries"
    },
    {
        "id": "dict_bonus_merge",
        "title": "🔁 Bonus : Fusionner deux dictionnaires",
        "instruction": "Fusionne {'a': 1} et {'b': 2} en un seul dictionnaire. Affiche le résultat.",
        "initial_code": "# Fusionne ici",
        "expected_output": "{'a': 1, 'b': 2}",
        "level": 4,
        "theme": "dictionaries"
    },
    {
        "id": "dict_bonus_nested",
        "title": "🔁 Bonus : Dictionnaire imbriqué",
        "instruction": "Crée un dictionnaire étudiant = {'nom': 'Nico', 'notes': [14, 16]} et affiche la deuxième note.",
        "initial_code": "# Notes imbriquées",
        "expected_output": "16",
        "level": 5,
        "theme": "dictionaries"
    }
]
