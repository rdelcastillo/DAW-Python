"""
Una vez que vemos la forma de ver si una cadena cumple el patrón, podemos querer extraer parte de ese patrón, por 
ejemplo, las cifras de la fecha (día, mes y año). 

Nuevamente, las expresiones regulares de java nos ayudan. Cambiemos el ejemplo. Queremos extraer los sumandos y el
resultado de una cadena así "xxxx+yyyy=zzzzz" donde x, y y z representan dígitos y pueden ser en cualquier número.
 
Con \d+ indicamos uno o más dígitos. La expresión regular para ver si una cadena cumple ese patrón puede ser 
"\d+\+\d+=\d+". 

Puesto que el + tiene un sentido especial en los patrones -indica uno o más-, para ver si hay un "+" en la cadena,
tenemos que "escaparlo", por eso el \ delante.

Las partes que queramos extraer, debemos meterlas entre paréntesis.

Así, la expresión regular quedaría "(\d+)\+(\d+)=(\d+)".

Fuente: http://chuwiki.chuidiang.org/index.php?title=Expresiones_Regulares_en_Java

Autor: Rafael del Castillo Gomariz
"""

import re

str_to_analyze = "23+12=35"
regex = "(\d+)\+(\d+)=(\d+)"
match = re.search(regex, str_to_analyze)

# Buscamos las partes (será 23, 12 y 35)
for n in match.groups():
    print(n)

"""
En la cadena “<a>uno</a><b>dos</b><c>tres</c>” queremos extraer usando expresiones regulares los trozos que hay entre 
los tags <a>, <b> y <c>, es decir, "uno", "dos" y "tres".
"""

regex = "<[^>]*>([^<]*)</[^>]*>"
str_to_analyze = "<a>uno</a><b>dos</b><c>tres</c>"
for str_ in re.findall(regex, str_to_analyze):
  print(str_)
