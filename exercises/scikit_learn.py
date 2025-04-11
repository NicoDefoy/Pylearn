exercises = [
    {
        "id": "sklearn_intro",
        "title": "📘 Introduction à scikit-learn",
        "instruction": "Scikit-learn est une bibliothèque pour le machine learning. On l’importe avec :\n\nfrom sklearn.linear_model import LinearRegression",
        "initial_code": "from sklearn.linear_model import LinearRegression\nprint('sklearn prêt !')",
        "expected_output": "sklearn prêt !",
        "level": 0,
        "theme": "scikit_learn"
    },
    {
        "id": "sklearn_model_create",
        "title": "Créer un modèle",
        "instruction": "Crée une instance de LinearRegression.",
        "initial_code": "# Crée un modèle",
        "expected_output": "",
        "level": 1,
        "theme": "scikit_learn"
    },
    {
        "id": "sklearn_fit_model",
        "title": "📘 Entraîner un modèle",
        "instruction": "On entraîne un modèle avec .fit(X, y). X = données d’entrée, y = cibles.\n\nmodel.fit(X, y)",
        "initial_code": "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nX = [[1], [2], [3]]\ny = [2, 4, 6]\nmodel.fit(X, y)",
        "expected_output": "",
        "level": 2,
        "theme": "scikit_learn"
    },
    {
        "id": "sklearn_predict",
        "title": "Prédiction simple",
        "instruction": "Prédit la valeur de y quand X = 4, en utilisant un modèle déjà entraîné.",
        "initial_code": "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit([[1], [2], [3]], [2, 4, 6])\nprint(model.predict([[4]]))",
        "expected_output": "[8.]",
        "level": 2,
        "theme": "scikit_learn"
    },
    {
        "id": "sklearn_accuracy",
        "title": "🔁 Bonus : Précision d’un modèle",
        "instruction": "Utilise .score(X, y) pour afficher la précision du modèle.",
        "initial_code": "from sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nX = [[1], [2], [3]]\ny = [2, 4, 6]\nmodel.fit(X, y)\nprint(model.score(X, y))",
        "expected_output": "1.0",
        "level": 3,
        "theme": "scikit_learn"
    },
    {
        "id": "sklearn_dataset",
        "title": "📘 Charger un dataset",
        "instruction": "Scikit-learn propose des jeux de données. Exemple :\n\nfrom sklearn.datasets import load_iris\ndata = load_iris()",
        "initial_code": "from sklearn.datasets import load_iris\ndata = load_iris()\nprint(data.feature_names)",
        "expected_output": "['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']",
        "level": 3,
        "theme": "scikit_learn"
    },
    {
        "id": "sklearn_split",
        "title": "🔁 Bonus : Diviser les données",
        "instruction": "Utilise train_test_split pour séparer données d'entraînement/test.",
        "initial_code": "from sklearn.model_selection import train_test_split\nX = [[1], [2], [3], [4]]\ny = [2, 4, 6, 8]\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)\nprint(len(X_train))",
        "expected_output": "2",
        "level": 4,
        "theme": "scikit_learn"
    }
]
