import csv
from datetime import datetime
from typing import Optional
from typeguard import typechecked
from movement import Movement

class CashRegisterError(Exception):

    def __init__(self, message):
        super().__init__(message)

@typechecked
class CashRegister:

    def __init__(self, csv_filename: Optional[str] = None):
        self.__movements = []
        if csv_filename:
            self.__append(csv_filename)

    def __append(self, csv_filename: str):
        try:
            with open(csv_filename) as csv_file:
                csv_reader = csv.reader(csv_file)
                for m in csv_reader:
                    movement = Movement(float(m[1]), m[2], datetime.strptime(m[3], "%H:%M:%S %d/%m/%Y"), int(m[0]))
                    self.__raise_if_movement_is_wrong(movement)
                    self.__movements.append(movement)
        except FileNotFoundError as e:
            raise CashRegisterError(f"No se puede abrir para lectura el fichero {csv_filename}: {e}")
        except ValueError as e:
            raise CashRegisterError(f"El importe o el número o la fecha del movimiento {m} son incorrectos: {e}")
        except IndexError as e:
            raise CashRegisterError(f"Faltan campos en el movimiento: {m}: {e}")

    def add(self, amount: float, concept: str, date_time: datetime = datetime.now()):
        movement = Movement(amount, concept, date_time)
        self.__raise_if_movement_is_wrong(movement)
        self.__movements.append(movement)

    def __raise_if_movement_is_wrong(self, movement: Movement):
        if self.balance + movement.amount < 0:  # saldo correcto
            raise CashRegisterError(f"No puede haber una salida de {-movement.amount} € porque el saldo quedaría "
                                    f"en negativo")
        if len(self.__movements) == 0:  # no hay movimientos, nada más que comprobar
            return
        if movement.number <= self.__movements[-1].number:  # identificador correcto
            raise CashRegisterError(f"No se puede añadir un movimiento con identificador anterior al "
                                    f"último: {self.__movements[-1].date_time}")
        if movement.date_time < self.__movements[-1].date_time:  # fecha correcta
            raise CashRegisterError(f"No se puede añadir un movimiento con fecha y hora anterior al "
                                    f"último: {self.__movements[-1].date_time}")

    def delete_last(self):
        if len(self.__movements) == 0:
            raise CashRegisterError("No hay movimientos")
        self.__movements.pop()

    def save(self, csv_filename: Optional[str] = None):
        if not csv_filename:
            csv_filename = "cash_register_" + datetime.now().strftime("%Y-%m-%d") + ".csv"
        with open(csv_filename, "wt") as csv_file:
            csv_writer = csv.writer(csv_file, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            for m in self.__movements:
                csv_writer.writerow([m.number, m.amount, m.concept, m.date_time.strftime("%H:%M:%S %Y/%m/%d")])
        return csv_filename

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
