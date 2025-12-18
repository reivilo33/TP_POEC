import sqlite3

# Connexion (ou création) à la base de données SQLite
conn = sqlite3.connect('recettes.db')
cur = conn.cursor()

# Suppression de la table si elle existe déjà
cur.execute('DROP TABLE IF EXISTS recettes')

# Création de la table 'recettes'
cur.execute('''
    CREATE TABLE recettes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        temps TEXT,
        image TEXT,
        difficulte TEXT,
        ingredients JSON NOT NULL,
        instructions JSON NOT NULL
    )
''')

# Suppression de la table si elle existe déjà
cur.execute('DROP TABLE IF EXISTS ingredients')

# Création de la table 'ingredients'
cur.execute('''
    CREATE TABLE ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom NOT NULL,
        image TEXT,
        prix FLOAT,
        categorie TEXT,
        unite TEXT NOT NULL
    )
''')

# Insertion des 
recettes = [
        
    ("Omelette", 
    "5 min", 
    "omelette.png", 
    "facile",
    '{1 : 3, 2 : 10, 3 : 10}',
    str({
        "1" : ["Battre les oeufs", [1]], 
        "2" : ["Assaisonner", [2, 3]]
        })
    ),
    ("Pates au beurre",
    "15 min",
    "pates_au_beurre.png",
    "moyenne",
    '{4 : 100, 5 : 10, 6 : 50}',
    str({
      "1" : ["Faire bouillir de l\'eau", []], 
      "2" : ["Mettre les pates dans l\'eau bouillante" ,[4]],
      "3" : ["Attendre 5 min", []],
      "4" : ["Egouter les pates et y ajouter le beurre et le fromage", [5, 6]]
      })
    )
]

ingredients = [
    (1, "Oeuf",
    "oeuf.png",
    1.50,
    "proteine",
    ""),
    (2, "Sel",
    "sel.png",
    2.00,
    "mineral",
    "g"),
    (3, "Poivre",
    "poivre.png",
    2.00,
    "mineral",
    "g"),
    (4, "Pates",
    "pates.png",
    1.20,
    "feculants",
    "g"),
    (5, "Beurre",
    "beurre.png",
    3.20,
    "matiere grasse",
    "g"),
    (6, "Fromage",
    "fromage.png",
    1.70,
    "produit laitier",
    "g")
]

cur.executemany('''
    INSERT INTO recettes (nom, temps, image, difficulte, ingredients, instructions)
    VALUES (?, ?, ?, ?, ?, ?)
''', recettes)

cur.executemany('''
    INSERT INTO ingredients (id, nom, image, prix, categorie, unite)
    VALUES (?, ?, ?, ?, ?, ?)
''', ingredients)

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print("La base de données 'recettes.db' a été initialisée avec succès.")
