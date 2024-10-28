"""
El patrón de diseño DAO (Data Access Object) es un patrón estructural utilizado para abstraer y encapsular todos los
accesos a una fuente de datos.

El DAO maneja la conexión con la fuente de datos para obtener y almacenar datos, lo que permite separar la lógica de
negocio de la interacción con la base de datos. Este patrón es muy útil en aplicaciones con estructuras complejas de
bases de datos y puede aplicarse en cualquier lenguaje de programación.

Objetivos del patrón DAO:

- Separación de preocupaciones: Divide la lógica de persistencia de datos (acceso a datos) de la lógica de negocio.
- Facilidad de modificación: Facilita el cambio o la actualización de la lógica de acceso a datos sin afectar la lógica
  de negocio.
- Ocultar detalles de implementación: Los detalles específicos de la base de datos o cualquier fuente de datos quedan
  ocultos detrás del DAO, lo que permite una mayor flexibilidad y portabilidad.

Componentes clave del patrón DAO:

- Interface DAO: Define las operaciones estándar a realizar en el modelo, como agregar, eliminar, actualizar, y buscar.
- Implementación DAO: Proporciona la implementación concreta de la interfaz DAO, la cual maneja la conexión con la base
  de datos y ejecuta las operaciones definidas.
- Modelo de Dominio o DTO (Data Transfer Object): Objetos que transportan datos entre procesos, en este caso, entre la
 base de datos y el DAO.

Este programa es un ejemplo básico de cómo podríamos implementar el patrón DAO en Python para gestionar entidades de
usuarios en una base de datos utilizando SQLite.
"""
import sqlite3

class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class UserDao:
    def __init__(self, db_connection):
        self.db_connection = db_connection
        self.db_cursor = db_connection.cursor()

    def create_users_table(self):
        # ¿Existe la tabla?
        # En SQLite, la información sobre las tablas y esquemas se almacena en una tabla especial llamada sqlite_master.
        self.db_cursor.execute("SELECT count(name) FROM sqlite_master WHERE type='table' AND name=?",('users',))
        if self.db_cursor.fetchone()[0] == 1:  # existe, acabamos
            return

        # Comando SQL para crear una tabla
        sql = '''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        '''

        # Ejecutar el comando de creación de tabla
        self.db_cursor.execute(sql)

        # Guardar (commit) los cambios
        self.db_connection.commit()


    def get_user_by_id(self, user_id):
        query = "SELECT id, name, email FROM users WHERE id = ?"
        self.db_cursor.execute(query, (user_id,))
        row = self.db_cursor.fetchone()
        if row:
            return User(*row)
        return None

    def add_user(self, user):
        query = "INSERT INTO users (name, email) VALUES (?, ?)"
        self.db_cursor.execute(query, (user.name, user.email))
        self.db_connection.commit()

    def update_user(self, user):
        query = "UPDATE users SET name = ?, email = ? WHERE id = ?"
        self.db_cursor.execute(query, (user.name, user.email, user.id))
        self.db_connection.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = ?"
        self.db_cursor.execute(query, (user_id,))
        self.db_connection.commit()


if __name__ == '__main__':
    # Conexión a la base de datos, 'example.db' se creará si no existe
    db = sqlite3.connect('example.db')

    # Uso del DAO
    user_dao = UserDao(db)

    # Creación de tabla 'users', si no existe
    user_dao.create_users_table()

    # Agregar un usuario
    new_user = User(None, 'John Doe', 'johndoe@example.com')
    user_dao.add_user(new_user)

    # Obtener un usuario
    retrieved_user = user_dao.get_user_by_id(1)
    print(retrieved_user.name)

    # Actualizar un usuario
    retrieved_user.name = 'John Updated'
    user_dao.update_user(retrieved_user)

    # Eliminar un usuario
    user_dao.delete_user(1)
