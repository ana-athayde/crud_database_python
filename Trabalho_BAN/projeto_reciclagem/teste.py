import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="projeto_reciclagemDB"
)

mycursor = mydb.cursor()

#mycursor.execute("DROP TABLE maquinas;")
#mycursor.execute("CREATE TABLE maquinas (idmaq int not null auto_increment, nome char(50), PRIMARY KEY (idmaq));")
mycursor.execute("INSERT INTO maquinas (idmaq, nome) VALUES (1, 50);")
mydb.commit()
mycursor.execute("INSERT INTO maquinas (idmaq, nome) VALUES (2, 30);")
mydb.commit()
mycursor.execute("SELECT * FROM maquinas")

for x in mycursor:
    print(x)

mydb.close()
