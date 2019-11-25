from tkinter import *
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication
from database import getClient, getProduct, listProduct, autenticacao, pagamento

authentication = firebase.FirebaseAuthentication(
    'oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap', 'elisa.rodrigues444@gmail.com', True, True)
firebase = FirebaseApplication(
    'https://pji2-ade1a.firebaseio.com', authentication)

listTag = ['2200D879C9','2200D879CA','2200D879C4','2200D879C8','2200D879C7']

condicao = True

class Application:
    def __init__(self, master=None):
        #-----------------------------
        self.framePrincipal = Frame(master)
        self.framePrincipal.pack()

        self.widget1 = Frame(master)
        self.widget1.pack() #????

        self.widget2 = Frame(master)
        self.widget2.pack()

        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()
  
        self.segundoContainer = Frame(master)
        self.segundoContainer["padx"] = 20
        self.segundoContainer.pack()
  
        self.terceiroContainer = Frame(master)
        self.terceiroContainer["padx"] = 20
        self.terceiroContainer.pack()
  
        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.iniciar = Button(self.framePrincipal)
        self.iniciar["text"] = "Iniciar"
        self.iniciar["font"] = ("Calibri", "15")
        self.iniciar["width"] = 15
        self.iniciar["command"] = self.outraAba
        self.iniciar.pack ()
        
        
    def outraAba(self):

        self.framePrincipal.pack_forget()
        
        lista = listProduct(listTag,firebase)
        self.msg = Label(self.widget1, text=lista[0])
        self.msg["font"] = ("Arial", "15","bold")
        #self.msg.pack ()
        self.msg.grid(row=1,column=1,padx=0, pady=0)

        self.sair = Button(self.widget2)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "15")
        self.sair["width"] = 10
        self.sair["command"] = self.widget1.quit
        #self.sair.pack ()
        self.sair.grid(row=3,column=1,padx= 0, pady=0)

        self.confirmar = Button(self.widget2)
        self.confirmar["text"] = "Confirmar"
        self.confirmar["font"] = ("Calibri", "15")
        self.confirmar["width"] = 8
        self.confirmar["command"] = self.confirmacao
        #self.confirmar["state"] = "DISABLED"

        self.confirmar.grid(row=3,column=0,padx= 0, pady=0)

        cont = 0
        while (condicao):
            self.msg["show"] = str(cont)
            cont = cont + 1


    def confirmacao(self):

        self.msg.pack_forget()
        self.sair.pack_forget()
        self.confirmar.pack_forget()



        self.fontePadrao = ("Arial", "15")

        self.titulo = Label(self.primeiroContainer, text="Dados do usuário")
        self.titulo["font"] = ("Arial", "15", "bold")
        self.titulo.pack()

        self.nomeLabel = Label(self.segundoContainer,text="Nome", font=self.fontePadrao)
        self.nomeLabel.pack(side=LEFT)
  
        self.nome = Entry(self.segundoContainer)
        self.nome["width"] = 30
        self.nome["font"] = self.fontePadrao
        self.nome.pack(side=LEFT)
  
        self.senhaLabel = Label(self.terceiroContainer, text="Senha", font=self.fontePadrao)
        self.senhaLabel.pack(side=LEFT)
  
        self.senha = Entry(self.terceiroContainer)
        self.senha["width"] = 30
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.pack(side=LEFT)
  
        self.autenticar = Button(self.quartoContainer)
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Calibri", "10")
        self.autenticar["width"] = 12
        self.autenticar["command"] = self.verificaSenha
        self.autenticar.pack()
  
        self.mensagem = Label(self.quartoContainer, text="", font=self.fontePadrao)
        self.mensagem.pack()

            #Método verificar senha
    def verificaSenha(self):

        usuario = self.nome.get()
        senha = self.senha.get()
        user = autenticacao(usuario,senha,firebase)
        if user['nome'] == 'null':
            self.mensagem["text"] = "Erro na autenticação"
        else:
            self.mensagem["text"] = "Autenticado"
#        if usuario == "usuario" and senha == "senha":
#            self.mensagem["text"] = "Autenticado"
#        else:
#            self.mensagem["text"] = "Erro na autenticação"

root = Tk()
root.title('Self-service')
root.geometry("500x500") #define a geometria
root.resizable(0,0) #não ajusta o tamanho
Application(root)
root.mainloop()


#12345612345
#testecamilla