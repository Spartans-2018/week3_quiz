from PokemonView import View
from PokemonModel import Model
import time

class Controller:
    """Controller speaks to the view and the model and orchestrates objects/data to and fro"""
    def __init__(self):
        self.view = View()

    # Start Pokemon App
    def start_pokemon(self):
        self.view.main_menu()
        useroption = self.view.get_user_input()
        self.process_initoption(useroption)

    # Initial options available and call of subsequent fuctions according to inputs
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
            # Checking if pokemon name is blank
            if pokemon_input == "":
                print("Blank is not allowed....")
                # 2 seconds delay after invalid option
                time.sleep(2)
                self.start_pokemon()
            objmodel = Model()
            # Checking if Pokemon exists
            if objmodel.check_pokemon(pokemon_input.lower()) == True:
                print("Pokemon exists....")
                # 2 seconds delay after pokemon exists error
                time.sleep(2)
                self.start_pokemon()
            self.process_pokemon_option(pokemon_input)
        # Exit program if option4 is selected
        elif useroption == "4":
            self.view.exit_program()
            exit()
        else:
            print("Invalid Entry, please select a valid option")
            time.sleep (2)
            self.start_pokemon()

    # Function calls for Option 1
    def process_habitat_option(self, habitat_input):
        if habitat_input.lower() == "cancel":
            # Main menu invoked after option 1 cancel completion
            self.start_pokemon()
        else:
            objmodel = Model()
            objmodel.add_habitat(habitat_input)
            # Main menu invoked after option 1 completion
            self.start_pokemon()

    # Function calls for Option 2
    def process_list_option(self):
        objmodel = Model()
        return_hab = objmodel.retrieve_habitat()
        hab_name = self.view.choice2_display(return_hab)
        pok_names = objmodel.retrieve_pokemon(hab_name.lower())
        self.view.list_pokemon_display(pok_names)
        # Main menu invoked after option 2 completion
        self.start_pokemon ()

    # Function calls for Option 3
    def process_pokemon_option(self, pokemon_input):
        if pokemon_input.lower () == "cancel":
            # Main menu invoked after option 3 cancel completion
            self.start_pokemon ()
        else:
            objmodel = Model ()
            self.view.pokemon_menu2 ()
            return_hab = objmodel.retrieve_habitat()
            self.view.pokemon_hab_display(return_hab)
            pokemon_habitat = self.view.get_pokemon_habitat()
            objmodel.add_pokemon(pokemon_input, return_hab[pokemon_habitat].lower())
            # Main menu invoked after option 3 completion
            self.start_pokemon()

# Main method to invoke application for the first time
if __name__ == "__main__":
    obj = Controller()
    obj.start_pokemon()
