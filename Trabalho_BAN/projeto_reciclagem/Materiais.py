import Conexao as con

class Materiais():
    def all_materiais():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM materiais ORDER BY idmate")
        result = mycursor.fetchall()
        for x in result:
            print(x)

        mycursor.close()
        mydb.close()

    def create_table():
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("CREATE TABLE materiais (\
                            idmate int not null auto_increment,\
                            reciclado boolean not null,\
                            cor varchar(50) not null,\
                            tipo varchar(50) not null,\
                            PRIMARY KEY (idmate)\
                            );")
        print("Tabela criada. \n")

        mycursor.close()
        mydb.close()


    def insert_into(values):
        mydb = con.connect()
        mycursor = mydb.cursor()

        query = '''INSERT INTO materiais (reciclado, cor, tipo) VALUES (%s, %s, %s)'''
        mycursor.execute(query, values)
        mydb.commit()
        print("Inserção concluida. \n")

        mycursor.close()
        mydb.close()

    def selec_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM materiais WHERE idmate = '%s';" % id)
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
        if(coluna == 'idmate'):
            print("Não é permitido atualizar o id do material. \n")
            aux = 0

        if(aux):
            mycursor.execute("UPDATE materiais SET {} = '{}' WHERE idmate = {};".format(coluna, valor, id))
            mydb.commit()
            print("Valor atualizado. \n")

        mycursor.close()
        mydb.close()


    def delete_row_by_id(id):
        mydb = con.connect()
        mycursor = mydb.cursor()

        mycursor.execute("SELECT idmate FROM materiais WHERE idmate = '%s';" % id)
        result_1 = mycursor.fetchall()
        aux_1 = 0
        for x in result_1: aux_1 = aux_1 + 1

        mycursor.close()


        if(not aux_1):
            print("Não foi possivel encontrar o material com o id passado. \n")
        else:      
            mycursor = mydb.cursor()

            mycursor.execute("SELECT idfilial FROM filiais WHERE idmate = '%s';" % id)
            result = mycursor.fetchall()
            aux = 0
            for x in result: aux = aux + 1

            mycursor.close()

            if (not aux):
                mycursor = mydb.cursor()

                mycursor.execute("DELETE FROM materiais WHERE idmate = '%s';" % id)
                mydb.commit()
                print("Exclusão concluida. \n")

                mycursor.close()
            else:
                print("As seguintes filiais são relacionadas a esse material, é necessario que as delete antes de apagar o material. \n")
                print(result)
            
        mydb.close()
    