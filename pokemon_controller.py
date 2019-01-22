from pokemon_views import Views
from pokemon_model import Pokemon
from pokemon_model import Habitat

class Controller:

    def __init__(self):
        self.views = Views()
        self.pokemon = Pokemon(pokemon_name, )
        self.habitat = Habitat(habitat_name)
        self.start()

    def start(self):
        user_info = self.views.get_options() # returns a tuple or an list
        check_options = self.models.get_options()
        if check_options == True:
            self.views.show_menu()
        else:
            self.views.get_options()
