"""
Pedimos dos números ‘nota’ y ‘edad’, y un carácter ‘sexo’ y mostramos el mensaje ‘ACEPTADA’ si la nota es mayor o igual
a cinco, la edad es mayor o igual a dieciocho y el sexo es ‘F’. En caso de que se cumpla lo mismo, pero el sexo sea ‘M’,
mostramos ‘POSIBLE’. Si no se cumplen dichas condiciones se debe mostrar ‘NO ACEPTADA’.

- Autor: Rafael del Castillo.
- Fecha: 4/11/2020.
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Nota    Edad    Sexo    Mensaje
< 5     < 18    F       NO ACEPTADA
< 5     < 18    M       NO ACEPTADA
< 5     >=18    F       NO ACEPTADA
< 5     >=18    M       NO ACEPTADA
>=5     < 18    F       NO ACEPTADA
>=5     < 18    M       NO ACEPTADA
>=5     >=18    F       ACEPTADA
>=5     >=18    M       POSIBLE

Para poner un mensaje distinto de 'NO ACEPTADA' la nota debe ser mayor o igual a 5 y la edad mayor o igual a 18.

- Entrada: nota, edad y sexo.
- Salida: mensaje de aceptación.
- Variables: value, age, sex
"""

print("Formulario de aceptación")
print("------------------------")

# Datos de entrada
value = float(input("Nota: "))
age = float(input("Edad: "))
sex = input("Nota: ")

# Salida
if value >= 5 and age >= 18:
    if sex.upper() == "F":
        print("ACEPTADA")
    else:  # asumimos que no hay errores en la entrada, siempre es 'F' ó 'M'
        print("POSIBLE")
else:
    print("NO ACEPTADA")
