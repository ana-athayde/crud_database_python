import mysql.connector
import Maquinas

#Inicializa banco de dados
#Já cria as tabelas

op = 1
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
    #if(not op): 
    #Opções: Inserir, atualizar, pesquisar, deletar valor da tabela