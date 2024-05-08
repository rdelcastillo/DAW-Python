"""
Programa que ordena alfabéticamente las palabras contenidas en un fichero de texto.

El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos.

El nombre del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo
palabras_sort.txt.

Suponemos que cada palabra ocupa una línea.

Mejoramos la versión anterior
"""
import sys

def main():
    filename_source, filename_target = read_filenames()

    words = read_sorted_words(filename_source)
    write_words(words, filename_target)

    print('Proceso concluido.')

def read_sorted_words(filename):
    try:
        with open(filename) as file:
            words = file.readlines()
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print(f"No puedo leer el fichero {filename}. Error: {e}", file=sys.stderr)
        exit(4)

    words = sorted([word.rstrip() for word in words])
    return words

def write_words(words, filename):
    try:
        with open(filename, 'xt') as file:
            for word in words:
                print(f'{word}', file=file)
    except (FileNotFoundError, PermissionError, IsADirectoryError, FileExistsError) as e:
        print(f'No se ha podido hacer la operación. Excepción {e}', file=sys.stderr)
        exit(1)

def read_filenames():
    check_args()
    filename_source = sys.argv[1]
    filename_target = filename_source[:-4] + '_sort.txt'
    return filename_source, filename_target

def check_args():
    if len(sys.argv) != 2:
        print("No ha llamado al programa con los argumentos correctos.", file=sys.stderr)
        exit(2)
    if not sys.argv[1].endswith('.txt'):
        print("El nombre del fichero pasado no tiene extensión txt.", file=sys.stderr)
        exit(3)

if __name__ == '__main__':
    main()