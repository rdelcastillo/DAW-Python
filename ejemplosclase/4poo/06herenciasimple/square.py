"""
Clase Cuadrado a partir de la clase Rectángulo. Ejemplo de herencia.

Un cuadrado es un rectángulo con el ancho y alto con el mismo valor, para determinarlo solo necesitamos el lado.

Esta herencia no sería adecuada si el rectángulo no fuera inmutable o quisiéramos ocultar las propiedades "ancho" y
"alto", se incumpliría el principio de sustitución de Liskov, que nos dice que si en alguna parte de nuestro código
estamos usando una clase, y esta clase es extendida, tenemos que poder utilizar cualquiera de las clases hijas y que el
programa siga siendo válido.

Autor: Rafael del Castillo Gomariz.
"""
from typeguard import typechecked
from rectangle import Rectangle

@typechecked
class Square(Rectangle):

    def __init__(self, side: int):
        super().__init__(side, side)  # llamamos al constructor de Rectángulo

    @property
    def side(self):
        return self.width  # o self.height

    def __repr__(self):  # redefinimos este método
        return f"{self.__class__.__name__}({self.side})"