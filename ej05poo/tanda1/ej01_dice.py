"""
Clase "Dado" que simula el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de salir.

Autor: Rafael del Castillo Gomariz.
Fecha: 22/1/2023.
"""
import random

NUM_SIDES = 6

class Dice:

    def __init__(self):
        self.__side = 1

    @property
    def side(self):
        return self.__side

    def __str__(self):
        return str(self.__side)

    def roll(self):
        self.__side = random.randint(1, NUM_SIDES)
        return self.__side
