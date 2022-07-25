import Conexao as con

mydb = con.connect()
mycursor = mydb.cursor()

class Materiais():
    def all_materiais():
        mycursor.execute("SELECT * FROM materiais ORDER BY idmate")
        result = mycursor.fetchall()
        for x in result:
            print(x)

    def create_table():
        mycursor.execute("CREATE TABLE materiais (\
                            idmate int not null auto_increment,\
                            reciclado boolean not null,\
                            cor varchar(50) not null,\
                            tipo varchar(50) not null,\
                            PRIMARY KEY (idmate)\
                            );")
        print("Tabela criada. \n")

    def insert_into(values):
        query = '''INSERT INTO materiais (reciclado, cor, tipo) VALUES (%s, %s, %s)'''
        mycursor.execute(query, values)
        mydb.commit()
        print("Inserção concluida. \n")

    def selec_by_id(id):
        mycursor.execute("SELECT * FROM materiais WHERE idmate = '%s';" % id)
        result = mycursor.fetchall()
        print(result)
        cont = 1
        for x in result: cont = cont + 1
        return cont
        
    def update_table(coluna, valor, id):
        mycursor.execute("UPDATE materiais SET {} = '{}' WHERE idmate = {};".format(coluna, valor, id))
        mydb.commit()
        print("Valor atualizado. \n")


    def delete_row_by_id(id):
        mycursor.execute("SELECT idfilial FROM filiais WHERE idmate = '%s';" % id)
        result = mycursor.fetchall()
        aux = 0
        for x in result: aux = aux + 1

        if (not aux):
            mycursor.execute("DELETE FROM materiais WHERE idmate = '%s';" % id)
            mydb.commit()
            print("Exclusão concluida. \n")
        else:
            print("As seguintes filiais são relacionadas a esse material, é necessario que as delete antes de apagar o material. \n")
            print(result)
    