## Project (Roll Dice)
import random


class Dice:
    def __init__(self):
        self.result = None

    def roll(self):
        self.result = (random.randint(1,6), random.randint(1,6))
        return self.result
        # In Python, if you want to return a tuple (a, b) from a method. You can use return (a, b) or return a, b


dice_roll = Dice()
print(f'{dice_roll.roll()}')
