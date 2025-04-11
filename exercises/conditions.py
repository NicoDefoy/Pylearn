exercises = [
  {
    "id": "cond_intro",
    "title": "📘 Introduction aux conditions",
    "instruction": "Une condition permet d’exécuter un bloc de code seulement si une condition est vraie.\nExemple :\n\nx = 5\nif x > 3:\n    print('x est grand')",
    "initial_code": "x = 5\nif x > 3:\n    print('x est grand')",
    "expected_output": "x est grand",
    "level": 0,
    "theme": "conditions"
  },
  {
    "id": "cond_1",
    "title": "Tester une valeur avec if",
    "instruction": "Crée une condition qui affiche 'OK' si x vaut 10.\nx = 10",
    "initial_code": "# Ton code ici",
    "expected_output": "OK",
    "level": 1,
    "theme": "conditions"
  },
  {
    "id": "cond_2",
    "title": "Tester une égalité simple",
    "instruction": "Si y est égal à 3, affiche 'Exact', sinon rien.\ny = 3",
    "initial_code": "# Ton code ici",
    "expected_output": "Exact",
    "level": 1,
    "theme": "conditions"
  },
  {
    "id": "cond_3",
    "title": "Afficher un message si vrai",
    "instruction": "Si age > 18, affiche 'Majeur'.\nage = 20",
    "initial_code": "# Code ici",
    "expected_output": "Majeur",
    "level": 1,
    "theme": "conditions"
  },
  {
    "id": "cond_else_example",
    "title": "📘 Exemple : if / else",
    "instruction": "if permet d’exécuter un bloc si vrai, else s'exécute sinon.\n\nx = 4\nif x > 5:\n    print('Grand')\nelse:\n    print('Petit')",
    "initial_code": "x = 4\nif x > 5:\n    print('Grand')\nelse:\n    print('Petit')",
    "expected_output": "Petit",
    "level": 2,
    "theme": "conditions"
  },
  {
    "id": "cond_4",
    "title": "Afficher Oui ou Non",
    "instruction": "Si x vaut 5, affiche 'Oui', sinon affiche 'Non'.\nx = 5",
    "initial_code": "# Code ici",
    "expected_output": "Oui",
    "level": 2,
    "theme": "conditions"
  },
  {
    "id": "cond_5",
    "title": "Afficher selon âge",
    "instruction": "Si age >= 18, affiche 'Adulte', sinon 'Mineur'.\nage = 16",
    "initial_code": "# Code ici",
    "expected_output": "Mineur",
    "level": 2,
    "theme": "conditions"
  },
  {
    "id": "cond_6",
    "title": "Tester une valeur négative",
    "instruction": "Si n est inférieur à 0, affiche 'Négatif', sinon 'Positif'.\nn = -1",
    "initial_code": "# Code ici",
    "expected_output": "Négatif",
    "level": 2,
    "theme": "conditions"
  },
  {
    "id": "cond_elif_example",
    "title": "📘 Exemple : if / elif / else",
    "instruction": "elif permet d'ajouter des alternatives à un test.\n\nscore = 15\nif score == 20:\n    print('Excellent')\nelif score == 15:\n    print('Bien')\nelse:\n    print('À revoir')",
    "initial_code": "score = 15\nif score == 20:\n    print('Excellent')\nelif score == 15:\n    print('Bien')\nelse:\n    print('À revoir')",
    "expected_output": "Bien",
    "level": 3,
    "theme": "conditions"
  },
  {
    "id": "cond_7",
    "title": "Choisir une note",
    "instruction": "Si note == 20 → 'Parfait', 15 → 'Très bien', sinon 'Continue'.\nnote = 20",
    "initial_code": "# Code ici",
    "expected_output": "Parfait",
    "level": 3,
    "theme": "conditions"
  },
  {
    "id": "cond_8",
    "title": "Système météo",
    "instruction": "Si temp > 30 → 'Chaud', < 10 → 'Froid', sinon 'Tempéré'.\ntemp = 8",
    "initial_code": "# Température ici",
    "expected_output": "Froid",
    "level": 3,
    "theme": "conditions"
  },
  {
    "id": "cond_9",
    "title": "Message d'accueil",
    "instruction": "Si langue est 'fr' → 'Bonjour', 'en' → 'Hello', sinon 'Salut'.\nlangue = 'en'",
    "initial_code": "# Test de langue",
    "expected_output": "Hello",
    "level": 3,
    "theme": "conditions"
  },
  {
    "id": "cond_logic_example",
    "title": "📘 Exemple : and / or",
    "instruction": "'and' exige deux conditions vraies, 'or' une seule suffit.\n\nage = 19\nticket = True\nif age > 18 and ticket:\n    print('Bienvenue')",
    "initial_code": "age = 19\nticket = True\nif age > 18 and ticket:\n    print('Bienvenue')",
    "expected_output": "Bienvenue",
    "level": 4,
    "theme": "conditions"
  },
  {
    "id": "cond_10",
    "title": "Accès selon condition",
    "instruction": "Si connecté et autorisé, affiche 'Accès ok'.\nconnecté = True, autorisé = True",
    "initial_code": "# Teste ici",
    "expected_output": "Accès ok",
    "level": 4,
    "theme": "conditions"
  },
  {
    "id": "cond_11",
    "title": "Mot de passe ou code",
    "instruction": "Si mot_de_passe est bon OU code est bon, affiche 'Accès'.",
    "initial_code": "# mot_de_passe = True, code = False",
    "expected_output": "Accès",
    "level": 4,
    "theme": "conditions"
  },
  {
    "id": "cond_12",
    "title": "Test imbriqué",
    "instruction": "Si a > 0, vérifie que b > 0 → 'Deux positifs'.\na = 2, b = 3",
    "initial_code": "# Code imbriqué",
    "expected_output": "Deux positifs",
    "level": 4,
    "theme": "conditions"
  },
  {
    "id": "cond_bonus_1",
    "title": "✅ BONUS : Pair ou impair",
    "instruction": "Si n % 2 == 0, affiche 'Pair', sinon 'Impair'.\nn = 5",
    "initial_code": "# Test pair/impair",
    "expected_output": "Impair",
    "level": 5,
    "theme": "conditions"
  },
  {
    "id": "cond_bonus_2",
    "title": "✅ BONUS : Devine un nombre",
    "instruction": "Si nombre == 7, affiche 'Gagné !', sinon 'Perdu...'.\nnombre = 7",
    "initial_code": "# Code devinette",
    "expected_output": "Gagné !",
    "level": 5,
    "theme": "conditions"
  },
  {
    "id": "cond_bonus_3",
    "title": "✅ BONUS : Catégorise une note",
    "instruction": "Si note >= 16 → 'Très bien', >=10 → 'Passable', sinon → 'Échec'.\nnote = 9",
    "initial_code": "# Note = 9",
    "expected_output": "Échec",
    "level": 5,
    "theme": "conditions"
  }
]
