"""
Clase para jugar al juego de dados del Punto:

Se hace uso de las clases para los jugadores ya implementados, entre ellas un "jugador tramposo".
Si la variable de entorno PYTHONPATH no está bien puesta no funcionará.
"""

from jugador import Jugador, JugadorTramposo


class PartidaPunto:
    """
    Clase que implementa una partida para el juego del punto:
    http://www.acanomas.com/Reglamentos-Juegos-de-Dados/042/Punto.htm

    Variables de instancia:
        * __jugadores: tupla con objetos de clase Jugador.
        * __turno: turno de la partida (hasta 4).
        * __pausa_en_tirada: Verdadero si queremos que se haga una pausa antes de tirar los dados.
        * __salida: lo que devolverá __str__() que será lo que salga en pantalla.

    Métodos:
        * juega: ejecuta la partida.
        * juega_turno: ejecuta uno de los turnos.
        * juega_turno_jugador: ejecuta la jugada de un jugador en un turno.
        * salida_tirada: lo que debería salir por pantalla en una tirada. Método estático.
        * __pon_en_pantalla: manda a la salida (pantalla) el texto pasado como parámetro.
        * marcador: devuelve el "marcador" final.
        * __puntuacion: devuelve la puntuación de un jugador. Método estático.
    """
    __TURNOS = 4

    def __init__(self, *jugadores):
        """
        Constructor de la clase.
        :param jugadores: lista de objetos de clase Jugador
        """
        self.__jugadores = jugadores
        self.__turno = 0
        self.__pausa_en_tirada = True
        self.__salida = [""] * (PartidaPunto.__TURNOS + 1)

    # propiedades get/set
    @property
    def jugadores(self):
        return self.__jugadores

    @property
    def turno(self):
        return self.__turno

    @property
    def pausa_en_tirada(self):
        return self.__pausa_en_tirada

    @pausa_en_tirada.setter
    def pausa_en_tirada(self, value):
        self.__pausa_en_tirada = value

    # métodos
    def juega(self):
        """
        Ejecuta la partida.
        :return: salida en pantalla.
        """
        # inicio
        self.__pon_en_pantalla("JUEGO DEL PUNTO")
        self.__pon_en_pantalla("---------------\n")
        # turnos
        for t in range(PartidaPunto.__TURNOS):
            self.juega_turno()
        # marcador final
        self.__pon_en_pantalla(self.marcador())
        return self.__str__()

    def juega_turno(self):
        """
        Juega un turno de la partida.
        """
        self.__turno += 1
        self.__pon_en_pantalla(f"Turno {self.turno}")
        self.__pon_en_pantalla("-------")
        for j in self.jugadores:
            self.juega_turno_jugador(j)
        self.__pon_en_pantalla("")

    def juega_turno_jugador(self, j):
        """
        Juega un turno de un jugador.
        :param j: jugador que juega el turno.
        """
        if self.pausa_en_tirada:
            print(f"{j.nombre} pulsa Intro para tirar los dados.", end="")
            input()
        j.haz_tirada()
        self.__pon_en_pantalla(PartidaPunto.salida_tirada(j))

    @staticmethod
    def salida_tirada(j):
        """
        Crea la salida por pantalla del jugador que se pasa como parámetro.
        :param j: jugador.
        :return: cadena que debe mostrarse por la pantalla.
        """
        salida = f"Dados {j.nombre}: "
        for d in j.dados:
            salida += f"{d.cara} "
        salida += f"\tPuntos: {j.puntos_tirada}\tACUMULADO: {j.puntos}"
        if j.tiro_premiado:
            salida += f"\tPREMIADO ({j.tiro_premiado})"
        return salida

    def __pon_en_pantalla(self, salida):
        """
        Manda a la "salida" la cadena enviada como parámetro. Si está activa la pausa en la tirada de dados
        hace una parada antes de la tirada de dados.
        :param salida: lo que debe mandarse a la "salida"
        """
        self.__salida[self.turno] += salida + "\n"
        if self.pausa_en_tirada:
            print(salida)

    def marcador(self):
        """
        Crea la salida por pantalla del marcador final.
        :return: cadena con el marcador que saldrá por la pantalla.
        """
        puesto = 1
        salida = ""
        l = list(self.jugadores)
        # ordenamos jugadores por puntuación
        l.sort(reverse=True, key=PartidaPunto.__puntuacion)
        # marcador
        self.__pon_en_pantalla("MARCADOR FINAL")
        self.__pon_en_pantalla("--------------")
        for j in l:
            salida += f"Puesto: {puesto}. {j.nombre}: {j.puntos} PUNTOS\n"
            puesto += 1
        salida += f"\nGANA: {l[0].nombre}"
        return salida

    @staticmethod
    def __puntuacion(j):
        """
        Devuelve la puntuación acumulada de un jugador. Necesario para ordenar.
        :param j: jugador.
        :return: puntuación.
        """
        return j.puntos

    def __str__(self):
        salida = ""
        for s in self.__salida:
            salida += s
        return salida


if __name__ == '__main__':
    p = PartidaPunto(Jugador("Jugador1"), JugadorTramposo("Tramposo"), Jugador("Jugador2"))
    # p.pausa_en_tirada = False
    # print(p.juega())
    p.juega();
    print(p)
