exercises = [
    {
        "id": "dict_intro",
        "title": "📘 Introduction aux dictionnaires",
        "instruction": "Un dictionnaire associe des clés à des valeurs. Exemple :\n\nage = {'Alice': 25, 'Bob': 30}\nprint(age['Alice'])",
        "initial_code": "age = {'Alice': 25, 'Bob': 30}\nprint(age['Alice'])",
        "expected_output": "25",
        "level": 0,
        "theme": "dictionaries",
        "hint": "Lis bien l'exemple et observe la syntaxe d'un dictionnaire.",
        "solution_code": "age = {'Alice': 25, 'Bob': 30}\nprint(age['Alice'])"
    },
    {
        "id": "dict_create",
        "title": "Créer un dictionnaire",
        "instruction": "Crée un dictionnaire infos avec les paires : 'nom': 'Jean', 'age': 28. Affiche-le.",
        "initial_code": "# Dico ici",
        "expected_output": "{'nom': 'Jean', 'age': 28}",
        "level": 1,
        "theme": "dictionaries",
        "hint": "Utilise des accolades et sépare les paires clé:valeur par des virgules.",
        "solution_code": "infos = {'nom': 'Jean', 'age': 28}\nprint(infos)"
    },
    {
        "id": "dict_access",
        "title": "Accéder à une valeur",
        "instruction": "Crée un dictionnaire capitales = {'France': 'Paris', 'Italie': 'Rome'} et affiche la capitale de l'Italie.",
        "initial_code": "# Accès par clé",
        "expected_output": "Rome",
        "level": 1,
        "theme": "dictionaries",
        "hint": "Utilise la clé 'Italie' pour accéder à la valeur.",
        "solution_code": "capitales = {'France': 'Paris', 'Italie': 'Rome'}\nprint(capitales['Italie'])"
    },
    {
        "id": "dict_modify",
        "title": "Modifier une valeur",
        "instruction": "Crée un dico stock = {'pommes': 10}. Change le nombre de pommes à 15 et affiche le dico.",
        "initial_code": "# Modification ici",
        "expected_output": "{'pommes': 15}",
        "level": 1,
        "theme": "dictionaries",
        "hint": "Affecte 15 à la clé 'pommes'.",
        "solution_code": "stock = {'pommes': 10}\nstock['pommes'] = 15\nprint(stock)"
    },
    {
        "id": "dict_add",
        "title": "Ajouter une entrée",
        "instruction": "Crée un dictionnaire vide, puis ajoute une paire 'clé': 'valeur'. Affiche le résultat.",
        "initial_code": "# Ajout d'une entrée",
        "expected_output": "{'clé': 'valeur'}",
        "level": 2,
        "theme": "dictionaries",
        "hint": "Crée un dico vide puis ajoute une clé et une valeur.",
        "solution_code": "d = {}\nd['clé'] = 'valeur'\nprint(d)"
    },
    {
        "id": "dict_delete",
        "title": "📘 Supprimer une clé",
        "instruction": "On peut supprimer une entrée avec del. Exemple :\n\npersonne = {'nom': 'Luc'}\ndel personne['nom']",
        "initial_code": "personne = {'nom': 'Luc'}\ndel personne['nom']\nprint(personne)",
        "expected_output": "{}",
        "level": 2,
        "theme": "dictionaries",
        "hint": "Lis bien l'exemple et observe l'utilisation de del.",
        "solution_code": "personne = {'nom': 'Luc'}\ndel personne['nom']\nprint(personne)"
    },
    {
        "id": "dict_loop",
        "title": "Parcourir un dictionnaire",
        "instruction": "Parcours ce dictionnaire et affiche chaque clé et valeur :\n\ncouleurs = {'rouge': '#FF0000', 'bleu': '#0000FF'}",
        "initial_code": "couleurs = {'rouge': '#FF0000', 'bleu': '#0000FF'}\n# Boucle ici",
        "expected_output": "rouge #FF0000\nbleu #0000FF",
        "level": 3,
        "theme": "dictionaries",
        "hint": "Utilise une boucle for sur dico.items().",
        "solution_code": "couleurs = {'rouge': '#FF0000', 'bleu': '#0000FF'}\nfor cle, val in couleurs.items():\n    print(cle, val)"
    },
    {
        "id": "dict_keys",
        "title": "Afficher les clés",
        "instruction": "Crée un dictionnaire et affiche uniquement ses clés avec .keys().",
        "initial_code": "d = {'x': 1, 'y': 2}\n# Affiche les clés",
        "expected_output": "dict_keys(['x', 'y'])",
        "level": 3,
        "theme": "dictionaries",
        "hint": "Utilise la méthode .keys() sur le dictionnaire.",
        "solution_code": "d = {'x': 1, 'y': 2}\nprint(d.keys())"
    },
    {
        "id": "dict_values",
        "title": "Afficher les valeurs",
        "instruction": "Affiche les valeurs du dico suivant : d = {'a': 10, 'b': 20}",
        "initial_code": "d = {'a': 10, 'b': 20}\n# Affiche les valeurs",
        "expected_output": "dict_values([10, 20])",
        "level": 3,
        "theme": "dictionaries",
        "hint": "Utilise la méthode .values() sur le dictionnaire.",
        "solution_code": "d = {'a': 10, 'b': 20}\nprint(d.values())"
    },
    {
        "id": "dict_get",
        "title": "📘 Utiliser get()",
        "instruction": "La méthode get() retourne la valeur associée à une clé, ou None si elle n'existe pas.\n\nexemple : age.get('Luc')",
        "initial_code": "age = {'Luc': 29}\nprint(age.get('Luc'))",
        "expected_output": "29",
        "level": 3,
        "theme": "dictionaries",
        "hint": "Lis bien l'exemple et observe l'utilisation de get().",
        "solution_code": "age = {'Luc': 29}\nprint(age.get('Luc'))"
    },
    {
        "id": "dict_in",
        "title": "Vérifier l'existence d'une clé",
        "instruction": "Crée un dico animaux = {'chien': 4}. Si 'chien' est une clé, affiche 'ok'.",
        "initial_code": "# Vérifie si 'chien' existe",
        "expected_output": "ok",
        "level": 3,
        "theme": "dictionaries",
        "hint": "Utilise l'opérateur in pour vérifier la présence de la clé.",
        "solution_code": "animaux = {'chien': 4}\nif 'chien' in animaux:\n    print('ok')"
    },
    {
        "id": "dict_bonus_merge",
        "title": "🔁 Bonus : Fusionner deux dictionnaires",
        "instruction": "Fusionne {'a': 1} et {'b': 2} en un seul dictionnaire. Affiche le résultat.",
        "initial_code": "# Fusionne ici",
        "expected_output": "{'a': 1, 'b': 2}",
        "level": 4,
        "theme": "dictionaries",
        "hint": "Utilise l'opérateur | (Python 3.9+) ou update().",
        "solution_code": "d1 = {'a': 1}\nd2 = {'b': 2}\nd3 = d1 | d2\nprint(d3)"
    },
    {
        "id": "dict_bonus_nested",
        "title": "🔁 Bonus : Dictionnaire imbriqué",
        "instruction": "Crée un dictionnaire étudiant = {'nom': 'Nico', 'notes': [14, 16]} et affiche la deuxième note.",
        "initial_code": "# Notes imbriquées",
        "expected_output": "16",
        "level": 5,
        "theme": "dictionaries",
        "hint": "Accède à la clé 'notes' puis à l'index 1.",
        "solution_code": "etudiant = {'nom': 'Nico', 'notes': [14, 16]}\nprint(etudiant['notes'][1])"
    }
]
