import sqlite3

# Подключение к базе данных (или создание новой)
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# Создание таблицы (если еще не существует)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()


# Функции для взаимодействия с базой данных

def add_user(name, email):
    cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()


def get_user_by_name(name):
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    return cursor.fetchone()


def update_user_email(name, new_email):
    cursor.execute('UPDATE users SET email = ? WHERE name = ?', (new_email, name))
    conn.commit()


def delete_user(name):
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.commit()


def main():
    name = "Siarhei"
    email = '111example@example.com'

    # Добавление пользователя в базу данных
    add_user(name, email)

    # Получить пользователя по name в базе данных
    print(get_user_by_name(name))

    # Обновление email в базе данных
    new_email = '222example@example.com'
    update_user_email(name, new_email)

    # Удаление пользователя из базы данных
    # delete_user(name)

    # Закрытие соединения с базой данных
    conn.close()


if __name__ == "__main__":
    main()

