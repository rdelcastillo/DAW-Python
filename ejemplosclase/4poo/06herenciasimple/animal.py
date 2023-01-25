"""
Clase Animal, que será una clase abstracta, base de otras clases para mostrar el funcionamiento de la herencia.

En Python se puede crear una clase abstracta usando la clase abc.ABC y el decorador @abstractmethod para indicar los
métodos abstractos. Las subclases de una clase abstracta deben implementar los métodos marcados como abstractos o de lo
contrario se producirá un error.

No es posible instanciar una clase abstracta, es solo una plantilla para generar otras clases.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.
"""
from typeguard import typechecked
from enum import Enum
from abc import ABC, abstractmethod

Sex = Enum('Sex', 'MACHO HEMBRA')  # tipo enumerado, así el atributo sexo solo podrá tener los valores MACHO o HEMBRA

@typechecked
class Animal(ABC):

    def __init__(self, name: str, sex: Sex = Sex.MACHO):
        self.__name = name
        self.__sex = sex

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex.name

    def __str__(self):
        return f"Nombre: {self.name}, Sexo: {self.sex}\n"

    def sleep(self):
        print(f"({self.name}) Zzzzzzz")

    @abstractmethod  # debe ser implementado obligatoriamente en las clases derivadas
    def eat(self, food: str):
        pass