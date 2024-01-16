# Pokemon Battle Simulator
This Python project is a simple text-based Pokemon battle simulator, built to practice Python Object-oriented programming (OOP) and demonstrate some of its most important concepts in action. The simulator allows two Pokemon to engage in a random battle, with each Pokemon having its own stats and abilities.

## Preview 👀
![preview_pbs](https://github.com/vangu1406/PokemonBattleSimulator/assets/156591465/e2ee4b74-f0a4-4003-a1a3-4bf7b56a44c2)

## Constructs used ⚙️

* Classes and objects
* Static method
* Dunder method
* Class method
* Inheritance
* Polymorphism

The project is divided into 5 Python files to maintain a clean and modular structure:

1. ### Pokemon.py
* Defines the base Pokemon class with attributes like name, attack, defense etc.
* Includes methods for attacking, gaining experience, leveling up and creating Pokemon instances from an Excel file (pokemon_data.xlsx).
2. ### Evolve1.py
* Inherits from the Pokemon class to create an evolved Pokemon.
* Introduces a special attack method specific to evolved Pokemon.
3. ### battle_utils.py
* Provides the utility function that implements the polymorphic behavior of Pokemon attacks. If the attacker is an evolved Pokemon, it calls *special_strike()* method; otherwise, it calls regular strike.
4. ### battle_manager.py 
 * Manages the flow of a Pokemon battle by randomly determining which Pokemon will attack first. 
 * Uses strike function from battle_utils.py to simulate attacks during the battle.
 * Determines the winner based on the remaining hit points (hp).
 5. ### playground.py
 * In this file Pokemon instances are created using *create_pokemon()* method from the Pokemon class.
 * Invokes random_battle function from battle_manager.py to start the battle between two Pokemon.

## Usage 👾

1. **Creating Pokemon**
```py
charmander = Pokemon.create_pokemon("Charmander")
```
2. **Displaying Pokemon stats**
```py
print(charmander)
```
3. **Battle simulation**
```py
bulbasaur = Pokemon("Bulbasaur", 8, 10, 20, 7, 9)
charmander.strike(bulbasaur)
```
4. **Comparing Pokemon strength**
```py
charmander == bulbasaur
```

Happy battling! 🎮✨ 
