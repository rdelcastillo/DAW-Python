"""
Función que recibe un número, lo convierte al sistema Morse y lo devuelve en una cadena de caracteres.

Por ejemplo, el 213 es el ..___ .____ ...__ en Morse.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Los números en Morse los puedes encontrar aquí: https://morsecw.com/alfabeto.html#numeros

Podemos testear el funcionamiento con este traductor https://morsedecoder.com/es/

Autor: Rafael del Castillo Gomariz
Fecha: 11/12/2022
"""
MINUS = "-....-"
DECIMAL_POINT = ".-.-.-"
DIGITS = ["-----", ".----", "..---", "...--", "....-", ".....", "-....", "--...", "---..", "----."]
SEP = " "

def morse(n):
    if not isinstance(n, int | float):  # si no es un número lanzamos una excepción
        raise TypeError(f"{n} no es un número.")

    n_in_morse = "" if n >= 0 else MINUS + SEP  # empieza con signo - si es un número negativo
    n_to_convert = abs(n)

    # parte entera del número
    for digit in str(int(n_to_convert)):
        n_in_morse += DIGITS[int(digit)] + SEP

    # parte decimal (si hay)
    if isinstance(n, float):
        n_in_morse += DECIMAL_POINT + SEP
        n_decimal_part = str(n_to_convert - int(n_to_convert))[2:]  # cadena de decimales (obviamos el 0.)
        for digit in n_decimal_part:
            n_in_morse += DIGITS[int(digit)] + SEP

    n_in_morse = n_in_morse[:-1]  # quitamos el separador final
    return n_in_morse
