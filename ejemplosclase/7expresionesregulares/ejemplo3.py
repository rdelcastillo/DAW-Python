"""
Ejemplo de uso de los cuantificadores para expresiones regulares greedy, reluctant y possesive que varían el
comportamiento según el número de caracteres que toman para encontrar ocurrencias.

- Greedy (por defecto): intenta obtener el emparejamiento más largo que pueda, si el emparejamiento no es válido
elimina un carácter de la cadena y lo intenta de nuevo.
- Reluctant: funciona al contrario que greedy, intentando inicialmente con ningún carácter, si el emparejamiento no es
válido añade otro y lo intenta de nuevo. Así sucesivamente.
- Possessive: funciona como greedy salvo que si el emparejamiento no es válido no elimina un carácter de la cadena que
se está comprobando y finaliza la comprobación.

Autor: Rafael del Castillo Gomariz
"""

import re

str_to_analyze = "xxyyxxxyxxyxx"

greedy_pattern = re.compile("xx(.*)xx")
reluctant_pattern = re.compile("xx(.*?)xx")
possessive_pattern = re.compile("xx(.*+)xx")

for m in re.findall(greedy_pattern, str_to_analyze):
    print("greedy:", m)

for m in re.findall(reluctant_pattern, str_to_analyze):
    print("reluctant:", m)

for m in re.findall(possessive_pattern, str_to_analyze):
    print("possessive:", m)
