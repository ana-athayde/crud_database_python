import mysql.connector
import Conexao

mydb = mysql.connector.connect(
    host="3306",
    user="root",
    password="1234",
    database="projeto_reciclagemDB"
)

mycursor = mydb.cursor()

class Maquinas():
    def all_maquinas(self, mode="DESC"):
        sql = "SELECT * FROM maquinas ORDER BY id {}".format(mode)
        mycursor.execute(sql)

    def create_table():
        mycursor.execute("CREATE TABLE maquinas ( \
                            idmaq int not null auto_increment,\
                            tpmaterial varchar(50) not null,\
                            anocompra date not null,\
                            anoulrev date nut null,\
                            nome varchar(50) not null,\
                            tipo varchar(50) not null,\
                            valor double not null,\
                            descricao varchar(50) not null,\
                            idfilial int,\
                            PRIMARY KEY (idmaq),\
                            FOREIGN KEY (idfilial) REFERENCES filiais\
                            );")

    def insert_into(tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial):
        #checar: anocompra, anolrev
        sql = f'INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial)\
                     VALUES ("{tpmaterial}", {anocompra}, {anoulrev}, "{nome}", "{tipo}", {valor}, "{descricao}", {idfilial})'
   
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
