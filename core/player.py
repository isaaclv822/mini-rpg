from abc import ABC
from components.stat_component import StatComponent
from utils.stats_factory import StatsFactory

class Player(ABC):
    def __init__(self, name):
        self._name = name
        self.hero_class: str
        self._weapon_point = 2
        initial_stats = StatsFactory.generate_for(self.hero_class)
        self._stats: dict = StatComponent(initial_stats)

    # Getters and setters
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def stats(self):
        return self._stats
    
    @stats.setter
    def stats(self, new_stats):
        self._stats = new_stats
    
    @property
    def hero_class(self):
        return self.hero_class
    
    @hero_class.setter
    def hero_class(self, new_hero_class):
        self.hero_class = new_hero_class

    @property
    def weapon_point(self):
        return self._weapon_point
    
    @weapon_point.setter
    def weapon_point(self, new_weapon_point):
        self._weapon_point = new_weapon_point