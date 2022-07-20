#import Conexao
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="projeto_reciclagemDB"
)

mycursor = mydb.cursor()

class Maquina():
    def all_maquinas(self, mode="DESC"):
        sql = "SELECT * FROM maquinas ORDER BY id {}".format(mode)
        mycursor.execute(sql)

    def create_table():
        mycursor.execute("CREATE TABLE maquinas ( \
                            idmaq int not null auto_increment,\
                            tpmaterial varchar(50) not null,\
                            anocompra varchar(50) not null,\
                            anoulrev varchar(50) not null,\
                            nome varchar(50) not null,\
                            tipo varchar(50) not null,\
                            valor double not null,\
                            descricao varchar(50) not null,\
                            idfilial int,\
                            PRIMARY KEY (idmaq)\
                            );")

    def insert_into(values):
        query = '''INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '''
        mycursor.execute(query, values)
        mydb.commit()
   
    def select():
        print("")

    def update_table():
        print("")

    def delete_table():
        print("")
    
    def join(tabela_1, tabela_2):
        print("")
    
    def funcao_agregacao():
        print("")
