import sqlite3
arquivo_bancodedados = "banco.db"

def criar():
  conexao=None
  try:
    conexao = sqlite3.connect(arquivo_banco)
  except sqlite3.Error as e:
    print("Algo deu errado", e)

  return 
  
def fechar (conexao):
  if conexao:
    conexao.close()

def criar_tabela(conexao, sql_criar_tabela):
  try:
    cursor = conexao. cursor()
    cursor. execute(sql_criar_tabela)
  except sqlite3.Error as e:
    print("algo deu errado", e)

def inserir_aluno (conexao, sql_inserir_aluno):
  try:
    cursor = conexao.cursor()
    cursor.execute(sql_inserir_aluno)
    conexao.commit()
  except sqlite3.Error as e:
    print("algo deu errado",e)
    
def buscar(conexao, sql_buscar):
  alunos = None
  try:
    cursor = conexao.cursor()
    cursor.execute(sql_buscar)
    alunos=cursor.fetchall()
  except sqlite3.Error as e:
    print("algo deu errado")
  finally:
    return alunos