from utils.dice import Dice

class DiceFactory:
    # Dés préconfigurés
    dice_3 = Dice(3)
    dice_5 = Dice(5)
    dice_6 = Dice(6)
    dice_8 = Dice(8)
    dice_10 = Dice(10)

    @staticmethod
    def roll_dice(roll_number, dice: Dice):
        result = 0
        for _ in range(roll_number):
            result += dice.roll()
            return result
        