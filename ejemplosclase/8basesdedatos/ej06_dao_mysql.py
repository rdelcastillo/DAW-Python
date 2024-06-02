import mysql.connector
from ej06_dao import UserDao, User

class MysqlUserDao(UserDao):
    def __init__(self, config):
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255))''')
        self.connection.commit()

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT id, name, email FROM users WHERE id = %s", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return User(*result)
        return None

    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (user.name, user.email))
        self.connection.commit()

    def update_user(self, user):
        self.cursor.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (user.name, user.email, user.id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        self.connection.commit()
