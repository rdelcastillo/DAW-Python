"""
Clase Pingüino derivada de Ave. Los pingüinos no vuelan.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.
"""
from bird import Bird

class Penguin(Bird):

    def flight(self):
        print(f"({self.name}) ¡No puedo volar! :-(")
