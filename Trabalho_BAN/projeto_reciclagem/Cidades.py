import this
import Conexao as con

mydb = con.connect()
mycursor = mydb.cursor()

class Cidades():
    def all_cidades():
        mycursor.execute("SELECT * FROM cidades ORDER BY idcida")
        result = mycursor.fetchall()
        for x in result:
            print(x)


    def create_table():
        mycursor.execute("CREATE TABLE cidades (\
                            idcida int not null auto_increment,\
                            nome varchar(50) not null,\
                            estado varchar(50) not null,\
                            tam int not null,\
                            PRIMARY KEY (idcida)\
                            );")
        print("Tabela criada. \n")

    def insert_into(values):
        query = '''INSERT INTO cidades (nome, estado, tam) VALUES (%s, %s, %s)'''
        mycursor.execute(query, values)
        mydb.commit()
        print("Inserção concluida. \n")
        
    def selec_by_id(id):
        mycursor.execute("SELECT * FROM cidades WHERE idcida = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        cont = 1
        for x in result: cont = cont + 1
        return cont
        
    def update_table(coluna, valor, id):
        record = mycursor.execute("UPDATE cidades SET {} = '{}' WHERE idcida = {};".format(coluna, valor, id))
        mydb.commit()
        print("Valor atualizado. \n")

    def delete_row_by_id(id):
        mycursor.execute("SELECT idfilial FROM filiais WHERE idcida = '%s';" % id)
        result = mycursor.fetchall()
        aux = 0
        for x in result: aux = aux + 1

        if(not aux):
            mycursor.execute("DELETE FROM cidades WHERE idcida = '%s';" % id)
            mydb.commit()
            print("Exclusão concluida. \n")
        else:
            print("As seguintes filiais são relacionadas a essa cidade, é necessario que as delete antes de apagar a cidade. ")
            print(result)
            
        
    