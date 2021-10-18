"""
Programa ej11calculardistancia.py

Propósito: Pide al usuario dos números y muestra la "distancia" entre ellos (el valor absoluto de su diferencia, de modo
que el resultado sea siempre positivo).

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Se piden dos números y se calcula el valor absoluto de la diferencia.

Datos de entrada: dos números (entero).

Información de salida: distancia (entero).

Variables: num1,num2 (enteros).
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer los dos números.
2. Mostrar distancia (valor absoluto de la diferencia)
"""

print("Cálculo de la distancia entre dos números")
print("-----------------------------------------")

# Pedimos datos
num1 = int(input("Dime el número 1: "))
num2 = int(input("Dime el número 2: "))

# Mostramos resultado
print("Distancia: ", abs(num1 - num2))
