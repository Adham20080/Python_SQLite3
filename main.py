import sqlite3

connection = sqlite3.connect('database.db')

connection.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name VARCHAR(255) ,
    surname VARCHAR(255) ,
    email TEXT NULL UNIQUE,
    phone INTEGER)''')

connection.commit()
connection.close()
