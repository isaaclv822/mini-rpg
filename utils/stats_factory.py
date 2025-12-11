from utils.dice_factory import DiceFactory

class StatsFactory():
    def __init__(self, player_class: str):
        self.player_class = player_class
        self.stats = {}
    
    def generate_for(player_class: str):
        if player_class == "Guerrier":
            stats = {
                "level" : 1,
                "action_point" : 10,
                "max_action_point" : 0,
                "end" : 12 + DiceFactory.roll_dice(3, DiceFactory.dice_5),
                "pow" : 5 + DiceFactory.roll_dice(3, DiceFactory.dice_5),
                "speed" : 3 + DiceFactory.roll_dice(1, DiceFactory.dice_6),
                "intel" : DiceFactory.roll_dice(1, DiceFactory.dice_10),
            }

        elif player_class == "Ranger":
            stats = {
                "level" : 1,
                "action_point" : 10,
                "max_action_point" : 0,
                "end" : 10 + DiceFactory.roll_dice(2, DiceFactory.dice_5),
                "pow" : 5 + DiceFactory.roll_dice(2, DiceFactory.dice_5),
                "speed" : 6 + DiceFactory.roll_dice(2, DiceFactory.dice_8),
                "intel" : DiceFactory.roll_dice(1, DiceFactory.dice_10),
            }

        elif player_class == "Mage":
            stats = {
                "level" : 1,
                "action_point" : 10,
                "max_action_point" : 0,
                "end" : 10 + DiceFactory.roll_dice(1, DiceFactory.dice_5),
                "pow" : 2 + DiceFactory.roll_dice(1, DiceFactory.dice_5),
                "speed" : 4 + DiceFactory.roll_dice(1, DiceFactory.dice_8),
                "intel" : 6 + DiceFactory.roll_dice(4, DiceFactory.dice_5),
            }
        
        stats["hp"] = stats.get("end")

        return stats
        
