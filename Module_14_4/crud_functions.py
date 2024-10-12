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

# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (f'Продукт{i}', f'Описание{i}', i*100))

cursor.execute("SELECT * FROM Products")
products_all = cursor.fetchall()

connection.commit()
connection.close()