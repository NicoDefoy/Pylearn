lesson = {
    "title": "Opérations de base",
    "description": (
        "### Qu'est-ce qu'une opération en Python ?\n"
        "Une opération, c'est demander à l'ordinateur de faire un calcul ou de manipuler des valeurs.\n\n"
        "### Les opérateurs arithmétiques\n"
        "Ce sont les symboles qui permettent de faire des calculs : +, -, *, /, //, %, **\n\n"
        "- + : addition (ex : 2 + 3 donne 5)\n"
        "- - : soustraction (ex : 5 - 2 donne 3)\n"
        "- * : multiplication (ex : 4 * 2 donne 8)\n"
        "- / : division (ex : 10 / 2 donne 5.0)\n"
        "- // : division entière (ex : 7 // 2 donne 3)\n"
        "- % : reste de la division (modulo) (ex : 7 % 2 donne 1)\n"
        "- ** : puissance (ex : 2 ** 3 donne 8)\n\n"
        "### Exemples\n"
        "# Addition\na = 2 + 3  # a vaut 5\n\n# Multiplication\nb = 4 * 2  # b vaut 8\n\n# Division\nc = 10 / 2  # c vaut 5.0\n\n# Division entière\nd = 7 // 2  # d vaut 3\n\n# Modulo\ne = 7 % 2  # e vaut 1\n\n# Puissance\nf = 2 ** 3  # f vaut 8\n\n"
        "### Concaténer des textes (chaînes de caractères)\n"
        "On peut coller deux textes ensemble avec +\n\n"
        "Exemple :\n"
        "prenom = 'Alice'\nnom = 'Dupont'\nnom_complet = prenom + ' ' + nom  # nom_complet vaut 'Alice Dupont'\n\n"
        "### Astuces\n"
        "- Tu peux utiliser les opérations directement dans print : print(2 + 3)\n- Attention à ne pas mélanger nombres et textes dans une addition\n- Pour répéter un texte, tu peux faire : print('ha' * 3)  # affiche 'hahaha'\n\n"
        "### Erreurs fréquentes\n"
        "- Oublier les espaces autour des opérateurs (ce n'est pas une erreur pour Python, mais c'est moins lisible)\n- Essayer d'additionner un nombre et un texte (ex : 2 + '3')\n- Oublier les parenthèses pour la puissance (ex : 2 ** 3 et pas 2 * * 3)\n"
    ),
    "examples": [
        {
            "code": "# Addition\na = 5 + 2\nprint(a)  # 7\n\n# Modulo\nb = 10 % 3\nprint(b)  # 1",
            "explanation": "Utilisation des opérateurs + et % pour faire des calculs."
        },
        {
            "code": "# Concaténation de textes\nprenom = 'Alice'\nnom = 'Dupont'\nnom_complet = prenom + ' ' + nom\nprint(nom_complet)  # Alice Dupont",
            "explanation": "Coller deux chaînes de caractères avec +."
        },
        {
            "code": "# Répéter un texte\nprint('ha' * 3)  # affiche 'hahaha'",
            "explanation": "On peut multiplier un texte par un nombre pour le répéter."
        }
    ],
    "tips": [
        "Les opérations peuvent être utilisées directement dans print pour voir le résultat.",
        "Pour concaténer un nombre et un texte, il faut convertir le nombre en texte avec str() : print('J'ai', str(3), 'ans')"
    ],
    "common_mistakes": [
        "Essayer d'additionner un nombre et un texte (ex : 2 + '3')",
        "Oublier les parenthèses pour la puissance (ex : 2 ** 3 et pas 2 * * 3)"
    ]
}
