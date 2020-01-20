"""
Clases para jugadores del juego de dados del Punto:

* Jugador: jugador normal.
* Jugador tramposo.

Se hace uso de las clases para los dados ya implementados, si la variable de entorno PYTHONPATH
no está bien puesta no funcionará.
"""

from dados import DadoSimple
from dado import Dado


class Jugador:
    """
    Clase que implementa un jugador para el juego del punto:
    http://www.acanomas.com/Reglamentos-Juegos-de-Dados/042/Punto.htm

    Variables de instancia:
        * __nombre: nombre del jugador.
        * __dados: tupla con tres objetos de tipo DadoSimple.
        * __puntos: puntuación acumulada.
        * __puntos_tirada: puntuación tirada actual.
        * __tiro_premiado: 0 si no hay premio y valor del dado repetido (2, 4 ó 6) si lo hay.

    Métodos:
        * tirar.
        * __tira_dados (el método anterior hace uso de este).
        * inicializa_marcador
    """
    __puntuaciones = (1, 0, 2, 0, 4, 0)  # puntuación de cada valor del dado

    def __init__(self, nombre):
        self.__nombre = nombre
        self.__dados = (DadoSimple(), DadoSimple(), DadoSimple())  # necesita tres dados
        self.__puntos = 0
        self.__puntos_tirada = 0
        self.__tiro_premiado = 0  # si es tiro premiado guardaremos 2, 4 ó 6 (dado repetido)

    @property
    def nombre(self):
        return self.__nombre

    @property
    def dados(self):
        return self.__dados

    @property
    def tiro_premiado(self):
        return self.__tiro_premiado

    @property
    def puntos(self):
        return self.__puntos

    @property
    def puntos_tirada(self):
        return self.__puntos_tirada

    def haz_tirada(self):
        """
        Tira los tres dados y acumula la puntuación.
        :return: puntuación obtenida
        """
        self.__tiro_premiado = 0    # si había premio en la tirada anterior se anula
        p = self.__tira_dados()     # tiramos los dados y recogemos puntuación
        # ¿es tiro premiado?
        d1, d2, d3 = self.dados[0].cara, self.dados[1].cara, self.dados[2].cara
        if (d1 == d2 == d3) and d1 in (2, 4, 6):    # si se cumple es un tiro premiado
            self.__tiro_premiado = d1
            p = 2 * self.__tira_dados()             # tiramos de nuevo y puntuamos doble
        # acumulamos puntuación y devolvemos la obtenida en la tirada
        self.__puntos += p
        self.__puntos_tirada = p
        return p

    def __tira_dados(self):
        """
        Tira los dados del jugador.
        :return: puntuación de la tirada
        """
        p = 0
        for d in self.dados:
            d.tirada()
            p += Jugador.__puntuaciones[d.cara - 1]
        return p

    def inicializa_marcador(self):
        self.__puntos = 0


class JugadorTramposo(Jugador):
    """
    Jugador del juego del punto que usa dados trucados.
    """
    __valores_dado = (1, 1, 2, 3, 3, 3, 4, 5, 5, 5, 5, 6)  # más probabilidad para 5, 3 y 1

    def __init__(self, nombre):
        """
        Constructor de JugadorTramposo.
        Creamos nuestros propios dados, que serán trucados.
        :param nombre: nombre del jugador.
        """
        super().__init__(nombre)
        caras = JugadorTramposo.__valores_dado
        self.__dados_trucados = (Dado(*caras), Dado(*caras), Dado(*caras))

    @property
    def dados(self):
        """
        Redefinimos la propiedad de la clase de la que hereda para que devuelva los dados trucados.
        :return: dados trucados.
        """
        return self.__dados_trucados


if __name__ == "__main__":
    j1 = Jugador("Honrado")
    j2 = JugadorTramposo("Tramposo")
    # Tiramos cuatro rondas
    for i in range(4):
        print("RONDA", i + 1)
        print(".......")
        for j in j1, j2:
            print(f"Tirada {j.nombre}: {j.haz_tirada()} puntos.")
            if j.tiro_premiado:
                print("Este tirada tiene PREMIO:", j.tiro_premiado)
            print("Dados: ", end="")
            for d in j.dados:
                print(d.cara, end=" ")
            print()
            print(f"Puntuación acumulada: {j.puntos}")
            print("---")
        print("")
    # Ganador
    if j1.puntos > j2.puntos:
        g = j1
    else:
        g = j2
    print("GANADOR:", g.nombre)