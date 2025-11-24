import random

class Dice:
    def __init__(self, max_value):
        self.max_value = max_value
        self.min_value = 1

    def roll(self):
        return random.randint(self.min_value, self.max_value)
