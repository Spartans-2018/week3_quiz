import sqlite3

db = "pokemon.db"
conn = sqlite3.connect(db)

# Drop Table If Exists
conn.execute("DROP TABLE IF EXISTS pokemons")
conn.execute("DROP TABLE IF EXISTS habitats")

conn.commit()
# Create Tables
conn.execute("CREATE TABLE habitats(habitat_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, habitat_name	varchar2 NOT NULL)")
conn.execute("CREATE TABLE pokemons(pokemon_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, pokemon_name varchar2(50) NOT NULL, habitat_id INTEGER NOT NULL)")

# Insert Values - Optional, comment below inserts if not required
conn.execute('insert into habitats (habitat_name) values ("Grassland")')
conn.execute('insert into habitats (habitat_name) values ("Forest")')
conn.execute('insert into habitats (habitat_name) values ("Water\'s-edge")')
conn.execute('insert into habitats (habitat_name) values ("Sea")')
conn.execute('insert into habitats (habitat_name) values ("Cave")')

conn.execute('insert into pokemons (pokemon_name, habitat_id) values ("Pikachu", 2)')
conn.commit()
