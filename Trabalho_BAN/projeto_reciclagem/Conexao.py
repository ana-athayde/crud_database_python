import mysql.connector

#Conexao
#getConnection
#closeConnection

class Database:
    my_db = my_cursor = None

    def __init__(self):
        global my_db, my_cursor
        my_db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="py_sms"
        )
        my_cursor = my_db.cursor()

    def __del__(self):
        my_db.commit()