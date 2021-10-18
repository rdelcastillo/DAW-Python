'''
Averiguamos si un número (7)) es primo.

Sacado del ejemplo del libro de Python página 134.
'''

numero = 7
divisor = 2
while divisor < numero:
    print(f"{numero} entre {divisor} es {numero//divisor} "
          f"con resto {numero%divisor}")
    divisor += 1
