# Jordan Leung
# 6/5/2019

from random import randint


class Die():
    """A Class representing a single die"""

    def __init__(self, num_sides=6):
        """assumes a 6 sided die """
        self.num_sides = num_sides

    def roll(self):
        """defines roll method, which returns a random value between 1 and 6, including"""
        return randint(1, self.num_sides)

