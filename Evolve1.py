from Pokemon import Pokemon
import time

class Evolve1(Pokemon):

    def __init__(self, name, attack, defense, hp, special_attack, special_defense, level=1, exp=0, base_exp_to_next_level=10):
        super().__init__(name, attack, defense, hp, special_attack, special_defense, level, exp, base_exp_to_next_level)

    def special_strike(self, other):
        damage = max(self.special_attack - other.special_defense, 0)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name} attacks {other.name} for {damage} hp using special strike!")
        time.sleep(1.5)