from random import randint

class Die :
    """a class to represent a die"""
    def __init__(self,num_sides = 6):
        """assume a sixe_side die"""
        self.sides = num_sides

    def roll(self):
        """return a random value from 1 to num_sides"""
        return randint(1 , self.sides)