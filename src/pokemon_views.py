import sys
from utils import findHabitatById


class Views:
    """Pokemon view class for user interaction"""

    def __init__(self):
        pass

    def main_menu(self):
        print("\nWelcome to the Pokedex\n\n")
        print("1. Create Habitat\n2. List Pokemon for Habitat\n3. Create Pokemon\n4. Quit")
        # respond with choice and combine with make choice

        choice = ""
        while True:
            choice = input("Your choice :")
            if choice in ["1", "2", "3", "4"]:
                break
        return int(choice)

    def create_habitat(self):
        habitat_name = ""
        print("Create a Habitat\nEnter habitat name or enter 'cancel' to cancel.\n")
        while True:
            habitat_name = input("Habitat Name: ")
            if habitat_name != "":
                if habitat_name.lower() == "cancel":
                    return
                break
        return habitat_name

    def create_pokemon(self):
        pokemon_name = ""
        print("Create a Pokemon\nEnter the Pokemon's name or enter 'cancel' to cancel.\n")

        while pokemon_name is not "cancel":
            pokemon_name = input("Pokemon Name: ")
            if pokemon_name.strip() != None:
                break

        return None if pokemon_name is "cancel" else pokemon_name.title()

    def select_habitat(self, habitats):
        # habitats = {}
        print("Which habitat does the Pokemon live in?\n")

        for habitat in habitats:
            print("{0}. {1}\n".format(habitat.habitat_id, habitat.habitat_name))

        habitat = None
        choice = ""
        while True:
            choice = input("\nYour choice :")
            habitat = findHabitatById(habitats, int(choice))
            if habitat is not None:
                break

        return habitat

    def quit(self):
        print("Exiting the system ...")
        sys.exit()
