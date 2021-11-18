"""
Averiguamos si un número (7)) es primo.

Sacado del ejemplo del libro de Python página 134.
"""

number = 7
restos_no_nulos = 0
for divisor in range(2, number):
    if number % divisor != 0:
        restos_no_nulos += 1

if restos_no_nulos == number - 2:
    print(f"El número {number} es primo")
else:
    print(f"El número {number} NO es primo")
