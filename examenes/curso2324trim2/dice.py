"""
Clase que modela un dado de manera que:

- El constructor recibe los valores de las caras que tiene el dado. Ejemplo:
    * dice1 = Dice(1, 2, 3, 4, 5, 6)
    * dice2 = Dice(‘A’, ‘K’, ’Q’, ‘J’, ‘R’, ‘N’)
- Los valores de las caras los obtendremos mediante una propiedad (sides).
- Dispondremos de un método para tirar el dado (roll) que devolverá el resultado (uno de los valores anteriores), además
  actualizará una variable de instancia privada (side) que podrá consultarse mediante una propiedad.
- Los métodos mágicos __str__() y __repr__() deben estar creados.
- Podemos usar los operadores == y != para comparar dos dados.
"""

from __future__ import annotations
from typeguard import typechecked
import random

@typechecked
class Dice:

    def __init__(self, *sides):
        self.__sides = sides
        self.__side = None
        self.roll()

    @property
    def side(self):
        return self.__side

    @property
    def sides(self):
        return self.__sides

    def roll(self):
        self.__side = random.choice(self.__sides)
        return self.__side

    def __str__(self):
        return f"|{self.__side}|"

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__sides}"

    def __eq__(self, other: Dice):
        return self.side == other.side

    def __ne__(self, other: Dice):
        return self.side != other.side
