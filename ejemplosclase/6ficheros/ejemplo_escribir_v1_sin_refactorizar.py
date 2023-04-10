"""
Ejemplo de escribir en un fichero. Crearemos un diccionario castellano - inglés en formato CSV.

Este programa funciona sobre un sistema operativo GNU/Linux y la codificación del fichero de texto es UTF-8, para que
funcione en otras codificaciones hay que pasar el parámetro encoding a la función open().

Este programa se puede (y debe) refactorizarse.

Autor: Rafael del Castillo Gomariz.
"""
import sys

print("Creación de un diccionario castellano - inglés")
print("----------------------------------------------")

filename = input("Nombre del fichero para guardar el diccionario: ")

# Comprobamos si el fichero existe, en ese caso, preguntamos al usuario si quiere sobreescribirlo
try:
    f = open(filename, "rt")
    # si llego aquí el fichero existe, pregunto si sobreescribimos
    f.close()
    while True:
        resp = input("El fichero ya existe ¿sobreescribimos? (S/N) ").upper()
        if resp == "N":
            print("Programa abortado...", file=sys.stderr)
            exit(1)
        elif resp == "S":
            break
        else:
            print("Debe responder S o N")

except FileNotFoundError:
    pass

# Creo mi diccionario
try:
    f = open(filename, "wt")
    print("Palabra,Traducción", file=f)  # Creo la cabecera del CSV
    while True:
        # Pido palabra en castellano y su traducción
        spanish_word = input("Dame una palabra en castellano: ")
        english_word = input("Dame la traducción en inglés: ")
        f.write(f"{spanish_word},{english_word}\n")

        # Pregunto si quiere continuar (fíjate que copio y pego código anterior, no es recomendable)
        while True:
            resp = input("¿Quiere continuar añadiendo palabras al diccionario? (S/N) ").upper()
            if resp == "N" or resp == "S":
                break
            print("Debe responder S o N")

        # Si no quiere continuar, salgo del bucle
        if resp == "N":
            break

    f.close()
    print("Diccionario guardado.")

except PermissionError | FileNotFoundError | ValueError:
    print(f"No se puede escribir en {filename}", file=sys.stderr)
    exit(2)