lesson = {
    "title": "Boucles (for, while)",
    "description": (
        "### Qu'est-ce qu'une boucle ?\n"
        "Une boucle permet de répéter une ou plusieurs instructions plusieurs fois, automatiquement.\n"
        "C'est comme dire à l'ordinateur : 'Fais ceci 5 fois !' ou 'Répète tant que ce n'est pas fini.'\n\n"
        "### Les deux types de boucles en Python\n"
        "- for : pour répéter un nombre précis de fois ou parcourir une liste\n"
        "- while : pour répéter tant qu'une condition est vraie\n\n"
        "### La boucle for\n"
        "On l'utilise souvent avec range() pour répéter un certain nombre de fois.\n\n"
        "Exemple :\n"
        "for i in range(3):\n    print('Bonjour !')\n# Affiche 3 fois 'Bonjour !'\n\n"
        "### La boucle while\n"
        "On l'utilise quand on ne sait pas à l'avance combien de fois il faudra répéter.\n\n"
        "Exemple :\n"
        "compteur = 0\nwhile compteur < 3:\n    print(compteur)\n    compteur += 1\n# Affiche 0, 1, 2\n\n"
        "### Astuces\n"
        "- N'oublie pas d'augmenter le compteur dans une boucle while, sinon la boucle ne s'arrête jamais !\n- On peut utiliser break pour arrêter une boucle, et continue pour passer à l'itération suivante.\n\n"
        "### Erreurs fréquentes\n"
        "- Oublier d'indenter le bloc à répéter\n- Oublier de modifier la condition dans while (boucle infinie)\n- Utiliser range sans le convertir en liste pour l'afficher (en Python 3, range ne donne pas directement une liste)\n"
    ),
    "examples": [
        {
            "code": "# Boucle for\nfor i in range(3):\n    print(i)\n# Affiche 0, 1, 2",
            "explanation": "La boucle for répète le bloc pour chaque valeur de i."
        },
        {
            "code": "# Boucle while\ncompteur = 0\nwhile compteur < 3:\n    print(compteur)\n    compteur += 1",
            "explanation": "La boucle while répète tant que la condition est vraie."
        },
        {
            "code": "# Utilisation de break\nfor i in range(10):\n    if i == 3:\n        break\n    print(i)\n# Affiche 0, 1, 2",
            "explanation": "break permet d'arrêter la boucle avant la fin."
        }
    ],
    "tips": [
        "range(5) donne les valeurs 0, 1, 2, 3, 4 (le dernier n'est pas inclus)",
        "On peut imbriquer des boucles (une boucle dans une boucle)"
    ],
    "common_mistakes": [
        "Oublier d'indenter le bloc à répéter",
        "Oublier de modifier la variable dans while (boucle infinie)",
        "Utiliser = au lieu de == dans la condition"
    ]
}
