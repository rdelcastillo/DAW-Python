import string


def encripta_cesar(cadena, desplazamiento):
    """
    Encripta la cadena recibida como parámetro.
    :param cadena:
    :param desplazamiento:
    :return: carácter encriptado
    """
    letras = string.ascii_letters + "áéíóúüñÁÉÍÓÚÜÑ"
    cadena_encriptada = ""
    for caracter in cadena:
        # si el carácter es alfabético, encriptamos
        if caracter in letras:
            posicion_donde_esta = letras.index(caracter)
            posicion_caracter_encriptado = (posicion_donde_esta + desplazamiento) % len(letras)
            caracter_encriptado = letras[posicion_caracter_encriptado]
        else:
            caracter_encriptado = caracter
        # añadimos a la cadena encriptada
        cadena_encriptada += caracter_encriptado
    return cadena_encriptada


while True:
    cadena = input("Cadena: ")
    print(encripta_cesar(cadena, -3000))
