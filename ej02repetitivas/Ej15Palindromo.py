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
VOCALES_CON_TILDE = "ÁÉÍÓÚ"
VOCALES_SIN_TILDE = "AEIOU"

# Inicializamos variables
cadena1 = ""  # cadena original en mayúscula, sin espacios ni tildes
cadena2 = ""  # cadena anterior invertida

# Pedimos datos
cadena = input("Introduce una cadena para comprobar si es palíndroma: ")

# Proceso

# Pasamos a mayúsculas la cadena orginal, quitamos tildes y espacios
cadena1 = cadena.upper().replace(" ",""); # mayúsculas y sin espacios
for i in range(len(VOCALES_CON_TILDE)):  # vocales con tilde
    cadena1 = cadena1.replace(VOCALES_CON_TILDE[i],VOCALES_SIN_TILDE[i])

# Invertimos cadena anterior
cadena2 = cadena1[::-1]

# ¿Es palíndromo?
if cadena1==cadena2:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")

