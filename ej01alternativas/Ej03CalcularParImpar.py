"""
Programa que lee un número e indique si es par o impar.

- Autor: Rafael del Castillo.
- Fecha: 4/11/2020.
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que pedir un número por teclado, y comprobar si es par o impar.

- Datos de entrada: número (entero).
- Información de salida: Un mensaje de texto indicando si el número es par o impar.
- Variables: number (entero)
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer el numero
2. Si el resto de dividir el número entre 2 es igual a 0 el número es par.
3. En caso contrario es impar
"""

print("Comprobación de la paridad de un número")
print("---------------------------------------")

# Lectura de datos
number = int(input("Dime el número: "))

# Comprobación de la paridad
if number % 2 == 0:
    print("Es Par")
else:
    print("Es impar")
