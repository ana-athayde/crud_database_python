import Conexao as con
from Filiais import Filiais as fil

mydb = con.connect()
mycursor = mydb.cursor()

class Maquina():
    def all_maquinas():
        mycursor.execute("SELECT * FROM maquinas ORDER BY idmaq")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    def create_table():
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

    def insert_into(values):
        aux = 1
        if( not fil.selec_by_id(values[7])):
            print("Id da filial não existe .\n")
            aux = 0

        if(aux):
            query = '''INSERT INTO maquinas (tpmaterial, anocompra, anoulrev, nome, tipo, valor, descricao, idfilial) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) '''
            mycursor.execute(query, values)
            mydb.commit()
            print("Inserção concluida. \n")
        
    def selec_by_id(id):
        mycursor.execute("SELECT * FROM maquinas WHERE idmaq = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        cont = 1
        for x in result: cont = cont + 1
        return cont

        
    def update_table(coluna, valor, id):
        aux = 1
        if(coluna == 'idfilial' and not fil.selec_by_id(valor)):
            print("Id da filial não existe .\n")
            aux = 0

        if(aux):
            record = mycursor.execute("UPDATE maquinas SET {} = '{}' WHERE idmaq = {};".format(coluna, valor, id))
            mydb.commit()
            print("Valor atualizado. \n")
    
    def delete_row_by_id(id):
        mycursor.execute("DELETE FROM maquinas WHERE idmaq = '%s';" % id)
        mydb.commit() 
        print("Exclusão concluida. \n")
