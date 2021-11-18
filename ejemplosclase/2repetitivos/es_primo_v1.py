"""
Averiguamos si un número (7)) es primo.

Sacado del ejemplo del libro de Python página 134.
"""

number = 7
divisor = 2
while divisor < number:
    print(f"{number} entre {divisor} es {number//divisor} "
          f"con resto {number%divisor}")
    divisor += 1
