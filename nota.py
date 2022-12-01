from tkinter import*

principal = Tk()
principal.title('notas')
principal.geometry("300x300+200+200")
princiapl.configure(background=cor1)

label=Label(principal, text= 'nome:', background = cor1) 
label.place(x=50, y=70)
entrada = entry(principal)
entrada.place(x=50,y=100)
botao = Button(principal, text= "nota", commamd=bt click)
botao.place(x=50,y=130)
def bt_click():
  num1=float(entrada.get())
  label["text"] = round(num1)
  