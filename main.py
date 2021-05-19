import sqlite3

db = sqlite3.connect('server.db')
cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    users_id INT NOT NULL PRIMARY KEY,
    login TEXT,
    password TEXT
)""")
# Всегда подтверждаем
db.commit()

cursor.execute("""CREATE TABLE IF NOT EXISTS short_table (
    users_id INT REFERENCES users (users_id),
    short_id INT NOT NULL,
    token TEXT NOT NULL,
    long_url TEXT NOT NULL,
    pub_gen_acc INT,
    counter INT
)""")
# Всегда подтверждаем
db.commit()


# функция регестрации
def reg():
    global user_login
    user_login = input("Login:")
    user_password = input("Password")

    cursor.execute(f"SELECT login FROM users WHERE login = '{user_login}'")
    if cursor.fetchone() is None:
        cursor.execute(f"INSERT INTO users VALUES ('{user_login}','{user_password}',{0})")
        db.commit()

        print("Зарегался")
    else:
        print("Такая запись уже есть")

        for value in cursor.execute("SELECT * FROM users"):
            print(value[0])


# Функция удаления
def delete_db():
    cursor.execute(f"DELETE FROM users WHERE login='{user_login}'")
    db.commit()

    print("Запись удалена")


# Вывод на экран авторизации
def enter():
    for i in cursor.execute('SELECT login FROM users'):
        print(i)

def main():
    reg()
    enter()

main()