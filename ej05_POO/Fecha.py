"""
Implementamos la clase Fecha basándonos en:

https://github.com/rdelcastillo/DAW-Python/blob/master/Examenes/2019-20_trimestre1/tiempo/fecha.py
"""


class FechaErronea(Exception):
    def __init__(self, mensaje_error):
        Exception.__init__(self)
        self.mensaje_error = mensaje_error


class Fecha:
    def __init__(self, dia, mes, anyo):
        if not Fecha.es_correcta(dia, mes, anyo):
            raise FechaErronea("Día, mes o año erróneo al construir la fecha")
        self.__dia = dia
        self.__mes = mes
        self.__anyo = anyo

    # Propiedades
    @property
    def dia(self):
        return self.__dia

    @dia.setter
    def dia(self, value):
        if not Fecha.es_correcta(value, self.__mes, self.__anyo):
            raise FechaErronea(f"Día asignado {value} incorrecto")
        self.__dia = value

    @property
    def mes(self):
        return self.__mes

    @mes.setter
    def mes(self, value):
        if not Fecha.es_correcta(self.__dia, value, self.__anyo):
            raise FechaErronea(f"Mes asignado {value} incorrecto")
        self.__mes = value

    @property
    def anyo(self):
        return self.__anyo

    @anyo.setter
    def anyo(self, value):
        if not Fecha.es_correcta(self.__dia, self.__mes, value):
            raise FechaErronea(f"Año asignado {value} incorrecto")
        self.__anyo = value

    # Métodos

    def __suma_1dia(self):
        """
        :return: Fecha almacenada + 1 día
        """
        dia = self.__dia + 1
        mes = self.__mes
        anyo = self.__anyo
        if dia > Fecha.dias_mes(mes, anyo):
            # mes siguiente
            dia = 1
            mes += 1
            if mes > 12:  # nos pasamos de diciembre, año siguiente
                mes = 1
                anyo += 1
        return Fecha(dia, mes, anyo)

    def __resta_1dia(self):
        """
        :return: Fecha almacenada - 1 día
        """
        dia = self.__dia - 1
        mes = self.__mes
        anyo = self.__anyo
        if dia == 0:
            # mes anterior
            mes -= 1
            if mes == 0:  # nos vamos al año anterior
                mes = 12
                anyo -= 1
                assert anyo >= 0  # si el año es negativo la fecha es errónea
            dia = Fecha.dias_mes(mes, anyo)
        return Fecha(dia, mes, anyo)

    def nombre_mes(self):
        meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        return meses[self.mes - 1]

    def clona(self):
        """
        :return: devuelve una copia de self
        """
        return Fecha(self.__dia, self.__mes, self.__anyo)

    # Sobrecarga

    def __str__(self):
        return f"{self.__dia} de {self.nombre_mes()} de {self.__anyo}"

    def __add__(self, n):
        f = self.clona()
        if n > 0:
            for i in range(n):
                f = f.__suma_1dia()
        else:
            for i in range(abs(n)):
                f = f.__resta_1dia()
        return f

    def __sub__(self, n):
        return self + -1 * n

    def __radd__(self, n):
        return self + n  # también vale "return self.__add__(n)"

    def __gt__(self, other):
        if self.__anyo != other.anyo:
            return self.__anyo > other.anyo
        elif self.__mes != other.mes:
            return self.__mes > other.mes
        else:
            return self.__dia > other.dia

    def __ge__(self, other):
        if self.__anyo != other.anyo:
            return self.__anyo >= other.anyo
        elif self.__mes != other.mes:
            return self.__mes >= other.mes
        else:
            return self.__dia >= other.dia

    def __eq__(self, other):
        return (self.__dia == other.dia) and (self.__mes == other.mes) and (self.__anyo == other.anyo)

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
        return 0 < dia <= Fecha.dias_mes(mes, anyo)

    @staticmethod
    def dias_mes(mes, anyo):
        """
        :return: Días del mes actual
        """
        dias_mes_ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Fecha.es_bisiesto(anyo):
            dias_mes_[1] = 29
        return dias_mes_[mes - 1]
