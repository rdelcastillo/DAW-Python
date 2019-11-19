"""
Comprobamos si hay una subcadena dentro de una cadena usando ciclos y obviando los métodos de Python
para ello.

Análisis:
---------
Para comprobar si una cadena es subcadena de otra iremos desplazando un índice y comparando la subcadena que se inicia
en ese índice con tantos caracteres como la cadena a comprobar con esa misma cadena. Si no es igual pasamos al índice
siguiente y así seguimos hasta que la encontremos o ya no podamos comparar más.

Ejemplo1: la subcadena está en la cadena.

cadena: "Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo"
subcadena: "cosas"

 0 --> "Dos c" != "cosas" (seguimos)
"Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo"
 ~~~~~ (subcadena tiene una longitud de 5)
  1 --> "os co" != "cosas" (seguimos)
"Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo"
  ~~~~~
   2 --> "s cos" != "cosas" (seguimos)
"Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo"
   ~~~~~
    3 --> " cosa" != "cosas" (seguimos)
"Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo"
    ~~~~~
     4 --> "cosas" == "cosas" (terminamos)
"Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo"
     ~~~~~
Resumen:
Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo
cosas       (0)
Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo
 cosas      (1)
Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo
  cosas     (2)
Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo
   cosas    (3)
Dos cosas son infinitas: el universo y la estupidez humana; y yo no estoy seguro sobre el universo
    cosas   (4 --> coincide)

Ejemplo2: la subcadena NO está en la cadena.

cadena: "¿Qué dice .GIF a .JPG?"
subcadena: "¡Anímate coleguita!"

 0 --> "¿Qué dice .GIF a .J" != "¡Anímate coleguita!" (seguimos)
"¿Qué dice .GIF a .JPG?"
 ~~~~~~~~~~~~~~~~~~~ (subcadena tiene una longitud de 19)
  1 --> "Qué dice .GIF a .JP" != "¡Anímate coleguita!" (seguimos)
"¿Qué dice .GIF a .JPG?"
  ~~~~~~~~~~~~~~~~~~~
   2 --> "ué dice .GIF a .JPG" != "¡Anímate coleguita!" (seguimos)
"¿Qué dice .GIF a .JPG?"
   ~~~~~~~~~~~~~~~~~~~
    3 --> "é dice .GIF a .JPG?" != "¡Anímate coleguita!" (terminamos, la subcadena no está, se han hecho 4 iteraciones,
                                                          la diferencia+1 entre la longitud de ambas cadenas)
"¿Qué dice .GIF a .JPG?"
    ~~~~~~~~~~~~~~~~~~~
Resumen:
¿Qué dice .GIF a .JPG
¡Anímate coleguita!     (0)
¿Qué dice .GIF a .JPG
 ¡Anímate coleguita!    (1)
¿Qué dice .GIF a .JPG
  ¡Anímate coleguita!   (2)
¿Qué dice .GIF a .JPG
   ¡Anímate coleguita!  (3 --> no es una subcadena)

Variables a usar:
- esta_subcadena: interruptor o indicador (switch) que servirá para terminar si la subcadena se encuentra.
- i: índice para moverse en la cadena.
- cadena: la cadena que tiene o no la subcadena.
- subcadena: la cadena a comprobar si es subcadena de la anterior.
- comprobar_hasta: hasta el índice que hay que comprobar (en función longitud subcadena).
"""

# Inicializamos variables
esta_subcadena = False
i = 0

# Pedimos datos
cadena = input("Dame una cadena: ")
subcadena = input(f"Dame una subcadena de '{cadena}': ")

# Proceso de búsqueda de la subcadena
comprobar_hasta = len(cadena)-len(subcadena)
while not esta_subcadena and i<=comprobar_hasta:
    if subcadena == cadena[i:i+len(subcadena)]:
        esta_subcadena = True
    i += 1

# Mostramos resultado
if esta_subcadena:
    print("Muy bien")
else:
    print(f"Me estás engañando '{subcadena}' no forma parte de '{cadena}'")