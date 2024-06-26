from paradassqlite import AdiconarProfessor, RemoverProfessor, EditarProfessor, cur
from tkinter import Frame, LEFT, TOP, N, W, E, S, Label, Tk, Toplevel, Entry, X, Button
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as msb


def professores():
    #Root

    root = Tk()
    root.title("Sistema Épico de Coisas e Trecos")
    width = 700
    height = 400
    sc_width = root.winfo_screenwidth()
    sc_height = root.winfo_screenheight()
    x = (sc_width/2) - (width/2)
    y = (sc_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.configure(bg='#fff')
    root.resizable(False, False)

    #Mainframe

    mainframe = Frame(root, bg='#fff')
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    top = Frame(mainframe, bg='#fff', padx=10)
    top.pack(side=TOP)
    mid = Frame(mainframe, bg='#fff')
    mid.pack(side=TOP)
    mid1 = Frame(mid, bg='#fff')
    mid1.pack(side=LEFT)
    mid2 = Frame(mid, bg='#fff')
    mid2.pack(side=LEFT)
    mid3 = Frame(mid, bg='#fff')
    mid3.pack(side=LEFT)
    bot = Frame(mainframe, bg='#fff')
    bot.pack(side=TOP)
    bot1 = Frame(bot, bg='#fff')
    bot1.pack(side=LEFT)
    bot2 = Frame(bot, bg='#fff')
    bot2.pack(side=LEFT)

    #Funções


    def fetch_data():
        cur.execute("SELECT ID, Nome, Materia FROM Professores")
        rows = cur.fetchall()
        
        return rows

    def checarid():
        ID = entry.get()
        if ID == '':
            msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
        else:
            cur.execute(f"SELECT 1 FROM \"Professores\" WHERE \"ID\" = {ID}")
            resultado = cur.fetchone()
            if resultado is None:
                msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
            else:
                botao_editar()

    def botao_editar():
        ID = entry.get()
        if ID == '':
            msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
        else:
            janela_adicionar = Toplevel()
            janela_adicionar.title("Editar Professor")
            form_titulo = Frame(janela_adicionar)
            form_titulo.pack(side=TOP)
            form_contato = Frame(janela_adicionar)
            form_contato.pack(side=TOP, pady=10)
            width = 400
            height = 200
            sc_width = janela_adicionar.winfo_screenwidth()
            sc_height = janela_adicionar.winfo_screenheight()
            x = (sc_width/2) - (width/2)
            y = (sc_height/2) - (height/2)
            janela_adicionar.geometry("%dx%d+%d+%d" % (width, height, x, y))
            janela_adicionar.resizable(0, 0)

            lbl_title = Label(form_titulo, text=f"Editando o professor de ID {ID}",
                            font=('arial', 18), bg='#57a1f9', width=280)
            lbl_title.pack(fill=X)
            lbl_id = Label(form_contato, text='ID', font=('arial', 12))
            lbl_id.grid(row=0, sticky=W)
            lbl_nome = Label(form_contato, text='Nome', font=('arial', 12))
            lbl_nome.grid(row=1, sticky=W)
            lbl_materia = Label(form_contato, text='Matéria', font=('arial', 12))
            lbl_materia.grid(row=2, sticky=W)

            # --------- ENTRY - EDITAR -------------
            
            nome_entry = Entry(form_contato, font=('arial', 12))
            nome_entry.grid(row=1, column=1)
            nome_entry.focus()
            materia_entry = Entry(form_contato, font=('arial', 12))
            materia_entry.grid(row=2, column=1)
            #Função do botão
            def botaoeditar():
                if nome_entry.get() == "" or materia_entry.get() == "":
                    msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
                else:
                    Nome = nome_entry.get()
                    Materia = materia_entry.get()
                    EditarProfessor(ID, Nome, Materia)
                    tree.delete(*tree.get_children())
                    dados = fetch_data()
                    for item in dados:
                        tree.insert('', tk.END, values=item)
                    janela_adicionar.destroy()

        # --------- BOTÃO - Editar -------------
        bttn_enviardados = Button(form_contato, text="Confirmar",
                                width=50, command=botaoeditar)
        bttn_enviardados.grid(row=6, columnspan=2, pady=10)


    def botao_remover(): #Quando clica no botão deletar, pega o ID digitado e roda a função que deleta o respectivo professor, depois atauzaliza a Treeview.
        check = entry.get()
        if check == '':
            msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
            return 0 
        else:    
            resultado = msb.askquestion('', f'Tem certeza que deseja deletar o professor de ID {check}?')
            if resultado == 'yes':
                ID = entry.get()
                RemoverProfessor(ID)
                tree.delete(*tree.get_children())
                dados = fetch_data()
                for item in dados:
                    tree.insert('', tk.END, values=item)
            else :
                return 0 


    def botao_adicionar():
        janela_adicionar = Toplevel()
        janela_adicionar.title("Adicionar Professor")
        form_titulo = Frame(janela_adicionar)
        form_titulo.pack(side=TOP)
        form_contato = Frame(janela_adicionar)
        form_contato.pack(side=TOP, pady=10)
        width = 400
        height = 200
        sc_width = janela_adicionar.winfo_screenwidth()
        sc_height = janela_adicionar.winfo_screenheight()
        x = (sc_width/2) - (width/2)
        y = (sc_height/2) - (height/2)
        janela_adicionar.geometry("%dx%d+%d+%d" % (width, height, x, y))
        janela_adicionar.resizable(0, 0)

        lbl_title = Label(form_titulo, text="Adicionando Professor",
                        font=('arial', 18), bg='#57a1f9', width=280)
        lbl_title.pack(fill=X)
        lbl_id = Label(form_contato, text='ID', font=('arial', 12))
        lbl_id.grid(row=0, sticky=W)
        lbl_nome = Label(form_contato, text='Nome', font=('arial', 12))
        lbl_nome.grid(row=1, sticky=W)
        lbl_materia = Label(form_contato, text='Matéria', font=('arial', 12))
        lbl_materia.grid(row=2, sticky=W)

        # --------- ENTRY - CADASTRAR -------------
        id_entry = Entry(form_contato, font=('arial', 12))
        id_entry.grid(row=0, column=1)
        id_entry.focus()
        nome_entry = Entry(form_contato, font=('arial', 12))
        nome_entry.grid(row=1, column=1)
        materia_entry = Entry(form_contato, font=('arial', 12))
        materia_entry.grid(row=2, column=1)

        def botaoadicionar():
            if id_entry.get() == "" or nome_entry.get() == "" or materia_entry.get() == "":
                msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
            else:
                IDadicionar = id_entry.get()
                Nome = nome_entry.get()
                Materia = materia_entry.get()
                AdiconarProfessor(IDadicionar, Nome, Materia)
                tree.delete(*tree.get_children())
                dados = fetch_data()
                for item in dados:
                    tree.insert('', tk.END, values=item)

        # --------- BOTÃO - CADASTRAR -------------
        bttn_enviardados = Button(form_contato, text="Cadastrar",
                                width=50, command=botaoadicionar)
        bttn_enviardados.grid(row=6, columnspan=2, pady=10)

    #Treeview

    tree = ttk.Treeview(top, columns=("ID", "Nome", "Materia"), show='headings')

    # Definição das colunas
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Materia", text="Materia")

    # Empacotamento da Treeview
    tree.pack(pady=20)

    # Busca de dados do banco de dados e inserção na Treeview
    dados = fetch_data()
    for item in dados:
        tree.insert('', tk.END, values=item)

    #Entrada ID
    entry = Entry(bot2, width=7)
    entry.pack(pady=10)
    lbl_id = Label(bot1, text='Digite o ID :', bg='#fff')
    lbl_id.pack(side=LEFT)
    #Botões
    butao = Button(mid1, text="Remover", command=botao_remover)
    butao.pack(pady=10)
    butao2 = Button(mid2, text="Adicionar", command=botao_adicionar)
    butao2.pack(pady=10)
    butao3 = Button(mid3, text="Editar", command=checarid)
    butao3.pack(pady=10)


    root.mainloop()