"""
Pedimos la edad a dos personas y decimos quién es más joven, la primera, la segunda o si tienen la misma edad.

No admitimos edades inferiores a 0.

------------------
A tener en cuenta:
------------------
* Con la orden exit() finalizo un programa, si no le paso parámetro el código de salida es 0. Se aconseja poner un
  código de salida distinto de 0 cuando finalicemos por una situación de error o anormal.
* La salida de la orden print() si no indicamos nada se hará sobre la salida estándar, podemos cambiarla con el
  parámetro file. Si queremos mostrar un error importante podríamos redirigirla a sys.stderr.

- Autor: Rafael del Castillo.
- Fecha: 4/11/2020.
"""
import sys

print("¿Quién es más joven?")
print("--------------------")

# Pedimos datos
age1 = int(input("Edad de la 1ª persona: "))
if age1 < 0:
    print("No se admiten edades negativas", file=sys.stderr)
    exit(1)

age2 = int(input("Edad de la 2ª persona: "))
if age2 < 0:
    print("No se admiten edades negativas", file=sys.stderr)
    exit(2)

# Proceso
if age1 < age2:
    print("La primera persona es más joven que la segunda.")
elif age1 > age2:
    print("La segunda persona es más joven que la primera.")
else:   # si llegamos aquí tienen la misma edad
    print("Las dos personas tienen la misma edad.")