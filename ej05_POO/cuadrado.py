from rectangulo import Rectangulo

class Cuadrado(Rectangulo):
    """
    Implementamos la clase Cuadrado partiendo de la clase Rectángulo.
    Consideraremos que un cuadrado es un rectángulo con base==altura.
    """
    def __init__(self, lado):
        super().__init__(lado, lado)

    @property
    def lado(self):
        return self.base

    @lado.setter
    def lado(self, value):
        self.base = value
        self.altura = value