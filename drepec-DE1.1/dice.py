from random import randint

class Dice:
    """
    This is our Dice object that has a set amount of side from 1 to 100.
    This object contains a roll_dice function to return us values after each roll.
    """
    def __init__(self, n_sides):
        self.n_sides = n_sides
        return print(f'Dice has {n_sides} sides')


    def roll_dice(self):
        return randint(1, self.n_sides)
