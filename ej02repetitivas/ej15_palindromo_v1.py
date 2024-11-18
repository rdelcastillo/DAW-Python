"""
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual
adelante que atrás.

Análisis.
Leo una cadena. La paso a mayúsculas, le quito espacios y vocales con tilde,
después creo una nueva cadena invirtiendo la cadena anterior.
Si ambas cadenas son iguales -> Es un palíndromo.

Datos de entrada: Cadena de caracteres
Información de salida: Mensaje indicando si es palíndromo o no.
Variables: cadena_usuario, cadena_usuario_procesada, cadena_invertida, índice (posición)
"""

# Pedimos datos
user_string = input("Introduce una cadena para comprobar si es palíndroma: ")

# Procesamos la cadena anterior pasándola a mayúsculas, quitando espacios y tildes
fixed_user_string = ""
for ch in user_string.upper():
    if ch == "Á":
        fixed_user_string += "A"
    elif ch == "É":
        fixed_user_string += "E"
    elif ch == "Í":
        fixed_user_string += "I"
    elif ch == "Ó":
        fixed_user_string += "O"
    elif ch == "Ú":
        fixed_user_string += "U"
    elif ch != " ":
        fixed_user_string += ch

# Invertimos la cadena anterior
inverted_fixed_user_string = ""
for ch in fixed_user_string:
    inverted_fixed_user_string = ch + inverted_fixed_user_string

# Comprobamos si la cadena invertida es igual a la original procesada
if inverted_fixed_user_string == fixed_user_string:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
