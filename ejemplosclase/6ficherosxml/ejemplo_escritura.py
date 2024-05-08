"""
Ejemplo de escritura en un fichero XML usando ET.

Añadiremos un nuevo libro a libros.xml

Autor: Rafael del Castillo Gomariz
"""
import xml.etree.ElementTree as ET

# Creamos árbol y sacamos la raíz
XML_FILE = "libros.xml"
tree = ET.parse(XML_FILE)
root = tree.getroot()

# Pedimos datos
print("Adición de libros a la biblioteca")
print("---------------------------------")

title = input("Título del libro: ")
genre = input("Género del libro: ").upper()
author = input("Autor/a del libro: ")
isbn = input("ISBN del libro: ")

# Creamos el libro y lo ponemos en el árbol xml
book = ET.Element('book', {'category':genre})
ET.SubElement(book, 'title').text = title
ET.SubElement(book, 'author').text = author
ET.SubElement(book, 'isbn').text = isbn
root.append(book)

# Escribimos los datos en el fichero
tree.write(XML_FILE, encoding='unicode')

"""
La salida del archivo no es "bonita", está sin formatear, podríamos solucionarlo con estas instrucciones:

from xml.dom import minidom

xml_minidom = minidom.parseString(ET.tostring(root))
xml_str = xml_minidom.toprettyxml()

# Escribir el XML formateado en un archivo
with open(XML_FILE, 'w') as xml_file:
    xml_file.write(xml_str)
"""