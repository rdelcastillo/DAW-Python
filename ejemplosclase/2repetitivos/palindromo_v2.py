"""
Este programa pide una cadena al usuario y nos dice si es palíndroma.

Ejemplo: Dábale arroz a la zorra el abad

En esta versión no construimos otra cadena y nos recorremos la misma cadena desde el inicio y el final.
"""
VOWELS_WITH_TILDE = "áéíóú"
VOWELS = "aeiou"

string = input("Dame una cadena de caracteres y te diré si es palíndroma: ")

# Construir cadena sin caracteres especiales y en minúsculas
string_to_check = ""
for c in string.lower():
    if c != ' ':
        if c in VOWELS_WITH_TILDE:  # ¿c lleva tilde?
            index_vowel = VOWELS_WITH_TILDE.find(c)
            c = VOWELS[index_vowel]
        string_to_check += c

# índices por el principio y el final
i, j = 0, len(string_to_check)-1

while i < j and string_to_check[i] != string_to_check[j]:
    i += 1
    j -= 1

# ¿Es palíndromo?
if i >= j:
    print(f"La cadena {string} es PALÍNDROMA")
else:
    print(f"La cadena {string} NO es palíndroma")