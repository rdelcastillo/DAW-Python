"""
Programa ej03_hipotenusa.py
Propósito: Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que leer los catetos del triángulo y calcular su hipotenusa aplicando el teorema de Pitágoras.

El teorema de Pitágoras dice que para un triángulo rectángulo: hipotenusa² = cateto1² + cateto2²

Por lo que la hipotenusa es la raíz cuadrada de la suma de los catetos al cuadrado.

Datos de entrada: catetos (números reales).
Información de salida: valor de la hipotenusa (real).

Variables: cateto1, cateto2, hipotenusa (reales).
-------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer catetos.
2. Calcular hipotenusa (raíz cuadrada de la suma de los catetos al cuadrado).
3. Mostrar hipotenusa.
"""

import math  # módulo necesario para usar función de raíz cuadrada: sqrt

print("Cálculo de la hipotenusa de un triángulo rectángulo.")
print("----------------------------------------------------")

# Pedimos datos
side1 = float(input("Introduce el primer cateto:  "))
side2 = float(input("Introduce el segundo cateto: "))

# Cálculos
hypotenuse = math.sqrt(side1**2 + side2**2)

# Mostramos resultado
print("La hipotenusa es", hypotenuse)
