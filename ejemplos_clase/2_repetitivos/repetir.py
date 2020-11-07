"""
Programa: repetir.py

Propósito: mostrar un ejemplo de como podemos emular un ciclo REPETIR en Python.
Pedimos un número para calcular su raíz cuadrada, hasta que introduzcan un número
positivo, después mostramos el resultado.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
A pesar de que Python no cuenta con el ciclo REPETIR es muy fácil emularlo con un
"while True:" y un "if" con un "break" al final del cuerpo del ciclo.

Hacemos un ciclo infinito y lo rompemos cuando la condición de salida del ciclo REPETIR
se cumpla.
-------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
MIENTRAS True
    LEER n
    SI n >= 0
        ROMPER-CICLO
    FIN-SI
    ESCRIBIR RAIZ-CUADRADA(n)
"""

print("Cálculo de la raíz cuadrada de un número")
print("----------------------------------------")

# Pedimos datos
while True:
    n = int(input("Dame un número positivo: "))
    if n >= 0:  # condición de salida
        break

# Mostramos resultados
print("La raíz cuadrada de", n, "es", n ** 0.5)
