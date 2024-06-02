"""
Ejemplo robusto que permita acceder a los datos de usuarios desde diferentes fuentes de datos como CSV, MySQL y SQLite
utilizando el patrón DAO, para ello usaremos clases abstractas para definir una interfaz común para los DAOs.

Diseñaremos el código de manera que sea fácil añadir nuevas fuentes de datos en el futuro sin modificar la lógica de
negocio que dependa de estas clases DAO.
"""

from abc import ABC, abstractmethod

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class UserDao(ABC):
    @abstractmethod
    def get_user_by_id(self, user_id):
        pass

    @abstractmethod
    def add_user(self, user):
        pass

    @abstractmethod
    def update_user(self, user):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass
