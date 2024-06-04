from paradassqlite import CriarSala, ColocarAluno, TirarAluno, RemoverSala, cur
from tkinter import Frame, LEFT, TOP, N, W, E, S, Label, Tk, Toplevel, Entry, X, Button
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as msb


def salas():
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
    mid4 = Frame(mid, bg='#fff')
    mid4.pack(side=LEFT)
    bot = Frame(mainframe, bg='#fff')
    bot.pack(side=TOP)
    bot1 = Frame(bot, bg='#fff')
    bot1.pack(side=LEFT)
    bot2 = Frame(bot, bg='#fff')
    bot2.pack(side=LEFT)


    #Funções

    def fetch_data():
        
        # Execute uma consulta
        cur.execute("SELECT IDPROFESSOR, Materia, Horario, Alunos FROM Salas")
        rows = cur.fetchall()
        
        return rows


    def checaridadd():
        ID = entry.get()
        if ID == '':
            msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
        else:
            cur.execute(f"SELECT 1 FROM \"Salas\" WHERE \"IDPROFESSOR\" = {ID}")
            resultado = cur.fetchone()
            if resultado is None:
                msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
            else:
                botao_addaluno()

    def checariddel():
        ID = entry.get()
        if ID == '':
            msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
        else:
            cur.execute(f"SELECT 1 FROM \"Salas\" WHERE \"IDPROFESSOR\" = {ID}")
            resultado = cur.fetchone()
            if resultado is None:
                msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
            else:
                botao_delaluno()

    def botao_delaluno():
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

            lbl_title = Label(form_titulo, text=f"Removendo aluno na sala de ID {ID}",
                            font=('arial', 18), bg='#57a1f9', width=280)
            lbl_title.pack(fill=X)
            lbl_id = Label(form_contato, text='ID Aluno', font=('arial', 12))
            lbl_id.grid(row=0, sticky=W)

            # --------- ENTRY - deletar -------------
            
            IDAluno_entry = Entry(form_contato, font=('arial', 12))
            IDAluno_entry.grid(row=0, column=1)
            IDAluno_entry.focus()

            def botaodeletar():
                if IDAluno_entry.get() == "":
                    msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
                else:
                    IDProfessor = ID
                    IDAluno = IDAluno_entry.get()
                    TirarAluno(IDAluno, IDProfessor)
                    tree.delete(*tree.get_children())
                    dados = fetch_data()
                    for item in dados:
                        tree.insert('', tk.END, values=item)
                    janela_adicionar.destroy()

        # --------- BOTÃO - deletar -------------
        bttn_enviardados = Button(form_contato, text="Confirmar",
                                width=50, command=botaodeletar)
        bttn_enviardados.grid(row=6, columnspan=2, pady=10)   

    def botao_addaluno():
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

            lbl_title = Label(form_titulo, text=f"Adicionando aluno na sala de ID {ID}",
                            font=('arial', 18), bg='#57a1f9', width=280)
            lbl_title.pack(fill=X)
            lbl_id = Label(form_contato, text='ID Aluno', font=('arial', 12))
            lbl_id.grid(row=0, sticky=W)

            # --------- ENTRY - CADASTRAR -------------
            
            IDAluno_entry = Entry(form_contato, font=('arial', 12))
            IDAluno_entry.grid(row=0, column=1)
            IDAluno_entry.focus()


            def botaoadicionar():
                if IDAluno_entry.get() == "" :
                    msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
                else:
                    IDAluno = IDAluno_entry.get()
                    cur.execute(f"SELECT 1 FROM \"Alunos\" WHERE \"ID\" = {IDAluno}")
                    resultado = cur.fetchone()
                    if resultado is None:
                        msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
                    else:
                        IDProfessor = ID
                        IDAluno = IDAluno_entry.get()
                        ColocarAluno(IDAluno, IDProfessor)
                        tree.delete(*tree.get_children())
                        dados = fetch_data()
                        for item in dados:
                            tree.insert('', tk.END, values=item)
                        janela_adicionar.destroy()

        # --------- BOTÃO - CADASTRAR -------------
        bttn_enviardados = Button(form_contato, text="Confirmar",
                                width=50, command=botaoadicionar)
        bttn_enviardados.grid(row=6, columnspan=2, pady=10)


    def botao_remover(): #Quando clica no botão deletar, pega o ID digitado e roda a função que deleta a sala, depois atauzaliza a Treeview.
        check = entry.get()
        if check == '':
            msb.showwarning("", "Por favor, digite um ID válido. ", icon="warning")
            return 0 
        else:
            resultado = msb.askquestion('', 'Tem certeza que deseja deletar a sala?')
            if resultado == 'yes':
                IDProfessor = entry.get()
                RemoverSala(IDProfessor)
                tree.delete(*tree.get_children())
                dados = fetch_data()
                for item in dados:
                    tree.insert('', tk.END, values=item)
            else :
                return 0
        


    def botao_adicionar():
        janela_adicionar = Toplevel()
        janela_adicionar.title("Adicionar Sala")
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

        lbl_title = Label(form_titulo, text="Adicionando Sala",
                        font=('arial', 18), bg='#57a1f9', width=280)
        lbl_title.pack(fill=X)
        lbl_id = Label(form_contato, text='IDPROFESSOR', font=('arial', 12))
        lbl_id.grid(row=0, sticky=W)
        lbl_horario = Label(form_contato, text='Horario', font=('arial', 12))
        lbl_horario.grid(row=1, sticky=W)

        # --------- ENTRY - CADASTRAR -------------
        id_entry = Entry(form_contato, font=('arial', 12))
        id_entry.grid(row=0, column=1)
        id_entry.focus()
        horario_entry = Entry(form_contato, font=('arial', 12))
        horario_entry.grid(row=1, column=1)


        def botaoadicionar():
            if id_entry.get() == "" or horario_entry.get() == "":
                msb.showwarning("", "Por favor, digite todos os campos.", icon="warning")
            else:
                IDProfessor = id_entry.get()
                Horario = horario_entry.get()
                CriarSala(IDProfessor, Horario)
                tree.delete(*tree.get_children())
                dados = fetch_data()
                for item in dados:
                    tree.insert('', tk.END, values=item)

        # --------- BOTÃO - CADASTRAR -------------
        bttn_enviardados = Button(form_contato, text="Cadastrar",
                                width=50, command=botaoadicionar)
        bttn_enviardados.grid(row=6, columnspan=2, pady=10)

    #Treeview

    tree = ttk.Treeview(top, columns=("IDPROFESSOR", "Materia", "Horario", "Alunos"), show='headings')
    tree.column(column='IDPROFESSOR', width=125, stretch=False)
    tree.column(column='Materia', width=125, stretch=False)
    tree.column(column='Horario', width=125, stretch=False)
    tree.column(column='Alunos', width=125, stretch=True)

    # Definição das colunas
    tree.heading("IDPROFESSOR", text="IDPROFESSOR")
    tree.heading("Materia", text="Materia")
    tree.heading("Horario", text="Horario")
    tree.heading("Alunos", text="Alunos")

    # Empacotamento da Treeview
    tree.pack(pady=20, fill='x')

    # Busca de dados do banco de dados e inserção na Treeview
    dados = fetch_data()
    for item in dados:
        tree.insert('', tk.END, values=item)

    #Entrada ID
    entry = Entry(bot2, width=7)
    entry.pack(pady=10)
    lbl_id = Label(bot1, text='Digite o IDProfessor:', bg='#fff')
    lbl_id.pack(side=LEFT)

    #Botões
    butao = Button(mid1, text="Remover", command=botao_remover)
    butao.pack(pady=10)
    butao2 = Button(mid2, text="Adicionar", command=botao_adicionar)
    butao2.pack(pady=10)
    butao3 = Button(mid3, text="Adicionar Aluno", command=checaridadd, width=15)
    butao3.pack()
    butao3 = Button(mid3, text="Remover Aluno", command=checariddel, width=15)
    butao3.pack()



    root.mainloop()

if __name__ == '__main__':
    salas()