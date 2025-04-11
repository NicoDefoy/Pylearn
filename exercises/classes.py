exercises = [
    {
        "id": "class_intro",
        "title": "📘 Introduction aux classes",
        "instruction": "Une classe est un modèle pour créer des objets. On utilise le mot-clé `class`.\n\nclass Person:\n    pass",
        "initial_code": "class Person:\n    pass",
        "expected_output": "",
        "level": 0,
        "theme": "classes"
    },
    {
        "id": "class_basic",
        "title": "Créer une classe simple",
        "instruction": "Crée une classe `Animal` vide (avec pass), puis crée une instance.",
        "initial_code": "# Classe Animal ici",
        "expected_output": "",
        "level": 1,
        "theme": "classes"
    },
    {
        "id": "class_attribute",
        "title": "📘 Attributs d'instance",
        "instruction": "On initialise les attributs avec `__init__`. Exemple :\n\nclass Person:\n    def __init__(self, name):\n        self.name = name",
        "initial_code": "class Person:\n    def __init__(self, name):\n        self.name = name\n\np = Person('Nico')\nprint(p.name)",
        "expected_output": "Nico",
        "level": 2,
        "theme": "classes"
    },
    {
        "id": "class_init_create",
        "title": "Initialiser une classe avec attribut",
        "instruction": "Crée une classe `Chien` avec un attribut `nom`, passé au moment de la création. Affiche le nom.",
        "initial_code": "# Classe avec __init__",
        "expected_output": "Rex",
        "level": 2,
        "theme": "classes"
    },
    {
        "id": "class_method",
        "title": "📘 Ajouter une méthode",
        "instruction": "Une méthode est une fonction définie dans une classe. Exemple :\n\nclass Person:\n    def saluer(self):\n        print('Salut')",
        "initial_code": "class Person:\n    def saluer(self):\n        print('Salut')\n\np = Person()\np.saluer()",
        "expected_output": "Salut",
        "level": 2,
        "theme": "classes"
    },
    {
        "id": "class_method_use",
        "title": "Définir une méthode",
        "instruction": "Crée une classe `Chat` avec une méthode `miauler()` qui affiche 'Miaou !'.",
        "initial_code": "# Classe Chat",
        "expected_output": "Miaou !",
        "level": 3,
        "theme": "classes"
    },
    {
        "id": "class_method_return",
        "title": "Méthode avec return",
        "instruction": "Ajoute une méthode `double_age()` qui retourne deux fois l'âge du chien.",
        "initial_code": "# Méthode return",
        "expected_output": "10",
        "level": 3,
        "theme": "classes"
    },
    {
        "id": "class_str_method",
        "title": "🔁 Bonus : méthode __str__",
        "instruction": "Ajoute une méthode `__str__()` pour qu’un objet `Livre` affiche 'Titre: Python 101'.",
        "initial_code": "# __str__ ici",
        "expected_output": "Titre: Python 101",
        "level": 4,
        "theme": "classes"
    },
    {
        "id": "class_inheritance",
        "title": "📘 Héritage",
        "instruction": "Une classe peut hériter d'une autre :\n\nclass VoitureElectrique(Voiture):\n    pass",
        "initial_code": "class Voiture:\n    def klaxon(self):\n        print('Beep')\n\nclass VoitureElectrique(Voiture):\n    pass\n\nv = VoitureElectrique()\nv.klaxon()",
        "expected_output": "Beep",
        "level": 4,
        "theme": "classes"
    },
    {
        "id": "class_inheritance_add",
        "title": "🔁 Bonus : Héritage + nouvelle méthode",
        "instruction": "Fais hériter `ChatRobot` de `Chat`, et ajoute une méthode `bip()` qui affiche 'Bip bip'.",
        "initial_code": "# Inhérence + méthode",
        "expected_output": "Bip bip",
        "level": 5,
        "theme": "classes"
    }
]
