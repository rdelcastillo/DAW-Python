"""
Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra palíndroma es aquella que se lee igual
adelante que atrás.

Análisis.
Leo una cadena. La paso a mayúsculas, le quito espacios y vocales con tilde,
después creo una nueva cadena invirtiendo la cadena anterior.
Si ambas cadenas son iguales-> Es un palíndromo.

Datos de entrada: Cadena de caracteres
Información de salida: Mensaje indicando si es palíndromo o no.
Variables: cadena, cadena1, cadena2, i (posición)
"""

# Constantes
VOWELS_WITH_TILDE = "ÁÉÍÓÚ"
VOWELS_WITHOUT_TILDE = "AEIOU"

# Inicializamos variables
reverse_string = ""  # cadena original invertida

# Pedimos datos
user_string = input("Introduce una cadena para comprobar si es palíndroma: ")

# Proceso

# Pasamos a mayúsculas la cadena original, quitamos tildes y espacios
original_string = user_string.upper().replace(" ", "")  # mayúsculas y sin espacios
for i in range(len(VOWELS_WITH_TILDE)):  # vocales con tilde
    original_string = original_string.replace(VOWELS_WITH_TILDE[i], VOWELS_WITHOUT_TILDE[i])

# Invertimos cadena anterior
for ch in original_string:
    reverse_string = ch + reverse_string

# En Python también podemos hacer: reverse_string = original_string[::-1]

# ¿Es palíndromo?
if original_string == reverse_string:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
