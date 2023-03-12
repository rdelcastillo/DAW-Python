from datetime import datetime
from typeguard import typechecked


@typechecked
class Movement:
    __last_number: int = 0

    def __init__(self, amount: float, concept: str, date_time: datetime):
        Movement.__last_number += 1
        self.__number = Movement.__last_number
        self.__amount = amount
        self.__concept = concept
        self.__date_time = date_time

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
