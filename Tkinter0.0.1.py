from tkinter import *
from awesometkinter import *
import awesometkinter as atk

root = Tk()

class Application():
    def __init__(self):
        self.root = root
        self.frame_da_tela()
        self.widgets_frame()
        self.tela()
        root.mainloop()

    def tela(self):
        self.root.title('ONG')
        self.root.configure(background='gray20')
        self.root.geometry('800x400')
        self.root.resizable(False, False)

    def frame_da_tela(self):
        self.frame = Frame(self.root, bd=4, bg='gray20', highlightbackground='gray20', highlightthickness=3)
        self.frame.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets_frame(self):
        self.lb_codigo = Label(text='Login', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_codigo.place(relx=0.05, rely=0.1)

        self.codigo_entry = Entry()
        self.codigo_entry.place(relx=0.05, rely=0.2, relwidth=0.9)

        self.lb_nome = Label(text='Senha', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_nome.place(relx=0.05, rely=0.4)

        self.nome_entry = Entry()
        self.nome_entry.place(relx=0.05, rely=0.5, relwidth=0.9)

        self.bt_limpar = atk.Button3d(self.frame, text='Entrar')
        self.bt_limpar.place(relx=0.42, rely=0.8, relwidth=0.15, relheight=0.15)

Application()
