import Conexao as con
from Filiais import Filiais as fil

class Maquina():
    def all_maquinas():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM maquinas ORDER BY idmaq")
        result = mycursor.fetchall()
        for x in result:
            print(x)

        mycursor.close()
        mydb.close()

    def create_table():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE maquinas ( \
                            idmaq int not null auto_increment,\
                            tpmaterial varchar(50) not null,\
                            anocompra date not null,\
                            anoulrev date not null,\
                            nome varchar(50) not null,\
                            tipo varchar(50) not null,\
                            valor double not null,\
                            descricao varchar(50) not null,\
                            idfilial int,\
                            PRIMARY KEY (idmaq),\
                            FOREIGN KEY (idfilial) REFERENCES filiais(idfilial)\
                            );")
        print("Tabela criada. \n")

        mycursor.close()
        mydb.close()

    def insert_into(values):
        mydb = con.connect()
        mycursor = mydb.cursor()

        aux = 1
        if(fil.selec_by_id(values[7]) == -1):
            print("Id da filial não existe. \n")
            aux = 0

        if(aux):
            query = '''INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '''
            mycursor.execute(query, values)
            mydb.commit()
            print("Inserção concluida. \n")

        mycursor.close()
        mydb.close()
        
    def selec_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM maquinas WHERE idmaq = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        cont = 0
        for x in result: cont = cont + 1

        mycursor.close()
        mydb.close()

        if(cont): return cont
        else: return -1

        
    def update_table(coluna, valor, id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        aux = 1
        if(coluna == 'idfilial' and (fil.selec_by_id(valor) == -1)):
            print("Id da filial não existe .\n")
            aux = 0
        if(coluna == 'idmaq'):
            print("Não é permitido atualizar o id da máquina. \n")
            aux = 0

        if(aux):
            record = mycursor.execute("UPDATE maquinas SET {} = '{}' WHERE idmaq = {};".format(coluna, valor, id))
            mydb.commit()
            print("Valor atualizado. \n")

        mycursor.close()
        mydb.close()
    
    def delete_row_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT idmaq FROM maquinas WHERE idmaq = '%s';" % id)
        result_1 = mycursor.fetchall()
        aux_1 = 0
        for x in result_1: aux_1 = aux_1 + 1

        mycursor.close()
        
        if(not aux_1):
            print("Não foi possivel encontrar a maquina com o id passado. \n")
        else:
            mycursor = mydb.cursor()
            mycursor.execute("DELETE FROM maquinas WHERE idmaq = '%s';" % id)
            mydb.commit() 
            print("Exclusão concluida. \n")
            mycursor.close()

        mydb.close()
