"""
Programa que recibe una url y el nombre de una etiqueta html. Si la url es válida muestra por la pantalla el contenido
de cada etiqueta y el número de ocurrencias de la misma.

Ejemplo: si ejecuto python mi_programa.py https://example.com/ p

La salida sería:
---------------------------------------------------------------------------------------------------------------------
Ocurrencia nº 1:
This domain is for use in illustrative examples in documents. You may use this domain in literature without prior
coordination or asking for permission.

Ocurrencia nº 2:
<a href="https://www.iana.org/domains/example">More information...</a>

Número de etiquetas p encontradas: 2
---------------------------------------------------------------------------------------------------------------------

Autor: Rafael del Castillo
"""
import re
import sys
import requests


def main():
    check_args()
    url, label = sys.argv[1], sys.argv[2]

    html = get_html(url)
    print_labels(label, html)


def check_args():
    if len(sys.argv) != 3:
        print("Error en el número de argumentos. La sintaxis correcta es <PROGRAMA> <URL> <ETIQUETA HTML>", file=sys.stderr)
        exit(1)


def get_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Error al hacer la petición:", response.status_code)
        exit(1)
    return response.text


def print_labels(label, html):
    print(f"HTML donde buscar la etiqueta <{label}>")
    print(f"-------------------------------{'-' * (len(label) + 1)}")
    print(html + "\n")

    print("Resultados")
    print("----------")

    regex = re.compile(f"<{label}[^>]*>(.*?)</{label}>", re.DOTALL)
    matches = regex.findall(html)
    for n, m in enumerate(matches):
       print(f"- Ocurrencia nº {n+1}:\n{m}\n")
    print(f"\nTotal etiquetas <{label}> encontradas: {n+1}")


if __name__ == '__main__':
    main()
