"""
Propósito: Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10€, el segundo 20€,
el tercero 40€ y así sucesivamente.

Este un programa determinará cuánto debe pagar mensualmente y el total de lo que pagará después de los 20 meses.

Autor: Rafael del Castillo Gomariz.
Fecha: 11/11/2020.
----------------------------------------------------------------------------------------------------------------
Algoritmo:
----------------------------------------------------------------------------------------------------------------
Variables:

- pago_mes: entero, guardaremos la cantidad a pagar el mes que toque, valor inicial 10 euros.
- pago_total: entero, pago acumulado, valor inicial 0 euros.
- mes: mes actual.

pago_total <-- 0
pago_mes <-- 10

PARA mes DESDE 1 HASTA 20
    ESCRIBIR "Pago mes", mes, ":", pago_mes
    pago_total <-- pago_total + pago_mes
    pago_mes <-- pago_mes * 2               # pago mes siguiente
FIN-PARA

ESCRIBIR pago_total
"""
MONTHS = 20
FIRST_PAYMENT = 10

print("Pago mensuales")
print("--------------")

# Inicializamos variables
total_payment = 0
payment_month = FIRST_PAYMENT   # primer mes

# Proceso de impresión de pagos mensuales
for mes in range(MONTHS):
    print(f"Pago mes {mes+1:2d}: {payment_month:8,d}€")
    total_payment += payment_month
    payment_month *= 2               # pago mes siguiente

# Pago total
print(f"\nTotal a pagar: {total_payment:,d}€")
