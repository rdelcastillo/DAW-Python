"""
Clase Punto Polar.

Ejemplo, usando clases de datos, de como proporcionar múltiples constructores usando métodos de clase, en este caso,
además de construir un punto polar dando la distancia desde el eje de coordenadas y el ángulo, usamos también
coordenadas cartesianas.

Autor: Rafael del Castillo Gomariz
"""
import math
from dataclasses import dataclass
from typeguard import typechecked

@typechecked
@dataclass
class PolarPoint:
    distance: float
    angle: float

    @classmethod
    def from_cartesian(cls, x: int, y: int):
        distance = math.dist((0, 0), (x, y))
        angle = math.degrees(math.atan2(y, x))
        return cls(distance, angle)


if __name__ == '__main__':
    p1 = PolarPoint(13, 22.6)
    print(f"Punto 1: {p1}")

    p2 = PolarPoint.from_cartesian(12, 5)
    print(f"Punto 2: {p1}")