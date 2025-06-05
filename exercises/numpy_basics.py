exercises = [
    {
        "id": "numpy_intro",
        "title": "📘 Introduction à NumPy",
        "instruction": "NumPy permet de manipuler des tableaux numériques performants. On commence par :\n\nimport numpy as np",
        "initial_code": "import numpy as np\nprint('NumPy prêt !')",
        "expected_output": "NumPy prêt !",
        "level": 0,
        "theme": "numpy_basics",
        "hint": "Commence toujours par importer numpy sous le nom np.",
        "solution_code": "import numpy as np\nprint('NumPy prêt !')"
    },
    {
        "id": "numpy_array_create",
        "title": "Créer un tableau",
        "instruction": "Crée un tableau contenant les éléments 1, 2, 3 à l'aide de np.array().",
        "initial_code": "# Crée ton array",
        "expected_output": "[1 2 3]",
        "level": 1,
        "theme": "numpy_basics",
        "hint": "Utilise np.array([1, 2, 3]) pour créer le tableau.",
        "solution_code": "import numpy as np\narr = np.array([1, 2, 3])\nprint(arr)"
    },
    {
        "id": "numpy_array_type",
        "title": "Vérifier le type",
        "instruction": "Crée un tableau NumPy et affiche son type avec type().",
        "initial_code": "import numpy as np\narr = np.array([1, 2])\nprint(type(arr))",
        "expected_output": "<class 'numpy.ndarray'>",
        "level": 1,
        "theme": "numpy_basics",
        "hint": "Utilise type() sur un tableau créé avec np.array().",
        "solution_code": "import numpy as np\narr = np.array([1, 2])\nprint(type(arr))"
    },
    {
        "id": "numpy_access_element",
        "title": "Accéder à un élément",
        "instruction": "Crée un tableau = [10, 20, 30] et affiche le deuxième élément.",
        "initial_code": "# Accès par index",
        "expected_output": "20",
        "level": 1,
        "theme": "numpy_basics",
        "hint": "Utilise l'index 1 pour accéder au deuxième élément.",
        "solution_code": "import numpy as np\narr = np.array([10, 20, 30])\nprint(arr[1])"
    },
    {
        "id": "numpy_operations",
        "title": "📘 Opérations vectorisées",
        "instruction": "NumPy permet d'appliquer des opérations à tous les éléments d'un tableau sans boucle.\n\nexemple : arr + 1",
        "initial_code": "import numpy as np\narr = np.array([1, 2, 3])\nprint(arr + 1)",
        "expected_output": "[2 3 4]",
        "level": 2,
        "theme": "numpy_basics",
        "hint": "Lis bien l'exemple et observe l'opération directe sur le tableau.",
        "solution_code": "import numpy as np\narr = np.array([1, 2, 3])\nprint(arr + 1)"
    },
    {
        "id": "numpy_sum",
        "title": "Somme des éléments",
        "instruction": "Crée un tableau et affiche la somme de ses éléments avec np.sum().",
        "initial_code": "# Somme totale",
        "expected_output": "6",
        "level": 2,
        "theme": "numpy_basics",
        "hint": "Utilise np.sum() sur le tableau.",
        "solution_code": "import numpy as np\narr = np.array([1, 2, 3])\nprint(np.sum(arr))"
    },
    {
        "id": "numpy_shape",
        "title": "Dimensions d'un tableau",
        "instruction": "Crée un tableau 2D [[1,2], [3,4]] et affiche sa forme avec .shape.",
        "initial_code": "# Dimensions du tableau",
        "expected_output": "(2, 2)",
        "level": 3,
        "theme": "numpy_basics",
        "hint": "Utilise arr.shape pour obtenir la forme du tableau.",
        "solution_code": "import numpy as np\narr = np.array([[1, 2], [3, 4]])\nprint(arr.shape)"
    },
    {
        "id": "numpy_reshape",
        "title": "Changer la forme",
        "instruction": "Crée un tableau de 6 éléments et transforme-le en 2 lignes, 3 colonnes.",
        "initial_code": "# reshape ici",
        "expected_output": "[[1 2 3]\n [4 5 6]]",
        "level": 3,
        "theme": "numpy_basics",
        "hint": "Utilise reshape((2, 3)) sur un tableau de 6 éléments.",
        "solution_code": "import numpy as np\narr = np.array([1, 2, 3, 4, 5, 6])\narr2d = arr.reshape((2, 3))\nprint(arr2d)"
    },
    {
        "id": "numpy_boolean_masking",
        "title": "🔁 Bonus : Masquage booléen",
        "instruction": "Affiche les éléments supérieurs à 2 dans [1,2,3,4].",
        "initial_code": "# Filtrage conditionnel",
        "expected_output": "[3 4]",
        "level": 4,
        "theme": "numpy_basics",
        "hint": "Utilise un masque booléen : arr[arr > 2]",
        "solution_code": "import numpy as np\narr = np.array([1, 2, 3, 4])\nprint(arr[arr > 2])"
    },
    {
        "id": "numpy_broadcasting",
        "title": "🔁 Bonus : Broadcasting",
        "instruction": "Multiplie un tableau [[1, 2], [3, 4]] par 10 (sans boucle).",
        "initial_code": "# Broadcasting",
        "expected_output": "[[10 20]\n [30 40]]",
        "level": 5,
        "theme": "numpy_basics",
        "hint": "Multiplie directement le tableau par 10.",
        "solution_code": "import numpy as np\narr = np.array([[1, 2], [3, 4]])\nprint(arr * 10)"
    }
]
