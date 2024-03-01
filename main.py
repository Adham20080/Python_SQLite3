import sqlite3

connection = sqlite3.connect('database.db')

connection.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name VARCHAR(255) ,
    surname VARCHAR(255) ,
    email TEXT NULL ,
    phone INTEGER)''')

connection.execute("""INSERT INTO users(name, surname, email, phone)
VALUES ("Ahmadjon", "Abdulfotih", "hmadjonbdul@gmail.com", 770333308)""")

connection.commit()
connection.close()
