import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('mydatabase.db')

# Создание таблицы
cursor = conn.cursor()
cursor.execute('''CREATE TABLE mytable
                  (id INTEGER PRIMARY KEY, name TEXT)''')

# Закрытие подключения
conn.close()