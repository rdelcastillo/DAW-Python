"""
Ejemplo de distintas formas de leer un fichero.

Este programa funciona sobre un sistema operativo GNU/Linux y la codificación del fichero de texto es UTF-8, para que
funcione en otras codificaciones hay que pasar el parámetro encoding a la función open().

Autor: Rafael del Castillo Gomariz.
"""
print("Distintas formas de leer un fichero en Python")
print("---------------------------------------------")

print("Primera forma: línea a línea (la manera estándar en cualquier lenguaje).\n")

f = open("diccionario.csv", "rt")  # la cabeza de lectura se pone en el primer byte
n = 0
line = f.readline()  # leo bytes desde el principio hasta el primer salto de línea
while line != "":    # mientras no llegue al final del archivo
    # Hemos leído una línea, la procesamos
    n += 1
    print(f"Línea {n}: {line.rstrip()}")  # escribo la línea leída quitando el salto de línea
    # Intentamos leer la siguiente línea, si estoy en el EOF, readline() devolverá ""
    line = f.readline()
f.close()

print("\nSegunda forma:")
print("Leemos el fichero entero, en una sola instrucción, y lo almacenamos en una lista.")
print("Usaremos 'with' para no tener que cerrar el fichero.\n")

with open("diccionario.csv", "rt") as f:
    lines = f.readlines()  # leo todo el fichero y creo una lista con tantos elementos como líneas
    for n, line in enumerate(lines):
        print(f"Línea {n+1}: {line.rstrip()}")

print("\nTercera forma:")
print("Leemos el fichero entero, en una sola instrucción, y lo almacenamos en una variable str.")
print("Capturaremos la excepción por si hay problemas de apertura.\n")

try:
    f = open("diccionario.csv", "rt")
    lines = f.read()  # leo todo el fichero como una cadena de caracteres
    print(lines)
    f.close()
except FileNotFoundError:
    print("No se ha podido abrir el fichero.")

print("Cuarta forma: con un ciclo for.")
print("Además guardaremos los datos en un diccionario.\n")
try:
    d = dict()
    f = open("diccionario.csv", "rt")
    f.readline()  # para que mueva la cabeza de lectura después de la cabecera del csv
    for line in f:
        entry = line.split(",")
        word, translation = entry[0], entry[1]
        d[word] = translation.rstrip()
    f.close()
    print(d)
except FileNotFoundError:
    print("No se ha podido abrir el fichero.")
