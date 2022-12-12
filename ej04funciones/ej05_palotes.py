"""
Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres.

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes.

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por
pantalla, solo se debe usar print desde el programa principal.

Autor: Rafael del Castillo Gomariz
Fecha: 11/12/2022
"""


def palotes(n):
    # si el número no es entero, 0 o positivo lanzamos una excepción
    if not isinstance(n, int) or n < 0:
        raise ValueError(f"{n} no puede ser convertido al sistema de palotes.")

    # proceso de conversión
    n_en_palotes = ""
    for d in str(n):
        n_en_palotes += "|" * int(d) + " - "

    # devolvemos sin guion y espacios del final
    return n_en_palotes[:-3]