'''
Averiguamos si un número (7)) es primo.

Sacado del ejemplo del libro de Python página 134.
'''

numero = 7
restos_no_nulos = 0
for divisor in range(2,numero):
    if numero % divisor != 0:
        restos_no_nulos += 1

if restos_no_nulos == numero-2:
    print(f"El número {numero} es primo")
else:
    print(f"El número {numero} NO es primo")