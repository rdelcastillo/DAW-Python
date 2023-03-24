"""
Programa que genera una secuencia de 5 cartas de la baraja española y suma los puntos según el juego de la brisca.
El valor de las cartas se guarda en un diccionario que debe contener parejas (figura, valor), por ejemplo (“CABALLO”,3).
La secuencia de cartas debe ser una lista que contiene objetos de la clase Carta.
El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto no vale nada.

En esta versión generamos las cartas aleatoriamente y las guardamos en un conjunto.

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""
import random
from ej05poo.tanda3.ej14deck.card import Card

SUITS = "BASTOS COPAS ESPADAS OROS".split()
NUMBERS = "AS 2 3 4 5 6 7 SOTA CABALLO REY".split()
POINTS = {"AS": 11, "3": 10, "SOTA": 2, "CABALLO": 3, "REY": 4}
NUM_CARDS = 5

cards = set()  # metemos las cartas en un conjunto, así nos aseguramos que no habrá duplicados
while len(cards) < NUM_CARDS:
    card = Card(random.choice(NUMBERS), random.choice(SUITS))  # carta aleatoria
    cards.add(card)

print(f"Puntuación en la BRISCA de estas {NUM_CARDS} cartas:\n")
total_score = 0
for n, c in enumerate(cards):
    card_points = POINTS.get(c.number, 0)  # si el número de la carta no está en el diccionario los puntos son 0
    print(f"{n+1: 2}. {c.number} de {c.suit}: {card_points}")
    total_score += card_points
print(f"\nTOTAL: {total_score}")
