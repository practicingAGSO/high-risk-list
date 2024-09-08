import pyodbc
from src.models.UserModel import User


class ItemDatabase:
    def __init__(self):
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER=DESKTOP-91O4SLE; DATABASE=VendorDB; Trusted_Connection=yes;')
        self.cursor = self.conn.cursor()
        
    def add_user(self, object):
            query = f"insert into users( username, password) values ('{object.username}', '{object.password}')"
            self.cursor.execute(query)
            self.conn.commit()
        
    def get_user_by_username(self, username):
            query = "SELECT id, username, password FROM users WHERE username = ?"
            self.cursor.execute(query, (username,))
            row = self.cursor.fetchone()
            if row:
                return User(id=row[0], username=row[1], password=row[2])  # Retorna un objeto User
            return None