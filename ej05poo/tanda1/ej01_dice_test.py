"""
Prueba de la clase "Dado".
"""
from ej01_dice import Dice

print("Diez tiradas de dos dados")
print("-------------------------")

dice1 = Dice()
dice2 = Dice()

for i in range(10):
    dice1.roll()
    dice2.roll()
    print(f"Tirada {i+1:2d}: {dice1} - {dice2}")