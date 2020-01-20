"""
Resolución del ejercicio:

Crea la clase Tiempo. Los objetos de la clase Tiempo son intervalos de tiempo y se crean
de la forma:

t = Tiempo(1, 20, 30)

donde los parámetros que se le pasan al constructor son las horas, los minutos y los segundos respectivamente.

Crea métodos para:

    Sumar y restar otro objeto de la clase Tiempo.
    Sumar y restar segundos, minutos y/o horas.
    Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5)
    la cadena sea 10h 35m 5s.

Realiza un programa de prueba para comprobar que la clase funciona bien.
"""


class Tiempo:
    """
    Los objetos de la clase Tiempo son intervalos de tiempo y se crean de la
    forma:

    t = Tiempo(1, 20, 30)

    donde los parámetros que se le pasan al constructor son las horas,
    los minutos y los segundos.
    """
    def __init__(self, horas, minutos, segundos):
        """
        Constructor de la clase.
        Lanza una excepción en caso de valores incorrectos.
        :param horas:
        :param minutos:
        :param segundos:
        """
        assert horas>=0 and 0<=minutos<60 and 0<=segundos<60
        # si estamos aquí se cumple lo anterior y los valores son correctos
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    # propiedades

    @property
    def horas(self):
        return self.__horas

    @property
    def minutos(self):
        return self.__minutos

    @property
    def segundos(self):
        return self.__segundos

    # Resto métodos

    def __str__(self):
        return f"{self.horas}h {self.minutos}m {self.segundos}s"

    # sumar y restar horas
    def suma_horas(self, horas):
        """
        Suma horas al objeto. Si el resultado es negativo lanza una excepción.
        :param horas:
        :return:
        """
        assert self.horas + horas >= 0
        self.__horas += horas

    def resta_horas(self, horas):
        """
        Resta horas al objeto. Si el resultado es negativo lanza una excepción.
        :param horas:
        :return:
        """
        assert self.horas - horas >= 0
        self.__horas -= horas
        # self.suma_horas(-horas) # también se puede hacer así

    # sumar y restar minutos

    def suma_minutos(self, minutos):
        """
        Suma minutos al objeto. Si las horas finales son negativas lanza una excepción
        :return:
        """
        seg = Tiempo.__segundos_total(self) + minutos*60
        assert seg >= 0  # si los segundos son negativos el estado es inconsistente
        result = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = result.horas, result.minutos, result.segundos

    def resta_minutos(self, minutos):
        self.suma_minutos(-minutos)

    # sumar y restar segundos

    def suma_segundos(self, segundos):
        """
        Suma segundos al objeto. Si las horas finales son negativas lanza una excepción
        :return:
        """
        seg = Tiempo.__segundos_total(self) + segundos
        assert seg >= 0  # si los segundos son negativos el estado es inconsistente
        result = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = result.horas, result.minutos, result.segundos

    def resta_segundos(self, segundos):
        self.suma_segundos(-segundos)

    # sumar y restar otro objeto tiempo

    def suma(self, t):
        """
        Suma otro objeto tiempo al objeto. Si las horas finales son negativas lanza una excepción
        :return:
        """
        seg = Tiempo.__segundos_total(self) + Tiempo.__segundos_total(t)
        result = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = result.horas, result.minutos, result.segundos

    def resta(self, t):
        """
        Suma otro objeto tiempo al objeto. Si las horas finales son negativas lanza una excepción
        :return:
        """
        seg = Tiempo.__segundos_total(self) - Tiempo.__segundos_total(t)
        assert seg>=0   # si los segundos son negativos el estado es inconsistente
        result = Tiempo.__segundos_a_tiempo(seg)
        self.__horas, self.__minutos, self.__segundos = result.horas, result.minutos, result.segundos

    # Métodos estáticos

    @staticmethod
    def __segundos_total(t):
        return t.horas*3600 + t.minutos*60 + t.segundos

    @staticmethod
    def __segundos_a_tiempo(s):
        horas = s // 3600
        s = s % 3600
        minutos = s // 60
        segundos = s % 60
        return Tiempo(horas, minutos, segundos)


if __name__ == '__main__':
    t1 = Tiempo(10, 10, 10)
    print(f"T1: {t1}")
    h = int(input(f"Horas a sumar a {t1} "))
    t1.suma_horas(h)
    print(f"Ahora T1 es {t1}")
    m = int(input(f"Minutos a sumar a {t1} "))
    t1.suma_minutos(m)
    print(f"Ahora T1 es {t1}")
