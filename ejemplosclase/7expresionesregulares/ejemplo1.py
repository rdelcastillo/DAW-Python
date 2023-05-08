"""
Ejemplos con expresiones regulares en Python.

Autor: Rafael del Castillo Gomariz
"""

import re

def test(regex, string):  # comprueba si string encaja con la expresión regular regex
    print(f"Cadena: {string}.\t")
    print(f"Patrón expresión regular: /{regex}/\t")
    print("ENCAJA.\n") if re.search(regex, string) else print("NO ENCAJA.\n")


"""
Expresión regular para fecha.

Imaginemos la fecha en formato dd/mm/yyyy. Son grupos de dos cifras separadas por barras. 
En una expresión regular \d representa una cifra. El día pueden ser una o dos cifras, es decir \d{1,2}, el mes igual y 
el año vamos a obligar que sean cuatro cifras exactamente \d{4}

Si queremos comprobar que una cadena leída por teclado cumple ese patrón podemos usar la función re.search pasándole
la expresión regular del patrón que queremos que cumpla nuestra cadena y la cadena, nos devolverá un objeto Match si la 
cumple o None en caso contrario,
"""

regex_date1 = "^\d{1,2}/\d{1,2}/\d{4}$"  # patrón para que la cadena sea exactamente una fecha

# Lo siguiente encaja con el patrón
test(regex_date1, "55/12/2014")
test(regex_date1, "11/12/2014")
test(regex_date1, "1/12/2014")
test(regex_date1, "11/2/2014")

# Lo siguiente no encaja
test(regex_date1, "11/12/14")  # el año no tiene cuatro cifras
test(regex_date1, "11//2014")  # el mes no tiene una o dos cifras
test(regex_date1, "11/12/14perico")  # sobra "perico"

"""
Supongamos que queremos que el mes se exprese como "ene", "feb", "mar", ... en vez de como un número. 
Cuando hay varias posibles cadenas válidas, en la expresión regular se ponen entre paréntesis y separadas por |. 
Es decir, algo como esto (ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic). 

Si además nos da igual mayúsculas o minúsculas, justo delante ponemos el flag de case insensitive (?i) 
(la 'i' es de ignore case)
"""

regex_date2 = "(?i)^\d{1,2}/(ene|feb|mar|abr|may|jun|jul|ago|sep|oct|nov|dic)/\d{4}$"

# Lo siguiente encaja con el patrón
test(regex_date2, "11/dic/2014")
test(regex_date2, "1/nov/2014")
test(regex_date2, "1/AGO/2014")   # mes en mayúsculas
test(regex_date2, "21/Oct/2014")  # primera letra del mes en mayúsculas.

# Lo siguiente no encaja
test(regex_date2, "11/abc/2014")   # abc no es un mes
test(regex_date2, "11//2014")      # falta el mes
test(regex_date2, "11/jul/2014perico")   # sobra perico

"""
Expresión regular para DNI.

El DNI (o NIF) lleva un número único y sirve para identificar a la persona. Este número son 8 cifras seguidas de una 
letra, que normalmente se escribe en mayúscula. Esta letra es una especie de checksum de las cifras anteriores.

Quedan excluidas las letras 'I', 'O' y 'U'. 
Las dos primeras por poder confundirse con uno y cero respectivamente. La tercera por algún extraño motivo.

Una expresión regular no va a realizar el checksum, pero sí nos puede ayudar a hacer una primera comprobación: 
8 cifras y una letra mayúscula. La expresión regular puede ser así \d{8}[A-HJ-NP-TV-Z]
"""

regex_dni = "^\d{8}[A-HJ-NP-TV-Z]$"

# Lo siguiente encaja con el patrón
test(regex_dni, "01234567C")

# Lo siguiente no encaja
test(regex_dni, "01234567U")    # La U no es válida
test(regex_dni, "0123567X")     # No tiene 8 cifras

"""
Expresión regular para email.

No existe una expresión regular para email que sea 100% fiable, hay muchos formatos válidos y muy complejos. 

Aquí vamos como una expresión regular más o menos sencilla: [^@]+@[^@]+\.[a-zA-Z]{2,}. 
"""

regex_email = "^[^@]+@[^@]+\.[a-zA-Z]{2,}$"

# Lo siguiente encaja con el patrón
test(regex_email, "a@b.com")
test(regex_email, "+++@+++.com")

# Lo siguiente no encaja
test(regex_email, "@b.com")      # Falta el nombre
test(regex_email, "a@b.c")       # El dominio final debe tener al menos dos letras
