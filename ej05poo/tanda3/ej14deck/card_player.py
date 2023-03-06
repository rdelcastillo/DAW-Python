"""
Clase CardPlayer. Simula un jugador de naipes. Un jugador tiene un conjunto de naipes.

- Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos.
- Puede deshacerse de una carta.
- Puede recibir cartas.

Autor: Rafael del Castillo
"""
from typing import List
from typeguard import typechecked
from card import Card
from deck import Deck


@typechecked
class CardPlayer:

    def __init__(self, name: str):
        self.__name = name
        self.__cards = []

    @property
    def name(self):
        return self.__name

    @property
    def cards(self):
        return self.__cards.copy()

    def receives(self, cards: List[Card]):
        self.__cards.extend(cards)

    def draws(self, deck: Deck):
        self.__cards.append(deck.draw())

    def throws(self, card: Card):
        self.__cards.remove(card)

    def __repr__(self):
        return f"{self.__class__.__name__}(name=,{self.__name} cards={self.__cards})"
