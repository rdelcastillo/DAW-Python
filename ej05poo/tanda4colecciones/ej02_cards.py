"""
Programa que escoge al azar 10 cartas de la baraja española (10 objetos de la clase Carta).

Empleamos una lista para almacenarlas y nos aseguramos de que no se repite ninguna. Las cartas se mostrarán ordenadas.
Se ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por número: as, 2, 3, 4, 5,
6, 7, sota, caballo, rey.

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""
import random
from ej05poo.tanda3.ej14deck.card import Card

SUITS = "BASTOS COPAS ESPADAS OROS".split()
NUMBERS = "AS 2 3 4 5 6 7 SOTA CABALLO REY".split()
NUM_CARDS = 10

cards_set = set()  # metemos las cartas en un conjunto, así nos aseguramos que no habrá duplicados
while len(cards_set) < NUM_CARDS:
    card = Card(random.choice(NUMBERS), random.choice(SUITS))  # carta aleatoria
    cards_set.add(card)

cards_list = list(cards_set)  # transformamos el conjunto en una lista
cards_list.sort(key=lambda c: (c.suit, NUMBERS.index(c.number)))  # ordenamos por palo y número

print(f"Generador aleatorio de {NUM_CARDS} cartas:")
for n, c in enumerate(cards_list):
    print(f"{n+1: 2}: {c.number} de {c.suit}")
