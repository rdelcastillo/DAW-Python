"""
Prueba clase "Punto".
"""
from point import Point

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(f"La suma de {p1} y {p2} es {p3}, su resta es {p1 - p2}")
print(f"El punto opuesto a {p1} es {-p1}")