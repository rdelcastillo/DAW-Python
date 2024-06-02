import sqlite3
from ej06_dao import UserDao, User

class SqliteUserDao(UserDao):
    def __init__(self, db_path):
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)''')
        self.connection.commit()

    def get_user_by_id(self, user_id):
        self.cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return User(*result)
        return None

    def add_user(self, user):
        self.cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (user.name, user.email))
        self.connection.commit()

    def update_user(self, user):
        self.cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (user.name, user.email, user.id))
        self.connection.commit()

    def delete_user(self, user_id):
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.connection.commit()
