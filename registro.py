from tkinter import *
from tkinter import messagebox
from Tk_Banco import registro
from PIL import Image, ImageTk
import os

def root_registrar(root_registro):
    root_registro.title('Registrar')
    root_registro.geometry('925x500+300+200')
    root_registro.configure(bg='#fff')
    root_registro.resizable(False, False)

    def registrar():
        login=ent_usuario.get()
        senha=ent_senha.get()
        if login == "Usuário" or login == "" or senha == "" or senha == "Senha":
            messagebox.showerror(message="Preencha corretamente todos os campos!")
        else:
            try:
                if registro(login, senha):
                    messagebox.showinfo(message="Cadastrado com sucesso!")
                    root_registro.destroy()
            except:
                root_error=Toplevel(root_registro)
                root_error.wm_title("Erro")
                
                lb_error=Label(root_error, text ="Erro ao cadastrar")
                lb_error.grid(row=0, column=0)
                
                btn_error=Button(root_error, text="Ok", command=root_error.destroy())
                btn_error.pack()



    image = Image.open(os.path.join(os.path.dirname(__file__), 'registro.jpg'))
    image=image.resize((400, 400))
    img= ImageTk.PhotoImage(image)
    Label(root_registro,image=img,bg='White').place(x=50,y=50)

    fr_registro=Frame(root_registro, width=400, height=400, bg="white")
    fr_registro.place(x=500, y=52)

    heading=Label(fr_registro, text='Registrar', fg='#57a1f9', bg='white', font=('Microsoft YaHei UI Light,', 23,'bold'))
    heading.place(x=110,y=5)

    def on_enter(e):
        nome=ent_usuario.get()
        if nome == 'Usuário':
            ent_usuario.delete(0, 'end')
        

    def on_leave(e):
        nome=ent_usuario.get()
        if nome=='':
            ent_usuario.insert(0, 'Usuário')

    ent_usuario= Entry(fr_registro, width=36, fg='black',border=0, bg='white',font=('Microsoft YaHei UI Light,',11), justify='center')
    ent_usuario.place(x=32,y=90)
    ent_usuario.insert(0, 'Usuário')
    ent_usuario.bind('<FocusIn>', on_enter)
    ent_usuario.bind('<FocusOut>', on_leave)
    Frame(fr_registro, width=295, height=2, bg='black').place(x=30, y=110)

    def on_enter(e):
        senha=ent_senha.get()
        if senha == 'Senha':
            ent_senha.delete(0, 'end')

    def on_leave(e):
        nome=ent_senha.get()
        if nome=='':
            ent_senha.insert(0, 'Senha')

    ent_senha= Entry(fr_registro, width=36, fg='black',border=0, bg='white',font=('Microsoft YaHei UI Light,',11), justify='center')
    ent_senha.place(x=32,y=190)
    ent_senha.insert(0, 'Senha')
    ent_senha.bind('<FocusIn>', on_enter)
    ent_senha.bind('<FocusOut>', on_leave)
    Frame(fr_registro, width=295, height=2, bg='black').place(x=30, y=210)

    Button(fr_registro,width=39,pady=7,text='Cadastrar', bg='#57a1f8', fg='White', border=0, command=registrar).place(x=35,y=240)

    root_registro.mainloop()
    
if __name__ == "__main__":
    root_registro=Tk()
    root_registrar(root_registro)