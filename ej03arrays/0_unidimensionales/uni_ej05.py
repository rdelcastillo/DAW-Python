"""
Programa que pide la temperatura media que ha hecho en cada mes de un determinado año y que muestra a continuación
un diagrama de barras horizontales con esos datos.

Las barras del diagrama se pueden dibujar a base de asteriscos o cualquier otro carácter.
"""

MONTHS = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre",
          "Octubre", "Noviembre", "Diciembre"]
temperatures = [0] * 12

# Petición de datos
for month in range(len(MONTHS)):
    temperatures[month] = float(input(f"Temperatura media del mes {MONTHS[month]}: "))

# Mostramos el diagrama de barras
for month in range(len(MONTHS)):
    print(f"{MONTHS[month]+':':11} "                # nombre del mes (alineados a 11 posiciones)
          f"{'*' * round(temperatures[month])}")    # * representado el valor de la temperatura media
