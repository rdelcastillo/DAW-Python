#paquete
import paquete_ejemplo.misfunciones
import paquete_ejemplo.misfunciones as paquete
from paquete_ejemplo.misfunciones import funcion3

#subpaquete
import paquete_ejemplo.subpaquete_ejemplo.misfunciones2
import paquete_ejemplo.subpaquete_ejemplo.misfunciones2 as subpaquete
from paquete_ejemplo.subpaquete_ejemplo.misfunciones2 import funcion4

# Ejemplo paquete
print("Ejemplos paquete:")
print("-----------------")
paquete_ejemplo.misfunciones.funcion1()
paquete.funcion2("PARÁMETRO1")
funcion3(1,2,3,4,5)
print()

# Ejemplo subpaquete
print("Ejemplos subpaquete:")
print("--------------------")
paquete_ejemplo.subpaquete_ejemplo.misfunciones2.funcion4()
subpaquete.funcion4("parámetro1")
funcion4("parámetro1", "parámetro2")