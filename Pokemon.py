import pandas as pd
import numpy as np
import os
import time
class Pokemon:

    exp_pts = 10

    def __init__(self, name, attack, defense, hp, special_attack, special_defense, level=1, exp=0, base_exp_to_next_level=10):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.hp = hp
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.level = level
        self.exp = exp
        self.base_exp_to_next_level = base_exp_to_next_level

    @staticmethod
    def display_intro_rules():
        print("Welcome to the Pokemon Battle Simulator!")
        print("Battle Rules:")
        print("- Each Pokemon takes turns attacking.")
        print("- The attacker and defender roles switch after each turn.")
        print("- The battle continues until one Pokemon's HP reaches 0.")

    def speak(self):
        print(f"{self.name} says: {self.name}, {self.name}")

    def strike(self, other):
        damage = max(self.attack - other.defense, 0)
        other.hp = max(other.hp - damage, 0)
        print(f"{self.name} attacks {other.name} for {damage} hp!\n")
        time.sleep(1.5)

        if damage > 0:
            self._gain_experience()

    def __eq__(self, other):
        self_stats_total = 0
        other_stats_total = 0

        for key, value in self.__dict__.items():
            if key != 'name':
                self_stats_total += np.int64(value)
        for key, value in other.__dict__.items():
            if key != 'name':
                other_stats_total += np.int64(value)

        if self_stats_total > other_stats_total:
            print(f"{self.name} is stronger!")
        else:
            print(f"{other.name} is stronger!")

    def __repr__(self):
        return (f"Printing Stats Report: \n"
                f"Name: {self.name} \n"
                f"Attack:{self.attack} \n"
                f"Defense:{self.defense} \n"
                f"Hp:{self.hp} \n"
                f"Special Attack: {self.special_attack} \n"
                f"Special Defender: {self.special_defense} \n"
                f"Level: {self.level} \n"
                f"Experience: {self.exp} \n"
                f"Experience to next level: {self.base_exp_to_next_level}")

    @classmethod
    def create_pokemon(cls, name):
        script_dir = os.path.dirname(__file__)
        file_path = os.path.join(script_dir, 'pokemon_data.xlsx')
        pokemon_df = pd.read_excel(file_path)
        pokemon_names = pokemon_df[pokemon_df.Generation == 1].Name

        if name not in pokemon_names.values:
            raise ValueError('Pokemon does not exist. Choose another one')

        Attack = pokemon_df[pokemon_df.Name == name].Attack.values[0]
        Defense = pokemon_df[pokemon_df.Name == name].Defense.values[0]
        Hp = pokemon_df[pokemon_df.Name == name].HP.values[0]
        Special_Attack = pokemon_df[pokemon_df.Name == name]['Sp. Atk'].values[0]
        Special_Defense = pokemon_df[pokemon_df.Name == name]['Sp. Def'].values[0]

        return Pokemon(name=name, attack=Attack, defense=Defense,
                       hp=Hp, special_attack=Special_Attack, special_defense=Special_Defense)

    def _gain_experience(self):
        self.exp += self.exp_pts
        print(f"{self.name} gained {self.exp_pts} experience points! Total: {self.exp}" )
        time.sleep(1.5)

        if self.exp >= self.base_exp_to_next_level:
            self._level_up()

    def _level_up(self):
        self.level += 1
        print(f"{self.name} has level up to level {self.level}")
        time.sleep(1.5)

        self.base_exp_to_next_level = round(self.base_exp_to_next_level * 1.5)  # incrementa la soglia del 50% per passare al livello successivo
        self.exp = 0

        for key, value in self.__dict__.items():
            if isinstance(value, str) == False and key != "level":
                lvl_diff = self.level - 1
                self.__dict__[key] = round(value * 1.02 ** lvl_diff)

        print(f"{self.name}'s stats increased: {self.__dict__}\n")
        time.sleep(1.5)