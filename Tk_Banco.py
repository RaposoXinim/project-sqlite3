import sqlite3
from tkinter import messagebox
import datetime
import os
def conectar():
    try:
        
        conn = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'escola.db'))

        return conn

    except (Exception, sqlite3.Error) as erro:
        print("Erro ao conectar ao Sqlite3", erro)

def registro(login, senha):
    conn=conectar()
    try:
        cur=conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS Cadastros(
    LOGIN TEXT PRIMARY KEY,
    SENHA TEXT
    )
    """)
        cur.execute("INSERT INTO Cadastros VALUES (?, ?)", (login, senha))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", "Usuário já existe. Escolha outro Usuário.")
        return False
    finally:
        conn.close()

def logar(login, senha):
    conn=conectar()
    try:
        cur=conn.cursor()
        cur.execute("SELECT login, senha FROM Cadastros WHERE login = ? and senha =?", (login, senha))
        resultado = cur.fetchone()
        if resultado:
            return True
        else:
            messagebox.showerror("Erro", "Usuário e/ou senha incorreto(s) ou não cadastrado!")
            return False
    except sqlite3.Error as e:
        print(f"Erro ao realizar o login: {e}")
    finally:
        conn.close()

def Gerarlog(usuario):
    with open("log.txt", "a") as arquivo:
        time = datetime.datetime.now()
        arquivo.write(f"{time} Usuario: {usuario}\n")