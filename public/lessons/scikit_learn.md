# Scikit-learn : Machine Learning

Scikit-learn est la bibliothèque de référence pour le machine learning en Python.

## Exemple de base : régression linéaire
```python
from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[5]])  # [10.]
```

- `fit` entraîne le modèle
- `predict` fait une prédiction
