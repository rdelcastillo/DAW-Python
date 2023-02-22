"""
Implementación de una clase Fecha (mutable).

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción ValueError.

Tendremos métodos para:

- Sumar y restar días a la fecha.
- Restar fechas. Devuelve el número de días comprendidos entre ambas.
- Comparar la fecha almacenada con otra.
- Saber si el año de la fecha almacenada es bisiesto.
- Obtener el día de la semana de una fecha concreta.
- El método __str__() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

Autor: Rafael del Castillo Gomariz.
"""
from typing import Optional
from typeguard import typechecked


@typechecked
class Date:

    def __init__(self, day = None, month = None, year = None):
        if isinstance(day, Date) and month is None and year is None:
            date = day
            self.__day, self.__month, self.__year = date.__day, date.__month, date.__year
        elif isinstance(day, int) and isinstance(month, int) and isinstance(year, int):
            if not Date.__is_ok(day, month, year):
                raise ValueError("Día, mes o año erróneo al construir la fecha")
            self.__day, self.__month, self.__year = day, month, year
        else:
            raise TypeError("Parámetros incorrectos para construir una fecha")

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value: int):
        if not Date.__is_ok(value, self.__month, self.__year):
            raise ValueError(f"Día asignado {value} incorrecto")
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value: int):
        if not Date.__is_ok(self.__day, value, self.__year):
            raise ValueError(f"Mes asignado {value} incorrecto")
        self.__month = value

    @property
    def month_name(self):
        month_names = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
                       "Octubre", "Noviembre", "Diciembre")
        return month_names[self.__month - 1]

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value: int):
        if not Date.__is_ok(self.__day, self.__month, value):
            raise ValueError(f"Año asignado {value} incorrecto")
        self.__year = value

    def __str__(self):
        return f"{self.__day} de {self.month_name} de {self.__year}"

    def to_iso_format(self):
        return f"{self.__year:04d}-{self.__month:04d}-{self.__day:04d}"

    def is_leap(self):
        return self.__is_leap(self.year)

    def day_of_week(self):
        first_date = self.__class__(1, 1, 1)  # ese día fue lunes
        total_days = 0
        while first_date != self:
            total_days += 1
            first_date += 1
        return total_days % 7

    def copy(self):
        return self.__class__(self.__day, self.__month, self.__year)

    def __add__(self, value: int):
        if value < 0:
            return self - abs(value)
        f = self.copy()
        for _ in range(value):
            f = f.__add_day()
        return f

    def __add_day(self):
        day, month, year = self.__day + 1, self.__month, self.__year
        if day > Date.__month_days(month, year):  # mes siguiente
            day = 1
            month += 1
            if month > 12:  # nos pasamos de diciembre, año siguiente
                month = 1
                year += 1
        return Date(day, month, year)

    def __sub__(self, value: (int, 'Date')):
        if isinstance(value, Date):
            return self.__subtract_date(value)
        if value < 0:
            return self + abs(value)
        return self.__subtract_days(value)

    def __subtract_date(self, other: 'Date'):
        if self < other:
            date1, date2 = self, other
            sign = -1
        else:
            date1, date2 = other, self
            sign = 1
        days = 0
        for _ in range(date1, date2):
            days += 1
        return sign * days

    def __subtract_days(self, n: int):
        f = self.copy()
        for _ in range(n):
            f = f.__subtract_day()
        return f

    def __subtract_day(self):
        day, month, year = self.__day - 1, self.__month, self.__year
        if day == 0:  # mes anterior
            month -= 1
            if month == 0:  # nos vamos al año anterior
                month = 12
                year -= 1
            day = Date.__month_days(month, year)
        return Date(day, month, year)

    def __radd__(self, n: int):
        return self + n

    def __eq__(self, other: 'Date'):
        return (self.__day, self.__month, self.__year) == (other.__day, other.__month, other.__year)

    def __ne__(self, other: 'Date'):
        return not self == other

    def __gt__(self, other: 'Date'):
        return self.to_iso_format() > other.to_iso_format()

    def __ge__(self, other: 'Date'):
        return self > other or self == other

    def __lt__(self, other: 'Date'):
        return not self >= other

    def __le__(self, other):
        return not self > other

    @staticmethod
    def __is_ok(day: int, month: int, year: int):
        if year < 1:  # año correcto
            return False
        if month < 1 or month > 12:   # mes correcto
            return False
        return 0 < day <= Date.__month_days(month, year)  # día correcto

    @staticmethod
    def __is_leap(year: int):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    @staticmethod
    def __month_days(month: int, year: int):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if Date.__is_leap(year):
            month_days[1] = 29
        return month_days[month - 1]

