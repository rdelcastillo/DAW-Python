from datetime import datetime
from typeguard import typechecked
from movement import Movement


@typechecked
class CashRegister:

    def __init__(self):
        self.__movements = []

    def add(self, amount: float, concept: str, date_time: datetime = datetime.now()):
        self.__raise_if_date_time_is_wrong(date_time)
        self.__raise_if_balance_is_negative(amount)
        self.__movements.append(Movement(amount, concept, date_time))

    def __raise_if_date_time_is_wrong(self, date_time: datetime):
        if len(self.__movements) == 0:  # no hay movimientos, nada que comprobar
            return
        last_movement = self.__movements[-1]
        if date_time < last_movement.date_time:
            raise ValueError(f"No se puede añadir un movimiento con fecha anterior al último {last_movement.date_time}")

    def __raise_if_balance_is_negative(self, amount: float):
        if amount >= 0:  # con una entrada no se puede generar un saldo negativo
            return
        if self.balance + amount < 0:
            raise ValueError(f"No puede haber una salida de {-amount} € porque el saldo quedaría en negativo")

    def delete_last(self):
        if len(self.__movements) == 0:
            raise ValueError("No hay movimientos")
        self.__movements.pop()

    @property
    def balance(self):
        balance_ = 0
        for m in self.__movements:
            balance_ += m.amount
        return balance_

    @property
    def size(self):
        return len(self.__movements)

    def __str__(self):
        str_ = "LISTADO DE MOVIMIENTOS DE LA CAJA REGISTRADORA\n" + \
               "______________________________________________\n" + \
               f"Núm {'Fecha':19s} {'Concepto':50s} Importe\n"
        str_ += self.__str_movements() + "\n"
        str_ += f"SALDO: {self.balance:.2f} €\n"
        return str_

    def __str_movements(self):
        str_ = ""
        for m in self.__movements:
            str_ += f"{m.number:3d} {m.date_time.strftime('%d/%m/%Y %H:%M:%S')} {m.concept:50s} {m.amount:7.2f} €\n"
        return str_
