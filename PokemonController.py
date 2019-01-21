from PokemonView import View
from PokemonModel import Model
import time

class Controller:
    """Controller speaks to the view and the model and orchestrates objects/data to and fro"""
    def __init__(self):
        self.view = View()

    def start_pokemon(self):
        self.view.main_menu()
        useroption = self.view.get_user_input()
        self.process_initoption(useroption)

    def process_initoption(self, useroption):
        if useroption == "1":
            self.view.habitat_menu()
            habitat_input = self.view.get_habitat_entry()
            self.process_habitat_option(habitat_input)
        elif useroption == "2":
            self.process_list_option()
        elif useroption == "3":
            self.view.pokemon_menu1 ()
            pokemon_input = self.view.get_pokemon_entry()
            if pokemon_input == "":
                print("Blank is not allowed....")
                time.sleep(2)
                self.start_pokemon()
            objmodel = Model()
            if objmodel.check_pokemon(pokemon_input.lower()) == True:
                print("Pokemon exists....")
                time.sleep(2)
                self.start_pokemon()
            self.process_pokemon_option(pokemon_input)
        elif useroption == "4":
            self.view.exit_program()
            exit()
        else:
            print("Invalid Entry, please select a valid option")
            time.sleep (2)
            self.start_pokemon()

    def process_habitat_option(self, habitat_input):
        if habitat_input.lower() == "cancel":
            self.start_pokemon()
        else:
            objmodel = Model()
            objmodel.add_habitat(habitat_input)
            self.start_pokemon()

    def process_list_option(self):
        objmodel = Model()
        return_hab = objmodel.retrieve_habitat()
        hab_name = self.view.choice2_display(return_hab)
        pok_names = objmodel.retrieve_pokemon(hab_name.lower())
        self.view.list_pokemon_display(pok_names)
        self.start_pokemon ()

    def process_pokemon_option(self, pokemon_input):
        if pokemon_input.lower () == "cancel":
            self.start_pokemon ()
        else:
            objmodel = Model ()
            self.view.pokemon_menu2 ()
            return_hab = objmodel.retrieve_habitat()
            self.view.pokemon_hab_display(return_hab)
            pokemon_habitat = self.view.get_pokemon_habitat()
            objmodel.add_pokemon(pokemon_input, return_hab[pokemon_habitat].lower())
            self.start_pokemon()


if __name__ == "__main__":
    obj = Controller()
    obj.start_pokemon()
