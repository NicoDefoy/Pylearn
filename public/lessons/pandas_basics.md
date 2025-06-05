# Pandas : Premiers pas

Pandas permet de manipuler facilement des tableaux de données (DataFrame).

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
