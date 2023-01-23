"""
Clase "Rectángulo" determinada por dos puntos (clase Point). Tiene como propiedades su área y su perímetro.

Autor: Rafael del Castillo Gomariz.
Fecha: 22/1/2023.
"""
from ej02point import Point
from typeguard import typechecked

@typechecked
class Rectangle:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

    @property
    def p1(self):
        return self.__p1

    @p1.setter
    def p1(self, value: Point):
        self.__p1 = value

    @property
    def p2(self):
        return self.__p2

    @p2.setter
    def p2(self, value: Point):
        self.__p2 = value

    @property
    def area(self):
        return abs((self.p1.x - self.p2.x) * (self.p1.y - self.p2.y))

    @property
    def perimeter(self):
        return 2 * abs(self.p1.x - self.p2.x) + 2 * abs(self.p1.y - self.p2.y)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.p1}, {self.p2})"