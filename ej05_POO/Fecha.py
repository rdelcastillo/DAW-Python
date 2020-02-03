"""
Implementamos la clase Fecha basándonos en:

https://github.com/rdelcastillo/DAW-Python/blob/master/Examenes/2019-20_trimestre1/tiempo/fecha.py
"""


class Fecha:
    def __init__(self, dia, mes, anyo):
        assert Fecha.es_correcta(dia, mes, anyo)
        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo

    # Propiedades
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        assert Fecha.es_correcta(value, self.__mes, self.__anyo)
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        assert Fecha.es_correcta(self.__dia, value, self.__anyo)
        self.__mes = value

    @property
    def anyo(self):
        return self.__anyo

    @anyo.setter
    def anyo(self, value):
        assert Fecha.es_correcta(self.__dia, self.__mes, value)
        self.__anyo = value

    # Sobrecarga

    def __str__(self):
        pass

    # Métodos estáticos

    @staticmethod
    def es_bisiesto(anyo):
        return anyo % 400 == 0 or (anyo % 4 == 0 and anyo % 100 != 0)

    @staticmethod
    def es_correcta(dia, mes, anyo):
        # tipo de dato correcto
        if not isinstance(dia, int) or not isinstance(mes, int) or not isinstance(anyo, int):
            return False
        # año correcto
        if anyo < 0:
            return False
        # mes correcto
        if mes < 1 or mes > 12:
            return False
        # día correcto
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(anyo):
            dias_mes[1] = 29
        return 0 < dia <= dias_mes[mes - 1]
