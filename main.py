from components.stat_component import StatComponent
from core.classes.ranger import Ranger
from core.classes.warrior import Warrior
from core.classes.wizard import Wizard


if __name__ == "__main__":
    # Test
    a = Wizard("Zac")
    StatComponent.display_stats(a)
