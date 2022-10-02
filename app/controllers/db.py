from decouple import config
import sqlite3 as sql


def createDB():
    conn = sql.connect(config('DATABASE_NAME'))
    conn.commit()
    conn.close()


def createUser(username, password, salt, email):
    conn = sql.connect(config('DATABASE_NAME'))
    cursor = conn.cursor()
    query = f"INSERT INTO user(username,password,salt,email) VALUES ('{username}','{password}','{salt}','{email}')"
    try:
        cursor.execute(query)
        conn.commit()
    except sql.Error as er:
        print('Error al insertar en SQLlite: %s' % (' '.join(er.args)))
    conn.close()


def getUser(username):
    conn = sql.connect(config('DATABASE_NAME'))
    cursor = conn.cursor()
    query = f"SELECT * FROM user WHERE username = '{username}'"
    try:
        cursor.execute(query)
        data = cursor.fetchone()
        print(data)
    except sql.Error as er:
        print('Error al realizar la consulta en SQLlite: %s' %
              (' '.join(er.args)))
    conn.close()


if __name__ == '__main__':
    getUser('maser84')
