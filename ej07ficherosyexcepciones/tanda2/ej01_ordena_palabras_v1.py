"""
Programa que ordena alfabéticamente las palabras contenidas en un fichero de texto.

El nombre del fichero que contiene las palabras se debe pasar como argumento en la línea de comandos.

El nombre del fichero resultado debe ser el mismo que el original añadiendo la coletilla sort, por ejemplo
palabras_sort.txt.

Suponemos que cada palabra ocupa una línea.
"""
import sys

def main():
    filename_source, filename_target = read_filenames()

    try:
        # Leo las palabras, las guardo en una lista y las ordeno
        with open(filename_source) as file:  # por defecto abre como 'rt'
            words = file.readlines()
            for i in range(len(words)):
                words[i] = words[i].rstrip()
            words.sort()
            # Las tres líneas de arriba podrían resumirse en:
            # words = sorted([word.rstrip() for word in words])

        # Escribo en el fichero
        with open(filename_target, 'xt') as file:
            for word in words:
                print(f'{word}', file=file)

    except (FileNotFoundError, PermissionError, IsADirectoryError, FileExistsError) as e:
        print(f'No se ha podido hacer la operación. Excepción {e}', file=sys.stderr)
        exit(1)

    print('Proceso concluido.')

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