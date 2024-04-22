"""
Clase Abstracta Movement. Representa una transacción bancaria.

Los movimientos estarán en clases especializadas.

Autor: Rafael del Castillo Gomariz.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from typeguard import typechecked
from datetime import datetime

MovementType = Enum('MovementType', 'IB DP WD TI TR')

class NegativeMoneyError(ValueError):

    def __init__(self, message: str):
        super().__init__(message)

@typechecked
@dataclass(frozen=True)
class Movement(ABC):
    type: MovementType
    amount: float
    concept: str
    date_time: datetime
    account: Optional[int] = None

    @staticmethod
    def check_amount(amount: float, error_message: str):
        if amount < 0:
            raise NegativeMoneyError(error_message)

    def __repr__(self):
        return f"{self.__class__.__name__}(type={self.type}, amount={self.amount}, concept={self.concept}," \
               f"date_time={self.date_time}, account={self.account})"

class Deposit(Movement):

    def __init__(self, amount: float, concept: Optional[str] = None, date_time: datetime = datetime.now()):
        super().check_amount(amount, "Un depósito en cuenta no puede ser negativo")
        if concept is None:
            concept = f"Ingreso de {amount:.2f} €"
        super().__init__(MovementType.DP, amount, concept, date_time)


class Withdraw(Movement):

    def __init__(self, amount: float, concept: Optional[str] = None, date_time: datetime = datetime.now()):
        super().check_amount(amount, "Un cargo en cuenta no puede ser negativo")
        if concept is None:
            concept = f"Cargo de {amount:.2f} €"
        super().__init__(MovementType.WD, -amount, concept, date_time)


class TransferIssued(Movement):

    def __init__(self, amount: float, account: int, concept: Optional[str] = None,
                 date_time: datetime = datetime.now()):
        super().check_amount(amount, "Una transferencia emitida no puede ser negativa")
        if concept is None:
            concept = f"Transferencia emitida de {amount:.2f} € a la cuenta {account:010d}"
        super().__init__(MovementType.TI, -amount, concept, date_time, account)


class TransferReceived(Movement):

    def __init__(self, amount: float, account: int, concept: Optional[str] = None,
                 date_time: datetime = datetime.now()):
        super().check_amount(amount, "Una transferencia recibida no puede ser negativa")
        if concept is None:
            concept = f"Transferencia recibida de {amount:.2f} € de la cuenta {account:010d}"
        super().__init__(MovementType.TI, amount, concept, date_time, account)
