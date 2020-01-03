"""
Ejemplo de POO. Clase Dado versión 1.

Autor: Rafael del Castillo.
"""
import random


class Dado():
    """
    Esta clase simula el comportamiento de un dado.
    """
    def __init__(self, valores):
        """
        Crea el objeto que simula un dado.
        :param valores: lista de valores de las caras del dado.
        """
        self.__caras = valores[:]
        self.cara = random.choice(self.__caras)

    def tirada(self):
        """
        Simula la tirada del dado.
        :return: valor del dado.
        """
        self.cara = random.choice(self.__caras)
        return self.cara


if __name__ == "__main__":
    d = Dado([1,2,3,4,5,6])
    print("Tiramos dado 5 veces: ", end="")
    for i in range(5):
        d.tirada()
        print(d.cara, end=" ")
    print("\nTiramos dado 5 veces: ", end="")
    for i in range(5):
        print(d.tirada(), end=" ")