"""
Programa que encripte un fichero que le pasamos como parámetro y almacena el resultado en otro, que también
pasamos como parámetro, de manera que:

- Si el programa no recibe dos parámetros termina con un error 1.
- Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
  antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
- Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
  código 2.
- Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje
  de error y código 2.

Para encriptar usamos el método César, necesitaremos una clave que hay que pedir al usuario.
"""

import sys
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


# ¿Número de parámetros correcto?
if len(sys.argv) < 2 or len(sys.argv) > 3:
    # mandamos el mensaje a la salida de error: sys.stderr (Por defecto: sys.stdout)
    print("Error en el número de parámetros", file=sys.stderr)
    exit(1)

# Averiguamos fichero origen y destino
fichero_origen = sys.argv[1]
if len(sys.argv) == 2:
    fichero_destino = fichero_origen
    # Advertimos de que se machacará el archivo
    print("Tenga en cuenta que solo ha indicado un nombre de archivo:", fichero_origen)
    print("Está operación machacará los datos de", fichero_origen)
    while True:
        resp = input("¿Continuamos con la operación? (S/N) ").upper()
        if resp in ["S", "N"]:
            break
    if resp == "N":
        exit(0)
else:
    fichero_destino = sys.argv[2]

# Abrimos fichero origen
try:  # ¿existe el fichero?
    manejador_origen = open(fichero_origen, "r")
except FileNotFoundError:
    print("No se ha podido abrir", fichero_origen)
    exit(2)

# Pedimos desplazamiento para el método César
while True:
    try:
        desplazamiento = int(input("Desplazamiento para la encriptación usando César: "))
    except ValueError:
        print("Tiene que introducir un valor entero.")
    else:
        break

# Leemos fichero origen
origen = manejador_origen.readlines()
manejador_origen.close()

# Abrimos fichero destino (a encriptar)
try:  # ¿puedo escribir en el fichero?
    manejador_destino = open(fichero_destino, "w")
except PermissionError or FileNotFoundError:
    print("No se ha podido abrir para escritura", fichero_origen)
    exit(2)

# Encriptamos y escribimos
for linea in origen:
    manejador_destino.write(encripta_cesar(linea, desplazamiento))
manejador_destino.close()
