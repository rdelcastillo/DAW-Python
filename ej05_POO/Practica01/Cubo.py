"""
Implementación en Python la clase Cubo del libro 'Aprende Java con Ejercicios'
"""


class Cubo():

    def __init__(self, c):
        self.__capacidad = c  # capacidad máxima en litros
        self.contenido = 0  # contenido actual en litros

    @property
    def capacidad(self):
        return self.__capacidad

    def vacia(self):
        """Vacía el cubo"""
        self.contenido = 0

    def llena(self):
        """Llena el cubo al máximo de su capacidad"""
        self.contenido = self.__capacidad

    def pinta(self):
        """
        Pinta el cubo en la pantalla.
        Se muestran los bordes del cubo con el carácter # y el
        agua que contiene con el carácter ~.
        """
        for nivel in range(self.__capacidad, 0, -1):
            if self.contenido >= nivel:
                print("#~~~~#")
            else:
                print("#    #")
        print("######")

    def vuelca_en(self, destino):
        """
        Vuelca el contenido de un cubo sobre otro.
        Antes de echar el agua se comprueba cuánto le cabe al cubo destino.
        """
        libres = destino.capacidad - destino.contenido
        if libres > 0:
            if self.contenido <= libres:
                destino.contenido += self.contenido
                self.vacia()
            else:
                self.contenido -= libres
                destino.llena()


# Prueba clase

if __name__ == "__main__":
    cubito = Cubo(2)
    cubote = Cubo(7)
    print("Cubito: \n")
    cubito.pinta()

    print("\nCubote: \n")
    cubote.pinta()

    print("\nLleno el cubito: \n")
    cubito.llena()
    cubito.pinta()

    print("\nEl cubote sigue vacío: \n")
    cubote.pinta()

    print("\nAhora vuelco lo que tiene el cubito en el cubote.\n")
    cubito.vuelca_en(cubote)

    print("Cubito: \n")
    cubito.pinta()

    print("\nCubote: \n")
    cubote.pinta()

    print("\nAhora vuelco lo que tiene el cubote en el cubito.\n")
    cubote.vuelca_en(cubito)

    print("Cubito: \n")
    cubito.pinta()

    print("\nCubote: \n")
    cubote.pinta()
