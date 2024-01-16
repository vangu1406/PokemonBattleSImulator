# Polymorphic function
def strike(attacker, defender):
    is_pokemon_evolved = 'Evolve1' in str(type(attacker))

    if is_pokemon_evolved:
        attacker.special_strike(defender)
    else:
        attacker.strike(defender)