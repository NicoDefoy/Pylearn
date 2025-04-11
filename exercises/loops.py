exercises = [
  {
    "id": "loop_intro",
    "title": "📘 Introduction aux boucles",
    "instruction": "Une boucle permet de répéter un bloc de code.\nExemple :\n\nfor i in range(3):\n    print(i)",
    "initial_code": "for i in range(3):\n    print(i)",
    "expected_output": "0\n1\n2",
    "level": 0,
    "theme": "loops"
  },
  {
    "id": "loop_1",
    "title": "Afficher une série de nombres",
    "instruction": "Utilise une boucle pour afficher les nombres de 1 à 3.",
    "initial_code": "# Boucle ici",
    "expected_output": "1\n2\n3",
    "level": 1,
    "theme": "loops"
  },
  {
    "id": "loop_2",
    "title": "Répéter une phrase",
    "instruction": "Affiche 'Salut' 4 fois avec une boucle.",
    "initial_code": "# Répète 'Salut'",
    "expected_output": "Salut\nSalut\nSalut\nSalut",
    "level": 1,
    "theme": "loops"
  },
  {
    "id": "loop_3",
    "title": "Boucle avec range personnalisé",
    "instruction": "Affiche les nombres de 5 à 7 inclus.",
    "initial_code": "# range(?, ?)",
    "expected_output": "5\n6\n7",
    "level": 1,
    "theme": "loops"
  },
  {
    "id": "loop_list_example",
    "title": "📘 Exemple : Boucler sur une liste",
    "instruction": "Tu peux boucler sur une liste d'éléments.\nExemple :\n\nfruits = ['pomme', 'banane']\nfor fruit in fruits:\n    print(fruit)",
    "initial_code": "fruits = ['pomme', 'banane']\nfor fruit in fruits:\n    print(fruit)",
    "expected_output": "pomme\nbanane",
    "level": 2,
    "theme": "loops"
  },
  {
    "id": "loop_4",
    "title": "Afficher les animaux",
    "instruction": "Boucle sur la liste ['chat', 'chien'] et affiche chaque mot.",
    "initial_code": "# Boucle sur la liste",
    "expected_output": "chat\nchien",
    "level": 2,
    "theme": "loops"
  },
  {
    "id": "loop_5",
    "title": "Lister des prénoms",
    "instruction": "Boucle sur ['Léo', 'Emma'] et affiche-les.",
    "initial_code": "# Boucle ici",
    "expected_output": "Léo\nEmma",
    "level": 2,
    "theme": "loops"
  },
  {
    "id": "loop_6",
    "title": "Liste de couleurs",
    "instruction": "Boucle sur ['rouge', 'bleu', 'vert'] et affiche chaque couleur.",
    "initial_code": "# Liste à parcourir",
    "expected_output": "rouge\nbleu\nvert",
    "level": 2,
    "theme": "loops"
  },
  {
    "id": "loop_sum_example",
    "title": "📘 Exemple : Somme d'une liste",
    "instruction": "On peut additionner les éléments d'une liste avec une boucle.\n\nnombres = [1, 2, 3]\ntotal = 0\nfor n in nombres:\n    total += n\nprint(total)",
    "initial_code": "nombres = [1, 2, 3]\ntotal = 0\nfor n in nombres:\n    total += n\nprint(total)",
    "expected_output": "6",
    "level": 3,
    "theme": "loops"
  },
  {
    "id": "loop_7",
    "title": "Somme de 3 nombres",
    "instruction": "Additionne tous les nombres dans [4, 5, 6] et affiche le total.",
    "initial_code": "# Code ici",
    "expected_output": "15",
    "level": 3,
    "theme": "loops"
  },
  {
    "id": "loop_8",
    "title": "Produit d'une liste",
    "instruction": "Multiplie tous les nombres dans [2, 3, 4] et affiche le résultat.",
    "initial_code": "# Produit total",
    "expected_output": "24",
    "level": 3,
    "theme": "loops"
  },
  {
    "id": "loop_9",
    "title": "Compter des voyelles",
    "instruction": "Compte combien de lettres dans ['a', 'e', 'i', 'o'] sont des voyelles.",
    "initial_code": "# Test voyelles",
    "expected_output": "4",
    "level": 3,
    "theme": "loops"
  },
  {
    "id": "loop_nested_example",
    "title": "📘 Exemple : Boucle imbriquée",
    "instruction": "On peut mettre une boucle dans une autre :\n\nfor i in range(2):\n    for j in range(2):\n        print(i, j)",
    "initial_code": "for i in range(2):\n    for j in range(2):\n        print(i, j)",
    "expected_output": "0 0\n0 1\n1 0\n1 1",
    "level": 4,
    "theme": "loops"
  },
  {
    "id": "loop_10",
    "title": "Créer une grille",
    "instruction": "Utilise 2 boucles pour afficher :\n*\n**\n***",
    "initial_code": "# Grille avec for",
    "expected_output": "*\n**\n***",
    "level": 4,
    "theme": "loops"
  },
  {
    "id": "loop_11",
    "title": "Triangle numérique",
    "instruction": "Affiche :\n1\n12\n123",
    "initial_code": "# Triangle croissant",
    "expected_output": "1\n12\n123",
    "level": 4,
    "theme": "loops"
  },
  {
    "id": "loop_12",
    "title": "Grille 2x2",
    "instruction": "Affiche :\na a\na a",
    "initial_code": "# 2 lignes, 2 colonnes",
    "expected_output": "a a\na a",
    "level": 4,
    "theme": "loops"
  },
  {
    "id": "loop_bonus_1",
    "title": "✅ BONUS : Afficher les carrés",
    "instruction": "Affiche les carrés des nombres de 1 à 3 : 1, 4, 9",
    "initial_code": "# Carrés de i",
    "expected_output": "1\n4\n9",
    "level": 5,
    "theme": "loops"
  },
  {
    "id": "loop_bonus_2",
    "title": "✅ BONUS : Mot inversé",
    "instruction": "Avec une boucle, affiche les lettres de 'salut' en ordre inverse.",
    "initial_code": "# Reverser une string",
    "expected_output": "t\nu\nl\na\ns",
    "level": 5,
    "theme": "loops"
  },
  {
    "id": "loop_bonus_3",
    "title": "✅ BONUS : Liste à l'envers",
    "instruction": "Affiche les éléments de [1,2,3] à l'envers : 3,2,1",
    "initial_code": "# Reverse loop",
    "expected_output": "3\n2\n1",
    "level": 5,
    "theme": "loops"
  }
]
