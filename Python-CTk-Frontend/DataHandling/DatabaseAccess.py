import sqlite3

connection = sqlite3.connect('Python-CTk-Frontend/DataHandling/UserData.db')
cursor = connection.cursor()

def fetch():
    cursor.execute("SELECT * FROM USERS")
    results = cursor.fetchall()
    return results

def close_connection():
    connection.close()
    print("UserData.db Connection Closed")

def enter_user(email, password):
    cursor.execute(f"INSERT INTO USERS (EMAIL, PASSWORD) VALUES ('{email}', '{password}');")
    print(f'new user. EMAIL: {email}, PASSWORD: {password}')
    connection.commit()
