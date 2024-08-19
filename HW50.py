import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(10):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i+1}', f'example{i+1}@gmail.com', f'{(i+1) * 10}', '1000'))
#
# step = 2
# amount = -500
# cursor.execute(f'UPDATE Users SET balance = balance + ? WHERE id % ? = 1', (amount, step))
# for i in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (i,))
#
# cursor.execute('SELECT  *  FROM Users WHERE age != 60')
# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[1]} | Почта: {user[2]} | Возраст: {user[3]} | Баланс: {user[4]}")

cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

count_members = cursor.execute('SELECT count( * ) FROM Users').fetchone()[0]
print(count_members)
sum_balance = cursor.execute('SELECT SUM(balance) FROM Users').fetchone()[0]
print(sum_balance)
print(sum_balance/count_members)

connection.commit()
connection.close()
