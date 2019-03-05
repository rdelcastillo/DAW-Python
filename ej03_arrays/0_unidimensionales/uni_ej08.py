'''
Programa que pide la temperatura media que ha hecho en cada mes de un determinado
año y muestra a continuación un diagrama de barras horizontales con esos datos.

@author Rafael del Castillo Gomariz

Ejercicio del libro "Aprende Java con Ejercicios" (https://leanpub.com/aprendejava)

'''

# listas con los meses y la temperatura media de cada mes
mes = [ "enero", "febrero", "marzo", "abril", "mayo", "junio",
        "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
temperatura = [None]*12

# colores (solo terminal gnu/linux)
verde = "\033[32m"
naranja = "\033[33m"
azul = "\033[34m"
morado = "\033[35m"
blanco = "\033[37m"

# pedimos temperaturas medias
for i in range(12):
    temperatura[i] = int(input(f"Introduzca la temperatura media de {mes[i]}: "))

# imprimimos diagrama de barras por mes
for i in range(12):
    print(azul + f"{mes[i]:{12}} " + verde + "│",end="")
    for j in range(temperatura[i]):
        print(morado + "▄",end="")
    print(naranja + f" {temperatura[i]}ºC" + blanco)
