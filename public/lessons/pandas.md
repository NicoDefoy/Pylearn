# Pandas : Manipulation de données

Pandas permet de manipuler facilement des tableaux de données (DataFrame).

## Exemple de base
```python
import pandas as pd

df = pd.DataFrame({
    'nom': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})

print(df)
#     nom  age
# 0  Alice   25
# 1    Bob   30
# 2 Charlie  35
```

- `pd.DataFrame` crée un tableau de données.
- On peut facilement filtrer, trier, grouper, etc.
