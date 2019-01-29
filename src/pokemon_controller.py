from pokemon_views import Views
from pokemon_model import Pokemon
from pokemon_model import Habitat


class Controller:
    """ Pokemon app controller module"""

    def __init__(self):
        self.views = Views()
        self.start()

    def start(self):
        choice = 0
        while True:
            choice = self.views.main_menu()

            # 1. create habitat
            if (choice == 1):
                self.create_habitat()
            # 2. list pokemon for habitat
            elif (choice == 2):
                self.list_pokemon()
            # 3. create pokemon
            elif (choice == 3):
                self.create_pokemon()
            elif (choice == 4):
                self.views.quit()
            


    def create_habitat(self):
        new_habitat_name = self.views.create_habitat()
        if new_habitat_name != None :
            new_habitat = Habitat(new_habitat_name)
            new_habitat.save()

    def create_pokemon(self):
        new_pokemon_name = self.views.create_pokemon()
        habitat_list = Pokemon(new_pokemon_name, None).get_habitats()
        habitat_id = self.views.select_habitat(habitat_list)
        new_pokemon = Pokemon(new_pokemon_name, )

    def list_pokemon(self):
        self.views.list_pokemon(self.habitat)


# Main method to invoke application for the first time
if __name__ == "__main__":
    pokedex = Controller()
    pokedex.start()
