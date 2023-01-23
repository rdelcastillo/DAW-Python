"""
Implementamos una clase Punto (Point) con sus atributos x e y (estado). El comportamiento de la clase viene determinado
por su constructor (vacío y con dos parámetros), getters y setters (propiedades) y un método (invert_coordinates()) que
invierte las coordenadas x e y del punto, además la clase debe tener un __str__() para poder imprimir los puntos en
formato '(x,y)' y un __repr__() que nos devuelve la forma canónica del objeto.

Usamos el decorador @typechecked para evitar que se puedan pasar a los métodos parámetros de tipo incorrecto. Se puede
aplicar a la clase, y comprobará el tipo de todos los métodos anotados (salvo clases internas) o a los métodos de forma
individual.

Autor: Rafael del Castillo Gomariz.
Fecha: 15/1/2023.
"""
from typeguard import typechecked

@typechecked
class Point:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value: int):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value: int):
        self.__y = value

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __repr__(self):
        return f"Point({self.__x}, {self.__y})"

    def invert_coordinates(self):
        self.__x, self.__y = self.__y, self.__x