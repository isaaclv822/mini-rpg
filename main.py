from components.level_component import LevelComponent
from components.stat_component import StatComponent
from core.classes.ranger import Ranger
from core.classes.warrior import Warrior
from core.classes.wizard import Wizard
from utils.dice_factory import DiceFactory


if __name__ == "__main__":
    # Test
    a = Wizard("Zac")
    StatComponent.display_stats(a)
    LevelComponent.level_up(a)
    StatComponent.display_stats(a)
