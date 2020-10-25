"""
Programa Ej14InvertirNumero.py

Propósito: Dado un número de dos cifras este programa lo invierte.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Vamos a hacerlo de dos formas.

1ª forma:   Pasamos el número a entero y extraemos sus dos cifras con
            la división (1ª) y el resto (2ª) entre 10.
            Variables: number, digit1, digit2, invertido

2ª forma:   Tratamos el número como una cadena de caracteres y mediante
            "slicing" accedemos a las posiciones de su primera y segunda
            cifra.
            Variables: number, digit1, digit2, invertido
"""

# -------------
# Primera forma
# -------------

# pedimos datos
number = int(input("Dame un número de dos cifras para invertir: "))

# cálculos
digit1 = number // 10
digit2 = number % 10
invertido = digit2 * 10 + digit1

# muestro resultado
print("El número invertido es", invertido)

# -------------
# Primera forma
# -------------

# pedimos datos
number = input("Dame un número de dos cifras para invertir: ")

# cálculos
digit1 = number[0]
digit2 = number[1]
invertido = digit2 + digit1
# otras opciones
# invertido = number[1] + number[0]

# muestro resultado
print("El número invertido es", invertido)
# otras opciones
# print("El número invertido es", number[::-1])
