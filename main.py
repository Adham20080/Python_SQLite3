import sqlite3

connection = sqlite3.connect('database.db')

connection.execute('''
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT ,
    name VARCHAR(255) ,
    surname VARCHAR(255) ,
    email TEXT NULL UNIQUE,
    phone INTEGER)''')

# try:
#     connection.execute('''
# INSERT INTO users(name, surname, email, phone) VALUES ("Abubakri", "Abdumalikov", "example@gamil.com", 773332255)''')
#     print("O'xshadi")
# except:
#     print("O'xshamadi!")

data = connection.execute("SELECT * FROM users")

for row in data:
    print(*row)

connection.commit()
connection.close()
