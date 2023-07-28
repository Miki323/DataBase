import sqlite3

DB_NAME = 'test.db'


def create_connection():
    # Создание подключения к базе данных (или создание новой, если она не существует)
    conn = sqlite3.connect(DB_NAME)
    return conn


def close_connection(conn):
    # Закрытие соединения с базой данных
    conn.close()


def create_table(conn):
    # Создание таблицы пользователей (если еще не существует)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()


def add_user(conn, name, email):
    # Добавление пользователя в базу данных
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        print(f"Пользователь с именем '{name}' и email '{email}' успешно добавлен.")
    except sqlite3.IntegrityError:
        print(f"Пользователь с именем '{name}' уже существует в базе данных.")


def get_user_by_name(conn, name):
    # Получить пользователя по имени из базы данных
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
    return cursor.fetchone()


def update_user_email(conn, name, new_email):
    # Обновление email пользователя в базе данных
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET email = ? WHERE name = ?', (new_email, name))
    conn.commit()
    print(f"Email пользователя с именем '{name}' успешно обновлен на '{new_email}'.")


def delete_user(conn, name):
    # Удаление пользователя из базы данных
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.commit()
    print(f"Пользователь с именем '{name}' успешно удален из базы данных.")


def main():
    name = "Siarhei"
    email = '111example@example.com'

    # Создание подключения к базе данных
    conn = create_connection()

    # Создание таблицы пользователей
    create_table(conn)

    # Добавление пользователя в базу данных
    add_user(conn, name, email)

    # Получение пользователя по имени из базы данных
    user = get_user_by_name(conn, name)
    print(user)

    # Обновление email пользователя в базе данных
    new_email = '222example@example.com'
    update_user_email(conn, name, new_email)

    # Закрытие соединения с базой данных
    close_connection(conn)


if __name__ == "__main__":
    main()
