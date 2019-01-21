import sqlite3
class Model:

    def __init__(self):
        pass

    # Create DB connection
    def create_connection(self):
        conn = sqlite3.connect ("pokemon.db")
        return conn

    # Retrieve list of habitats available and return them in a dictionary
    def retrieve_habitat(self):
        conn = self.create_connection()
        cur = conn.cursor()
        return_obj = cur.execute("SELECT distinct(habitat_name) FROM habitats")
        index = 1
        hab_option = {}
        for i in return_obj.fetchall():
            var = str(i)
            hab_option[index] = ''.join(filter(str.isalnum, var))
            index+=1
        cur.close()
        return hab_option

    # Retrieve Pokemons for a particular Habitat
    def retrieve_pokemon(self, habitat_name):
        conn = self.create_connection()
        cur = conn.cursor()
        return_obj = cur.execute("SELECT distinct(pokemon_name) FROM pokemons where habitat_id in (select habitat_id from habitats where lower(habitat_name) = (?))",(habitat_name,))
        index = 1
        pok_option = {}
        for i in return_obj.fetchall():
            var = str(i)
            pok_option[index] = ''.join(filter(str.isalnum, var))
            index+=1
        conn.close()
        return pok_option

    # Adding a new Habitat
    def add_habitat(self, habitat_input):
        conn = self.create_connection()
        # conn.execute(f"INSERT INTO habitats(habitat_name) VALUES ({habitat_input})")
        conn.execute("INSERT INTO habitats(habitat_name) VALUES(?)",(habitat_input,))
        conn.commit()
        conn.close()
        return

    # Adding a new Pokemon
    def add_pokemon(self, pokemon_name, habitat_name):
        conn = self.create_connection()
        habitat_cur = conn.execute("SELECT habitat_id from habitats where lower(habitat_name) = (?)",(habitat_name,))
        habitat_id = habitat_cur.fetchone()[0]
        conn.execute("INSERT INTO pokemons(pokemon_name, habitat_id) VALUES(?,?)",(pokemon_name, habitat_id,))
        conn.commit()
        conn.close()
        return

    # Check if a Pokemon exists and return True if exists and False if does not exist
    def check_pokemon(self, pokemon_name):
        conn = self.create_connection()
        cur = conn.execute("SELECT count(pokemon_id) FROM pokemons where lower(pokemon_name) = (?)",(pokemon_name,))
        if cur.fetchone()[0] == 0: status = False
        else: status = True
        conn.close()
        return status