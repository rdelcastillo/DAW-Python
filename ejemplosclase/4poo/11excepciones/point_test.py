"""
Test clase Point.

Creamos una serie de puntos y alguno incorrecto para que salte la excepción PointTypeError.
"""
from point import Point, PointTypeError

has_exited_without_problems = False

try:
    print("Vamos a crear una serie de puntos...")
    p1 = Point(2, 3)
    print(p1)
    p2 = Point(4, 6)
    print(p2)
    p3 = Point(2.6, 8) # aquí se debe lanzar una excepción PointTypeError
    print(p3)          # esta instrucción y las siguientes no se ejecutan
    p4 = Point(1,1)
    print(p4)

except ValueError:  # esta parte no se ejecutará
    print("Se ha producido una excepción ValueError.")
except PointTypeError as e:  # en e está el objeto correspondiente a la excepción generada
    print(f"Se ha producido un error de tipo de parámetros con (x={e.x}, y={e.y})")
except Exception:  # no es muy aconsejable, si se pone debe ser al final
    print("Se ha producido un error desconocido.")

else:  # solo se ejecuta si no se han producido excepciones en el bloque try
    has_exited_without_problems = True

finally:  # se ejecutará siempre
    print("El programa ha terminado.")
    print("No ha habido errores.") if has_exited_without_problems else print("Se han producido errores.")