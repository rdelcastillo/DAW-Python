"""
Programa que genera una secuencia de 5 cartas de la baraja española y suma los puntos según el juego de la brisca.
El valor de las cartas se guarda en un diccionario que debe contener parejas (figura, valor), por ejemplo (“CABALLO”,3).
La secuencia de cartas debe ser una lista que contiene objetos de la clase Carta.
El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto no vale nada.

En esta versión creamos una baraja española, la barajamos y de ahí sacamos las cartas.

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""
from ej05poo.tanda3.ej14deck.spanish_deck import SpanishDeck

POINTS = {"AS": 11, "3": 10, "SOTA": 2, "CABALLO": 3, "REY": 4}
NUM_CARDS = 5

deck = SpanishDeck()
deck.shuffle()
cards = [deck.draw() for _ in range(NUM_CARDS)]

print(f"Puntuación en la BRISCA de estas {NUM_CARDS} cartas:\n")
total_score = 0
for n, c in enumerate(cards):
    card_points = POINTS.get(c.number, 0)  # si el número de la carta no está en el diccionario los puntos son 0
    print(f"{n+1: 2}. {c.number} de {c.suit}: {card_points}")
    total_score += card_points
print(f"\nTOTAL: {total_score}")
