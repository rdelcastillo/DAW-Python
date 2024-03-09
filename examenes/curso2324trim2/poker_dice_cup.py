"""
Clase que modela un cubilete de dados de póker de manera que tenga una propiedad (score) que devuelva la puntuación
total del cubilete (la suma de la de cada dado).
"""

from typeguard import typechecked
from dice_cup import DiceCup
from poker_dice import PokerDice


@typechecked
class PokerDiceCup(DiceCup):

    def __init__(self, *dices: PokerDice):
        super().__init__(*dices)

    @property
    def score(self):
        score_ = 0
        for d in self.dices:
            score_ += d.score
        return score_
    