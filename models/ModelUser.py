from .entities.User import User
import sqlite3 as sql

class ModelUser():
    @classmethod
    def login(self, db, user):
        try:
            conn = db
            print("Conectando con DB:" + conn)
            cursor = sql.connect(conn).cursor()
            query = """SELECT password, email FROM user 
                    WHERE email='{}'""".format(user.email)
            cursor.execute(query)
            print("Query ejecutado: ==>" +query)
            data = {}
            row = cursor.fetchone()
            data['row'] = row
            print("Resultado del query: ==>"+ row)
            if row != None:
                user=User(row[0],row[1],User.check_password(row[2],user.password),row[3],row[4],row[5])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)