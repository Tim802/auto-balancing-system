import sqlite3
from Encryption import encrypt

connection = sqlite3.connect('DataHandling/UserData.db')
cursor = connection.cursor()

def retreive(id):
    cursor.execute(f'SELECT {id} FROM USERS')
    values = cursor.fetchall()
    return values