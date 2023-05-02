"""
Programa que desencripte un fichero con el método César que le pasamos como parámetro y almacena el resultado en otro,
que también pasamos como parámetro, de manera que:

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
from ej02_encripta_cesar import exit_if_wrong_number_of_parameters, get_filenames, input_scrolling_caesar, \
    EXIT_CODE_FILE_WRITE_ERROR, EXIT_CODE_FILE_READ_ERROR


def main():
    exit_if_wrong_number_of_parameters()

    source_filename, destination_filename = get_filenames()
    scrolling = input_scrolling_caesar()

    try:
        CaesarEncryption.encrypt_file(source_filename, destination_filename, -scrolling)
    except CaesarEncryptionError as e:
        print(f"No se ha podido realizar la operación, se ha generado una excepción:\n{e}", file=sys.stderr)
        exit(EXIT_CODE_FILE_READ_ERROR if source_filename in str(e) else EXIT_CODE_FILE_WRITE_ERROR)

    print("Proceso concluido")


if __name__ == '__main__':
    main()
