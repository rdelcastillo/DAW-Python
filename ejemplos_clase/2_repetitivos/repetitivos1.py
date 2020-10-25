"""
Ejemplo de uso de ciclos precondición.

Haremos flexiones mientras no estemos cansados. Para ver si estamos cansados le
preguntaremos al usuario si lo está.

Autor: Clase de 1ºDAW-A
Fecha: 23/10/2020.
---------
Análisis:
---------
Usaremos una variable (is_tired) de tipo cadena, que tendrá una "S" (sí) ó una "N" (no).
Supondremos que inicialmente NO estamos cansados.
"""

print("Programa para ejercitarse haciendo flexiones.")
print("---------------------------------------------")

# Inicializar las variables
is_tired = "N"

# Proceso
while is_tired == "N":
    print("Hago una flexión")
    is_tired = input("¿Estás cansado? (S/N) ")
