"""
Prueba de la clase PlainCat.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 8/01/2023.
"""
from plain_cat import PlainCat

garfield = PlainCat("Garfield", "macho")
print("Hola gatito!!!")
garfield.meow()
print("Toma tarta.")
garfield.eat("tarta selva negra")
print("Toma pescado, a ver si esto te gusta.")
garfield.eat("pescado")

tom = PlainCat("Tom", "macho")
print(f"{tom.name}, toma sopita de verduras.")
tom.eat("sopa de verduras")

lisa = PlainCat("Lisa", "hembra")

print("Gatitos, a ver cómo maulláis.")
garfield.meow()
tom.meow()
lisa.meow()

print("Gatitos, echad una pelea sin haceros daño.")
garfield.fight_with(lisa)
lisa.fight_with(tom)
tom.fight_with(garfield)