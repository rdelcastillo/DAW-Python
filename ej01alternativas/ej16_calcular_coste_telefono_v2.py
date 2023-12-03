"""
Modificación del programa anterior con mejoras.
"""
import sys

COST_FARE3 = 70
STAGE3 = 10
COST_FARE2 = 80
STAGE2 = 8
STAGE1 = 5
COST_FARE1 = 100

# Pedimos datos
duration = int(input("¿Cuántos minutos dura la llamada?: "))
if duration <= 0:
    print("Los minutos tienen que ser un valor entero. Abortamos...", file=sys.stderr)
    exit(1)

is_sunday = input("¿Es Domingo? (S/N): ").upper()
if is_sunday == "N":
    turn = input("¿Qué turno: Mañana o Tarde? (M/T)?: ").upper()
    if turn != "M" and turn != "T":
        print("La respuesta era M ó T, ha dado una distinta. Abortamos...", file=sys.stderr)
        exit(1)
elif is_sunday != "S":
    print("La respuesta era S ó N, ha dado una distinta. Abortamos...", file=sys.stderr)
    exit(1)

# Proceso
if duration <= STAGE1:
    cost = duration * COST_FARE1
elif duration <= STAGE2:
    cost = STAGE1 * COST_FARE1 + (duration - STAGE1) * COST_FARE2
elif duration <= STAGE3:
    cost = STAGE1 * COST_FARE1 + STAGE2 * COST_FARE2 + (duration - STAGE3) * COST_FARE3
else:
    cost = STAGE1 * COST_FARE1 + STAGE2 * COST_FARE2 + STAGE3 * COST_FARE3 + (duration - STAGE3) * 50 + 140 + 240 + 500

# impuestos
if is_sunday.upper() == "S":
    cost += cost * 0.03
elif turn == "M":
    cost += cost * 0.15
else:
    cost += cost * 0.10

# Salida
print("El coste de la llamada:", cost / 100, "euros.")
