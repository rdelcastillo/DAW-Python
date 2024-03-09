"""
Test clase LudoDice.
"""
from ludo_dice import LudoDice

dice1 = LudoDice()
dice2 = LudoDice()

print(f"{dice1} < {dice2}: {dice1 < dice2}")
print(f"{dice1} <= {dice2}: {dice1 <= dice2}")
print(f"{dice1} > {dice2}: {dice1 > dice2}")
print(f"{dice1} >= {dice2}: {dice1 >= dice2}")
print(f"{dice1} == {dice2}: {dice1 == dice2}")
print(f"{dice1} != {dice2}: {dice1 != dice2}")
