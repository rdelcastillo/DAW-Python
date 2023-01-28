"""
Interfaz Mascota.

Nuestras mascotas juegan con el juguete que le demos y nos dan besitos.

Todas las clases que implementen (hereden) esta interfaz deberán crear los métodos definidos aquí.

Autor: Rafael del Castillo.
"""
from abc import ABC, abstractmethod
from typeguard import typechecked

@typechecked
class Pet(ABC):

    @abstractmethod
    def play(self, toy: str):
        pass

    @abstractmethod
    def kiss(self):
        pass