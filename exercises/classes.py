exercises = [
    {
        "id": "class_intro",
        "title": "📘 Introduction aux classes",
        "instruction": "Une classe permet de regrouper des données et des fonctions. Exemple :\n\nclass Chien:\n    def aboyer(self):\n        print('Wouf')\n\nrex = Chien()\nrex.aboyer()",
        "initial_code": "class Chien:\n    def aboyer(self):\n        print('Wouf')\n\nrex = Chien()\nrex.aboyer()",
        "expected_output": "Wouf",
        "level": 0,
        "theme": "classes",
        "hint": "Lis bien l'exemple et observe la structure d'une classe et d'une méthode.",
        "solution_code": "class Chien:\n    def aboyer(self):\n        print('Wouf')\n\nrex = Chien()\nrex.aboyer()"
    },
    {
        "id": "class_basic",
        "title": "Créer une classe simple",
        "instruction": "Crée une classe `Animal` vide (avec pass), puis crée une instance.",
        "initial_code": "# Classe Animal ici",
        "expected_output": "",
        "level": 1,
        "theme": "classes",
        "hint": "Utilise le mot-clé class et le mot-clé pass pour une classe vide.",
        "solution_code": "class Animal:\n    pass\n\na = Animal()"
    },
    {
        "id": "class_attribute",
        "title": "📘 Attributs d'instance",
        "instruction": "On initialise les attributs avec `__init__`. Exemple :\n\nclass Person:\n    def __init__(self, name):\n        self.name = name",
        "initial_code": "class Person:\n    def __init__(self, name):\n        self.name = name\n\np = Person('Nico')\nprint(p.name)",
        "expected_output": "Nico",
        "level": 2,
        "theme": "classes",
        "hint": "Lis bien l'exemple et observe l'utilisation de __init__ pour les attributs.",
        "solution_code": "class Person:\n    def __init__(self, name):\n        self.name = name\n\np = Person('Nico')\nprint(p.name)"
    },
    {
        "id": "class_init_create",
        "title": "Initialiser une classe avec attribut",
        "instruction": "Crée une classe `Chien` avec un attribut `nom`, passé au moment de la création. Affiche le nom.",
        "initial_code": "# Classe avec __init__",
        "expected_output": "Rex",
        "level": 2,
        "theme": "classes",
        "hint": "Ajoute un __init__ qui prend nom en paramètre et l'affecte à self.nom.",
        "solution_code": "class Chien:\n    def __init__(self, nom):\n        self.nom = nom\n\nrex = Chien('Rex')\nprint(rex.nom)"
    },
    {
        "id": "class_method",
        "title": "📘 Ajouter une méthode",
        "instruction": "Une méthode est une fonction définie dans une classe. Exemple :\n\nclass Person:\n    def saluer(self):\n        print('Salut')",
        "initial_code": "class Person:\n    def saluer(self):\n        print('Salut')\n\np = Person()\np.saluer()",
        "expected_output": "Salut",
        "level": 2,
        "theme": "classes",
        "hint": "Lis bien l'exemple et observe la définition d'une méthode.",
        "solution_code": "class Person:\n    def saluer(self):\n        print('Salut')\n\np = Person()\np.saluer()"
    },
    {
        "id": "class_method_use",
        "title": "Définir une méthode",
        "instruction": "Crée une classe `Chat` avec une méthode `miauler()` qui affiche 'Miaou !'.",
        "initial_code": "# Classe Chat",
        "expected_output": "Miaou !",
        "level": 3,
        "theme": "classes",
        "hint": "Définis une méthode dans la classe et appelle-la sur une instance.",
        "solution_code": "class Chat:\n    def miauler(self):\n        print('Miaou !')\n\nc = Chat()\nc.miauler()"
    },
    {
        "id": "class_method_return",
        "title": "Méthode avec return",
        "instruction": "Ajoute une méthode `double_age()` qui retourne deux fois l'âge du chien.",
        "initial_code": "# Méthode return",
        "expected_output": "10",
        "level": 3,
        "theme": "classes",
        "hint": "La méthode doit retourner self.age * 2.",
        "solution_code": "class Chien:\n    def __init__(self, age):\n        self.age = age\n    def double_age(self):\n        return self.age * 2\n\nrex = Chien(5)\nprint(rex.double_age())"
    },
    {
        "id": "class_str_method",
        "title": "🔁 Bonus : méthode __str__",
        "instruction": "Ajoute une méthode `__str__()` pour qu'un objet `Livre` affiche 'Titre: Python 101'.",
        "initial_code": "# __str__ ici",
        "expected_output": "Titre: Python 101",
        "level": 4,
        "theme": "classes",
        "hint": "Définis __str__ pour retourner la chaîne voulue.",
        "solution_code": "class Livre:\n    def __str__(self):\n        return 'Titre: Python 101'\n\nl = Livre()\nprint(l)"
    },
    {
        "id": "class_inheritance",
        "title": "📘 Héritage",
        "instruction": "Une classe peut hériter d'une autre :\n\nclass VoitureElectrique(Voiture):\n    pass",
        "initial_code": "class Voiture:\n    def klaxon(self):\n        print('Beep')\n\nclass VoitureElectrique(Voiture):\n    pass\n\nv = VoitureElectrique()\nv.klaxon()",
        "expected_output": "Beep",
        "level": 4,
        "theme": "classes",
        "hint": "Lis bien l'exemple et observe la syntaxe de l'héritage.",
        "solution_code": "class Voiture:\n    def klaxon(self):\n        print('Beep')\n\nclass VoitureElectrique(Voiture):\n    pass\n\nv = VoitureElectrique()\nv.klaxon()"
    },
    {
        "id": "class_inheritance_add",
        "title": "🔁 Bonus : Héritage + nouvelle méthode",
        "instruction": "Fais hériter `ChatRobot` de `Chat`, et ajoute une méthode `bip()` qui affiche 'Bip bip'.",
        "initial_code": "# Inhérence + méthode",
        "expected_output": "Bip bip",
        "level": 5,
        "theme": "classes",
        "hint": "Définis ChatRobot(Chat) et ajoute la méthode bip().",
        "solution_code": "class Chat:\n    pass\n\nclass ChatRobot(Chat):\n    def bip(self):\n        print('Bip bip')\n\ncr = ChatRobot()\ncr.bip()"
    }
]
