"""
Clase que modela un cubilete de dados de póker de manera que tenga una propiedad (score) que devuelva la puntuación
total del cubilete (la suma de la de cada dado).

Bonus: sobrecargamos los operadores relaciones para comparar puntuaciones de cubiletes.
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

    def add(self, dice: PokerDice):  # para evitar añadir dados que no sean de póker
        super().add(dice)

    def __lt__(self, other: PokerDice):
        return self.score < other.score

    def __le__(self, other: PokerDice):
        return self.score <= other.score

    def __gt__(self, other: PokerDice):
        return self.score > other.score

    def __ge__(self, other: PokerDice):
        return self.score >= other.score

    def __eq__(self, other: PokerDice):
        return self.score == other.score

    def __ne__(self, other: PokerDice):
        return self.score != other.score
