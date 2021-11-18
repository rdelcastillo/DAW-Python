"""
Programa Ej02CalcularDistanciaEntrePuntos.py

Propósito: Pide al usuario dos pares de números x1,y1 y x2,y2, que representan dos puntos en el plano.
Calcula y muestra la distancia entre ellos.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Se piden dos puntos y se calcula la distancia entre ellos.

Datos de entrada: dos puntos; cuatro coordenadas (x1,y1) (x2,y2) (entero).

Información de salida: distancia (real).

Variables: x1,y1,x2,y2(entero), distancia(real).
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer las cuatro coordenadas.
2. Calcular distancia: raíz cuadrada de (x2-x1)^2 + (y2-y1)^2
3. Mostrar distancia
"""

import math

print("Cálculo de la distancia entre dos puntos")
print("----------------------------------------")

# Pedimos datos
x1 = int(input("Dime las coordenadas del punto 1:\n"))
y1 = int(input())
x2 = int(input("Dime las coordenadas del punto 2:\n"))
y2 = int(input())

# Cálculos
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# Salida
print(f"Distancia: {distance}")
