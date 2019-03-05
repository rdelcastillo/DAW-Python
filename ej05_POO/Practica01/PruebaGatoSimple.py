"""
Programa que prueba la clase GatoSimple
"""

from Practica01.GatoSimple import GatoSimple

garfield = GatoSimple("macho")

print("hola gatito")
garfield.maulla()
print("toma tarta")
garfield.come("tarta selva negra")
print("toma pescado, a ver si esto te gusta")
garfield.come("pescado")

tom = GatoSimple("macho")

print("Tom, toma sopita de verduras")
tom.come("sopa de verduras")

lisa = GatoSimple("hembra")

print("gatitos, a ver cómo maulláis")
garfield.maulla()
tom.maulla()
lisa.maulla()

garfield.peleaCon(lisa)
lisa.peleaCon(tom)
tom.peleaCon(garfield)
