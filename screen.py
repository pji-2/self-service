import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import pathlib
import sys
import serial
import os
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication
from database import listProduct, autenticacao, pagamento, getClient, getProduct
from gi.repository import GLib

authentication = firebase.FirebaseAuthentication(
    'oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap', 'elisa.rodrigues444@gmail.com', True, True)
firebase = FirebaseApplication(
    'https://pji2-ade1a.firebaseio.com', authentication)

tag_list = []
global listaDB

class Inicio:
    def __init__(self,arq):
        self.bd = Gtk.Builder()
        self.bd.add_from_file(arq)
        self.inicio = self.bd.get_object('inicioWin')
        self.inicio.show_all()
        self.botaoConfirmar = self.bd.get_object('botaoIniciar')
        self.bd.connect_signals({"btIniciar_click": self.btIniciar_click, "quit_win": self.quit})
    
    def btIniciar_click(self,obj,data=None):
        path = pathlib.Path(sys.argv[0])
        path = str(path.parent)
        tela = Tela('%s/tela.glade' % path)
        self.inicio.hide()
        #rfid = RFID(tela)
        rfid = RFID()
        
  
    def quit(self,*args):
        Gtk.main_quit()

class Tela:
    def __init__(self,arq):
        self.bd = Gtk.Builder()
        self.bd.add_from_file(arq)
        self.tela = self.bd.get_object('tela')
        self.tela.show_all()
        self.botaoCancelar = self.bd.get_object('botaoCancelar')
        self.botaoConfirmar = self.bd.get_object('botaoConfirmar')
        self.labelTexto = self.bd.get_object('labelTexto')
        self.bd.connect_signals({"btConfirmar_click": self.btConfirmar_click, "quit_win": self.quit, "btCancelar_click":self.btCancelar_click})

    def btConfirmar_click(self,obj,data=None):
        self.mostraProduto()
        path = pathlib.Path(sys.argv[0])
        path = str(path.parent)
        if len(listaDB) != 0:
            auth = AutenticacaoTela('%s/autenticacao.glade' % path,listaDB[1])
            #self.tela.hide()
        else:
            self.labelTexto.set_text("Nenhum produto foi adicionado.\nPasse algum produto!")
        

    def btCancelar_click(self,obj,data=None):
        self.quit()
        #iniTela = self.tela.get_transient_for()
        #iniTela.show_all()

    def mostraProduto(self,*args):
        global listaDB
        if len(tag_list)==0:
            self.labelTexto.set_text("Nenhum produto foi adicionado.\nPasse algum produto!")
        else:
            listaDB = listProduct(tag_list,firebase)
            self.labelTexto.set_text(listaDB[0])

    def quit(self,*args):
        Gtk.main_quit()

class AutenticacaoTela:
    def __init__(self,arq,valor_pag):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arq)
        self.authWin = self.builder.get_object('authWin')
        self.authWin.show_all()
        self.valor_pag = valor_pag
        self.nomeEntry = self.builder.get_object('nomeEntry')
        self.senhaEntry = self.builder.get_object('senhaEntry')
        self.botaoOk = self.builder.get_object('botaoOK')
        self.botaoCancelar = self.builder.get_object('botaoCancelar')
        self.builder.connect_signals({"quit_win": self.quit,"autenticar_click":self.autenticar})

    def quit(self,*args):
        Gtk.main_quit()

    def autenticar(self,*args):
        id_cpf = self.nomeEntry.get_text()
        senha = self.senhaEntry.get_text()
        
        user = getClient(id_cpf,firebase)
        if autenticacao(id_cpf,senha,firebase):
            path = pathlib.Path(sys.argv[0])
            path = str(path.parent)
            self.authWin.hide()
            pagTela = PagTela('%s/pagamento.glade' % path,id_cpf,user,self.valor_pag)

        else:
            self.nomeEntry.set_text('Inválido.')
            self.senhaEntry.set_text('Inválido.')

class PagTela:
    def __init__(self,arq,id_cpf,user,valor_pag):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arq)
        self.pagWin = self.builder.get_object('pagWin')
        self.pagWin.show_all()
        self.user = user
        self.id_cpf = id_cpf
        self.valor_pag = valor_pag
        self.botaoSim = self.builder.get_object('botaoSim')
        self.botaoNao = self.builder.get_object('botaoNao')
        self.labelPag = self.builder.get_object('labelPag')
        text = self.user['nome'] + " seu saldo é de R$" + str(self.user['saldo']) + ".\nConfirmar o pagamento de R$ "+ str(self.valor_pag) +"?"
        self.labelPag.set_text(text)
        self.builder.connect_signals({"quit_win": self.quit,"btSim_click":self.btSim_click, "btNao_click":self.btNao_click})
    
    def btSim_click(self,obj,data=None):
        pagamento(self.id_cpf,firebase,self.valor_pag)
        userAtual = getClient(self.id_cpf,firebase)
        text = "Pagamento realizado com sucesso!\nSaldo atual =  R$ "+ str(userAtual['saldo'])+"."
        path = pathlib.Path(sys.argv[0])
        path = str(path.parent)
        self.pagWin.hide()
        confTela = ConfirmacaoTela('%s/confirmacao.glade' % path,text)


    def btNao_click(self,obj,data=None):
        self.quit()

    def quit(self,*args):
        Gtk.main_quit()

class ConfirmacaoTela:
    def __init__(self,arq,text):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arq)
        self.confiWin = self.builder.get_object('confiWin')
        self.confiWin.show_all()
        self.botaoOk = self.builder.get_object('botaoOk')
        self.labelConf = self.builder.get_object('labelConf')
        self.labelConf.set_text(text)
        self.builder.connect_signals({"quit_win": self.quit,"btOk_click":self.btOk_click})
    
    def btOk_click(self,obj,data=None):
        self.quit()
        
    def quit(self,*args):
        Gtk.main_quit()

class RFID:
    
    def __init__(self):
        global tag_list
        # configuração da porta serial
        #self.tela = tela
        self.serial_port = '/dev/ttyUSB0'
        self.port_speed = 9600
        self.max_bytes = -1
        self.ser = serial.Serial(self.serial_port, self.port_speed, timeout=3)
#------------------------------------------------------------------
        self.channel = GLib.IOChannel(self.ser.fileno())
        self.channel.set_flags(GLib.IO_FLAG_NONBLOCK)

        self.cond = GLib.IOCondition(GLib.IOCondition.IN)
        self.channel.add_watch(self.cond,self.leituraRFID)

# #-----------------------------------------------------------------

    def leituraRFID(self,*args):
            global tag_list
            tag = bytearray()
            tag = self.ser.readline(self.max_bytes)
            tag = tag.decode("utf-8", "ignore")
            tag = tag.split("\r\n")[0]
            try:
                tag = tag.split("\x03")[1]
            except:
                pass
            try:
                tag = tag.split("\x02")[1]
            except:
                pass
            if len(tag) > 0 and not tag_list.__contains__(tag):
                tag_list.append(tag)
                print(tag)                
                #self.tela.mostraProduto(getProduct(tag,firebase)['nome']);
                #self.tela.labelTexto.set_text(tag)
            return tag

if __name__ == '__main__':
    path = pathlib.Path(sys.argv[0])
    path = str(path.parent)
    inicio = Inicio('%s/inicio.glade' % path)
    Gtk.main()



