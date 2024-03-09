"""
Clase que modela un dado de parchís.
Un dado de parchís tiene seis caras que van del 1 al 6 (valores enteros).
En esta clase tendremos la posibilidad de comparar dados entre sí con los operadores relaciones <, <=, > y >=.
"""

from __future__ import annotations
from  typeguard import typechecked
from dice import Dice

@typechecked
class LudoDice(Dice):

    def __init__(self):
        super().__init__(1,2,3,4,5,6)

    def __lt__(self, other: LudoDice):
        return self.side < other.side

    def __le__(self, other: LudoDice):
        return self.side <= other.side

    def __gt__(self, other: LudoDice):
        return self.side > other.side

    def __ge__(self, other: LudoDice):
        return self.side >= other.side
