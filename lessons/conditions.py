lesson = {
    "title": "Conditions (if, else, elif)",
    "description": (
        "### Qu'est-ce qu'une condition ?\n"
        "Une condition, c'est une question que tu poses à l'ordinateur : 'Est-ce que ceci est vrai ?'\n"
        "Si la réponse est oui (True), alors on exécute un bloc de code. Sinon, on peut faire autre chose.\n\n"
        "### Les mots-clés if, else, elif\n"
        "- if : si la condition est vraie, on exécute le bloc\n"
        "- else : sinon, on exécute ce bloc\n"
        "- elif : sinon si (pour tester plusieurs cas)\n\n"
        "### Exemples\n"
        "# Exemple simple\nage = 18\nif age >= 18:\n    print('Majeur')\nelse:\n    print('Mineur')\n\n# Plusieurs cas\nnote = 15\nif note >= 16:\n    print('Très bien')\nelif note >= 10:\n    print('Moyen')\nelse:\n    print('Insuffisant')\n\n"
        "### Les opérateurs de comparaison\n"
        "- == : égal à\n- != : différent de\n- >  : strictement supérieur\n- <  : strictement inférieur\n- >= : supérieur ou égal\n- <= : inférieur ou égal\n\n"
        "### Astuces\n"
        "- Les blocs à exécuter après if, elif, else doivent être indentés (décalés vers la droite)\n- On peut combiner plusieurs conditions avec and (et), or (ou), not (non)\n- Les conditions fonctionnent aussi avec des booléens\n\n"
        "### Erreurs fréquentes\n"
        "- Oublier les deux-points (:) après if, elif, else\n- Ne pas indenter le bloc de code\n- Utiliser = au lieu de == pour comparer\n"
    ),
    "examples": [
        {
            "code": "# if/else\nage = 20\nif age >= 18:\n    print('Majeur')\nelse:\n    print('Mineur')",
            "explanation": "Utilisation de if/else pour choisir entre deux cas."
        },
        {
            "code": "# if/elif/else\nnote = 12\nif note >= 16:\n    print('Très bien')\nelif note >= 10:\n    print('Moyen')\nelse:\n    print('Insuffisant')",
            "explanation": "Utilisation de elif pour tester plusieurs cas."
        },
        {
            "code": "# Comparaison\nx = 5\nif x != 0:\n    print('x n\'est pas nul')",
            "explanation": "Utilisation de l'opérateur != pour tester la différence."
        }
    ],
    "tips": [
        "N'oublie jamais les deux-points (:) après if, elif, else.",
        "L'indentation (décalage à droite) est obligatoire en Python pour les blocs."
    ],
    "common_mistakes": [
        "Utiliser = au lieu de == pour comparer",
        "Oublier d'indenter le bloc de code après if/else",
        "Oublier les deux-points (:)"
    ]
}
