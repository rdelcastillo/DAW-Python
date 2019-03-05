"""
<p>Programa que pide caracteres e imprime 'VOCAL' si son vocales y 'NO VOCAL'
en caso contrario, el programa termina cuando se introduce un espacio.</p>

<p>Análisis</p>
<ul>
<li>Leer un carácter hasta que sea el espacio.
<li>Si el carácter no es espacio -> si es una vocal -> Muestro "Es vocal"
<li>Si no muestro "No es vocal"
</ul>
<p>Datos de entrada:vamos leyendo un carácter.</p>
<p>Información de salida:Mensajes: "Es vocal", "No es vocal"</p>
<p>Variables:car (caracter)</p>

<p>Diseño</p>
<ol>
<li>Repetir -> Leer carácter hasta que sea un sólo carácter
<li>Mientras no sea espacio
<li>Si car no es el espacio
<li>Si es A,E,I,O,U o a,e,i,o,u -> Mostrar "Es vocal"
<li>Si no mostrar "No es vocal"
<li>Repetir -> Leer carácter hasta que sea un sólo carácter
</ol>

<strong>author</strong> Rafael del Castillo
"""

# ---------
# Funciones
# ---------

def caracter():
    """Pide un solo carácter y comprueba si se ha introducido correctamente,
    si no es así lo pide de nuevo.
    
    <strong>devuelve:</strong> <cod>String</code> de longitud 1

    """
    while True:
        car = input("Introduce un carácter: ")
        if not (len(car)!=1): break
    return car

def es_vocal(c):
    """Comprueba si una cadena es vocal o no.

    <strong>parámetros</strong> <em>c</em>: una cadena de caracteres
    
    <strong>devuelve:</strong> <code>true</code> si la cadena es vocal y <code>false</code> en caso contrario

    """
    c = c.upper()
    return c in "AEIOUÁÉÍÓÚ" and len(c)==1

# ---------
# Principal
# ---------
if __name__ == "__main__":
    # Pedimos un solo carácter y si no se introduce lo pedimos de nuevo
    car = caracter()
 
    #Proceso
    while car!=" ":
        if es_vocal(car):
            print("VOCAL")
        else:
            print("NO VOCAL")
        # Pedimos otro carácter
        car = caracter()
