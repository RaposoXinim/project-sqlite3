from dataclasses import dataclass
import sqlite3
import os
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as msb


def conectar():
    try:
        nome_banco= os.path.join(os.path.dirname(__file__), 'escola.db')
        conn = sqlite3.connect(nome_banco)
        return conn
    except (Exception, sqlite3.Error) as erro:
        print("Erro ao conectar ao PostgreSQL", erro)

conn=conectar()

cur = conn.cursor()



#@dataclass

#class Aluno():
#   ID : int
#    Nome : str
#
#class Professor():
#    ID : int
#    Nome : str
#    Materia : str


def AdicionarAluno(ID, Nome):
    try:
        cur.execute("INSERT INTO Alunos VALUES (?, ?)", (ID, Nome))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def RemoverAluno(ID):
    try:
        cur.execute(f"DELETE FROM \"Alunos\" WHERE \"ID\" = {ID}")
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def EditarAluno(ID, NomeNovo):
    try:
        cur.execute("UPDATE Alunos SET Nome = ? WHERE ID = ?", (NomeNovo, ID))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def AdiconarProfessor(ID, Nome, Materia):
    try:   
        cur.execute("""INSERT INTO \"Professores\"(\"ID\", \"Nome\", \"Materia\") VALUES (?, ?, ?)""", (ID, Nome, Materia))
        conn.commit()
    except sqlite3.Error as e:
        msb.showwarning("erro", {e})
        conn.rollback()



def RemoverProfessor(ID):
    try:
        cur.execute(f"DELETE FROM \"Professores\" WHERE \"ID\" = {ID}")
        conn.commit()
    except sqlite3.Error as e:
        msb.showwarning("", "Digite um ID para ser deletado", icon="warning")
        conn.rollback()
    except ValueError:
        pass


def EditarProfessor(ID, NomeNovo, MateriaNova):
    try:
        cur.execute("UPDATE \"Professores\" SET \"Nome\" = ? WHERE \"ID\" = ?", (NomeNovo, ID))
        cur.execute("UPDATE \"Professores\" SET \"Materia\" = ? WHERE \"ID\" = ?", (MateriaNova, ID))
        conn.commit()
    except sqlite3.Error as e:
        print(e)


def CriarSala(IDProfessor, Horario):
    try:
        cur.execute("SELECT Materia FROM Professores WHERE ID = ?", (IDProfessor,))
        Materia = cur.fetchone()[0]
        aluno = " 0 "
        cur.execute("INSERT INTO Salas (IDPROFESSOR, Materia, Horario, Alunos) VALUES (?, ?, ?, ?)", (IDProfessor, Materia, Horario, aluno))
        conn.commit()
    except sqlite3.Error as e:
        msb.showwarning("", "Horarios podem ser apenas 'manha' ou 'tarde'", icon="warning")


def RemoverSala(IDProfessor):
    cur.execute(f"DELETE FROM Salas WHERE IDPROFESSOR = {IDProfessor}")
    conn.commit()


def ColocarAluno(IDAluno, IDProfessor):
    if IDAluno == 0 :
        print("Id do aluno não pode ser 0")
        return 0
    cur.execute(f"UPDATE Salas SET Alunos = Alunos || '{IDAluno} ' WHERE IDPROFESSOR = ?", (IDProfessor,))
    conn.commit()


def TirarAluno(IDAluno, IDProfessor):
    if IDAluno == 0 :
        print("Id do aluno não pode ser 0")
        return 0
    else:
        cur.execute(f"UPDATE Salas SET Alunos = REPLACE(Alunos, '{IDAluno} ', '') WHERE IDPROFESSOR = ?;", (IDProfessor,))
        conn.commit()

    
