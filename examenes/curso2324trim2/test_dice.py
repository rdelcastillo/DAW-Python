"""
Test clase Dice.
"""
from dice import Dice

dice1 = Dice(1,2,3,4,5,6)
dice2 = Dice('A','K','Q','J','R','N')

print(f"Tiro cinco veces los dados {repr(dice1)} y {repr(dice2)}:")
for i in range(5):
    dice1.roll()
    dice2.roll()
    print(f"Tirada {i+1}: {dice1} {dice2}")
