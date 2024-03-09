"""
Clase que modela un cubilete de dados de manera que:

- Al construirla le pasamos una serie de dados.
    * Ejemplo: cup = DiceCup(LudoDace(), LudoDace(), LudoDace())
- Dispondremos de una propiedad que devuelva los dados (dices) y otra que devuelva el número de dados que contiene.
- Dispondremos de un método para añadir un dado.
- Dispondremos de un método para quitar un dado pasándole el dado concreto que queremos quitar.
- Debe estar creado el método mágico __str__().
"""

from typeguard import typechecked
from dice import Dice


@typechecked
class DiceCup:

    def __init__(self, *dices: Dice):
        self.__dices = list(dices)

    @property
    def dices(self):
        return self.__dices.copy()

    @property
    def size(self):
        return len(self.__dices)

    def add(self, dice: Dice):
        self.__dices.append(dice)

    def remove(self, dice: Dice):
        if dice not in self.__dices:
            raise ValueError(f"El dado {dice} no está en el cubilete")
        self.__dices.remove(dice)

    def __str__(self):
        str_ = "["
        for d in self.__dices:
            str_ += f" {d}"
        str_ += " ]"
        return str_
