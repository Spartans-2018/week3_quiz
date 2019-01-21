class View:
    """View class for Pokemon, this is used for client side interactions"""
    def __init__(self):
        pass

    # Main menu options
    def main_menu(self):
        print("*"*20)
        print("Welcome to the Pokedex")
        print("1. Create Habitat")
        print("2. List Pokemon for Habitat")
        print("3. Create Pokemon")
        print("4. Quit")

    def get_user_input(self):
        """Get user input to action accordingly"""
        print("Enter your Input")
        user_input = input()
        return user_input

    def habitat_menu(self):
        print("Enter habitat name or enter 'cancel' to cancel.")

    def get_habitat_entry(self):
        user_input = input("Habitat Name: ")
        return user_input.strip(" ")

    def choice2_display(self, hab_dict):
        for k,v in hab_dict.items():
            print(f'{k}. {v}')
        user_input = int(input("Your choice: "))
        print(f"{hab_dict[user_input]} Pokemon:")
        return hab_dict[user_input]

    # Display Habitat
    def pokemon_hab_display(self, hab_dict):
        for k,v in hab_dict.items():
            print(f'{k}. {v}')

    # Display pokemons for a habitat provided by user
    def list_pokemon_display(self, poknames):
        for i in poknames.values():
            print(i)
        return

    # Option 3 display broken up into 2 parts, this is part 1
    def pokemon_menu1(self):
        print("Create a Pokemon")
        print("Enter the Pokemon's name or enter 'cancel' to cancel.")

    # Option 3 display broken up into 2 parts, this is part 2
    def pokemon_menu2(self):
        print ("Which habitat does the Pokemon live in?")

    def get_pokemon_entry(self):
        user_input = input("Pokemon Name: ")
        return user_input.strip(" ")

    def get_pokemon_habitat(self):
        user_input = input("Your choice: ")
        return int(user_input)
    # Choice 4 display
    def exit_program(self):
        print("Exiting program.....")



