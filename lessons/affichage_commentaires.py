lesson = {
    "title": "Affichage et commentaires",
    "description": (
        "### Qu'est-ce qu'afficher en Python ?\n"
        "Afficher, c'est demander à l'ordinateur de montrer quelque chose à l'écran. En Python, on utilise la fonction print pour cela.\n\n"
        "### Comment afficher un texte ou une valeur ?\n"
        "On écrit print, puis entre parenthèses ce qu'on veut afficher.\n\n"
        "Exemples :\n"
        "print('Bonjour !')\nprint(42)\nnom = 'Alice'\nprint(nom)\n\n"
        "### Afficher plusieurs choses à la fois\n"
        "On peut séparer les éléments par une virgule dans print.\n\n"
        "Exemple :\n"
        "age = 10\nprint('Âge :', age)\n\n"
        "### Les commentaires\n"
        "Un commentaire, c'est une note pour toi ou pour d'autres humains. Python l'ignore complètement.\n\n"
        "Pour écrire un commentaire, commence la ligne par le symbole #.\n\n"
        "Exemple :\n"
        "# Ceci est un commentaire\nprint('Hello')  # Ceci affiche Hello\n\n"
        "### Pourquoi utiliser des commentaires ?\n"
        "- Pour expliquer ce que fait ton code\n"
        "- Pour te souvenir de pourquoi tu as écrit une ligne\n"
        "- Pour rendre ton code plus facile à comprendre\n\n"
        "### Astuces\n"
        "- Les commentaires ne sont jamais exécutés par Python\n"
        "- Utilise-les pour clarifier, pas pour tout répéter\n"
        "- Un bon commentaire explique le 'pourquoi', pas le 'comment'\n\n"
        "### Erreurs fréquentes\n"
        "- Oublier les parenthèses dans print (Python 3)\n"
        "- Oublier les guillemets autour d'un texte\n"
        "- Mettre un # dans une chaîne de caractères (il sera pris comme du texte, pas comme un commentaire)\n"
    ),
    "examples": [
        {
            "code": "# Afficher un texte\nprint('Bienvenue !')\n\n# Afficher une variable\nnom = 'Alice'\nprint(nom)\n\n# Afficher plusieurs choses\nage = 12\nprint('Âge :', age)",
            "explanation": "Utilisation de print pour afficher du texte, une variable, et plusieurs éléments."
        },
        {
            "code": "# Un commentaire seul\n# Ceci est une note pour moi\n\n# Un commentaire à la fin d'une ligne\nprint('Hello')  # Ceci affiche Hello",
            "explanation": "Différentes façons d'utiliser les commentaires en Python."
        }
    ],
    "tips": [
        "Les commentaires rendent ton code plus lisible pour toi et les autres.",
        "Tu peux afficher le résultat d'un calcul directement : print(2 + 3) affiche 5."
    ],
    "common_mistakes": [
        "Oublier les parenthèses dans print (Python 3)",
        "Oublier les guillemets autour d'un texte",
        "Mettre un # dans une chaîne de caractères (il sera pris comme du texte, pas comme un commentaire)"
    ]
}
