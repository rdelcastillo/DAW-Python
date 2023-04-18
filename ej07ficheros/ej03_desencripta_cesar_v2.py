"""
Haz un programa que reciba como parámetro un fichero encriptado con el método César y y almacene el resultado en otro,
que también pasamos como parámetro, de manera que:

- Si el programa no recibe dos parámetros termina con un error 1.
- Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero antes
  advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
- Si el fichero origen no existe (da error al abrirlo como lectura) el programa termina con un mensaje de error y
  código 2.
- Si en el fichero destino no se puede escribir da error al abrirlo como lectura) el programa termina con un mensaje de
  error y código 3.

En esta versión buscamos la clave de desencriptación.

Probaremos a desencriptar automáticamente empezando por el desplazamiento 1 y continuando hasta el último posible.

Para comprobar si se ha desencriptado bien consultaremos un número máximo de palabras a la RAE (no lo haremos con todas
para agilizar) y estableceremos un porcentaje de éxito (palabras que estén en la RAE) a partir del cual consideramos
que no hay error.
"""

import sys
import string
import requests

MAX_PALABRAS = 25
PORCENTAJE_EXITO = 0.75
LETRAS = string.ascii_letters + "áéíóúüñÁÉÍÓÚÜÑ"


# ---------
# FUNCIONES
# ---------

# Funciones relativas a la desencriptación
# ----------------------------------------
def desencripta(lista_encriptada, desplazamiento):
    """
    Desencripta la lista recibida.
    :param lista_encriptada:
    :param desplazamiento:
    :return: lista desencriptada.
    """
    lista_desencriptada = []
    for linea in lista_encriptada:
        lista_desencriptada.append(desencripta_cesar(linea, desplazamiento))
    return lista_desencriptada


def desencripta_cesar(cadena, desplazamiento):
    """
    Desencripta la cadena recibida como parámetro.
    :param cadena:
    :param desplazamiento: desplazamiento César
    :return: carácter encriptado
    """
    cadena_desencriptada = ""
    for caracter in cadena:
        # si el carácter es alfabético, encriptamos
        if caracter in LETRAS:
            posicion_donde_esta = LETRAS.index(caracter)
            posicion_caracter_desencriptado = (posicion_donde_esta - desplazamiento) % len(LETRAS)
            if posicion_caracter_desencriptado < 0:
                posicion_caracter_desencriptado = len(LETRAS) + posicion_caracter_desencriptado
            caracter = LETRAS[posicion_caracter_desencriptado]
        # añadimos a la cadena encriptada
        cadena_desencriptada += caracter
    return cadena_desencriptada


# Funciones relativas a buscar en la RAE
# --------------------------------------
def palabras_en_rae(lista, max_palabras):
    """
    Devuelve el porcentaje de palabras que están en la RAE.
    :param lista: lista de cadenas de caracteres.
    :param max_palabras: máximo de palabras a procesar.
    :return: porcentaje (entre 0 y 1) de acierto
    """
    palabras = []
    aciertos = 0

    # separo las palabras de cada línea y las añado
    for linea in lista:
        palabras.extend(lista_palabras(linea))  # el método extend permite "extender" una lista con otra
        # ¿tenemos palabras suficientes?
        if len(palabras) >= max_palabras:
            palabras = palabras[:max_palabras]  # recortamos si es necesario
            break

    # compruebo las palabras
    for palabra in palabras:
        if palabra_en_rae(palabra):
            aciertos += 1

    return aciertos / len(palabras)  # devuelvo tasa de aciertos


def lista_palabras(cadena):
    """
    :param cadena:
    :return: lista de palabras (con caracteres alfabéticos) que hay en cadena
    """
    palabras = []
    palabra = ""

    # recorro cada carácter de la cadena, si es alfabético es parte de la palabra, si no lo es la palabra acaba
    for caracter in cadena:
        if caracter in LETRAS:
            palabra += caracter
        elif palabra != "":
            palabras.append(palabra)
            palabra = ""

    return palabras


def palabra_en_rae(palabra):
    """
    Busca en rae.es la palabra pasada como parámetro.
    Consideramos que si PALABRA no está, en la url devuelta aparecerá:

        Aviso: <span>La palabra <b>PALABRA</b> no está en el Diccionario.

    :param palabra:
    :return: verdadero si está, falso si no está.
    """
    # Hacemos la petición
    response = requests.get("https://dle.rae.es/?w=" + palabra)
    if response.status_code != 200:
        print("Error al acceder a la RAE.", file=sys.stderr)
        exit(5)

    # Devolvemos si la cadena NO se encuentra en la url
    return not "Aviso: <span>La palabra <b>" + palabra + "</b> no está en el Diccionario." in response.text


# ---------
# PRINCIPAL
# ---------

# ¿Número de parámetros correcto?
if len(sys.argv) == 1 or len(sys.argv) > 3:
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
    print("No se ha podido abrir", fichero_origen, file=sys.stderr)
    exit(3)

# Leemos fichero origen
origen = manejador_origen.readlines()
manejador_origen.close()

# Probamos desplazamientos
solucion_encontrada = False
for desplazamiento in range(len(LETRAS)):
    print("Probando con desplazamiento", desplazamiento, "...")
    posible_solucion = desencripta(origen, desplazamiento)
    if palabras_en_rae(posible_solucion, MAX_PALABRAS) >= PORCENTAJE_EXITO:
        solucion_encontrada = True
        break

# ¿Ha habido éxito? Si no es así terminamos
if not solucion_encontrada:
    print("No se ha podido desencriptar el archivo.", file=sys.stderr)
    exit(4)

# Abrimos fichero destino (con la información desencriptada)
try:  # ¿puedo escribir en el fichero?
    manejador_destino = open(fichero_destino, "w")
except PermissionError or FileNotFoundError:
    print("No se ha podido abrir para escritura", fichero_origen, file=sys.stderr)
    exit(2)

# Escribimos
for linea in posible_solucion:
    manejador_destino.write(linea)
manejador_destino.close()

print(f"Proceso concluido, el desplazamiento usado fue {desplazamiento}.")
