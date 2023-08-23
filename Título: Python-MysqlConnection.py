#Título: Python-MysqlConnection
#Para todos os exercícios utilize o pacote: mysql-connector-python.
#Todos os exercícios devem ser feitos em programas Python. Não deve ser entregue apenas comandos SQL feitos no Workbench.

#Crie a tabela “tb_jogador” com os campos:

#idt_jogador - INT AUTO_INCREMENT PRIMARY KEY
#nme_jogador - nome - VARCHAR(50)
#dsc_posicao_jogador - descrição da posição - TEXT
#vlr_passe_jogador - valor do passe - DECIMAL(10,2)

import mysql.connector
cnx = mysql.connector.connect(user='root', password="uniceub", host='127.0.0.1', database='TIME')
cs = cnx.cursor()
sql = '''CREATE TABLE JOGADOR(
idt_jogador INT AUTO_INCREMENT PRIMARY KEY,
nme_jogador VARCHAR(50) NOT NULL,
dsc_posicao_jogador TEXT,
vlr_passe_jogador DECIMAL(10,2));'''

cs.execute(sql, [])
cnx.commit()
cs.close()
cnx.close()

print("Tabela tb_jogador criada!")


#Insira três jogadores quaisquer na tabela tb_jogador (insert)
svl = "INSERT INTO JOGADOR(nme_jogador,dsc_posicao_jogador,vlr_passe_jogador) VALUES(%s,%s,%s);"
cs.execute(svl, ["guima","atacante", "50"])
idt = cs.lastrowid
cnx.commit()

cs.execute(svl, ["joao","goleiro", "80"])
idt = cs.lastrowid
cnx.commit()

cs.execute(svl, ["jefe","zaga", "25"])
idt = cs.lastrowid
cnx.commit()

#Liste (consulte) os jogadores persistidos (guardados) na tabela tb_jogador (select)

sql = "SELECT * FROM JOGADOR;"
cs.execute(sql, [])

print("tabela de jogadores:")

for (idt, nme, dsc, vlr) in cs:
   print(idt, nme, dsc, vlr)


cs.close()
cnx.close()





