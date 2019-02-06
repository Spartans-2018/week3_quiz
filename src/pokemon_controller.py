from pokemon_views import Views
from pokemon_model import Pokemon
from pokemon_model import Habitat
from utils import findHabitatById


class Controller:
    """ Pokemon app controller module"""

    def __init__(self):
        self.views = Views()
        self.start()

    def start(self):
        choice = 0
        while choice != 4:
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

        self.views.quit()

    def create_habitat(self):
        new_habitat_name = self.views.create_habitat()
        if new_habitat_name != None:
            new_habitat = Habitat(new_habitat_name)
            new_habitat.save()

    def create_pokemon(self):
        new_pokemon_name = self.views.create_pokemon()
        if new_pokemon_name is not None:
            #   STOPPED HERE
            habitat_list = Pokemon.get_habitats()
            # habitat_map = dict([habitat.habitat_id, habitat for habitat in habitat_list])
            habitat_id = self.views.select_habitat(habitat_list)
            selected_habitat = findHabitatById(habitat_list, habitat_id)
            new_pokemon = Pokemon(new_pokemon_name, selected_habitat)
            print(new_pokemon)

    def list_pokemon(self):
        # self.views.list_pokemon(self.habitat)
        pass


# Main method to invoke application for the first time
if __name__ == "__main__":
    pokedex = Controller()
    pokedex.start()
