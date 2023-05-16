from datetime import datetime
from typing import Optional
from typeguard import typechecked

FILENAME_LAST_NUMBER = "last_number_movement.txt"

class MovementError(Exception):

    def __init__(self, message):
        super().__init__(message)

@typechecked
class Movement:

    def __init__(self, amount: float, concept: str, date_time: datetime, number: Optional[int] = None):
        self.__amount = amount
        self.__concept = concept
        self.__date_time = date_time
        if number is None:
            self.__number = self.__next_number()
        else:
            self.__number = number
            if number > Movement.last_number():
                Movement.__save_number(number)

    @property
    def number(self):
        return self.__number

    @property
    def amount(self):
        return self.__amount

    @property
    def concept(self):
        return self.__concept

    @property
    def date_time(self):
        return self.__date_time

    def __repr__(self):
        return f"{self.__class__.__name__}(number={self.__number}, amount={self.__amount}, concept={self.__concept}, " \
               f"date_time={self.date_time})"

    @staticmethod
    def __next_number():
        next_number = Movement.last_number() + 1
        Movement.__save_number(next_number)
        return next_number

    @staticmethod
    def last_number():
        try:
            with open(FILENAME_LAST_NUMBER) as f:
                number = int(f.read().strip())
            return number
        except FileNotFoundError as e:
            raise MovementError(f"No se encuentra el fichero {FILENAME_LAST_NUMBER}: {e}")
        except ValueError as e:
            raise MovementError(f"Hay caracteres no permitidos en el fichero {FILENAME_LAST_NUMBER}: {e}")

    @staticmethod
    def __save_number(number):
        try:
            with open(FILENAME_LAST_NUMBER, "w") as f:
                print(number, file=f)
        except FileNotFoundError as e:
            raise MovementError(f"No se encuentra el fichero {FILENAME_LAST_NUMBER}: {e}")
        except PermissionError as e:
            raise MovementError(f"No hay permiso para abrir el fichero {FILENAME_LAST_NUMBER}: {e}")
        except ValueError as e:
            raise MovementError(f"Hay caracteres no permitidos en el fichero {FILENAME_LAST_NUMBER}: {e}")
