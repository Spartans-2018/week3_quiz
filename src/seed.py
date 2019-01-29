from db_helper import db

# Drop Table If Exists
db.execute("DROP TABLE IF EXISTS Pokemons")
db.execute("DROP TABLE IF EXISTS Habitats")


db.execute( """CREATE TABLE Pokemons (PokemonID INTEGER PRIMARY KEY AUTOINCREMENT,
     PokemonName VARCHAR2(50) NOT NULL, HabitatID INTEGER NOT NULL ); """)

db.execute("""CREATE TABLE Habitats ( HabitatID INTEGER PRIMARY KEY AUTOINCREMENT,HabitatName VARCHAR2(50) NOT NULL);""")

# db.conn.commit()  # must commit when manipulating the database

print("Your database was created successfully!")
