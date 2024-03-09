"""
Test clase PokerDiceCup.
"""
from poker_dice import PokerDice
from poker_dice_cup import PokerDiceCup

cup = PokerDiceCup(PokerDice(), PokerDice(), PokerDice())
print(f"La puntuación de {cup} es {cup.score}")
