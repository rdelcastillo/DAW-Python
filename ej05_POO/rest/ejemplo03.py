"""
Ejemplo3 de uso de peticiones web y REST.

Accedemos a una web y pedimos recursos con GET.
"""
import requests

# datos para hacer la petición
url = "http://httpbin.org/get"
p = {'p1':'parámetro 1', 'p2':'parámetro 2'}

# petición
r = requests.get(url, params=p)

# datos de respuesta
print("URL:", r.url)
if r.status_code == 200:
    print(r.content)