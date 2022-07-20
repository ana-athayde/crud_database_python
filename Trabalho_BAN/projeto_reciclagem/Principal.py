#import mysql.connector
from Maquinas import Maquina as maq
#from Filiais import Filial as fil
#from 

#Inicializa banco de dados
#Já cria as tabelas

op = 1
maq.create_table()

def inserirValor():
    tabela = input("Digite a tabela desejada: \n")
    valores = input("Valores: \n").split(',')

    if(tabela == "maquinas"):
        maq.insert_into(valores)
    #elif (tabela == "filiais"):
        #fil.insert_into(valores)
    op = 0



while(op):
    print("------- MENU -------")
    print("1 - Inserir valores ")
    print("2 - Atualizar tabela")
    print("3 - Pesquisar a partir de uma coluna")
    print("4 - Deletar elemento")
    print("5 - Imprimir tabela")
    print("6 - Join")
    print("7 - Funcao de agregacao")
    print("0 - Sair do programa \n")
    op = int(input("Digite a opcao desejada: \n"))

    if(op == 1): inserirValor()
    #if(not op): 
    #Opções: Inserir, atualizar, pesquisar, deletar valor da tabela


