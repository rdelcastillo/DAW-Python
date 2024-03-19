"""
Test clase PokerDiceCup.
"""
from poker_dice import PokerDice
from poker_dice_cup import PokerDiceCup
from ludo_dice import LudoDice

cup = PokerDiceCup(PokerDice(), PokerDice(), PokerDice())
print(f"La puntuación de {cup} es {cup.score}")

other = PokerDice()
print(f"Hemos creado el dado {other} y se lo añadimos al cubilete")

cup.add(other)
print(f"La puntuación de {cup} ahora es {cup.score}")

other = LudoDice()
input(f"Hemos creado el dado de parchís {other} y si lo añado al cubilete saltará una excepción...")
cup.add(other)
