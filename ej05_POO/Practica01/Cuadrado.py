"""
Implementación en Python la clase Cubo del libro 'Aprende Java con Ejercicios'
"""

class Cuadrado:

    def __init__(self, l):
        self.lado = l

    def __str__(self):
        resultado = ""
        # Parte superior del cuadrado
        for i in range(self.lado):
            resultado += "██"
        resultado += "\n"
        # Parte media del cuadrado
        for i in range(1,self.lado - 1):
            resultado += "██"
            for espacios in range(1,self.lado - 1):
                resultado += "  "
            resultado += "██\n"
        # Parte inferior del cuadrado
        for i in range(self.lado):
            resultado += "██"
        resultado += "\n"
        return resultado

# Prueba de la clase
if __name__ == "__main__":
    miCuadradito = Cuadrado(5)
    print(miCuadradito)
    miCuadradito.lado = 10
    print(miCuadradito)