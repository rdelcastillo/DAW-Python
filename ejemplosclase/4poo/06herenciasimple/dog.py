"""
Clase Perro que implementará la interfaz Mascota.

Autor: Rafael del Castillo.
"""
from enum import Enum
from typeguard import typechecked
from animal import Animal, Sex
from pet import Pet

Size = Enum("Size", "PEQUEÑO MEDIANO GRANDE")

@typechecked
class Dog(Animal, Pet):

    def __init__(self, name: str, size: Size = Size.MEDIANO, sex: Sex = Sex.MACHO):
        super().__init__(name, sex)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value: Size):
        self.__size = value

    def eat(self, food: str):
        print(f"({self.name}) ¡Guau! ¡Me encanta comer {food}! :-)")

    def play(self, toy: str):
        print(f"({self.name}) ¿{toy}? ¡Me encanta jugar! ¡Guau guau! :-)")

    def kiss(self):
        print(f"({self.name}) Muá ;-)")

    def __str__(self):
        return super().__str__() + "Tamaño: " + self.size.name + "\n"