"""
Modificación del programa anterior para que no de error si al
contestar si es o no domingo se pone un carácter distinto de S ó N.
"""

# Pedimos datos
import sys

duration = int(input("¿Cuánto time dura la llamada?: "))
is_sunday = input("¿Es Domingo? (S/N): ")
if is_sunday.upper() == "N":
    turn = input("¿Qué turno: Mañana o Tarde? (M/T)?: ")
elif is_sunday.upper() != "S":
    print("La respuesta era S ó N, ha dado una distinta. Abortamos...", file=sys.stderr)
    exit(1)

# Proceso
if duration <= 5:
    cost = duration * 100
elif duration <= 8:
    cost = (duration - 5) * 80 + 500
elif duration <= 10:
    cost = (duration - 8) * 70 + 240 + 500
else:
    cost = (duration - 10) * 50 + 140 + 240 + 500

# impuestos
if is_sunday.upper() == "S":
    cost += cost * 0.03
elif turn.upper() == "M":
    cost += cost * 0.15
else:
    cost += cost * 0.10

# Salida
print("El coste de la llamada:", cost / 100, "euros.")
