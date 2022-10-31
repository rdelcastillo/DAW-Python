"""
Programa que calcule el desglose mínimo en billetes y monedas de una cantidad exacta de euros.

Hay billetes de 500, 200, 100, 50, 20, 10 y 5 euros y monedas de 2 y 1 euros.

Por ejemplo, si deseamos conocer el desglose de 434 €, el programa mostrará por pantalla el siguiente
resultado:

2 billetes de 200 euros.
1 billete de 20 euros.
1 billete de 10 euros.
2 monedas de 2 euros.

Autoría: Clase de CEIABD
Fecha: 26/10/2022
"""
import sys

BILLS_AND_COINS = [500, 200, 100, 50, 20, 10, 5, 2, 1]
MINIMUM_BILL_VALUE = 5

print("Desglose de dinero")
print("------------------")

money = int(input("¿Cuánto dinero quieres desglosar? "))
if money <= 0:
    print("Este programa solo funciona con valores positivos.", file=sys.stderr)
    exit(1)

for change in BILLS_AND_COINS:
    units_bills_or_coins = money // change
    if units_bills_or_coins > 0:
        money_type = "billete" if change >= MINIMUM_BILL_VALUE else "moneda"
        print(f"{units_bills_or_coins} {money_type}{'s' if units_bills_or_coins > 1 else ''} de {change} €")
        money = money % change
