import sqlite3

db = "pokemon.db"
conn = sqlite3.connect(db)



conn.execute("DROP TABLE pokemons")
conn.execute("DROP TABLE habitats")

conn.commit()

conn.execute("CREATE TABLE habitats(habitat_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, habitat_name	varchar2 NOT NULL)")
conn.execute("CREATE TABLE pokemons(pokemon_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, pokemon_name varchar2(50) NOT NULL, habitat_id INTEGER NOT NULL)")