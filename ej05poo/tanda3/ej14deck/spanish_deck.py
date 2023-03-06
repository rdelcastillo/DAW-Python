"""
Clase SpanishDeck. Simula una baraja española.

Autor: Rafael del Castillo Gomariz.
"""
from deck import Deck
from card import Card


class SpanishDeck(Deck):

    def __init__(self):
        numbers = "1 2 3 4 5 6 7 8 9 SOTA CABALLO REY".split()
        suits = "OROS COPAS ESPADAS BASTOS".split()
        cards = [Card(n, s) for n in numbers for s in suits]
        super().__init__(cards)
        self.shuffle()
