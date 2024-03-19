"""
Clase que modela un dado de póker de manera que:

- Los posibles valores del dado son ‘A’, ‘K’, ’Q’, ‘J’, ‘R’ y ‘N’.
- El dado tiene una propiedad (score) que nos da la puntuación del dado (6, 5, 4, 3, 2, 1).
"""

from dice import Dice

class PokerDice(Dice):
    __SCORES = {'A':6, 'K':5, 'Q':4, 'J':3, 'R':2, 'N':1}

    def __init__(self):
        super().__init__(*self.__SCORES.keys())

    @property
    def score(self):
        return self.__SCORES[self.side]
