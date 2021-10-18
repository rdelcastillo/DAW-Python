"""
Programa ej02_rectangulo.py
Propósito: Calcular el perímetro y área de un rectángulo dada su base y su altura.
Autor: Rafael del Castillo Gomariz
Fecha: 8/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que leer la base y la altura del rectángulo y calcular el perímetro y el área.

Datos de entrada: base (número real), altura (número real).
Información de salida: perímetro (real) y área (real).

Variables: base, altura, perímetro y area (real).
-------------------------------------------------------------------------------------
Diseño:
-------------------------------------------------------------------------------------
1. Leer base y altura.
2. Calcular perímetro (2*base + 2*altura).
3. Calcular área (base * altura).
4. Mostrar perímetro y área.
"""

print("Cálculo del perímetro y área de un rectángulo.")
print("----------------------------------------------")

# Pedimos datos
base = float(input("Introduce la base: "))
height = float(input("Introduce la altura: "))

# Cálculos
perimeter = 2 * (base + height)
area = base * height

# Mostramos resultado
print("El perímetro es", perimeter, "y el área es", area)
