"""
Clase BankAccount.

Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta se genera de forma aleatoria cuando
se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta. La cuenta se puede crear con un
saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente.

En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra.
No se permite el saldo negativo.

Cada cuenta lleva un registro de todos los movimientos realizados: ingresos, cargos y transferencias (tanto enviadas
como recibidas) en una lista de diccionarios.

Crearemos un tipo enumerado con los tipos de movimiento bancario:

- IB: Saldo Inicial (Initial Balance)
- DP: Ingreso (Deposit)
- WD: Cargo (Withdraw)
- TI: Transferencia Emitida (Transfer Issued)
- TR: Transferencia Recibida (Transfer Received)

Autor: Rafael del Castillo Gomariz.
"""
from __future__ import annotations
import random
from enum import Enum
from typeguard import typechecked

MovementType = Enum('MovementType', 'IB DP WD TI TR')

@typechecked
class BankAccount:
    __registered_accounts = []

    def __init__(self, balance: float = 0):
        if balance < 0:
            raise ValueError("No puede crearse una cuenta bancaria con saldo negativo")
        self.__number = BankAccount.__create_number_account()
        self.__movements = [{'type':MovementType.IB, 'amount':balance}] if balance > 0 else []

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
            balance_ += m['amount']
        return balance_

    @property
    def number(self):
        return self.__number

    def deposit(self, money: float):
        if money <= 0:
            raise ValueError("Un depósito en cuenta no puede ser negativo")
        self.__movements.append({'type': MovementType.DP, 'amount': money})

    def withdraw(self, money: float):
        if money <= 0:
            raise ValueError("Un cargo en cuenta no puede ser negativo")
        if self.balance - money < 0:
            raise ValueError("El cargo no se puede hacer porque la cuenta quedaría con saldo negativo")
        self.__movements.append({'type': MovementType.WD, 'amount': -money})

    def transfer(self, other: BankAccount, money: float):
        if money <= 0:
            raise ValueError("Una transferencia no puede ser negativa")
        if self.balance - money < 0:
            raise ValueError("No hay saldo suficiente para hacer la transferencia")
        self.__movements.append({'type': MovementType.TI, 'amount': -money, 'account':other.__number})
        other.__movements.append({'type': MovementType.TR, 'amount': money, 'account':self.__number})

    @property
    def movements(self):
        str_ = f"Movimientos de la cuenta {self.__number:010d}\n-----------------------------------"
        balance_ = 0
        for m in self.__movements:
            balance_ += m['amount']
            str_ += "\n" + self.__movement2str(m, balance_)
        return str_

    @staticmethod
    def __movement2str(m, balance_):
        if m['type'] == MovementType.IB:
            return f"Creación de la cuenta con ingreso de: {m['amount']:.2f} €. Saldo: {balance_:.2f} €"
        elif m['type'] == MovementType.DP:
            return f"Ingreso de {m['amount']:.2f} €. Saldo: {balance_:.2f} €"
        elif m['type'] == MovementType.WD:
            return f"Cargo de {-m['amount']:.2f} €. Saldo: {balance_:.2f} €"
        elif m['type'] == MovementType.TI:
            return f"Transferencia emitida de {-m['amount']:.2f} € a la cuenta {m['account']:010d}. " \
                   f"Saldo: {balance_:.2f} €"
        elif m['type'] == MovementType.TR:
            return f"Transferencia recibida de {m['amount']:.2f} € de la cuenta {m['account']:010d}. " \
                   f"Saldo: {balance_:.2f} €"
        else:
            raise ValueError("Tipo de movimiento desconocido:", m.type)

    def __str__(self):
        return f"Número de cuenta {self.__number:010d} Saldo: {self.__balance:.2f} €"
