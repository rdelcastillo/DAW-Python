"""
Prueba de la clase PlainCat.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 8/01/2023.
"""
import datetime
from plain_cat import PlainCat

garfield = PlainCat("Garfield", "macho", "siamés", datetime.date(2020, 10, 10))
print("Hola gatito!!!")
garfield.meow()
print("Toma tarta.")
garfield.eat("tarta selva negra")
print("Toma pescado, a ver si esto te gusta.")
garfield.eat("pescado")

tom = PlainCat("Tom", "macho", "romano")
tom.set_birth_day(datetime.date(2018, 11, 2))
print(f"{tom.get_name()}, toma sopita de verduras.")
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
