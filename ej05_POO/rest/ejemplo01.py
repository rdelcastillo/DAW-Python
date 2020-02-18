"""
Ejemplo1 de uso de peticiones web y REST.

Accedemos a una web y mostramos su status.
"""
import requests

url = "https://informatica.iesgrancapitan.org"
r = requests.get(url)
print(r)