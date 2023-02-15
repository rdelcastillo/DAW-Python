"""
Implementamos una clase Punto (Point) con sus atributos x e y (estado) e inmutable.

Como usamos clases de datos no necesitamos implementar su constructor ni otros métodos mágicos como __repr()__, además
indicamos que los objetos de esta clase son inmutables (con frozen=True), así que no tenemos necesidad de poner los
atributos privados ni crear getters.

Autor: Rafael del Castillo Gomariz.
"""
from dataclasses import dataclass
from typeguard import typechecked

@typechecked
@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0


if __name__ == '__main__':
    p1 = Point()
    p2 = Point(3, 5)
    print(f"El punto 1 es de {p1} y el punto 2 es {p2}")
    print(f"Las coordenadas x e y de {p1} son {p1.x, p1.y}")