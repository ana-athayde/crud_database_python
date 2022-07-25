import select
import this
import Conexao as con
from Cidades import Cidades as cid
from Materiais import Materiais as mat


class Filiais():
    def all_filiais():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM filiais ORDER BY idfilial")
        result = mycursor.fetchall()
        for x in result:
            print(x)

        mycursor.close()
        mydb.close()


    def create_table():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE filiais (\
                            idfilial int not null auto_increment,\
                            nome varchar(50) not null,\
                            fone varchar(50) not null,\
                            rua varchar(50) not null,\
                            numero int not null,\
                            bairro varchar(50) not null,\
                            idcida int,\
                            idmate int,\
                            PRIMARY KEY (idfilial),\
                            FOREIGN KEY (idcida) REFERENCES cidades(idcida),\
                            FOREIGN KEY (idmate) REFERENCES materiais(idmate)\
                            );")
        print("Tabela criada. \n")

        mycursor.close()
        mydb.close()


    def insert_into(values):
        mydb = con.connect()
        mycursor = mydb.cursor()

        aux = 1
        if(cid.selec_by_id(values[5]) == -1):
            print("Id da cidade não existe. \n")
            aux = 0

        if(mat.selec_by_id(values[6]) == -1):
            print("Id do material não existe. \n")
            aux = 0

        if(aux):
            query = '''INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            mycursor.execute(query, values)
            mydb.commit()
            print("Inserção concluida. \n")
        
        mycursor.close()
        mydb.close()


    def selec_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM filiais WHERE idfilial = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        cont = 0
        for x in result: 
            cont = cont + 1

        mycursor.close()
        mydb.close()
        
        if(cont): return cont
        else: return -1
        
    def update_table(coluna, valor, id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        aux = 1
        if(coluna == 'idcida' and (cid.selec_by_id(valor) == -1)):
            print("Id da cidade não existe .\n")
            aux = 0
        if(coluna == 'idmate' and (mat.selec_by_id(valor) == -1)):
            print("Id do material não existe .\n")
            aux = 0
        if(coluna == 'idfilial'):
            print("Não é permitido atualizar o id da filial. \n")
            aux = 0

        if(aux): 
            record = mycursor.execute("UPDATE filiais SET {} = '{}' WHERE idfilial = {} ;".format(coluna, valor, id))
            mydb.commit()
            print("Valor atualizado. \n")

        mycursor.close()
        mydb.close()

    def delete_row_by_id(id):
        mydb = con.connect()

        mycursor = mydb.cursor()

        mycursor.execute("SELECT idfilial FROM filiais WHERE idfilial = '%s';" % id)
        result_1 = mycursor.fetchall()
        aux_1 = 0
        for x in result_1: aux_1 = aux_1 + 1

        mycursor.close()
        
        if(not aux_1):
            print("Não foi possivel encontrar a filial com o id passado. \n")
        else:
            mycursor = mydb.cursor()

            mycursor.execute("SELECT idmaq FROM maquinas WHERE idfilial = '%s';" % id)
            result = mycursor.fetchall()
            print(result)
            aux = 0
            for x in result: aux = aux + 1

            mycursor.close()

            if (not aux):
                mycursor = mydb.cursor()

                mycursor.execute("DELETE FROM filiais WHERE idfilial = '%s';" % id)
                mydb.commit()
                print("Exclusão concluida. \n")

                mycursor.close()
            else:
                print("As seguintes maquinas são relacionadas a essa filial, é necessario que as delete antes de apagar a filial. \n")
                print(result)

        mydb.close()
    