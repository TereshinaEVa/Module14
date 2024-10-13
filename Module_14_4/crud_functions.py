import sqlite3

connection = sqlite3.connect('Products.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
);
''')
connection.commit()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
);
''')
connection.commit()

def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',(username, email, age, 1000))
    connection.commit()


def is_included(username):
    cursor.execute("SELECT * FROM Users WHERE username=?", (username,))
    check_user = cursor.fetchone()[0]
    if check_user == 0:
        checker = False
    else:
        checker = True
    connection.commit()
    return checker


# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Продукт{i}', f'Описание{i}', i*100))

cursor.execute("SELECT * FROM Products")
products_all = cursor.fetchall()

connection.commit()
connection.close()
