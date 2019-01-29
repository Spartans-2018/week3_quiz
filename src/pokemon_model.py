from db_helper import db


class Habitat:

    def __init__(self, habitat_name, habitat_id=None):
        self.habitat_id = habitat_id
        self.habitat_name = habitat_name

    def save(self):
        sql = """INSERT INTO Habitats(HabitatName) VALUES(?)"""
        db.conn.execute(sql, (self.habitat_name,))


class Pokemon:

    def __init__(self, pokemon_name, habitat=None):
        self.pokemon_name = pokemon_name
        self.habitat = habitat

    @staticmethod
    def get_habitats(habitat_name):
        if habitat_name != None:
            sql = """SELECT habitatid, HabitatName FROM Habitats WHERE habitatname in (?) ; """
            rows = db.conn.execute(sql, (habitat_name,))
        else:
            sql = """SELECT habitatid, HabitatName FROM Habitats ; """
            rows = db.conn.execute(sql, (habitat_name,))

        return [Habitat(row.habitat) for row in rows]

    # @staticmethod
    def save(self):
        sql = """INSERT INTO Pokemons (pokemonname, habitatid) values ((?), (?)) ; """
        db.conn.execute(sql, (self.pokemon_name), (self.habitat.habitat_id))

    @staticmethod
    def get_pokemons(habitat_name=None):
        selectst = """select p.pokemonname, p.habitatid, h.habitatname
                    from Pokemons p inner join Habitats h 
                    ON p.habitatid=h.habitatid (?) """
        # use the placeholder for semicolon
        wherecl = """  WHERE h.habitatname in ((?)) (?) """
        if habitat_name != None:
            rows = db.conn.execute(
                selectst, wherecl, (""), (habitat_name), (";"))
        else:
            rows = db.conn.execute(selectst, (";"))

        # pokemons = []
        # for row in rows:
        #       habitat = Habitat(row.habitatname, row.habitatid)
        #     pokemon = Pokemon(row.pokemonname, habitat)
        #     pokemons.append(pokemon)

        return [Pokemon(row.pokemonname, Habitat(row.habitatname, row.habitatid)) for row in rows]
