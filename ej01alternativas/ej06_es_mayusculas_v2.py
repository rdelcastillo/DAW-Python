"""
Lee una cadena por teclado y comprueba si es una letra mayúscula.

- Autor: Rafael del Castillo.
- Fecha: 4/11/2020.
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
- Datos de entrada: cadena (cadena)
- Información de salida: Mensajes de si es mayúscula o no.
- Variables: letter (cadena)
-------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer la cadena
2. Si la cadena es una letra y mayúscula mostramos "La cadena es mayúsculas"
3. En caso contrario mostramos "La cadena no es mayúsculas"
"""

print("Comprobación de letras mayúsculas")
print("---------------------------------")

# Pedir datos
letter = input("Introduce una cadena: ")

# Comprobamos y mostramos resultados
if len(letter) == 1 \
        and (("A" <= letter <= "Z")  # letras normales
             or letter == "Á" or letter == "É" or letter == "Í" or letter == "Ó" or letter == "Ú"  # con tilde
             or letter == "Ñ" or letter == "Ü"):  # especiales
    print("La cadena es una letra mayúscula.")
else:
    print("La cadena no es una letra mayúscula.")
