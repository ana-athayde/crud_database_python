import mysql.connector

def connect():
    my_db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="projeto_reciclagemDB"
    )
    return my_db

def desconectar(my_db):
    my_db.close()
