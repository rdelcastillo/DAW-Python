"""
Ejemplo de lectura de un fichero XML usando ET.

En esta versión usaremos algunos métodos útiles de Element que permitirán buscar directamente por etiquetas.

- Element.iter(): itera recursivamente sobre todo el sub-árbol por debajo de él (sus hijos, los hijos de sus hijos...)
- Element.findall(): encuentra sólo los elementos con una etiqueta que son hijos directos del elemento actual.
- Element.find():

Autor: Rafael del Castillo Gomariz
"""
import xml.etree.ElementTree as ET

XML_FILE = "libros.xml"

tree = ET.parse(XML_FILE)
root = tree.getroot()

# Buscamos todos los libros
for book in root.findall('book'):
    print(f"Libro de género: {book.attrib['category']}")
    for element in book:
        print(f"- {element.tag}: {element.text}")
    print()

# Buscamos todos títulos (no se puede usar findall aquí)
print("Títulos de libros:")
for title in root.iter("title"):
    print("-", title.text)
