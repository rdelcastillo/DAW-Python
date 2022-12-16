"""
Ejemplo de captura de excepciones.
"""
print("Cálculo del cociente de dos números")
print("-----------------------------------")

while True:
    try:
        a = int(input("Dame el numerador: "))
        b = int(input("Dame el denominador: "))
        print(f"El cociente de {a} y {b} es {a / b}")
        break
    except ValueError:
        print("Ha introducido un valor que no es entero")
    except ZeroDivisionError:
        print("No se puede dividir por 0")
    except KeyboardInterrupt:
        print("Ha pulsado Ctrl-C, aquí no es válido.")
