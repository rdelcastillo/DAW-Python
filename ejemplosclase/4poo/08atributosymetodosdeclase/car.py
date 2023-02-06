"""
Clase Coche. Uso de métodos y variables de clase.

Autor: Rafael del Castillo Gomariz.
"""
from typeguard import typechecked

@typechecked
class Car:
    __total_mileage = 0

    @classmethod
    def total_mileage(cls):
        return cls.__total_mileage

    def __init__(self, registration: str):
        self.__registration = registration
        self.__mileage = 0

    @property
    def registration(self):
        return self.__registration

    @property
    def mileage(self):
        return self.__mileage

    def travel(self, distance: int):
        if distance < 0:
            raise ValueError("La distancia recorrida por el coche no puede ser negativa.")
        self.__mileage += distance
        Car.__total_mileage += distance  # no puedo usar self aquí

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__registration, self.__mileage})"

    def __del__(self):  # destructor, si un objeto desaparece restamos del total sus kilómetros recorridos
        Car.__total_mileage -= self.__mileage