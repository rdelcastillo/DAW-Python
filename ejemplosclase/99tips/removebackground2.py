"""
Borramos el fondo de una imagen.

Idea sacada de https://youtu.be/nkhFh5eUFSM?si=2McaL_g9kv35iy4a
"""
IMG_SOURCE = 'img/python.png'
IMG_TARGET = 'img/python_sin_fondo.png'

from rembg import remove
from PIL import Image

input_image = Image.open(IMG_SOURCE)
output_image = remove(input_image)
output_image.save(IMG_TARGET)

print(f'Fondo de {IMG_SOURCE} eliminado y guardado en {IMG_TARGET}')
