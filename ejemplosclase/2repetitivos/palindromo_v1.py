"""
Este programa pide una cadena al usuario y nos dice si es palíndroma.

Ejemplo: Dábale arroz a la zorra el abad

En esta versión construimos otra cadena sin espacios, tildes y en mayúscula.
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

# Construir al revés la cadena a chequear
reverse_string_to_check = ""
for i in range(len(string_to_check)-1, -1, -1):
    reverse_string_to_check += string_to_check[i]

# ¿Es palíndromo?
if string_to_check == reverse_string_to_check:
    print(f"La cadena {string} es PALÍNDROMA")
else:
    print(f"La cadena {string} NO es palíndroma")