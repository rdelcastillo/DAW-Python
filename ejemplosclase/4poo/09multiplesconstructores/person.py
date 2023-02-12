"""
Clase Persona.

Usamos parámetros opcionales y verificación de tipos para simular múltiples constructores.

Posibles formas de construir un objeto:

pepe = Person("Pepe Pérez")
lola = Person("Lola Vázquez", "10/01/2001")
juan = Person("Miguel López", date(2000, 10, 2))

Autor: Rafael del Castillo Gomariz
"""
from datetime import date

class Person:
    def __init__(self, name, birth_date=date.today()):
        self.name = name
        if isinstance(birth_date, date):
            self.birth_date = birth_date
        elif isinstance(birth_date, str):
            self.birth_date = date.fromisoformat(birth_date)
        else:
            raise TypeError("Parámetros erróneos")

    def __str__(self):
        return f"{self.name} - {self.birth_date.strftime('%d/%m/%Y')}"

if __name__ == '__main__':
    pepe = Person("Pepe Pérez")
    lola = Person("Lola Vázquez", "2001-10-01")
    juan = Person("Miguel López", date(2000, 10, 2))
    for p in (pepe, lola, juan):
        print(p)