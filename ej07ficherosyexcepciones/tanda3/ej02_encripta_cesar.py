"""
Programa que encripte un fichero con el método César que le pasamos como parámetro y almacena el resultado en otro, que
también pasamos como parámetro, de manera que:

- Si el programa no recibe dos parámetros termina con un error 1.
- Si el programa recibe un solo parámetro guardará la información encriptada en el mismo archivo del que lee, pero
  antes advertirá al usuario de que machacará el archivo origen, dando opción a que la operación no se haga.
- Si el fichero origen no existe (da error al abrirlo) el programa termina con un mensaje de error y
  código 2.
- Si en el fichero destino no se puede escribir (da error al abrirlo) el programa termina con un mensaje
  de error y código 3.

Para encriptar usamos el método César, necesitaremos una clave que hay que pedir al usuario.
"""

import sys
from caesar_encryption import CaesarEncryption, CaesarEncryptionError

EXIT_CODE_PARAMS_ERROR = 1
EXIT_CODE_FILE_READ_ERROR = 2
EXIT_CODE_FILE_WRITE_ERROR = 3

def main():
    exit_if_wrong_number_of_parameters()

    source_filename, destination_filename = get_filenames()
    scrolling = input_scrolling_caesar()

    try:
        CaesarEncryption.encrypt_file(source_filename, destination_filename, scrolling)
    except CaesarEncryptionError as e:
        print(f"No se ha podido realizar la operación, se ha generado una excepción:\n{e}", file=sys.stderr)
        exit(EXIT_CODE_FILE_READ_ERROR if source_filename in str(e) else EXIT_CODE_FILE_WRITE_ERROR)

    print("Proceso concluido")


def exit_if_wrong_number_of_parameters():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Error en el número de parámetros", file=sys.stderr)
        exit(EXIT_CODE_PARAMS_ERROR)


def get_filenames():

    def exit_if_user_not_want_overwrite_file():
        print("Tenga en cuenta que solo ha indicado un nombre de archivo:", source_filename)
        print("Está operación machacará los datos de", source_filename)
        while True:
            resp = input("¿Continuamos con la operación? (S/N) ").upper()
            if resp in ["S", "N"]:
                break
        if resp == "N":
            exit(0)

    source_filename = sys.argv[1]
    if len(sys.argv) == 2:
        destination_filename = source_filename
        exit_if_user_not_want_overwrite_file()
    else:
        destination_filename = sys.argv[2]

    return source_filename, destination_filename


def input_scrolling_caesar():
    while True:
        try:
            return int(input("Desplazamiento para la encriptación usando César: "))
        except ValueError:
            print("Tiene que introducir un valor entero.")


if __name__ == '__main__':
    main()
