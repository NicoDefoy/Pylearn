exercises = [
    {
        "id": "tuple_intro",
        "title": "📘 Introduction aux tuples",
        "instruction": "Un tuple est une collection **ordonnée et immuable**. On le crée avec des parenthèses.\n\nexemple :\ncoord = (10, 20)\nprint(coord[0])",
        "initial_code": "coord = (10, 20)\nprint(coord[0])",
        "expected_output": "10",
        "level": 0,
        "theme": "sets_tuples",
        "hint": "Lis bien l'exemple et observe la syntaxe d'un tuple.",
        "solution_code": "coord = (10, 20)\nprint(coord[0])"
    },
    {
        "id": "tuple_create",
        "title": "Créer un tuple",
        "instruction": "Crée un tuple appelé infos avec les éléments 'Nico' et 28. Affiche-le.",
        "initial_code": "# Crée ton tuple ici",
        "expected_output": "('Nico', 28)",
        "level": 1,
        "theme": "sets_tuples",
        "hint": "Utilise des parenthèses pour créer le tuple.",
        "solution_code": "infos = ('Nico', 28)\nprint(infos)"
    },
    {
        "id": "tuple_access",
        "title": "Accéder à un élément du tuple",
        "instruction": "Crée un tuple jours = ('lundi', 'mardi') puis affiche le deuxième élément.",
        "initial_code": "# Accès tuple",
        "expected_output": "mardi",
        "level": 1,
        "theme": "sets_tuples",
        "hint": "Utilise l'index 1 pour accéder au deuxième élément.",
        "solution_code": "jours = ('lundi', 'mardi')\nprint(jours[1])"
    },
    {
        "id": "tuple_unpacking",
        "title": "📘 Décomposer un tuple (unpacking)",
        "instruction": "On peut affecter les valeurs d'un tuple à plusieurs variables en une seule ligne.\n\nex :\nnom, age = ('Paul', 30)",
        "initial_code": "nom, age = ('Paul', 30)\nprint(nom)\nprint(age)",
        "expected_output": "Paul\n30",
        "level": 2,
        "theme": "sets_tuples",
        "hint": "Lis bien l'exemple et observe l'affectation multiple.",
        "solution_code": "nom, age = ('Paul', 30)\nprint(nom)\nprint(age)"
    },
    {
        "id": "tuple_immutable",
        "title": "Tuple immuable",
        "instruction": "Crée un tuple fixe = (1, 2). Tente de modifier un élément. Gère l'erreur avec try/except.",
        "initial_code": "# Test d'immuabilité",
        "expected_output": "Tu ne peux pas changer un tuple",
        "level": 3,
        "theme": "sets_tuples",
        "hint": "Tente une affectation sur un tuple et attrape l'exception TypeError.",
        "solution_code": "fixe = (1, 2)\ntry:\n    fixe[0] = 10\nexcept TypeError:\n    print('Tu ne peux pas changer un tuple')"
    },
    {
        "id": "set_intro",
        "title": "📘 Introduction aux ensembles",
        "instruction": "Un ensemble (set) stocke des valeurs uniques. Exemple :\n\nfruits = {'pomme', 'banane'}\nprint(fruits)",
        "initial_code": "fruits = {'pomme', 'banane'}\nprint(fruits)",
        "expected_output": "{'pomme', 'banane'}",
        "level": 0,
        "theme": "sets_tuples",
        "hint": "Lis bien l'exemple et observe la syntaxe d'un set.",
        "solution_code": "fruits = {'pomme', 'banane'}\nprint(fruits)"
    },
    {
        "id": "set_add",
        "title": "Ajouter dans un set",
        "instruction": "Crée un set vide puis ajoute-lui 'kiwi'. Affiche le set.",
        "initial_code": "# Ajout dans un set",
        "expected_output": "{'kiwi'}",
        "level": 1,
        "theme": "sets_tuples",
        "hint": "Utilise la méthode add() sur un set vide.",
        "solution_code": "s = set()\ns.add('kiwi')\nprint(s)"
    },
    {
        "id": "set_remove",
        "title": "Supprimer dans un set",
        "instruction": "Crée un set = {'a', 'b'} et retire 'a' avec remove(). Affiche le set.",
        "initial_code": "# Supprime un élément",
        "expected_output": "{'b'}",
        "level": 2,
        "theme": "sets_tuples",
        "hint": "Utilise la méthode remove() sur le set.",
        "solution_code": "s = {'a', 'b'}\ns.remove('a')\nprint(s)"
    },
    {
        "id": "set_loop",
        "title": "Boucle sur un set",
        "instruction": "Parcours le set {'x', 'y'} et affiche chaque élément.",
        "initial_code": "# Parcours un set",
        "expected_output": "x\ny",
        "level": 2,
        "theme": "sets_tuples",
        "hint": "Utilise une boucle for pour parcourir le set.",
        "solution_code": "s = {'x', 'y'}\nfor elem in s:\n    print(elem)"
    },
    {
        "id": "set_union",
        "title": "📘 Union de sets",
        "instruction": "On peut unir deux sets avec union() ou |. Exemple :\na = {1, 2}, b = {2, 3}\nprint(a | b)",
        "initial_code": "a = {1, 2}\nb = {2, 3}\nprint(a | b)",
        "expected_output": "{1, 2, 3}",
        "level": 3,
        "theme": "sets_tuples",
        "hint": "Lis bien l'exemple et observe l'utilisation de | pour unir deux sets.",
        "solution_code": "a = {1, 2}\nb = {2, 3}\nprint(a | b)"
    },
    {
        "id": "set_intersection",
        "title": "Intersection de sets",
        "instruction": "Crée deux sets : {1,2,3} et {2,3,4}. Affiche leur intersection (éléments communs).",
        "initial_code": "# Intersection ici",
        "expected_output": "{2, 3}",
        "level": 3,
        "theme": "sets_tuples",
        "hint": "Utilise la méthode intersection() ou l'opérateur &.",
        "solution_code": "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(a & b)"
    },
    {
        "id": "set_difference",
        "title": "🔁 Bonus : Différence de sets",
        "instruction": "Affiche les éléments dans {1, 2, 3} qui ne sont pas dans {2, 3}.",
        "initial_code": "# Différence",
        "expected_output": "{1}",
        "level": 4,
        "theme": "sets_tuples",
        "hint": "Utilise la méthode difference() ou l'opérateur -.",
        "solution_code": "a = {1, 2, 3}\nb = {2, 3}\nprint(a - b)"
    },
    {
        "id": "tuple_in_set",
        "title": "🔁 Bonus : Tuples dans un set",
        "instruction": "Ajoute deux tuples distincts (1,2) et (3,4) dans un set, puis affiche-le.",
        "initial_code": "# Set de tuples",
        "expected_output": "{(1, 2), (3, 4)}",
        "level": 5,
        "theme": "sets_tuples",
        "hint": "Crée un set et ajoute deux tuples avec add().",
        "solution_code": "s = set()\ns.add((1, 2))\ns.add((3, 4))\nprint(s)"
    }
]
