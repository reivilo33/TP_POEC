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
        nom TEXT NOT NULL,
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
    '{"Oeuf" : 3, "Sel" : 10, "Poivre" : 10}',
    '{"1" : ["Battre les oeufs", ["Oeuf"]], "2" : ["Assaisonner", ["Sel", "Poivre"]]}')
]

cur.executemany('''
    INSERT INTO recettes (nom, temps, image, difficulte, ingredients, instructions)
    VALUES (?, ?, ?, ?, ?, ?)
''', recettes)

# Valider les changements et fermer la connexion
conn.commit()
conn.close()

print("La base de données 'recettes.db' a été initialisée avec succès.")
