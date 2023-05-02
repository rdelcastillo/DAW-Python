"""
Ejemplo de lectura de un fichero XML usando ET.

XML es un formato de datos inherentemente jerárquico, y la forma más natural de representarlo es con un árbol.
ET tiene dos clases para este propósito:

- ElementTree que representa todo el documento XML como un árbol.
- Element que representa un solo nodo en este árbol.

Las interacciones con todo el documento (leer y escribir en/desde archivos) se realizan normalmente en el nivel de
ElementTree. Las interacciones con un solo elemento XML y sus sub-elementos se realizan en el nivel Element.

En esta versión "parsearemos" el fichero XML, obtendremos el nodo raíz y lo recorreremos como un árbol usando ciclos.

Autor: Rafael del Castillo Gomariz
"""
import xml.etree.ElementTree as ET

XML_FILE = "libros.xml"

tree = ET.parse(XML_FILE)  # creamos árbol XML (ElementTree)
root = tree.getroot()  # obtenemos nodo raíz

print(f"Etiqueta nodo raíz: {root.tag}\n")

# Leemos los elementos usando ciclos
for book in root:
    print(f"Nodo etiqueta: {book.tag}, atributos: {book.attrib}:")
    for child in book:
        print(f"- {child.tag}: {child.text}")
    print()
