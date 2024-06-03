import tkinter as tk
from tkinter import ttk
import os
from telaalunos import alunos
from telaprofessores import professores
from telasalas import salas
def menu():
 
         
    menu_central = tk.Tk()

    menu_central.title("MENU")
    menu_central.config(background= '#fff')
    menu_central.geometry("925x500+300+200")
    menu_central.resizable(False,False)

    frame = ttk.Frame(menu_central)
    frame.place(relx=0.32,rely=0.25,relheight=0.01,relwidth=0.4)
    frame.config(padding=10)


    label = ttk.Label(menu_central,text= "MENU",font=30,background='white')
    label.place(relx=0.48,rely=0.2)

    botão = ttk.Button()
    aluno = ttk.Button(menu_central,text="Aluno",command = alunos)
    aluno.place(relx=0.3,rely=0.6)
    professor = ttk.Button(menu_central,text="Professor",command=professores)
    professor.place(relx=0.45,rely=0.6)
    aulas = ttk.Button(menu_central,text="Aulas",command=salas)
    aulas.place(relx=0.6,rely=0.6)



    frame.mainloop()
    label.mainloop()
    menu_central.mainloop()