import select
import this
import Conexao as con
from Cidades import Cidades as cid
from Materiais import Materiais as mat

mydb = con.connect()
mycursor = mydb.cursor()

class Filiais():
    def all_filiais():
        mycursor.execute("SELECT * FROM filiais ORDER BY idfilial")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    def create_table():
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

    def insert_into(values):
        aux = 1
        if(not cid.selec_by_id(values[5])):
            print("Id da cidade não existe. \n")
            aux = 0
        if(not mat.selec_by_id(values[6])):
            print("Id do material não existe. \n")
            aux = 0

        if(aux):
            query = '''INSERT INTO filiais (nome, fone, rua , numero, bairro, idcida, idmate) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
            mycursor.execute(query, values)
            mydb.commit()
            print("Inserção concluida. \n")


    def selec_by_id(id):
        mycursor.execute("SELECT * FROM filiais WHERE idfilial = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        cont = 1
        for x in result: cont = cont + 1
        return cont
        
    def update_table(coluna, valor, id):
        aux = 1
        if(coluna == 'idcida' and not cid.selec_by_id(valor)):
            print("Id da cidade não existe .\n")
            aux = 0
        if(coluna == 'idmate' and not mat.selec_by_id(valor)):
            print("Id do material não existe .\n")
            aux = 0

        if(aux): 
            record = mycursor.execute("UPDATE filiais SET {} = '{}' WHERE idfilial = {} ;".format(coluna, valor, id))
            mydb.commit()
            print("Valor atualizado. \n")

    def delete_row_by_id(id):
        mycursor.execute("SELECT idmaq FROM maquinas WHERE idfilial = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        aux = 0
        for x in result: aux = aux + 1

        if (not aux):
            mycursor.execute("DELETE FROM filiais WHERE idfilial = '%s';" % id)
            mydb.commit()
            print("Exclusão concluida. \n")
        else:
            print("As seguintes maquinas são relacionadas a essa filial, é necessario que as delete antes de apagar a filial. \n")
            print(result)
    