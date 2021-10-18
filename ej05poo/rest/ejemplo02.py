"""
Ejemplo2 de uso de peticiones web y REST.

Accedemos a una web y si no hay errores la guardamos.
"""
import requests

url = "https://informatica.iesgrancapitan.org"
r = requests.get(url)
if r.status_code == 200:
    f = open("informatica.html", "wb")
    f.write(r.content)
    f.close()