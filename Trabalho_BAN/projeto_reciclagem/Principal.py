#import mysql.connector
import Conexao as con
from Maquinas import Maquina as maq
from Materiais import Materiais as mat
from Filiais import Filiais as fil
from Cidades import Cidades as cid

mydb = con.connect()
mycursor = mydb.cursor()

#Criar banco de dados
#CREATE DATABASE projeto_reciclagemDB;

op = 1

#Criar tabelas
# maq.create_table()
# mat.create_table()
# fil.create_table()
# cid.create_table()

def inserirValor():
    tabela = input("Digite a tabela desejada: \n")
    valores = input("Valores: \n").split(',')

    if(tabela == "maquinas"):
        maq.insert_into(valores)
    elif (tabela == "filiais"):
        fil.insert_into(valores)
    elif (tabela == "materiais"):
        mat.insert_into(valores)
    elif (tabela == "cidades"):
        cid.insert_into(valores)
    else:
        print("Tabela não existe")

def pesqValor():
    tabela = input("Digite a tabela desejada: \n")
    id = input("Digite o id: \n")

    if(tabela == "maquinas"):
        maq.selec_by_id(id)
    elif (tabela == "filiais"):
        fil.selec_by_id(id)
    elif (tabela == "materiais"):
        mat.selec_by_id(id)
    elif (tabela == "cidades"):
        cid.selec_by_id(id)
    else:
        print("Tabela não existe")    


def atualizar():
    tabela = input("Digite a tabela desejada: \n")
    coluna = input("Digite a coluna: \n")
    valor = input("Digite o valor que deseja atualizar: \n")
    id = input("Digite o id: \n")

    if(tabela == "maquinas"):
        maq.update_table(coluna, valor, id)
    elif (tabela == "filiais"):
        fil.update_table(coluna, valor, id)
    elif (tabela == "materiais"):
        mat.update_table(coluna, valor, id)
    elif (tabela == "cidades"):
        cid.update_table(coluna, valor, id)
    else:
        print("Tabela não existe")   

def delValor():
    tabela = input("Digite a tabela desejada: \n")
    id = input("Digite o id: \n")

    if(tabela == "maquinas"):
        maq.delete_row_by_id(id)
    elif (tabela == "filiais"):
        fil.delete_row_by_id(id)
    elif (tabela == "materiais"):
        mat.delete_row_by_id(id)
    elif (tabela == "cidades"):
        cid.delete_row_by_id(id)
    else:
        print("Tabela não existe")   

def imprimirTabela():
    tabela = input("Digite a tabela desejada: \n")

    if(tabela == "maquinas"):
        maq.all_maquinas()
    elif (tabela == "filiais"):
        fil.all_filiais()
    elif (tabela == "materiais"):
        mat.all_materiais()
    elif (tabela == "cidades"):
        cid.all_cidades()
    else:
        print("Tabela não existe")  

def join():
    print("Todas as máquinas da filial com o id inserido:")
    id = input("Digite o id: \n")

    mycursor.execute("SELECT maquinas.nome\
                        FROM filiais\
                        JOIN maquinas ON maquinas.idFilial = filiais.idFilial\
                        WHERE filiais.idFilial = '%s';" %id)
    
    for x in mycursor:
        print(x)

def agregacao():
    print("Nome da filiais com as máquinas mais caras: \n")
    mycursor.execute("SELECT filiais.nome\
                        FROM filiais\
                        JOIN maquinas ON maquinas.idFilial = filiais.idFilial\
                        WHERE maquinas.valor = (SELECT max(valor) FROM maquinas);\
                        ")

    # mycursor.execute("SELECT filiais.nome FROM filiais JOIN maquinas ON maquinas.idFilial = filiais.idFilial WHERE maquinas.valor = (SELECT max(valor) FROM maquinas)")
    for x in mycursor:
        print(x)

while(op):
    print("------- MENU -------")
    print("1 - Inserir valores ")
    print("2 - Atualizar tabela")
    print("3 - Pesquisar a partir do id")
    print("4 - Deletar elemento")
    print("5 - Imprimir tabela")
    print("6 - Join")
    print("7 - Funcao de agregacao")
    print("8 - Mostrar todas as tabelas")
    print("0 - Sair do programa \n")
    op = int(input("Digite a opcao desejada: \n"))

    if(op == 1): inserirValor()
    elif (op == 2): atualizar()
    elif (op == 3): pesqValor()
    elif (op == 4): delValor()
    elif (op == 5): imprimirTabela()
    elif (op == 6): join()
    elif (op == 7): agregacao()
    elif (op == 8):
            print("\n --- Maquinas --- ")
            maq.all_maquinas()
            print("\n --- Filiais ---")
            fil.all_filiais()
            print("\n --- Materiais ---")
            mat.all_materiais()
            print("\n --- Cidades ---")
            cid.all_cidades()