exercises = [
  {
    "id": "str_intro",
    "title": "📘 Introduction aux chaînes de caractères",
    "instruction": "Une chaîne de caractères est un texte entouré de guillemets.\n\nmessage = 'Bonjour'\nprint(message)",
    "initial_code": "message = 'Bonjour'\nprint(message)",
    "expected_output": "Bonjour",
    "level": 0,
    "theme": "strings"
  },
  {
    "id": "str_1",
    "title": "Créer une chaîne simple",
    "instruction": "Crée une variable texte avec 'Salut !' et affiche-la.",
    "initial_code": "# Chaîne simple ici",
    "expected_output": "Salut !",
    "level": 1,
    "theme": "strings"
  },
  {
    "id": "str_2",
    "title": "Concaténer deux chaînes",
    "instruction": "Crée deux variables prenom = 'Léo' et nom = 'Dupont'. Affiche 'Léo Dupont'.",
    "initial_code": "# Concaténation",
    "expected_output": "Léo Dupont",
    "level": 1,
    "theme": "strings"
  },
  {
    "id": "str_length_example",
    "title": "📘 Exemple : Longueur d'une chaîne",
    "instruction": "On utilise len() pour connaître la longueur d'une chaîne.\n\nnom = 'Alice'\nprint(len(nom))",
    "initial_code": "nom = 'Alice'\nprint(len(nom))",
    "expected_output": "5",
    "level": 2,
    "theme": "strings"
  },
  {
    "id": "str_3",
    "title": "Longueur d'un mot",
    "instruction": "Crée la variable mot = 'bonjour' et affiche sa longueur.",
    "initial_code": "# Utilise len()",
    "expected_output": "7",
    "level": 2,
    "theme": "strings"
  },
  {
    "id": "str_4",
    "title": "Longueur d'une phrase",
    "instruction": "Calcule la longueur de 'Je suis content'.",
    "initial_code": "# len de la phrase",
    "expected_output": "16",
    "level": 2,
    "theme": "strings"
  },
  {
    "id": "str_case_example",
    "title": "📘 Exemple : Majuscules et minuscules",
    "instruction": "On peut transformer le texte avec upper() ou lower().\n\nprint('Bonjour'.upper())",
    "initial_code": "print('Bonjour'.upper())",
    "expected_output": "BONJOUR",
    "level": 2,
    "theme": "strings"
  },
  {
    "id": "str_5",
    "title": "Tout en majuscules",
    "instruction": "Crée une variable mot = 'python' et affiche-la en majuscules.",
    "initial_code": "# upper() ici",
    "expected_output": "PYTHON",
    "level": 2,
    "theme": "strings"
  },
  {
    "id": "str_6",
    "title": "Tout en minuscules",
    "instruction": "Crée mot = 'PROGRAMMATION', affiche-le en minuscules.",
    "initial_code": "# lower() ici",
    "expected_output": "programmation",
    "level": 2,
    "theme": "strings"
  },
  {
    "id": "str_format_example",
    "title": "📘 Exemple : Formatage de chaîne",
    "instruction": "On peut insérer des variables dans une chaîne avec f-strings :\n\nprenom = 'Emma'\nprint(f'Bonjour {prenom}')",
    "initial_code": "prenom = 'Emma'\nprint(f'Bonjour {prenom}')",
    "expected_output": "Bonjour Emma",
    "level": 3,
    "theme": "strings"
  },
  {
    "id": "str_7",
    "title": "Utiliser f-string",
    "instruction": "nom = 'Luc', ville = 'Lyon'. Affiche : Luc habite à Lyon.",
    "initial_code": "# f-string ici",
    "expected_output": "Luc habite à Lyon",
    "level": 3,
    "theme": "strings"
  },
  {
    "id": "str_8",
    "title": "f-string avec âge",
    "instruction": "prenom = 'Nico', age = 28. Affiche : Nico a 28 ans.",
    "initial_code": "# Encore un f-string",
    "expected_output": "Nico a 28 ans",
    "level": 3,
    "theme": "strings"
  },
  {
    "id": "str_find_example",
    "title": "📘 Exemple : Trouver une lettre",
    "instruction": "On peut chercher un caractère avec in ou find().\n\nprint('a' in 'papa')",
    "initial_code": "print('a' in 'papa')",
    "expected_output": "True",
    "level": 4,
    "theme": "strings"
  },
  {
    "id": "str_9",
    "title": "Chercher un mot",
    "instruction": "Texte = 'J'adore Python'. Vérifie si 'Python' est dans le texte.",
    "initial_code": "# in ici",
    "expected_output": "True",
    "level": 4,
    "theme": "strings"
  },
  {
    "id": "str_10",
    "title": "Position d'une lettre",
    "instruction": "mot = 'programmation'. Affiche l'indice de la lettre 'g'.",
    "initial_code": "# find ici",
    "expected_output": "5",
    "level": 4,
    "theme": "strings"
  },
  {
    "id": "str_bonus_1",
    "title": "✅ BONUS : Remplacer un mot",
    "instruction": "Texte = 'Python est cool'. Remplace 'cool' par 'incroyable'.",
    "initial_code": "# replace ici",
    "expected_output": "Python est incroyable",
    "level": 5,
    "theme": "strings"
  },
  {
    "id": "str_bonus_2",
    "title": "✅ BONUS : Compter un mot",
    "instruction": "phrase = 'le python est un langage. python est facile'. Compte les 'python'.",
    "initial_code": "# count ici",
    "expected_output": "2",
    "level": 5,
    "theme": "strings"
  }
]
