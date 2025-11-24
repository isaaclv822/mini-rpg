from utils.dice_factory import DiceFactory

class LevelComponent():
    def __init__(self, _stats: dict):
        self.stats = _stats

    @property
    def data(self):
        return self.stats
    
    def level_up(player):
        if player.hero_class == "Guerrier":
            player.stats.data['level'] = player.stats.data['level'] + 1
            player.stats.data['max_action_point'] = player.stats.data['action_point'] + 2
            player.stats.data['end'] += DiceFactory.roll_dice(3, DiceFactory.dice_3)
            player.stats.data['pow'] += DiceFactory.roll_dice(3, DiceFactory.dice_3)
            player.stats.data['speed'] += DiceFactory.roll_dice(1, DiceFactory.dice_3) 
            player.stats.data['intel'] += DiceFactory.roll_dice(1, DiceFactory.dice_3) 

        elif player.hero_class == "Ranger":
            player.stats.data['level'] = player.stats.data['level'] + 1
            player.stats.data['max_action_point'] = player.stats.data['action_point'] + 2
            player.stats.data['end'] += DiceFactory.roll_dice(2, DiceFactory.dice_3) 
            player.stats.data['pow'] += DiceFactory.roll_dice(2, DiceFactory.dice_3)
            player.stats.data['speed'] += DiceFactory.roll_dice(3, DiceFactory.dice_3) 
            player.stats.data['intel'] += DiceFactory.roll_dice(1, DiceFactory.dice_3)

        else:
            player.stats.data['level'] = player.stats.data['level'] + 1
            player.stats.data['max_action_point'] = player.stats.data['action_point'] + 2
            player.stats.data['end'] += DiceFactory.roll_dice(1, DiceFactory.dice_3) 
            player.stats.data['pow'] += DiceFactory.roll_dice(1, DiceFactory.dice_3)
            player.stats.data['speed'] += DiceFactory.roll_dice(2, DiceFactory.dice_3) 
            player.stats.data['intel'] += DiceFactory.roll_dice(4, DiceFactory.dice_3)
        
        player.stats.data['hp'] = player.stats.data['end']
