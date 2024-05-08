"""
Genera el código QR de una página web.

Fuente: https://youtu.be/0IVgFf9c7_w?si=X7MsTB0jCsynx1H4
"""
URL = 'https://github.com/rdelcastillo/DAW-Python'

import qrcode

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=7, border=2)
qr.add_data(URL)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')
img.save('url.png')
