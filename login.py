from tkinter import Tk, Label, Frame, Entry, Button, Toplevel
from tkinter import messagebox
from PIL import Image, ImageTk
import os
from registro import root_registrar
from Tk_Banco import logar, Gerarlog
from menu_inicial import menu





def login(root_login):
    root_login.title('Login')
    root_login.geometry('925x500+300+200')
    root_login.configure(bg='#fff')
    root_login.resizable(False, False)
    def entrar():
        nome=ent_usuario.get()
        senha=ent_senha.get()
        
        if nome=='admin' and senha=='1234':
            messagebox.showinfo(message="Boa tentativa!")
        else:
            try: 
                resultado=logar(nome, senha)
                if resultado:
                    Gerarlog(nome)
                    messagebox.showinfo(message="Entrou")
                    root_login.destroy()
                    menu()
            except:
                print("Erro ao chamar a função logar")


    image = Image.open(os.path.join(os.path.dirname(__file__), 'login.jpg'))
    image=image.resize((400, 400))
    img= ImageTk.PhotoImage(image)
    Label(root_login,image=img,bg='White').place(x=50,y=50)

    fr_login=Frame(root_login, width=400, height=400, bg="white")
    fr_login.place(x=500, y=52)

    heading=Label(fr_login, text='Logar', fg='#57a1f9', bg='white', font=('Microsoft YaHei UI Light,', 23,'bold'))
    heading.place(x=135,y=5)

    def on_enter(e):
        nome=ent_usuario.get()
        if nome == 'Usuário':
            ent_usuario.delete(0, 'end')
        

    def on_leave(e):
        nome=ent_usuario.get()
        if nome=='':
            ent_usuario.insert(0, 'Usuário')

    ent_usuario= Entry(fr_login, width=36, fg='black',border=0, bg='white',font=('Microsoft YaHei UI Light,',11), justify='center')
    ent_usuario.place(x=32,y=90)
    ent_usuario.insert(0, 'Usuário')
    ent_usuario.bind('<FocusIn>', on_enter)
    ent_usuario.bind('<FocusOut>', on_leave)
    Frame(fr_login, width=295, height=2, bg='black').place(x=30, y=110)

    def on_enter(e):
        senha=ent_senha.get()
        if senha == 'Senha':
            ent_senha.delete(0, 'end')

    def on_leave(e):
        nome=ent_senha.get()
        if nome=='':
            ent_senha.insert(0, 'Senha')

    ent_senha= Entry(fr_login, width=36, fg='black',border=0, bg='white',font=('Microsoft YaHei UI Light,',11), justify='center')
    ent_senha.place(x=32,y=190)
    ent_senha.insert(0, 'Senha')
    ent_senha.bind('<FocusIn>', on_enter)
    ent_senha.bind('<FocusOut>', on_leave)
    Frame(fr_login, width=295, height=2, bg='black').place(x=30, y=210)

    Button(fr_login,width=39,pady=7,text='Entrar', bg='#57a1f8', fg='White', border=0, command=entrar).place(x=35,y=240)

    lb_pergunta=Label(fr_login,text='Não tem conta?', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    lb_pergunta.place(x= 125, y=288)

    def registrar_comando():
        root_registro=Toplevel(root_login)
        root_registrar(root_registro)
        

    btn_registrar= Button(fr_login, width=6, text='Registrar', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=registrar_comando)
    btn_registrar.place(x=225, y=288)

    root_login.mainloop()
    
def iniciar():
    root_login=Tk()
    login(root_login)