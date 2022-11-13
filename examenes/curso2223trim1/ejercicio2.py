"""
Nos podemos aproximar al número PI usando la serie de Leibniz que dice que PI se puede obtener a partir de la siguiente
sucesión: 4/1 – 4/3 + 4/5 – 4/7 + 4/9...

Si te fijas, el 4 (numerador) es fijo, y el denominador se aumenta de 2 en 2. Además, en cada paso se intercambia
el signo.

Este programa pide el número de iteraciones y muestra el valor de PI.
"""
import sys

print("Cálculo del valor de PI usando la sucesión de Leibniz")
print("-----------------------------------------------------")

iterations = int(input("¿Cuantas iteraciones usamos? "))
if iterations < 0:
    print("El número de iteraciones no es válido.", file=sys.stderr)
    exit(1)

pi = 4
den = 1
sign = 1
for _ in range(iterations):
    den += 2
    sign *= -1
    pi += sign * 4/den

print("El valor de Pi es", pi)
