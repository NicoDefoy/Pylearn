exercises = [
    {
        "id": "func_intro",
        "title": "📘 Introduction aux fonctions",
        "instruction": "Une fonction est un bloc de code réutilisable. On la crée avec 'def nom():', puis on l'appelle avec 'nom()'.",
        "initial_code": "def hello():\n    print('Hello!')\n\nhello()",
        "expected_output": "Hello!",
        "level": 0,
        "theme": "functions"
    },
    {
        "id": "func_1",
        "title": "Définir une fonction bonjour",
        "instruction": "Définis une fonction bonjour() qui affiche 'Salut !'. Appelle-la ensuite.",
        "initial_code": "# Écris ton code ici",
        "expected_output": "Salut !",
        "level": 1,
        "theme": "functions"
    },
    {
        "id": "func_2",
        "title": "Encore une fonction simple",
        "instruction": "Crée une fonction coucou() qui affiche 'Hey !'. Appelle-la ensuite.",
        "initial_code": "# Écris ton code ici",
        "expected_output": "Hey !",
        "level": 1,
        "theme": "functions"
    },
    {
        "id": "func_3",
        "title": "Afficher une autre phrase",
        "instruction": "Crée une fonction test() qui affiche 'Je progresse !'. Appelle-la ensuite.",
        "initial_code": "# Tape ta solution ici",
        "expected_output": "Je progresse !",
        "level": 1,
        "theme": "functions"
    },
    {
        "id": "func_param_example",
        "title": "📘 Exemple : Fonction avec paramètre",
        "instruction": "Voici une fonction qui prend un paramètre :\n\ndef dire_bonjour(nom):\n    print('Salut', nom)\n\ndire_bonjour('Emma')",
        "initial_code": "def dire_bonjour(nom):\n    print('Salut', nom)\n\ndire_bonjour('Emma')",
        "expected_output": "Salut Emma",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_4",
        "title": "Fonction avec un paramètre",
        "instruction": "Crée une fonction hello(nom) qui affiche 'Hello' suivi du nom donné. Appelle-la avec ton prénom.",
        "initial_code": "# Écris la fonction ici",
        "expected_output": "Hello Nico",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_5",
        "title": "Message personnalisé",
        "instruction": "Crée une fonction bienvenue(prenom) qui affiche 'Bienvenue ' + prenom. Appelle-la avec Paul.",
        "initial_code": "# À toi de jouer !",
        "expected_output": "Bienvenue Paul",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_6",
        "title": "Utiliser un paramètre dans une phrase",
        "instruction": "Crée une fonction presentation(prenom) qui affiche 'Je m'appelle prénom'. Appelle-la avec Alex.",
        "initial_code": "# Présente-toi",
        "expected_output": "Je m'appelle Alex",
        "level": 2,
        "theme": "functions"
    },
    {
        "id": "func_return_example",
        "title": "📘 Exemple : Fonction avec return",
        "instruction": "Voici une fonction qui retourne une valeur :\n\ndef carre(x):\n    return x * x\n\nprint(carre(3))",
        "initial_code": "def carre(x):\n    return x * x\n\nprint(carre(3))",
        "expected_output": "9",
        "level": 3,
        "theme": "functions"
    },
    {
        "id": "func_7",
        "title": "Fonction qui retourne un double",
        "instruction": "Crée une fonction double(x) qui retourne x*2. Affiche le résultat de double(5).",
        "initial_code": "# Fonction double",
        "expected_output": "10",
        "level": 3,
        "theme": "functions"
    },
    {
        "id": "func_8",
        "title": "Addition de deux nombres",
        "instruction": "Crée une fonction addition(a, b) qui retourne leur somme. Appelle-la avec 2 et 4.",
        "initial_code": "# Addition",
        "expected_output": "6",
        "level": 3,
        "theme": "functions"
    },
    {
        "id": "func_9",
        "title": "Retourner une phrase",
        "instruction": "Crée une fonction salutation(nom) qui retourne 'Bonjour nom !'. Affiche salutation('Lucas').",
        "initial_code": "# Teste avec un nom",
        "expected_output": "Bonjour Lucas !",
        "level": 3,
        "theme": "functions"
    },
    {
        "id": "func_default_example",
        "title": "📘 Exemple : Paramètre avec valeur par défaut",
        "instruction": "On peut donner une valeur par défaut à un paramètre. Cela permet d'appeler la fonction sans toujours fournir l'argument.\n\ndef hello(nom='ami'):\n    print('Salut', nom)\n\nhello()\nhello('Bob')",
        "initial_code": "def hello(nom='ami'):\n    print('Salut', nom)\n\nhello()\nhello('Bob')",
        "expected_output": "Salut ami\nSalut Bob",
        "level": 4,
        "theme": "functions"
    },
    {
        "id": "func_10",
        "title": "Utiliser un paramètre par défaut",
        "instruction": "Crée une fonction salut(nom='toi') qui affiche 'Salut nom'. Appelle-la sans argument puis avec 'Léo'.",
        "initial_code": "# À toi !",
        "expected_output": "Salut toi\nSalut Léo",
        "level": 4,
        "theme": "functions"
    },
    {
        "id": "func_multi_return_example",
        "title": "📘 Exemple : Retourner plusieurs valeurs",
        "instruction": "Une fonction peut retourner plusieurs valeurs avec return, séparées par des virgules.\n\ndef stats(a, b):\n    return a + b, a * b\n\nsomme, produit = stats(3, 4)\nprint(somme, produit)",
        "initial_code": "def stats(a, b):\n    return a + b, a * b\n\nsomme, produit = stats(3, 4)\nprint(somme, produit)",
        "expected_output": "7 12",
        "level": 4,
        "theme": "functions"
    },
    {
        "id": "func_11",
        "title": "Retourner deux résultats",
        "instruction": "Crée une fonction info(nombre) qui retourne (nombre + 1, nombre - 1). Affiche les deux résultats pour 5.",
        "initial_code": "# Let's go",
        "expected_output": "6 4",
        "level": 4,
        "theme": "functions"
    },
    {
        "id": "func_list_param_example",
        "title": "📘 Exemple : Paramètre de type liste",
        "instruction": "On peut passer une liste en paramètre. Exemple :\n\ndef moyenne(notes):\n    return sum(notes) / len(notes)\n\nprint(moyenne([10, 12, 14]))",
        "initial_code": "def moyenne(notes):\n    return sum(notes) / len(notes)\n\nprint(moyenne([10, 12, 14]))",
        "expected_output": "12.0",
        "level": 4,
        "theme": "functions"
    },
    {
        "id": "func_12",
        "title": "Calculer une moyenne",
        "instruction": "Crée une fonction moyenne(liste) qui retourne la moyenne des valeurs. Teste-la sur [10, 12, 14].",
        "initial_code": "# Moyenne d'une liste",
        "expected_output": "12.0",
        "level": 4,
        "theme": "functions"
    },
    {
        "id": "func_recursive_example",
        "title": "📘 Exemple : Fonction récursive",
        "instruction": "Une fonction récursive s'appelle elle-même. Exemple :\n\ndef fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(4))",
        "initial_code": "def fact(n):\n    if n <= 1:\n        return 1\n    return n * fact(n - 1)\n\nprint(fact(4))",
        "expected_output": "24",
        "level": 5,
        "theme": "functions"
    },
    {
        "id": "func_13",
        "title": "Créer une fonction factorielle récursive",
        "instruction": "Crée une fonction factorielle(n) qui retourne la factorielle de n. Teste-la avec n = 4.",
        "initial_code": "# Fonction récursive",
        "expected_output": "24",
        "level": 5,
        "theme": "functions"
    }
]
