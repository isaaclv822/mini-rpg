
class StatComponent():
    def __init__(self, initial_stats: dict):
        self.base_stats = initial_stats
    
    @property
    def data(self):
        return self.base_stats
    
    def display_stats(player):
        print('\n' + player.name + ', ' + player.hero_class + ' Lv', player.stats.data['level'])
        print('PV :', player.stats.data['hp'])
        print('Endurance :', player.stats.data['end'])
        print('Force :', player.stats.data['pow'])
        print('Agilité :', player.stats.data['speed'])
        print('Intelligence :', player.stats.data['intel'])
        print('Point d\'action :', player.stats.data['action_point'])
        
