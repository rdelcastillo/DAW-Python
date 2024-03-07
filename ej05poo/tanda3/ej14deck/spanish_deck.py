"""
Clase SpanishDeck. Simula una baraja española.

Autor: Rafael del Castillo Gomariz.
"""
from ej05poo.tanda3.ej14deck.card import Card
from ej05poo.tanda3.ej14deck.deck import Deck


class SpanishDeck(Deck):

    def __init__(self):
        numbers = "1 2 3 4 5 6 7 SOTA CABALLO REY".split()
        suits = "OROS COPAS ESPADAS BASTOS".split()
        cards = [Card(n, s) for s in suits for n in numbers]
        super().__init__(cards)
