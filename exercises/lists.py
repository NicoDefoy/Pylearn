exercises = [
    {
        "id": "lists_intro",
        "title": "📘 Introduction aux listes",
        "instruction": "Une liste permet de stocker plusieurs valeurs. Exemple :\n\nfruits = ['pomme', 'banane']\nprint(fruits)",
        "initial_code": "fruits = ['pomme', 'banane']\nprint(fruits)",
        "expected_output": "['pomme', 'banane']",
        "level": 0,
        "theme": "lists",
        "hint": "Lis bien l'exemple et observe la syntaxe d'une liste.",
        "solution_code": "fruits = ['pomme', 'banane']\nprint(fruits)"
    },
    {
        "id": "lists_create",
        "title": "Créer une liste",
        "instruction": "Crée une liste appelée fruits avec les éléments 'pomme', 'banane', 'orange'. Affiche-la.",
        "initial_code": "# Écris ton code ici",
        "expected_output": "['pomme', 'banane', 'orange']",
        "level": 1,
        "theme": "lists",
        "hint": "Utilise des crochets pour créer la liste et print() pour l'afficher.",
        "solution_code": "fruits = ['pomme', 'banane', 'orange']\nprint(fruits)"
    },
    {
        "id": "lists_access",
        "title": "Accéder à un élément",
        "instruction": "Crée une liste avec 3 éléments de ton choix. Affiche le deuxième élément (indice 1).",
        "initial_code": "# Ta liste ici",
        "expected_output": "banane",
        "level": 1,
        "theme": "lists",
        "hint": "Utilise l'index 1 pour accéder au deuxième élément.",
        "solution_code": "liste = ['pomme', 'banane', 'orange']\nprint(liste[1])"
    },
    {
        "id": "lists_modify",
        "title": "Modifier un élément",
        "instruction": "Crée une liste [1, 2, 3] puis modifie le premier élément pour qu'il vaille 10. Affiche la liste.",
        "initial_code": "# Modifie la liste",
        "expected_output": "[10, 2, 3]",
        "level": 1,
        "theme": "lists",
        "hint": "Affecte 10 à l'index 0 de la liste.",
        "solution_code": "liste = [1, 2, 3]\nliste[0] = 10\nprint(liste)"
    },
    {
        "id": "lists_append",
        "title": "Ajouter un élément",
        "instruction": "Crée une liste vide, ajoute-lui l'élément 42 avec append() puis affiche-la.",
        "initial_code": "# Ajoute un élément",
        "expected_output": "[42]",
        "level": 1,
        "theme": "lists",
        "hint": "Utilise la méthode append() sur une liste vide.",
        "solution_code": "liste = []\nliste.append(42)\nprint(liste)"
    },
    {
        "id": "lists_length",
        "title": "Longueur d'une liste",
        "instruction": "Crée une liste avec 4 éléments. Affiche sa longueur avec len().",
        "initial_code": "# Combien d'éléments ?",
        "expected_output": "4",
        "level": 2,
        "theme": "lists",
        "hint": "Utilise len() sur la liste.",
        "solution_code": "liste = [1, 2, 3, 4]\nprint(len(liste))"
    },
    {
        "id": "lists_remove",
        "title": "Supprimer un élément",
        "instruction": "Crée une liste [10, 20, 30] et retire l'élément 20 avec remove(). Affiche la liste.",
        "initial_code": "# Supprime un élément",
        "expected_output": "[10, 30]",
        "level": 2,
        "theme": "lists",
        "hint": "Utilise la méthode remove() pour supprimer 20.",
        "solution_code": "liste = [10, 20, 30]\nliste.remove(20)\nprint(liste)"
    },
    {
        "id": "lists_pop",
        "title": "Retirer avec pop()",
        "instruction": "Crée une liste [5, 6, 7] et utilise pop() pour retirer le dernier élément. Affiche la liste.",
        "initial_code": "# Retire le dernier",
        "expected_output": "[5, 6]",
        "level": 2,
        "theme": "lists",
        "hint": "Utilise la méthode pop() sans argument pour retirer le dernier.",
        "solution_code": "liste = [5, 6, 7]\nliste.pop()\nprint(liste)"
    },
    {
        "id": "lists_loop",
        "title": "📘 Boucle sur une liste",
        "instruction": "On peut parcourir une liste avec une boucle for :\n\nfruits = ['pomme', 'banane']\nfor fruit in fruits:\n    print(fruit)",
        "initial_code": "fruits = ['pomme', 'banane']\nfor fruit in fruits:\n    print(fruit)",
        "expected_output": "pomme\nbanane",
        "level": 2,
        "theme": "lists",
        "hint": "Lis bien l'exemple et observe la syntaxe de la boucle sur une liste.",
        "solution_code": "fruits = ['pomme', 'banane']\nfor fruit in fruits:\n    print(fruit)"
    },
    {
        "id": "lists_sum",
        "title": "Somme des éléments",
        "instruction": "Crée une liste de nombres et affiche la somme des éléments avec sum().",
        "initial_code": "# Fais la somme",
        "expected_output": "15",
        "level": 3,
        "theme": "lists",
        "hint": "Utilise sum() sur la liste.",
        "solution_code": "liste = [1, 2, 3, 4, 5]\nprint(sum(liste))"
    },
    {
        "id": "lists_max",
        "title": "Trouver le plus grand",
        "instruction": "Crée une liste [4, 8, 2] et affiche le plus grand élément avec max().",
        "initial_code": "# Trouve le max",
        "expected_output": "8",
        "level": 3,
        "theme": "lists",
        "hint": "Utilise max() sur la liste.",
        "solution_code": "liste = [4, 8, 2]\nprint(max(liste))"
    },
    {
        "id": "lists_sort",
        "title": "Trier une liste",
        "instruction": "Crée une liste [3, 1, 2] et trie-la avec sort(). Affiche-la ensuite.",
        "initial_code": "# Trie-moi ça",
        "expected_output": "[1, 2, 3]",
        "level": 3,
        "theme": "lists",
        "hint": "Utilise la méthode sort() puis print().",
        "solution_code": "liste = [3, 1, 2]\nliste.sort()\nprint(liste)"
    },
    {
        "id": "lists_bonus_reverse",
        "title": "🔁 Bonus : Inverser une liste",
        "instruction": "Crée une liste [1, 2, 3, 4] puis inverse-la avec reverse(). Affiche-la.",
        "initial_code": "# Inverse la liste",
        "expected_output": "[4, 3, 2, 1]",
        "level": 4,
        "theme": "lists",
        "hint": "Utilise la méthode reverse() sur la liste.",
        "solution_code": "liste = [1, 2, 3, 4]\nliste.reverse()\nprint(liste)"
    },
    {
        "id": "lists_bonus_comprehension",
        "title": "🔁 Bonus : Compréhension de liste",
        "instruction": "Utilise une compréhension de liste pour créer une liste des carrés de 0 à 4. Affiche-la.",
        "initial_code": "# Carrés puissants",
        "expected_output": "[0, 1, 4, 9, 16]",
        "level": 5,
        "theme": "lists",
        "hint": "Utilise [x**2 for x in range(5)] pour générer la liste.",
        "solution_code": "carres = [x**2 for x in range(5)]\nprint(carres)"
    }
]
