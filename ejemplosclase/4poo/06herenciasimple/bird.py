"""
Clase Ave derivada de Animal. Además de los comportamientos definidos para los animales, las aves se asearán y volarán.

Al tener la clase Animal el método eat() como abstracto es obligatorio implementarlo.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.
"""
from typeguard import typechecked
from animal import Animal

@typechecked
class Bird(Animal):

    def eat(self, food: str):
        """
        Nuestras aves comen lo que les demos.
        """
        print(f"({self.name}) Hmmmm, gracias :-)")

    def wash_yourself(self):
        print(f"({self.name}) Me estoy limpiando las plumas ;-)")

    def flight(self):
        print(f"({self.name}) ¡Estoy volando!")