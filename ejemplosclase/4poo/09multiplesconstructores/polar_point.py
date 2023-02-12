"""
Clase Punto Polar.

Ejemplo de como proporcionar múltiples constructores usando métodos de clase, en este caso, además de construir un punto
polar dando la distancia desde el eje de coordenadas y el ángulo, usamos también coordenadas cartesianas.

Fuente: https://realpython.com/python-multiple-constructors/
"""
import math
from typeguard import typechecked

@typechecked
class PolarPoint:
    def __init__(self, distance: float, angle: float):
        self.distance = distance
        self.angle = angle

    @classmethod
    def from_cartesian(cls, x: int, y: int):
        distance = math.dist((0, 0), (x, y))
        angle = math.degrees(math.atan2(y, x))
        return cls(distance, angle)

    def __repr__(self):
        return f"{self.__class__.__name__}(distance={self.distance:.2f}, angle={self.angle:.2f})"


if __name__ == '__main__':
    p1 = PolarPoint(13, 22.6)
    print(f"Punto 1: {p1}")

    p2 = PolarPoint.from_cartesian(12, 5)
    print(f"Punto 2: {p1}")