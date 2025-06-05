# Numpy : Tableaux et calculs scientifiques

Numpy est la bibliothèque de référence pour manipuler des tableaux de nombres et faire des calculs scientifiques en Python.

## Exemple de base
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

somme = a + b  # [5 7 9]
produit = a * b  # [4 10 18]
```

- `np.array` crée un tableau.
- Les opérations sont vectorisées (plus rapides qu’avec des listes classiques).
