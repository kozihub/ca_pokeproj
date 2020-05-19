# ca_pokeproj
Pokemon project


Simple python project that creates a Pokemon and Trainer Class.

The Pokemon class has name, type, level, max hp, and knocked out parameters.
The Trainer class has trainer name, pokemon class list, number of potions, current pokemon.  

The trainer contains a list of pokemon in the pokemon class which can call functions within the class to battle, damage, check ko, regain health, and revive.

The trainer class is the main class to call attack, use potions, and swap pokemon. 
The trainer attack will use the pokemon attack, check damage and ko to determine if the attack will ko the opponent. If it does, the opponent has the input command to use a potion to revive current pokemon or swap pokemon for a fresh one.

It doesn't have a final check to see if all pokemon are ko'ed yet.
