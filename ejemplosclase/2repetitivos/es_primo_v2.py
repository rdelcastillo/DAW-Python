"""
Averiguamos si un número (7)) es primo.

Sacado del ejemplo del libro de Python página 134.
"""

number = 7
for divisor in range(2, number):
    print(f"{number} entre {divisor} es {number // divisor} "
          f"con resto {number % divisor}")
