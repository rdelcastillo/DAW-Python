"""
Clase BankAccount.

Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta se genera de forma aleatoria cuando
se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta. La cuenta se puede crear con un
saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente.

En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra.
No se permite el saldo negativo.

Cada cuenta lleva un registro de todos los movimientos realizados: ingresos, cargos y transferencias (tanto enviadas
como recibidas) en una lista de objetos de tipo movimiento.

Autor: Rafael del Castillo Gomariz.
"""
from __future__ import annotations
import random
from typeguard import typechecked
from movement import Deposit, Withdraw, TransferIssued, TransferReceived, Movement

class NegativeBalanceError(ValueError):

    def __init__(self, message: str):
        super().__init__(message)

@typechecked
class BankAccount:
    __registered_accounts = []

    def __init__(self, balance: float = 0):
        if balance < 0:
            raise NegativeBalanceError("No puede crearse una cuenta bancaria con saldo negativo")
        self.__number = BankAccount.__create_number_account()
        if balance > 0:
            self.__movements = [Deposit(balance, f"Creación de la cuenta con ingreso de: {balance:.2f} €")]
        else:
            self.__movements = []

    @classmethod
    def __create_number_account(cls):
        while True:
            number = random.randint(1, 9999999999)
            if number not in cls.__registered_accounts:
                break
        cls.__registered_accounts.append(number)
        return number

    @property
    def balance(self):
        balance_ = 0
        for m in self.__movements:
            balance_ += m.amount
        return balance_

    @property
    def number(self):
        return self.__number

    def __check_balance(self, money: float, error_message: str):
        if self.balance - money < 0:
            raise NegativeBalanceError(error_message)

    def deposit(self, money: float):
        self.__append(Deposit(money))

    def withdraw(self, money: float):
        self.__check_balance(money, "El cargo no se puede hacer porque la cuenta quedaría con saldo negativo")
        self.__append(Withdraw(money))

    def transfer(self, other: BankAccount, money: float):
        self.__check_balance(money, "No hay saldo suficiente para hacer la transferencia")
        self.__append(TransferIssued(money, other.__number))
        other.__append(TransferReceived(money, self.__number))

    def __append(self, m: Movement):  # la lista de movimientos debe estar ordenada por fecha
        self.__movements = sorted(self.__movements + [m], key=lambda m: m.date_time)

    @property
    def movements(self):
        str_ = f"Movimientos de la cuenta {self.__number:010d}\n-----------------------------------"
        balance_ = 0
        for m in self.__movements:
            balance_ += m.amount
            str_ += f"\n{m.concept}. Saldo: {balance_:.2f} €"
        return str_

    def __str__(self):
        return f"Número de cuenta {self.__number:010d} Saldo: {self.__balance:.2f} €"
