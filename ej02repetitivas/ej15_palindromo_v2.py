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

# Pedimos datos
user_string = input("Introduce una cadena para comprobar si es palíndroma: ")

# Proceso

# Pasamos a mayúsculas la cadena original, quitamos tildes y espacios
fixed_user_string = user_string.upper().replace(" ", "")  # mayúsculas y sin espacios
for i in range(len(VOWELS_WITH_TILDE)):  # vocales con tilde
    fixed_user_string = fixed_user_string.replace(VOWELS_WITH_TILDE[i], VOWELS_WITHOUT_TILDE[i])

# Invertimos cadena anterior
reverse_fixed_user_string = fixed_user_string[::-1]

# ¿Es palíndromo?
if fixed_user_string == reverse_fixed_user_string:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
