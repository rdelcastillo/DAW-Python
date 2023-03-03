"""
Clase Abstracta Vehicle.

Dispone de los atributos de clase vehicles_created y total_kilometers, y del atributo de instancia kilometers_traveled.

Tiene un método para viajar (travel) que incrementa los kilómetros recorridos.

Autor: Rafael del Castillo Gomariz.
"""
from abc import ABC
from typeguard import typechecked


@typechecked
class Vehicle(ABC):
    __vehicles_created = 0
    __total_kilometers = 0

    def __init__(self):
        self.__kilometers_traveled = 0
        Vehicle.__vehicles_created += 1

    def travel(self, kilometers_traveled: int):
        if kilometers_traveled < 0:
            raise ValueError("Los kilómetros a recorrer no pueden ser negativos.")
        self.__kilometers_traveled += kilometers_traveled
        Vehicle.__total_kilometers += kilometers_traveled

    @property
    def kilometers_traveled(self):
        return self.__kilometers_traveled

    @classmethod
    def total_kilometers(cls):
        return cls.__total_kilometers

    @classmethod
    def vehicles_created(cls):
        return cls.__vehicles_created

    def __repr__(self):
        return f"{self.__class__.__name__} [kilometers_traveled={self.__kilometers_traveled}]"