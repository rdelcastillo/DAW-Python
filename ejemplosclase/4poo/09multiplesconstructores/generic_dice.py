"""
Clase Dado Genérico.

Al construir el dado le pasamos los valores de las caras que tiene en formato lista, tupla, cadena o entero.

Usamos 'single-dispatch generic functions' De esta forma podemos agregar varios constructores a la clase y ejecutarlos
de forma selectiva, según el tipo de su primer parámetro.

Definiremos múltiples funciones que implementan la misma operación para diferentes tipos de datos y el propio Python
escogerá la implementación ejecutar en función del tipo del parámetro.

Debemos definir una implementación de método base y decorarla con @singledispatchmethod y escribir implementaciones
alternativas decorándolas con el nombre del método base más .register.
"""

import random
from functools import singledispatchmethod

class GenericDice:
    @singledispatchmethod
    def __init__(self, values):  # caso genérico
        raise ValueError("Parámetro erróneo:", values)

    @__init__.register(list)
    @__init__.register(tuple)
    @__init__.register(str)
    def _(self, values):
        self.sides = tuple(values)

    @__init__.register(int)
    def _(self, values):
        self.sides = tuple([int(side) for side in str(values)])

    def roll(self):
        return random.choice(self.sides)

    def __repr__(self):
        return f"{self.__class__.__name__}{self.sides}"

if __name__ == '__main__':
    d1 = GenericDice(123456)
    d2 = GenericDice([2, 2, 3, 4, 5, 5])
    d3 = GenericDice("NRJQKA")

    for d in (d1, d2, d3):
        print(f"Tirada dado {d} -> {d.roll()}")
