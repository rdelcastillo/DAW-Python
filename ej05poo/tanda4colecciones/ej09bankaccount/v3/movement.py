"""
Clase Movement. Representa una transacción bancaria.

Crearemos un tipo enumerado con los tipos de movimiento bancario:

- IB: Saldo Inicial (Initial Balance)
- DP: Ingreso (Deposit)
- WD: Cargo (Withdraw)
- TI: Transferencia Emitida (Transfer Issued)
- TR: Transferencia Recibida (Transfer Received)

Autor: Rafael del Castillo Gomariz.
"""
from dataclasses import dataclass
from enum import Enum
from typing import Optional
from typeguard import typechecked

MovementType = Enum('MovementType', 'IB DP WD TI TR')

@typechecked
@dataclass(frozen=True)
class Movement:
    type: MovementType
    amount: float
    account: Optional[int] = None

    def __str__(self):
        if self.type == MovementType.IB:
            return f"Creación de la cuenta con ingreso de: {self.amount:.2f} €"
        elif self.type == MovementType.DP:
            return f"Ingreso de {self.amount:.2f} €"
        elif self.type == MovementType.WD:
            return f"Cargo de {-self.amount:.2f} €"
        elif self.type == MovementType.TI:
            return f"Transferencia emitida de {-self.amount:.2f} € a la cuenta {self.account:010d}"
        elif self.type == MovementType.TR:
            return f"Transferencia recibida de {self.amount:.2f} € de la cuenta {self.account:010d}"
        else:
            raise ValueError("Tipo de movimiento desconocido:", self.type)
