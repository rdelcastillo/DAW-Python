"""
Clase Card.

Simula una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto de valores).

Autor: Rafael del Castillo.
"""
from dataclasses import dataclass
from typeguard import typechecked


@typechecked
@dataclass(frozen=True)
class Card:
    number: str
    suit: str
