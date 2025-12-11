
from components.stat_component import StatComponent
from utils.dice_factory import DiceFactory


class CombatComponent():
    def __init__(self, bonus, damage, roll_init, action_cost):
        self.bonus = bonus
        self.damage = damage
        self.roll_init = roll_init
        self.action_cost = action_cost
    
    def normal_attack(attacker, target):
        bonus = 0
        damage = 0
        roll_init = 5
        action_cost = 1

        try:
            attacker._stats.data['action_point'] -= action_cost
            roll = DiceFactory.roll_dice(1, DiceFactory.dice_10)
            print(f'{attacker.name} effectue \"Attaque au poing\"')
            print(f'Lancer d\'un dé de 10: {roll}')

            bonus = int( (attacker._stats.data['speed'] / 10) - (target._stats.data['speed'] / 10) )
            roll_init -= bonus 

            if roll_init >= roll:
                print('Miss ! Cible manquée')
            elif roll == 10:
                damage = int( (attacker._stats.data['pow'] * (1 - (target._stats.data['end'] / (attacker._stats.data['pow'] + target._stats.data['end'])))) * 3 ) 
                target._stats.data['hp'] -= damage
                print(f'Crit ! {damage} point(s) de dégâts infligés')
            else:
                damage = int( (attacker._stats.data['pow'] * (1 - (target._stats.data['end'] / (attacker._stats.data['pow'] + target._stats.data['end'])))) ) 
                target._stats.data['hp'] -= damage
                print(f'{damage} point(s) de dégâts infligés')

        except ValueError:
            print('Une erreur est survenue')

    # Dans le projet initial, cette atk est liée à l'arme équipée sur le Mage
    def magic_attack(attacker, target):
        bonus = 0
        damage = 0
        roll_init = 5
        action_cost = 2

        try:
            attacker._stats.data['action_point'] -= action_cost
            roll = DiceFactory.roll_dice(1, DiceFactory.dice_10)
            print(f'{attacker.name} effectue \"Attaque au poing\"')
            print(f'Lancer d\'un dé de 10: {roll}')

            bonus = int( (attacker._stats.data['speed'] / 10) - (target._stats.data['speed'] / 10) )
            roll_init -= bonus 

            if roll_init >= roll:
                print('Miss ! Cible manquée')
            elif roll == 10:
                damage = int( (attacker._stats.data['intel'] * (1 - (target._stats.data['end'] / (attacker._stats.data['intel'] + target._stats.data['end'])))) * 3 ) 
                target._stats.data['hp'] -= damage
                print(f'Crit ! {damage} point(s) de dégâts infligés')
            else:
                damage = int( (attacker._stats.data['intel'] * (1 - (target._stats.data['end'] / (attacker._stats.data['intel'] + target._stats.data['end'])))) ) 
                target._stats.data['hp'] -= damage
                print(f'{damage} point(s) de dégâts infligés')

        except ValueError:
            print('Une erreur est survenue')

    def weapon_attack(attacker, target):
        pass

    def no_AP_attack(attacker, target):
        damage = 0

        try:
            roll = DiceFactory.roll_dice(1, DiceFactory.dice_2)
            print(f'{attacker.name} effectue \"Lancer de pierre\"')
            print(f'Lancer d\'un dé de 2: {roll}')

            if roll == 1:
                print('Miss ! Cible manquée')
                attacker._stats.data['hp'] -= 1
                print(f'Vous perdez un 1 point de PV: {attacker._stats.data['hp']}(-1)')
            else:
                damage = int(attacker._stats.data['pow'] / 5)
                target._stats.data['hp'] -= damage
                print(f'{damage} point(s) de dégâts infligés')

                attacker._stats.data['hp'] -= 1
                print(f'Vous perdez un 1 point de PV: {attacker._stats.data['hp']}(-1)')

        except ValueError:
            print('Une erreur est survenue')