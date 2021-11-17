"""
Este programa pedirá una cantidad de números primos para mostrar.

Versión 1.

Autoría: Clase 1ºDAW-B
Fecha: 17/11/2021
"""
import sys

print("Relación de números primos")
print("--------------------------")

# Petición de datos
num_primos_a_mostrar = int(input("¿Cuántos números primos mostramos? "))
if num_primos_a_mostrar < 1:
    print("No puedo imprimir esa cantidad de primos", file=sys.stderr)
    exit(1)

# Proceso
num_primos_mostrados = 0
candidato_a_primo = 2

while num_primos_mostrados < num_primos_a_mostrar:
    # ¿el candidato a primo lo es?
    # vamos a comprobar cuantos divisores tiene entre dos y candidato-1
    total_divisores = 0
    for n in range(2, candidato_a_primo):
        if candidato_a_primo % n == 0:
            total_divisores += 1

    # si no tiene divisores es primo
    if total_divisores == 0:
        print(candidato_a_primo)
        num_primos_mostrados += 1

    # pasar al siguiente candidato
    candidato_a_primo += 1