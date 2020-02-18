"""
Ejemplo4 de uso de peticiones web y REST.

Accedemos a una web y pedimos recursos con GET.

Usamos JSON.
"""
import requests

# datos para hacer la petición
url = "http://httpbin.org/get"
parametros = {'p1': 'parámetro 1', 'p2': 'parámetro 2'}

# petición
respuesta = requests.get(url, params=parametros)

# datos de respuesta
print("URL:", respuesta.url)
if respuesta.status_code == 200:
    contenido = respuesta.json()    # lo pasa a un diccionario
    print("Contenido:", contenido)
    print("---")
    print("IP cliente:", contenido['origin'])
    print("---")
    print("Argumentos:")
    for argumento in contenido['args'].keys():
        print(argumento, "-->", contenido['args'][argumento])