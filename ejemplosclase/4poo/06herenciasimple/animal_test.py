"""
Programa que prueba la clase Animal y sus subclases.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.
"""
from animal import Sex
from cat import Cat
from bird import Bird
from penguin import Penguin
from dog import Dog

garfield = Cat("Garfield", Sex.MACHO, "romano")
tom = Cat("Tom", Sex.MACHO)
lisa = Cat("Lisa", Sex.HEMBRA)
silvestre = Cat("Silvestre")
lorito = Bird("Mi Loro")
pingu = Penguin("Pingu", Sex.HEMBRA)
perrito = Dog("Perrito")

print(garfield)
print(tom)
print(lisa)
print(silvestre)
print(lorito)
print(pingu)
print(perrito)

lorito.wash_yourself()
lorito.flight()

pingu.wash_yourself()
pingu.flight()

perrito.eat("Huesos")
perrito.play("Pelotas")