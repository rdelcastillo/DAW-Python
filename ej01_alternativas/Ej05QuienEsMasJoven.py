"""
Pedimos la edad a dos personas y decimos quién es más joven, la primera, la segunda o si tienen la misma edad.

- Autor: Rafael del Castillo.
- Fecha: 4/11/2020.
"""

print("¿Quién es más joven?")
print("--------------------")

# Pedimos datos
age1 = int(input("Edad de la 1ª persona: "))
age2 = int(input("Edad de la 2ª persona: "))

# Proceso
if age1 < age2:
    print("La primera persona es más joven que la segunda.")
elif age1 > age2:
    print("La segunda persona es más joven que la primera.")
else:   # si llegamos aquí tienen la misma edad
    print("Las dos personas tienen la misma edad.")