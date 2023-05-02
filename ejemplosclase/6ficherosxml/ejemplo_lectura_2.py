"""
Ejemplo de lectura de un fichero XML usando ET.

En esta versión leeremos el fichero XML en una cadena y desde la misma construiremos el árbol, obtendremos el nodo raíz
y accederemos a los libros como si fuesen elementos de listas.

Autor: Rafael del Castillo Gomariz
"""
import xml.etree.ElementTree as ET

XML_FILE = "libros.xml"

with open(XML_FILE) as xml_file:  # Otra forma de obtener el nodo raíz, leer todo el fichero en una cadena y procesarla
    xml_str = xml_file.read()
root = ET.fromstring(xml_str)

for i in range(len(root)):  # los hijos están anidados, y podemos acceder a nodos hijos específicos por el índice
    print(f"Libro de género: {root[i].attrib['category']}")
    for j in range(len(root[i])):
        print(f"- {root[i][j].tag}: {root[i][j].text}")
    print()
