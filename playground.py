from Pokemon import Pokemon
from Evolve1 import Evolve1
from battle_manager import random_battle

if __name__ == "__main__":

    regular_pokemon = Pokemon.create_pokemon("Charmander")
    evolved_pokemon = Evolve1.create_pokemon("Ivysaur")

    random_battle(regular_pokemon, evolved_pokemon)