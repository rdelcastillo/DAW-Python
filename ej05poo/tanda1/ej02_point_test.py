"""
Prueba de la clase "Punto".

Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el método __str__(), imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto.
"""
from ej02_point import Point

p = Point(3,5)
print(f"La coordenada x de {p} es {p.x}")
p.x = 0
print("Punto modificado:", p)
