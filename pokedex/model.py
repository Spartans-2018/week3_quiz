import sqlite3

conn = sqlite3.connect('pokedex/pokedex.db')

class Habitat:

    def __init__(self, habitat_name, habitat_id=None):
        self.habitat_id = habitat_id
        self.habitat_name = habitat_name

    def save(self):
        sql = """insert into habitats (habitatname) values ((?))"""
        conn.execute(sql,(self.habitat_name))

class Pokemon:

    def __init__(self, pokemon_name, habitat):
        self.pokemon_name = pokemon_name
        self.habitat = habitat
    
    def get_habitats(self, habitat_name):        
        if habitat_name!=None:
            sql = """SELECT * FROM habitats WHERE habitatname in (?) ; """
            rows = conn.execute(sql, (habitat_name))
        else:
            sql = """SELECT * FROM habitats ; """
            rows = conn.execute(sql, (habitat_name))

        return [Habitat(row.habitat) for row in rows]

    # @staticmethod
    def save(self):
        sql = """INSERT INTO pokemons (pokemonname, habitatid) values ((?), (?)) ; """
        conn.execute(sql, (self.pokemon_name), (self.habitat.habitat_id))

    @staticmethod
    def get_pokemons(habitat_name=None):
        selectst = """select p.pokemonname, p.habitatid, h.habitatname
                    from pokemons p inner join habitats h 
                    ON p.habitatid=h.habitatid (?) """
        # use the placeholder for semicolon
        wherecl =  """  WHERE h.habitatname in ((?)) (?) """
        if habitat_name!=None:
            rows = conn.execute(selectst,wherecl,(""), (habitat_name),(";"))
        else:
            rows = conn.execute(selectst,(";"))

        # pokemons = []
        # for row in rows:
        #       habitat = Habitat(row.habitatname, row.habitatid)
        #     pokemon = Pokemon(row.pokemonname, habitat)
        #     pokemons.append(pokemon)

        return [Pokemon(row.pokemonname, Habitat(row.habitatname, row.habitatid)) for row in rows]

 