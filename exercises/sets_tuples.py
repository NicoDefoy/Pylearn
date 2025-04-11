exercises = [
    {
        "id": "tuple_intro",
        "title": "📘 Introduction aux tuples",
        "instruction": "Un tuple est une collection **ordonnée et immuable**. On le crée avec des parenthèses.\n\nexemple :\ncoord = (10, 20)\nprint(coord[0])",
        "initial_code": "coord = (10, 20)\nprint(coord[0])",
        "expected_output": "10",
        "level": 0,
        "theme": "sets_tuples"
    },
    {
        "id": "tuple_create",
        "title": "Créer un tuple",
        "instruction": "Crée un tuple appelé infos avec les éléments 'Nico' et 28. Affiche-le.",
        "initial_code": "# Crée ton tuple ici",
        "expected_output": "('Nico', 28)",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "tuple_access",
        "title": "Accéder à un élément du tuple",
        "instruction": "Crée un tuple jours = ('lundi', 'mardi') puis affiche le deuxième élément.",
        "initial_code": "# Accès tuple",
        "expected_output": "mardi",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "tuple_unpacking",
        "title": "📘 Décomposer un tuple (unpacking)",
        "instruction": "On peut affecter les valeurs d’un tuple à plusieurs variables en une seule ligne.\n\nex :\nnom, age = ('Paul', 30)",
        "initial_code": "nom, age = ('Paul', 30)\nprint(nom)\nprint(age)",
        "expected_output": "Paul\n30",
        "level": 2,
        "theme": "sets_tuples"
    },
    {
        "id": "tuple_immutable",
        "title": "Tuple immuable",
        "instruction": "Crée un tuple fixe = (1, 2). Tente de modifier un élément. Gère l’erreur avec try/except.",
        "initial_code": "# Test d'immuabilité",
        "expected_output": "Tu ne peux pas changer un tuple",
        "level": 3,
        "theme": "sets_tuples"
    },
    {
        "id": "set_intro",
        "title": "📘 Introduction aux sets (ensembles)",
        "instruction": "Un set est une collection **non ordonnée et sans doublons**. On l’écrit avec des accolades {} ou set().",
        "initial_code": "fruits = {'pomme', 'banane', 'pomme'}\nprint(fruits)",
        "expected_output": "{'pomme', 'banane'}",
        "level": 0,
        "theme": "sets_tuples"
    },
    {
        "id": "set_add",
        "title": "Ajouter dans un set",
        "instruction": "Crée un set vide puis ajoute-lui 'kiwi'. Affiche le set.",
        "initial_code": "# Ajout dans un set",
        "expected_output": "{'kiwi'}",
        "level": 1,
        "theme": "sets_tuples"
    },
    {
        "id": "set_remove",
        "title": "Supprimer dans un set",
        "instruction": "Crée un set = {'a', 'b'} et retire 'a' avec remove(). Affiche le set.",
        "initial_code": "# Supprime un élément",
        "expected_output": "{'b'}",
        "level": 2,
        "theme": "sets_tuples"
    },
    {
        "id": "set_loop",
        "title": "Boucle sur un set",
        "instruction": "Parcours le set {'x', 'y'} et affiche chaque élément.",
        "initial_code": "# Parcours un set",
        "expected_output": "x\ny",
        "level": 2,
        "theme": "sets_tuples"
    },
    {
        "id": "set_union",
        "title": "📘 Union de sets",
        "instruction": "On peut unir deux sets avec union() ou |. Exemple :\na = {1, 2}, b = {2, 3}\nprint(a | b)",
        "initial_code": "a = {1, 2}\nb = {2, 3}\nprint(a | b)",
        "expected_output": "{1, 2, 3}",
        "level": 3,
        "theme": "sets_tuples"
    },
    {
        "id": "set_intersection",
        "title": "Intersection de sets",
        "instruction": "Crée deux sets : {1,2,3} et {2,3,4}. Affiche leur intersection (éléments communs).",
        "initial_code": "# Intersection ici",
        "expected_output": "{2, 3}",
        "level": 3,
        "theme": "sets_tuples"
    },
    {
        "id": "set_difference",
        "title": "🔁 Bonus : Différence de sets",
        "instruction": "Affiche les éléments dans {1, 2, 3} qui ne sont pas dans {2, 3}.",
        "initial_code": "# Différence",
        "expected_output": "{1}",
        "level": 4,
        "theme": "sets_tuples"
    },
    {
        "id": "tuple_in_set",
        "title": "🔁 Bonus : Tuples dans un set",
        "instruction": "Ajoute deux tuples distincts (1,2) et (3,4) dans un set, puis affiche-le.",
        "initial_code": "# Set de tuples",
        "expected_output": "{(1, 2), (3, 4)}",
        "level": 5,
        "theme": "sets_tuples"
    }
]
