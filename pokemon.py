import random as rd


#Creates a pokemon class that can check super effective and not very effective for just fire, water, grass types
class Pokemon:
    def __init__(self, name, level, type, max_health, ko = False):
        self.name = name
        self.level = level
        self.type = type
        self.max_health = max_health
        self.current_health = self.max_health
        self.ko = ko
    def __repr__(self):
        return f'{self.name}'
    def lose_health(self, health_loss):
        self.current_health -= health_loss
        if self.current_health <= 0:
            self.current_health = 0
            self.knocked_out()
        else:
            print(self.name + ' now has ' + str(self.current_health) + ' health.\n')
    def gain_health(self, health_gain):
        self.current_health += health_gain
        print(self.name + ' now has ' + str(self.current_health) + ' health.')
    def knocked_out(self):
        self.current_health = 0
        self.ko = True
        print(f'{self.name} fainted!')
    def revive(self,potion_amount=10):
        if self.ko:
            self.ko = False
            self.current_health += potion_amount
            print(self.name + ' has been revived and is now at ' + str(self.current_health) + ' health.')
    def attack(self, other_pokemon):
        stab = 1.0
        if (self.type == 'fire' and other_pokemon.type == 'grass') \
            or (self.type  == 'grass' and other_pokemon.type == 'water') \
            or (self.type  == 'water' and other_pokemon.type == 'fire'):
            stab += .5
        elif (self.type  == 'fire' and other_pokemon.type == 'water') \
            or (self.type  == 'grass' and other_pokemon.type == 'fire') \
            or (self.type  == 'water' and other_pokemon.type == 'grass'):
            stab -= .5
        dmg = self.level*stab + (rd.randint(-5,5)*0.10)
        print(other_pokemon.name + " has taken " + str(dmg) + " points of damage!")
        other_pokemon.lose_health(dmg)
 
# Creates a Trainer class that has user name, pokemons with Pokemon class, potion amounts, current pokemon.
# The Trainer class has user inputs if user attacks opponet and opponet pokemon faints. 
# If opponent pokemon faints, they can use potion to revive or switch to another pokemon        
class Trainer:
    def __init__(self, name, pokemons, potions, current_mon):
        self.name = name
        self.pokemons = pokemons[:6] if len(pokemons) > 6 else pokemons
        self.potions = potions
        self.current_mon = current_mon
    def __repr__(self):
        print(f'{self.name} currently has the following pokemons:')
        for pokemon in self.pokemons:
            print(pokemon)
        return f'Current pokemon: {self.current_mon}'    
    def use_potion(self, potion_amount = 10):
        if self.potions > 0:
            if (self.current_mon.max_health - self.current_mon.current_health) > potion_amount:
                print(self.name + ' used a potion!')
                self.current_mon.gain_health(potion_amount)
                self.potions -= 1
                print(self.name + ' now has ' + str(self.potions) + ' potions left.\n')
            else:
                print(self.name + ' used a potion!')
                self.current_mon.current_health = self.current_mon.max_health
                print(self.current_mon.name + ' now has ' + str(self.current_mon.current_health) + ' health.')
                self.potions -= 1
                print(self.name + ' now has ' + str(self.potions) + ' potions left.\n')
        else:
            print(self.name + ' is out of potions!')
    def swap_pokemon(self, pokemon_to_switch):
        pokemon = None
        for i in self.pokemons:
            if i.__repr__()==pokemon_to_switch:
                pokemon = i
                break        
        if pokemon == None:
            print(f'{pokemon_to_switch} is not in your team!')
        elif pokemon.ko:
            print(f'{pokemon_to_switch} has fainited and can''t switch!')
        else:
            self.current_mon = self.pokemons.index(pokemon)
            print(f'{self.name} switched to {pokemon}.')
            
    def trainer_attack(self, other_trainer):
        print(self.current_mon.name + " attacks " + other_trainer.current_mon.name + '!')
        if self.current_mon.current_health != 0:
            self.current_mon.attack(other_trainer.current_mon)
            if other_trainer.current_mon.current_health <= 0:
                other_trainer.current_mon.current_health = 0
                     
                while True:
                    potion = input('Use a potion to revive? (Yes/No)\n')
                    potion = potion.lower()
                    if  potion == 'yes' or potion == 'y':
                        other_trainer.current_mon.revive()
                        other_trainer.potions -= 1
                        break
                    elif potion == 'no' or potion == 'n':
                        print("Switch pokemon!")
                        other_trainer.pokemons.remove(other_trainer.current_mon)
                        print('Which pokemon to switch in?\n'\
                              +'Your options are: \n'\
                              + str(other_trainer.pokemons))
                        pokeswitch = input('Please enter with correct spelling and capitalization: ') 
                        other_trainer.swap_pokemon(pokeswitch)
                        break
                    else:
                        print('Please answer with Yes or No\n')
        else:
            print(str(self.current_mon.name) + ' is knocked out and unable to attack.')




bulbasaur = Pokemon("Bulbasaur", 3, "grass", 15, False)
squirtle = Pokemon("Squirtle", 3, "water", 15, False)
charmander = Pokemon("Charmander", 3, "fire", 15, False)       

Ash = Trainer('Ash', [squirtle, charmander], 4, charmander)
Brock = Trainer('Brock', [bulbasaur, charmander], 6, bulbasaur)



Ash.trainer_attack(Brock)
Brock.trainer_attack(Ash)
Ash.trainer_attack(Brock)
Brock.trainer_attack(Ash)
Ash.trainer_attack(Brock)
Brock.trainer_attack(Ash)
Ash.trainer_attack(Brock) #By here, Brock's bulbasaur faints and you're given the option to revive or swap 