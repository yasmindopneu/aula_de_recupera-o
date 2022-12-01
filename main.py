from conexao import*

conexao = iniciar_conexao()
sql_criar_tabela = """CREATE TABLE IF NOT EXISTS alunos (id intereger PRIMARY KEY AUTOINCREMENT, nome text NOT NULL, nota integer NOT NULL);"""

criar_tabela(conexao, sql_criar_tabela)
sql_inserir_aluno="INSERT INTO alunos (nome,nota) VALUES (" "," ")"
inserir_aluno (conexao, sql_inserir_aluno)
fechar_conexao(conexao)
for aluno in alunos:
  print(f'0 aluno {aluno[1]} tirou nota {aluno[2]}') 

import tkinter as tk

window = tk.Tk()
window.title("Hello wold")
window.geometry("300x300")

hello = tk.Label(text="Hello world!")
hello.pack()
button = tk.Button(text="Click me!")
button.pack()

tk.mainloop()