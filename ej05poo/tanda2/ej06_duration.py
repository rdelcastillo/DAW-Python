"""
Clase que almacena duraciones de tiempo. Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

- t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.
- t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.
- t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Tiene getters y setters mediante propiedades y métodos para:

- Sumar y restar objetos de la clase (el resultado es otro objeto).
- Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
- Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea '10h 35m 5s'

Aunque el ejercicio no lo pide, hemos implementado también la posibilidad de aplicar operaciones relacionales sobre
los objetos de esta clase sobrecargando los métodos correspondientes.

Autor: Rafael del Castillo Gomariz
"""
from __future__ import annotations
from typeguard import typechecked

@typechecked
class Duration:

    def __init__(self, hours, minutes=None, seconds=None):
        if isinstance(hours, Duration) and (minutes, seconds) == (None, None):  # solo tiene que llegar un parámetro
            other = hours
            self.__hours, self.__minutes, self.__seconds = other.__hours, other.__minutes, other.__seconds
        elif isinstance(hours, int) and isinstance(minutes, int) and isinstance(seconds, int):
            self.__hours, self.__minutes, self.__seconds = hours, minutes, seconds
            self.__normalize()
        else:
            raise TypeError("Un objeto Duration se construye con tres enteros o con otro objeto Duration")

    def __normalize(self):
        """
        Cambia las horas, minutos y segundos del objeto Duration para que estén en el rango de valores adecuados.
        Pasamos todo a segundos, recalculamos las horas, minutos y segundos.
        No admitimos duraciones de tiempo negativas, lanzamos excepción en ese caso.
        """
        seconds = self.__total_seconds()
        if seconds < 0:
            raise ValueError("No puede haber duraciones de tiempo negativas")
        self.__hours = seconds // 3600
        self.__minutes = seconds % 3600 // 60
        self.__seconds = seconds % 3600 % 60

    def __total_seconds(self):
        return self.__hours * 3600 + self.__minutes * 60 + self.__seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, value: int):
        aux = Duration(value, self.__minutes, self.__seconds)
        self.__hours, self.__minutes, self.__seconds = aux.__hours, aux.__minutes, aux.__seconds

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, value: int):
        aux = Duration(self.__hours, value, self.__seconds)
        self.__hours, self.__minutes, self.__seconds = aux.__hours, aux.__minutes, aux.__seconds

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, value: int):
        aux = Duration(self.hours, self.minutes, value)
        self.__hours, self.__minutes, self.__seconds = aux.__hours, aux.__minutes, aux.__seconds

    def add_seconds(self, seconds: int):
        self.seconds += seconds

    def sub_seconds(self, seconds: int):
        self.seconds -= seconds

    def add_minutes(self, minutes: int):
        self.minutes += minutes

    def sub_minutes(self, minutes: int):
        self.minutes -= minutes

    def add_hours(self, hours: int):
        self.hours += hours

    def sub_hours(self, hours: int):
        self.hours -= hours

    def __str__(self):
        return f"{self.__hours}h {self.__minutes}m {self.__seconds}s"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__hours}, {self.__minutes}, {self.__seconds})"

    # Sobrecarga de operadores

    def __add__(self, other: Duration):
        return Duration(self.__hours + other.__hours, self.__minutes + other.__minutes, 
                        self.__seconds + other.__seconds)

    def __sub__(self, other: Duration):
        return Duration(self.__hours - other.__hours, self.__minutes - other.__minutes, 
                        self.__seconds - other.__seconds)

    def __eq__(self, other: Duration):
        return (self.__hours, self.__minutes, self.__seconds) == (other.__hours, other.__minutes, other.__seconds)

    def __ne__(self, other: Duration):
        return not self == other

    def __lt__(self, other: Duration):
        return self.__total_seconds() < other.__total_seconds()

    def __le__(self, other: Duration):
        return self.__total_seconds() <= other.__total_seconds()

    def __gt__(self, other: Duration):
        return not self <= other

    def __ge__(self, other: Duration):
        return not self < other
