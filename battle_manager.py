import random
from battle_utils import strike
import time

def random_battle(pokemon1, pokemon2):
    print(f"Random Battle between {pokemon1.name} (Level {pokemon1.level}) and {pokemon2.name} (Level {pokemon2.level})! \n"
          f"-------------------------------------------------------------------")
    time.sleep(1.5)

    attacker, defender = random.sample([pokemon1, pokemon2], k=2)

    start_time = time.time()

    while pokemon1.hp > 0 and pokemon2.hp > 0:
        strike(attacker, defender)

        if defender.hp <= 0:
            print(f"{defender.name} fainted!\n")

        time.sleep(1.5)

        attacker, defender = defender, attacker

    end_time = time.time()

    winner = pokemon1 if pokemon1.hp > 0 else pokemon2
    print(f"{winner.name} is the winner!\n")

    duration = end_time - start_time
    print(f"The battle took {duration:.2f} seconds.")