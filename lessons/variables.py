lesson = {
    "title": "Variables et Types",
    "description": (
        "### Qu’est-ce qu’une variable ?\n"
        "Imagine une boîte sur laquelle tu colles une étiquette. Cette étiquette, c’est le nom de la variable. Tu peux mettre ce que tu veux dans la boîte : un nombre, un mot, etc.\n\n"
        "En Python, une variable sert à retenir une information pour la réutiliser plus tard.\n\n"
        "### Comment créer une variable ?\n"
        "On écrit le nom de la variable, puis un =, puis la valeur à stocker.\n\n"
        "Exemples :\n"
        "age = 10\nnom = 'Alice'\nprix = 3.5\n\n"
        "### Les types de valeurs (expliqué simplement)\n"
        "Quand tu ranges quelque chose dans une boîte (une variable), tu peux y mettre :\n"
        "- Un nombre entier : par exemple 7, -2, 0. C'est un nombre sans virgule. On appelle ça un 'entier' (en anglais : integer, abrégé en int).\n"
        "- Un nombre à virgule : par exemple 3.14, -0.5. C'est un nombre qui n'est pas rond, il a une partie après la virgule. On appelle ça un 'nombre à virgule' (en anglais : float).\n"
        "- Un texte : par exemple 'bonjour', 'Alice', '42'. C'est tout ce qui est entre guillemets. On appelle ça une 'chaîne de caractères' (en anglais : string, abrégé en str).\n"
        "- Vrai ou faux : par exemple True, False. C'est une valeur qui ne peut être que vraie ou fausse, comme une réponse oui/non. On appelle ça un 'booléen' (en anglais : boolean, abrégé en bool).\n\n"
        "### Exemples\n"
        "# int\nage = 10\n\n# float\nprix = 3.5\n\n# str\nnom = 'Alice'\n\n# bool\nest_majeur = True\n\n"
        "### Afficher une variable\n"
        "Pour voir ce qu’il y a dans la boîte, on utilise la fonction print() :\n"
        "nom = 'Bob'\nprint(nom)  # Affiche Bob\n\n"
        "### Changer la valeur d’une variable\n"
        "On peut remplacer ce qu’il y a dans la boîte à tout moment :\n"
        "score = 0\nscore = 10\nprint(score)  # Affiche 10\n\n"
        "### Règles pour nommer une variable\n"
        "- Pas d’espace\n- Pas de chiffre au début\n- Pas de caractères spéciaux\n- Pas de mot réservé (comme print, if, etc.)\n- Utilise des noms clairs : age, prix_total, nom_utilisateur\n\n"
        "### Astuces\n"
        "- Les guillemets (simples ou doubles) servent pour les textes\n- Les majuscules/minuscules comptent (Nom ≠ nom)\n- On peut vérifier le type d’une variable avec la fonction type() : type(nom)\n- On peut changer la valeur d’une variable à tout moment\n\n"
        "### Erreurs fréquentes\n"
        "- Oublier les guillemets pour un texte (ex : nom = Alice au lieu de nom = 'Alice')\n- Mettre un espace dans le nom (ex : mon age = 5 → interdit)\n- Utiliser un mot réservé (ex : print = 3 → interdit)\n- Confondre = (affectation) et == (comparaison)\n"
    ),
    "examples": [
        {
            "code": "# int\nage = 25\n\n# str\nnom = 'Alice'\n\n# float\nprix = 19.99\n\n# bool\nest_majeur = True",
            "explanation": "Déclaration de variables de différents types (avec les vrais noms anglais)."
        },
        {
            "code": "# On peut réutiliser une variable\nprix = 10\nprix = prix + 5  # prix vaut maintenant 15",
            "explanation": "On peut modifier la valeur d'une variable."
        },
        {
            "code": "# Afficher une variable\nnom = 'Bob'\nprint(nom)",
            "explanation": "La fonction print permet d'afficher la valeur d'une variable."
        }
    ],
    "tips": [
        "On peut vérifier le type d'une variable avec la fonction type() : type(nom)",
        "Attention aux fautes de frappe dans les noms de variables !"
    ],
    "common_mistakes": [
        "Oublier les guillemets pour les textes (ex : nom = Alice au lieu de nom = 'Alice')",
        "Mettre un espace dans le nom (ex : mon age = 5 → interdit)",
        "Utiliser un nom réservé (ex : print = 3 → interdit)",
        "Confondre = (affectation) et == (comparaison)"
    ]
}
