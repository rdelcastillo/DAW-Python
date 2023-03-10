"""
Ejemplo de excepciones personalizadas.

Autor: Rafael del Castillo Gomariz.
"""

class PointTypeError(TypeError):

    def __init__(self, x, y):
        super().__init__(f"Los parámetros de un punto deben ser enteros, recibido x={x}, y={y}")
        self.x = x
        self.y = y


class Point:

    def __init__(self, x, y):
        if not isinstance(x, int) or not isinstance(y, int):
            raise PointTypeError(x, y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"
