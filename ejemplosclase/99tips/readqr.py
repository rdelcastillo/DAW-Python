"""
Decodificamos QR.

Sacado de https://youtu.be/WnhuWX0dwbA?si=v1MyYigopNBpSZ5_
"""
IMG = 'url.png'

import cv2
from pyzbar.pyzbar import decode

def read_qr_code(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)  # convierte la imagen a grises
    decoded_objects = decode(gray_image)
    return decoded_objects


if __name__ == '__main__':
    qr_objects = read_qr_code(IMG)
    print("Datos encontrados en el QR:")
    for obj in qr_objects:
        data = obj.data.decode('utf-8')
        print(data)
