import sqlite3

conn = sqlite3.connect('Pokedex.db')

conn.execute(
    """
    --- Pokemons
    CREATE TABLE Pokemons IF NOT EXISTS (
        PokemonID INTEGER PRIMARY KEY, 
        PokemonName TEXT NOT NULL,
        HabitatID TEXT,
        LastModified TEXT,
        FOREIGN KEY(HabitatID) REFERENCES Habitats(HabitatID)
     );
    """
)

conn.execute (
    """
    --- Habitats
    CREATE TABLE Habitats (
        HabitatID INTEGER PRIMARY KEY,
        HabitatName TEXT NOT NULL,
        LastModified TEXT
    );
    """
)

conn.commit() # must commit when manipulating the database
conn.close()

print("Your database was created successfully!")