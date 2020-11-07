"""
Pedimos al usuario dos números y mostramos su división si el segundo no es cero,
o un mensaje de aviso en caso contrario.

- Autor: Rafael del Castillo.
- Fecha: 4/11/2020.
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que pedir dos números, y mostrar el resultado de la división.
Si el divisor es 0 debemos responder un mensaje de error.

- Datos de entrada: dividendo, divisor (entero)
- Información de salida: El resultado de la división o un mensaje de error indicando que el divisor es igual a 0.
- Variables: dividend, divider (enteros)
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer los números
2. Si el divisor es igual a 0 escribir "No se puede dividir por 0"
3. En caso contrario mostrar el resultado de la división
"""

# Pedimos datos
dividend = int(input("Dime el número 1: "))
divider = int(input("Dime el número 2: "))

# Mostramos
if divider == 0:
    print("No puedes dividir por 0")
else:
    print(f"La división es {dividend / divider}")
