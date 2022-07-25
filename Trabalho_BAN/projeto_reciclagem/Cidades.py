import this
import Conexao as con

class Cidades():
    def all_cidades():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM cidades ORDER BY idcida")
        result = mycursor.fetchall()
        for x in result:
            print(x)

        mycursor.close()
        mydb.close()

    def create_table():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE cidades (\
                            idcida int not null auto_increment,\
                            nome varchar(50) not null,\
                            estado varchar(50) not null,\
                            tam int not null,\
                            PRIMARY KEY (idcida)\
                            );")
        print("Tabela criada. \n")

        mycursor.close()
        mydb.close()

    def insert_into(values):
        mydb = con.connect()
        mycursor = mydb.cursor()

        query = '''INSERT INTO cidades (nome, estado, tam) VALUES (%s, %s, %s)'''
        mycursor.execute(query, values)
        mydb.commit()
        print("Inserção concluida. \n")

        mycursor.close()
        mydb.close()
        
    def selec_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM cidades WHERE idcida = '%s';" % id)
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
        if(coluna == 'idcida'):
            print("Não é permitido atualizar o id da cidade. \n")
            aux = 0

        if(aux):
            record = mycursor.execute("UPDATE cidades SET {} = '{}' WHERE idcida = {};".format(coluna, valor, id))
            mydb.commit()
            print("Valor atualizado. \n")

        


    def delete_row_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT idcida FROM cidades WHERE idcida = '%s';" % id)
        result_1 = mycursor.fetchall()
        aux_1 = 0
        for x in result_1: aux_1 = aux_1 + 1

        mycursor.close()
        
        if(not aux_1):
            print("Não foi possivel encontrar a cidade com o id passado. \n")
        else:
            mycursor = mydb.cursor()

            mycursor.execute("SELECT idfilial FROM filiais WHERE idcida = '%s';" % id)
            result = mycursor.fetchall()
            aux = 0
            for x in result: aux = aux + 1

            mycursor.close()

            if(not aux):
                mycursor = mydb.cursor()
                mycursor.execute("DELETE FROM cidades WHERE idcida = '%s';" % id)
                mydb.commit()
                print("Exclusão concluida. \n")
                mycursor.close()
            else:
                print("As seguintes filiais são relacionadas a essa cidade, é necessario que as delete antes de apagar a cidade. ")
                print(result)

        mydb.close()
            
        
    