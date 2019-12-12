"""
Ejemplo de biblioteca de funciones con test dentro del archivo.
"""

def funcion1():
    print("Soy la función 1 y mi 'namespace' es:", __name__)

def funcion2(param):
    print("Soy la función 2 y me has pasado", param, "como parámetro",
          "y mi 'namespace' es:", __name__)

if __name__ == "__main__":
    funcion1()
    funcion2("TEST desde función 2")