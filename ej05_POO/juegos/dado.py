"""
Ejemplo de POO. Clase Dado versión 2.

Cambios:
* En vez de pasar una lista al dado le pasamos los valores de las caras como parámetros.
* Ocultamos el atributo "cara" del dado y accedemos a él a través de una propiedad para que no pueda ser cambiado.

Autor: Rafael del Castillo.
"""
import random


class Dado:
    """
    Esta clase simula el comportamiento de un dado.
    """
    def __init__(self, *valores):
        """
        Crea el objeto que simula un dado.
        :param valores: lista de valores de las caras del dado.
        """
        self.__caras = valores[:]
        self.__cara = random.choice(self.__caras)

    @property
    def cara(self):
        """
        Similar getter de Java, pero con una filosofía 'pythonica'.
        En Python se prefiere acceder a los atributos directamente, si son ocultos se hace con una propiedad.
        """
        return self.__cara

    def tirada(self):
        """
        Simula la tirada del dado.
        :return: valor del dado.
        """
        self.__cara = random.choice(self.__caras)
        return self.__cara


if __name__ == "__main__":
    d = Dado(1,2,3,4,5,6)
    print("Tiramos dado 5 veces: ", end="")
    for i in range(5):
        d.tirada()
        print(d.cara, end=" ")
    print("\nTiramos dado 5 veces: ", end="")
    for i in range(5):
        print(d.tirada(), end=" ")