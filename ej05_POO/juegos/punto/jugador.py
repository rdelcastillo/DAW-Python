from dados import DadoSimple


class JugadorPunto:
    """
    Clase que implementa un jugador para el juego del punto:
    http://www.acanomas.com/Reglamentos-Juegos-de-Dados/042/Punto.htm
    """
    __puntuaciones = (1, 0, 2, 0, 4, 0) # puntuación de cada valor del dado

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__dados = (DadoSimple(), DadoSimple(), DadoSimple())   # necesita tres dados
        self.__puntos = 0

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dados(self):
        return self.__dados

    @property
    def puntos(self):
        return self.__puntos

    def tirada(self):
        """
        Tira los tres dados y acumula la puntuación.
        :return: puntuación obtenida
        """
        p = 0
        for d in self.dados:
            d.tirada()
            p += JugadorPunto.__puntuaciones[d.cara - 1]
        self.__puntos += p
        return p