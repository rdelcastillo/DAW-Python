"""
Realiza el control de acceso a una caja fuerte. La combinación será un número de 4 cifras.

El programa nos pedirá la combinación para abrirla. Si no acertamos, se nos mostrará el mensaje
“Lo siento, esa no es la combinación” y si acertamos se nos dirá “La caja fuerte se ha abierto satisfactoriamente”.

Tendremos cuatro oportunidades para abrir la caja fuerte.

Si no se introduce un número o este no tiene cuatro cifras, el programa debe terminar de manera anormal con
un mensaje de error.
"""
import sys

print("Acceso a la caja fuerte")
print("-----------------------")

KEY = "1234"
MAX_ATTEMPTS = 4

for _ in range(MAX_ATTEMPTS):
    key = input("Combinación para abrir la caja fuerte: ")
    if len(key) != len(KEY) or not key.isdigit():   # terminación anormal
        print("ERROR. La longitud de la combinación es errónea o los caracteres no son válidos.", file=sys.stderr)
        exit(1)

    if key == KEY:  # acertamos y terminamos
        print("La caja fuerte se ha abierto satisfactoriamente.")
        exit(0)

    print("Lo siento, esa no es la combinación.")    # si llega aquí la clave es incorrecta, no hace falta 'else'

print("Ha agotado el número de intentos para abrir la caja fuerte")