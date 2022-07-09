# Importando a biblioteca de GUI do Python
from tkinter import *
from turtle import color


class telas(object):
    
    def __init__(self,instancia):        

        # Definindo o tamanho da Janela
        instancia.geometry("800x600")  # LarguraxAltura

        # Título para Janela
        instancia.title("Minha Primeira Janela")

        # Icone da Janela
        instancia.wm_iconbitmap("icon\\casa.ico")


        self.input = Entry(instancia)
        self.input.pack()
        
        self.botao = Button(instancia, text="Clique", bg="orange", command=self.Nome)
        self.botao.pack()

        self.label = Label(instancia, text="Minha Primeira Tela!", bg="white", fg="blue")
        self.label.pack()
        
        instancia.mainloop()

    def Nome(self):
        self.label["text"] = self.input.get()








# Instanciando o objeto/classe de Janela do pacote "tkinter"
tela = Tk()
telas(tela)


