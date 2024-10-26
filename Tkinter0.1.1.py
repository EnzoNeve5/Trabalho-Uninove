from tkinter import *
from awesometkinter import *
import awesometkinter as atk
import tkinter as tk

class Application():
    def __init__(self):
        self.root = tk.Tk()
        self.frame_da_tela()
        self.janela1()
        self.root.mainloop()

    def frame_da_tela(self):
        self.root.title('ONG')
        self.root.geometry('800x400')
        self.root.configure(background='gray20')
        self.root.resizable(False, False)

    def frame_da_tela2(self):
        self.frame1 = Frame(self.root, bd=4, bg='gray20', highlightbackground='gray20', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def frame_da_tela3(self):
        self.frame2 = Frame(self.root2, bd=4, bg='gray50', highlightbackground='gray50', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def frame_da_tela4(self):
        self.frame3 = Frame(self.root3, bd=4, bg='gray20', highlightbackground='gray20', highlightthickness=3)
        self.frame3.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets_frame2(self):
        self.lb_codigo = Label(self.frame1, text='E-mail', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_codigo.place(relx=0.05, rely=0.1)

        self.codigo_entry = Entry(self.frame1)
        self.codigo_entry.place(relx=0.05, rely=0.2, relwidth=0.9)

        self.lb_nome = Label(self.frame1, text='Senha', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_nome.place(relx=0.05, rely=0.4)

        self.nome_entry = Entry(self.frame1)
        self.nome_entry.place(relx=0.05, rely=0.5, relwidth=0.9)

        self.bt_limpar = atk.Button3d(self.frame1, text='Criar Conta', command=self.janela2)
        self.bt_limpar.place(relx=0.52, rely=0.8, relwidth=0.15, relheight=0.15)

        self.bt_limpar = atk.Button3d(self.frame1, text='Entrar', command=self.janela3)
        self.bt_limpar.place(relx=0.32, rely=0.8, relwidth=0.15, relheight=0.15)

    def widgets_frame3(self):
        self.lb_root2 = Label(self.frame2, text='Criar Conta', font=('verdana', 11, 'bold'), bg='white')
        self.lb_root2.place(relx=0.05, rely=0.05)

        self.lb_codigo = Label(self.frame2, text='E-mail', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_codigo.place(relx=0.05, rely=0.2)

        self.codigo_entry = Entry(self.frame2)
        self.codigo_entry.place(relx=0.05, rely=0.3, relwidth=0.9)

        self.lb_nome = Label(self.frame2, text='Senha', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_nome.place(relx=0.05, rely=0.4)

        self.nome_entry = Entry(self.frame2)
        self.nome_entry.place(relx=0.05, rely=0.5, relwidth=0.9)

        self.lb_nome = Label(self.frame2, text='Confirmar Senha', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_nome.place(relx=0.05, rely=0.6)

        self.nome_entry = Entry(self.frame2)
        self.nome_entry.place(relx=0.05, rely=0.7, relwidth=0.9)

        self.bt_limpar = atk.Button3d(self.frame2, text='Criar Conta', command=self.janela3)
        self.bt_limpar.place(relx=0.27, rely=0.85, relwidth=0.45, relheight=0.1)
    
    def widgets_frame4(self):
        self.lb_root3 = Label(self.frame3, text='Carregando...', font=('verdana', 11, 'bold'), bg='blue')
        self.lb_root3.place(relx=0.05, rely=0.15)

        bar = atk.RadialProgressbar3d(self.frame3, fg='blue', bg=atk.DEFAULT_COLOR, size=100)
        bar.place(relx=0.35, rely=0.5)
        bar.start()


    def janela1(self):
        self.root1 = tk.Toplevel()
        self.frame_da_tela2()
        self.widgets_frame2()
        self.root1.title('ONG bem vindo')
        self.root1.geometry('300x200')
        self.root1.configure(background='gray20')
        self.root1.resizable(False, False)
        self.root1.transient(self.root)
        self.root1.grab_set()

        label1 = tk.Label(self.root1, text="Sejam Bem Vindos!", bg='white', font=('verdana', 18, 'bold'))
        label1.pack(pady=70)

    def janela2(self):
        self.root2 = Toplevel()
        self.frame_da_tela3()
        self.widgets_frame3()
        self.root2.title('ONG criar conta')
        self.root2.configure(background='gray30')
        self.root2.geometry('400x600')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

    def janela3(self):
        self.root3 = Toplevel()
        self.frame_da_tela4()
        self.widgets_frame4()
        self.root3.title('ONG entrando')
        self.root3.configure(background='blue')
        self.root3.geometry('400x300')
        self.root3.resizable(False, False)
        self.root3.transient(self.root)
        self.root3.focus_force()
        self.root3.grab_set()

Application()
