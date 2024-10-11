import sqlite3

connection = sqlite3.connect('../not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NON NULL
)
''')

# for i in range(1, 11):
#      cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f'User{i}', f'example{i}@gmail.com', i*10, 1000))

#cursor.execute("UPDATE Users SET balance = ? WHERE id%2 = ?", (500, 1))
#cursor.execute("DELETE FROM Users WHERE id%3 = ?", (1,))

#cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != ?", (60,))
# users = cursor.fetchall()
# for user, em, age, balance in users:
#     print(f"Имя: {user} | Почта: {em} | Возраст: {age} | Баланс: {balance}")

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

connection.commit()

cursor.execute("SELECT COUNT(*) FROM Users")
count_oll = cursor.fetchone()[0]

cursor.execute("SELECT SUM(balance) FROM Users")
balance_oll = cursor.fetchone()[0]

cursor.execute("SELECT AVG(balance) FROM Users")
avg_balance = cursor.fetchone()[0]

print(balance_oll/count_oll)
print(avg_balance)

connection.commit()
connection.close()