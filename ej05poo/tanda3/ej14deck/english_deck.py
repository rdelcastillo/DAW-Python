"""
Clase EnglishDeck. Simula una baraja inglesa.

Autor: Rafael del Castillo Gomariz.
"""
from deck import Deck
from card import Card


class EnglishDeck(Deck):

    def __init__(self):
        numbers = "1 2 3 4 5 6 7 8 9 10 J Q K".split()
        suits = "♠ ♡ ♢ ♣".split()
        cards = [Card(n, s) for n in numbers for s in suits]
        super().__init__(cards)
        self.shuffle()
