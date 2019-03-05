################################################################################
# Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
# El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
# Escribir un algoritmo que determine la hora de llegada a la ciudad B.
################################################################################
# Análisis
# Tenemos que pedir la hora de salida (hora, minutos y segundos).
# Tengo que saber también el tiempo en segundo que ha tardado en llegar.
# Tenemos que calcular la hora de llegada.
# Datos de entrada: hora, minutos y segundos de salida (entero),
# segundos que tarda (entero).
# Información de salida: hora, minutos y segundos de llegada (enteros)
# Variables: horapartida, minpartida, segpartida, segviaje, horallegada,
# minllegada, segllegada (enteros)
################################################################################
# Diseño
# 1. Leer hora de salida
# 2. Leer segundos que tarda
# 3. Convierto la hora de salida a segundos (necesito una variable seginicial)
# 4 Le sumo los segundos que he tardado(necesito una variable segfinal)
# 5. Convierto los segundos totales a hora, minuto y segundos
# 6. Muestro la hora de llegada
################################################################################

# Pedimos datos
horapartida = int(input("Hora de salida: "))
minpartida = int(input("Minutos de salida: "))
segpartida = int(input("Segundos de salida: "))
segviaje = int(input("Tiempo que has tardado en segundos: "))

# Hacemos cálculos
# convierto la hora de salida a segundos
seginicial = horapartida*3600+minpartida*60+segpartida
# le sumo los segundos que he tardado
segfinal = seginicial+segviaje
# convierto los segundos totales a hora, minúto y segundos
horallegada = segfinal//3600
minllegada = (segfinal%3600)//60
segllegada = (segfinal%3600)%60

# Muestro la hora de llegada
print(f"Hora de llegada {horallegada}:{minllegada}:{segllegada}")



