import csv
from pathlib import Path
from ej06_dao import UserDao, User

class CsvUserDao(UserDao):
    def __init__(self, file_path):
        self.file_path = Path(file_path)
        if not self.file_path.exists():
            with open(self.file_path, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['id', 'name', 'email'])

    def get_user_by_id(self, user_id):
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id']) == user_id:
                    return User(row['id'], row['name'], row['email'])
        return None

    def add_user(self, user):
        with open(self.file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([user.id, user.name, user.email])

    def update_user(self, user):
        # Leer todos los datos y modificar el necesario
        rows = []
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id']) == user.id:
                    row['name'] = user.name
                    row['email'] = user.email
                rows.append(row)

        # Reescribir el archivo CSV con los datos actualizados
        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'email'])
            writer.writeheader()
            writer.writerows(rows)

    def delete_user(self, user_id):
        rows = []
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if int(row['id']) != user_id:
                    rows.append(row)

        with open(self.file_path, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'email'])
            writer.writeheader()
            writer.writerows(rows)
