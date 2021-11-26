"""
Creado el 14 dic. 2018

Pide un DNI y comprueba que es correcto, será correcto si tiene 9 caracteres y la letra es correcta.

Para calcular la letra se divide el número entre 23 y el resto indica la posición de la cadena de letras:
"TRWAGMYFPDXBNJZSQVHLCKE"

Usar una función para validar el DNI y otra que te devuelva la letra del mismo

Autor: Rafael del Castillo
"""


# ---------
# Funciones
# ---------

def dni_correcto(dni):
    """
    Valida el DNI.

    El DNI será válido cuando tenga nueve caracteres, los ocho primeros
    sean números y la letra sea correcta.
    """

    return len(dni) == 9 and dni[:8].isdecimal() and letra_dni_correcta(dni)


def letra_dni_correcta(dni):
    """
    Valida la letra del DNI pasado como parámetro.

    La letra será válida si coincide con la letra resultante de usar el índice del
    resto de la división del número del DNI entre 23 para la cadena de letras:
    "TRWAGMYFPDXBNJZSQVHLCKE"
    """

    num_dni = int(dni[:8])
    letra_dni = dni[8].upper()
    return letra_dni == "TRWAGMYFPDXBNJZSQVHLCKE"[num_dni % 23]


# ---------
# Principal
# ---------

if __name__ == "__main__":
    dni = input("Dame un DNI: ")
    if dni_correcto(dni):
        print("El DNI", dni, "es válido")
    else:
        print("El DNI", dni, "es incorrecto")
