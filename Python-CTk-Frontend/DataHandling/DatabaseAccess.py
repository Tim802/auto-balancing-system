import sqlite3

connection = sqlite3.connect('Python-CTk-Frontend/DataHandling/UserData.db')
cursor = connection.cursor()

def retreive_all(id):
    cursor.execute(f'SELECT {id} FROM USERS')
    values = cursor.fetchall()
    return values

def retreive_id(inp, identifier):
    cursor.execute(f'SELECT id WHERE {identifier} = {inp}')
    values = cursor.fetchall()
    return values

def retreive_val(inp, identifier, VAL):
    cursor.execute(f'SELECT {VAL} WHERE {identifier} = {inp}')
    values = cursor.fetchall()
    return values

def close_connection():
    connection.close()
    print("UserData.db Connection Closed")
