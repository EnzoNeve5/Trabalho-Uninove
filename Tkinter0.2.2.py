from tkinter import *
from awesometkinter import *
import awesometkinter as atk
import tkinter as tk
from tkinter import messagebox  # Para exibir mensagens

class Application():
    def __init__(self):
        # Inicializa a aplicação, cria a tela principal e executa o loop principal da interface gráfica.
        self.root = tk.Tk()
        self.frame_da_tela()

        # Lista para armazenar dados dos usuários criados
        self.usuarios = []

        # Abre a primeira janela (login/criação de conta)
        self.janela1()
        self.root.mainloop()

    def frame_da_tela(self):
        # Configura a tela principal da aplicação com título, dimensões e cor de fundo.
        self.root.title('ONG')
        self.root.geometry('800x400')
        self.root.configure(background='gray20')
        self.root.resizable(False, False)

    def frame_da_tela2(self):
        # Configura um frame na tela principal para organizar os widgets do login.
        self.frame1 = Frame(self.root, bd=4, bg='gray20', highlightbackground='gray20', highlightthickness=3)
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def frame_da_tela3(self):
        # Configura um frame em uma nova janela (root2) para organizar os widgets da criação de conta.
        self.frame2 = Frame(self.root2, bd=4, bg='gray50', highlightbackground='gray50', highlightthickness=3)
        self.frame2.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def frame_da_tela4(self):
        # Configura um frame em uma nova janela (root3) para organizar os widgets após login bem-sucedido.
        self.frame3 = Frame(self.root3, bd=4, bg='gray20', highlightbackground='gray20', highlightthickness=3)
        self.frame3.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)

    def widgets_frame2(self):
        # Define e posiciona os widgets da tela de login: campos para nome, email, senha, e botões de criar conta ou entrar.
        self.lb_nome = Label(self.frame1, text='Nome Completo', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_nome.place(relx=0.05, rely=0.05)

        self.entry_nome = Entry(self.frame1)
        self.entry_nome.place(relx=0.05, rely=0.15, relwidth=0.9)

        self.lb_email = Label(self.frame1, text='E-mail', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_email.place(relx=0.05, rely=0.25)

        self.entry_email = Entry(self.frame1)
        self.entry_email.place(relx=0.05, rely=0.35, relwidth=0.9)

        self.lb_senha = Label(self.frame1, text='Senha', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_senha.place(relx=0.05, rely=0.45)

        self.entry_senha = Entry(self.frame1, show='*')
        self.entry_senha.place(relx=0.05, rely=0.55, relwidth=0.9)

        # Botão para abrir a janela de criação de conta
        self.bt_criar_conta = atk.Button3d(self.frame1, text='Criar Conta', command=self.janela2)
        self.bt_criar_conta.place(relx=0.52, rely=0.8, relwidth=0.15, relheight=0.15)

        # Botão para verificar login ao clicar em "Entrar"
        self.bt_entrar = atk.Button3d(self.frame1, text='Entrar', command=self.verificar_login)
        self.bt_entrar.place(relx=0.32, rely=0.8, relwidth=0.15, relheight=0.15)

    def widgets_frame3(self):
        # Define e posiciona os widgets da tela de criação de conta: campos para nome, email, senha, confirmação de senha, e botão de criação de conta.
        self.lb_titulo = Label(self.frame2, text='Criar Conta', font=('verdana', 11, 'bold'), bg='white')
        self.lb_titulo.place(relx=0.05, rely=0.05)

        self.lb_nome = Label(self.frame2, text='Nome Completo', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_nome.place(relx=0.05, rely=0.15)

        self.entry_nome_criar = Entry(self.frame2)
        self.entry_nome_criar.place(relx=0.05, rely=0.22, relwidth=0.9)

        self.lb_email = Label(self.frame2, text='E-mail', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_email.place(relx=0.05, rely=0.3)

        self.entry_email_criar = Entry(self.frame2)
        self.entry_email_criar.place(relx=0.05, rely=0.37, relwidth=0.9)

        self.lb_senha = Label(self.frame2, text='Senha', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_senha.place(relx=0.05, rely=0.45)

        self.entry_senha_criar = Entry(self.frame2, show='*')
        self.entry_senha_criar.place(relx=0.05, rely=0.52, relwidth=0.9)

        self.lb_confirmar_senha = Label(self.frame2, text='Confirmar Senha', font=('verdana', 11, 'bold'), bg='gray80')
        self.lb_confirmar_senha.place(relx=0.05, rely=0.6)

        self.entry_confirmar_senha_criar = Entry(self.frame2, show='*')
        self.entry_confirmar_senha_criar.place(relx=0.05, rely=0.67, relwidth=0.9)

        # Botão para confirmar e criar a conta
        self.bt_criar_conta = atk.Button3d(self.frame2, text='Criar Conta', command=self.criar_conta)
        self.bt_criar_conta.place(relx=0.27, rely=0.85, relwidth=0.45, relheight=0.1)

    def criar_conta(self):
        # Função que coleta os dados de nome, email e senha para criar a conta e armazenar os dados na lista de usuários
        nome = self.entry_nome_criar.get()
        email = self.entry_email_criar.get()
        senha = self.entry_senha_criar.get()
        confirmar_senha = self.entry_confirmar_senha_criar.get()

        # Valida se todos os campos estão preenchidos e se as senhas coincidem
        if not nome or not email or not senha:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos!")
            return

        if senha != confirmar_senha:
            messagebox.showerror("Erro", "As senhas não coincidem!")
            return

        # Armazenar os dados do usuário criado
        self.usuarios.append({'nome': nome, 'email': email, 'senha': senha})

        # Exibe mensagem de sucesso e fecha a janela de criação de conta
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        self.root2.destroy()

    def verificar_login(self):
        # Função que verifica se o email e senha inseridos no login correspondem a um usuário cadastrado.
        email = self.entry_email.get()
        senha = self.entry_senha.get()

        # Itera pela lista de usuários para encontrar um usuário correspondente ao email e senha
        for usuario in self.usuarios:
            if usuario['email'] == email and usuario['senha'] == senha:
                messagebox.showinfo("Sucesso", f"Bem-vindo, {usuario['nome']}!")
                self.janela3()  # Chama a próxima janela após login bem-sucedido
                return

        # Exibe mensagem de erro se o login for inválido
        messagebox.showerror("Erro", "Email ou senha inválidos!")

    def widgets_frame4(self):
        # Configura um botão, três labels e três campos de entrada na janela após login bem-sucedido.
        self.lb_nome_instituicao = Label(self.frame3, text='Nome da Instituição', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_nome_instituicao.place(relx=0.05, rely=0.1)

        self.entry_nome_completo = Entry(self.frame3)
        self.entry_nome_completo.place(relx=0.05, rely=0.2, relwidth=0.9)

        self.lb_valor = Label(self.frame3, text='Valor', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_valor.place(relx=0.05, rely=0.3)

        self.entry_valor = Entry(self.frame3)
        self.entry_valor.place(relx=0.05, rely=0.4, relwidth=0.9)

        self.lb_chavepix = Label(self.frame3, text='Chave PIX', font=('verdana', 11, 'bold'), bg='gray70')
        self.lb_chavepix.place(relx=0.05, rely=0.5)

        self.entry_chavepix = Entry(self.frame3)
        self.entry_chavepix.place(relx=0.05, rely=0.6, relwidth=0.9)

        self.bt_doar = atk.Button3d(self.frame3, text='Doar')
        self.bt_doar.place(relx=0.42, rely=0.8, relwidth=0.15, relheight=0.15)

    def janela1(self):
        # Cria a primeira janela que contém o login e opções para criar uma conta ou entrar.
        self.root1 = tk.Toplevel()
        self.frame_da_tela2()
        self.widgets_frame2()
        self.root1.title('ONG Bem Vindo')
        self.root1.geometry('300x200')
        self.root1.configure(background='gray20')
        self.root1.resizable(False, False)
        self.root1.transient(self.root)
        self.root1.grab_set()

        # Define rótulos de boas-vindas e instruções.
        self.label1 = tk.Label(self.root1, text="Sejam Bem Vindos!", bg='white', font=('verdana', 18, 'bold'))
        self.label1.pack(pady=20)

        self.label2 = tk.Label(self.root1, text="Você pode ajudar pessoas em situação vulnerável doando para a sua ONG de preferência!", bg='white', font=('verdana', 12), wraplength=280)
        self.label2.pack(pady=10)

    def janela2(self):
        # Cria a janela para criar uma conta, com campos para nome, email, senha, etc.
        self.root2 = Toplevel()
        self.frame_da_tela3()
        self.widgets_frame3()
        self.root2.title('Criar Conta')
        self.root2.configure(background='gray30')
        self.root2.geometry('400x600')
        self.root2.resizable(False, False)
        self.root2.transient(self.root)
        self.root2.focus_force()
        self.root2.grab_set()

    def janela3(self):
        # Cria a janela após login bem-sucedido, com uma barra de progresso simulando carregamento.
        self.root3 = Toplevel()
        self.frame_da_tela4()
        self.widgets_frame4()
        self.root3.title('Entrando')
        self.root3.configure(background='gray30')
        self.root3.geometry('400x300')
        self.root3.resizable(False, False)
        self.root3.transient(self.root)
        self.root3.focus_force()
        self.root3.grab_set()

Application()
