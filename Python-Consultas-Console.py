import mysql.connector
from prettytable import PrettyTable
cnx = mysql.connector.connect(user='root', password='uniceub',
                            host='127.0.0.1',
                            database='crudatividade')

def incluir():
  sigla = input("Digite a sigla da DISCIPLINA para adicionar ao banco de dados:")
  nome = input("Digite o nome da disciplina:")
  carga = input("Digite a carga da disciplina:")


  sql = "INSERT INTO tb_dis(sgl_dis, nme_dis, num_ch_dis) VALUES(%s, %s,%s);"
  cursor = cnx.cursor()
  cursor.execute(sql, (sigla, nome,carga))
  idt = cursor.lastrowid
  print("Criada a tabela com a informçãoes=", idt)
  cnx.commit()
  cursor.close()

def consultar():
  print("Consultar a disciplina no banco de dados")
  cursor = cnx.cursor()
  sql = "SELECT * FROM tb_dis;"
  cursor.execute(sql)
  tab = PrettyTable(["Identificador", "Sigla", "Nome", "Carga"])
  for reg in cursor:
      tab.add_row(reg)
  cursor.close()
  print(tab)
  print("-------------------------------------------------")
  input("[Enter] para menu")

def alterar():
  print("Alterar UF")
  idt = int(input("Qual o identificador da disciplina para alterar? "))
  cursor = cnx.cursor()
  sql = "SELECT * FROM tb_dis WHERE idt_dis=%s;"
  cursor.execute(sql, [idt])
  dados = cursor.fetchone()# escolher só um
  cursor.close()
  if dados == None:
      print('UF não existe')
  else:
      (idt, sgl, nme,num_dis) = dados
      sigla = input("Digite a nova sigla da UF [" + sgl + "]: ")
      nome = input("Digite o novo nome da UF [" + nme + "]: ")
      carga = input("Digite novo valor para carga horária [" + str(num_dis) + "]:")
      sql = "UPDATE tb_dis SET sgl_dis=%s, nme_dis=%s, num_ch_dis=%s WHERE idt_dis=%s;"
      cursor = cnx.cursor()
      cursor.execute(sql, (sigla, nome,carga, idt))
      print("UF alterada!")
      cnx.commit()
      cursor.close()
  input("[Enter] para menu")

def excluir():
  print("Excluir UF")
  idt = int(input("Qual o identificador da disciplina para excluir? "))
  cursor = cnx.cursor()
  sql = "SELECT * FROM tb_dis WHERE idt_dis=%s;"
  cursor.execute(sql, [idt])
  dados = cursor.fetchone()
  cursor.close()
  if dados == None:
      print('UF não existe')
  else:
      (idt, sgl, nme,num_ch_dis) = dados
      print("Identificador:", idt)
      print("Sigla:", sgl)
      print("Nome:", nme)
      print("Carga:",num_ch_dis)
      exc = input("Deseja realmente excluir [S/N]: ")
      if exc == "S" or exc == 's':
          sql = "DELETE FROM tb_dis WHERE idt_dis=%s;"
          cursor = cnx.cursor()
          cursor.execute(sql, [idt])
          print("UF excluída!")
          cnx.commit()
          cursor.close()
  input("[Enter] para menu")
# Menu do CRUD
while True:

  print("CRUD de UF")
  print("1 - Incluir")
  print("2 - Consultar")
  print("3 - Alterar")
  print("4 - Excluir")
  print("5 - Sair")
  opcao = int(input("Qual a sua opção? "))
  match opcao:
      case 1: incluir()
      case 2: consultar()
      case 3: alterar()
      case 4: excluir()
      case 5:
          print("--- FIM DO CRUD ---")
          break
          #continuar = False
          cnx.close()




