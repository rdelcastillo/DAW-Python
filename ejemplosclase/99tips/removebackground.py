"""
Borramos el fondo de una imagen.

Idea sacada de https://youtu.be/nkhFh5eUFSM?si=2McaL_g9kv35iy4a
"""
IMG_SOURCE = 'img/Cleo.png'
IMG_TARGET = 'img/Cleo_sin_fondo.png'

from rembg import remove

# Abrimos la imagen
with open(IMG_SOURCE, 'rb') as input_file:
    input_image = input_file.read()

# Borramos el fondo de la imagen
output_image = remove(input_image)

# Guardamos la imagen resultante
with open(IMG_TARGET, 'wb') as output_file:
    output_file.write(output_image)

print(f'Fondo de {IMG_SOURCE} eliminado y guardado en {IMG_TARGET}')
