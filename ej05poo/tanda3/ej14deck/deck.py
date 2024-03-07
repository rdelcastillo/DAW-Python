"""
Clase Deck. Simula un conjunto de cartas de naipes.

- Inicialmente, la baraja tiene las cartas que le llegan con el constructor.
- Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas.
- Le pueden quitar la primera carta (robar).
- Puede barajarse.

Autor: Rafael del Castillo.
"""
import random
from typing import List
from typeguard import typechecked
from card import Card


@typechecked
class Deck:

    def __init__(self, cards: List[Card]):
        self.__cards = cards.copy()
    @property
    def size(self):
        return len(self.__cards)

    def deal(self, player, num_cards: int):  # no ponemos tipo a player porque tendríamos un error de referencia cíclica
        self.__check_deal(num_cards)
        cards_to_deal = self.__cards[:num_cards]
        player.receives(cards_to_deal)
        self.__cards = self.__cards[num_cards:]

    def __check_deal(self, number):
        if number < 0:
            raise ValueError("El número de cartas a repartir tiene que ser positivo")
        if number > len(self.__cards):
            raise ValueError("No hay cartas suficientes para repartir")

    def draw(self):
        if self.size == 0:
            raise ValueError("No quedan cartas en la baraja")
        return self.__cards.pop(0)

    def shuffle(self):
        random.shuffle(self.__cards)

    def __repr__(self):
        return repr(self.__cards)
