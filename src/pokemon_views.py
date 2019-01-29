import sys


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

    def create_pokemon(self, habitats):
        pokemon_name = ""
        print("Create a Pokemon\nEnter the Pokemon's name or enter 'cancel' to cancel.\n")

        while True:
            pokemon_name = input("Pokemon Name: ")
            if pokemon_name != "":
                if pokemon_name.lower() == "cancel":
                    return
                break
        return pokemon_name

    def select_habitat(self, habitats):
        # habitats = {}
        print("Which habitat does the Pokemon live in?\n")

        for habitat_id, habitat_name in habitats.items():
            print("{0}. {1}\n".format(habitat_id, habitat_name))

        choice = ""
        while True:
            choice = input("\nYour choice :")
            if choice in habitats.keys():
                break
        habitat_name = habitats[choice]

        return int(choice), habitat_name

    def quit(self):
        print("Exiting the system ...")
        sys.exit()
