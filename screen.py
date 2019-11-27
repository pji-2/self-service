import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import pathlib
import sys
import serial
import os
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication
from database import listProduct, autenticacao, pagamento, getClient
from gi.repository import GLib

authentication = firebase.FirebaseAuthentication(
    'oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap', 'elisa.rodrigues444@gmail.com', True, True)
firebase = FirebaseApplication(
    'https://pji2-ade1a.firebaseio.com', authentication)

listTag = ['2200D879C9','2200D879CA','2200D879C4','2200D879C8','2200D879C7']
lista = listProduct(listTag,firebase)
class Inicio:
    def __init__(self,arq):
        self.bd = Gtk.Builder()
        self.bd.add_from_file(arq)
        self.tela = self.bd.get_object('inicioWin')
        self.tela.show_all()
        self.botaoConfirmar = self.bd.get_object('botaoIniciar')
        self.bd.connect_signals({"btIniciar_click": self.btIniciar_click, "quit_win": self.quit})
    
    def btIniciar_click(self,obj,data=None):
        path = pathlib.Path(sys.argv[0])
        path = str(path.parent)
        tela = Tela('%s/tela.glade' % path)
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
        self.bd.connect_signals({"btConfirmar_click": self.btConfirmar_click, "quit_win": self.quit})

    def btConfirmar_click(self,obj,data=None):
        path = pathlib.Path(sys.argv[0])
        path = str(path.parent)
        auth = AutenticacaoTela('%s/autenticacao.glade' % path)

    def mostraProduto(self,tag,*args):
        self.labelTexto.set_text(tag)

    def quit(self,*args):
        Gtk.main_quit()

class AutenticacaoTela:
    def __init__(self,arq):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arq)
        self.authWin = self.builder.get_object('authWin')
        self.authWin.show_all()
        self.nomeEntry = self.builder.get_object('nomeEntry')
        self.senhaEntry = self.builder.get_object('senhaEntry')
        self.botaoOk = self.builder.get_object('botaoOK')
        self.botaoCancelar = self.builder.get_object('botaoCancelar')
        self.builder.connect_signals({"quit_win": self.quit,"autenticar_click":self.autenticar})

    def quit(self,*args):
        Gtk.main_quit()

    def autenticar(self,*args):
        nome = self.nomeEntry.get_text()
        senha = self.senhaEntry.get_text()
        
        user = getClient(nome,firebase)
        if autenticacao(nome,senha,firebase):
            path = pathlib.Path(sys.argv[0])
            path = str(path.parent)
            pagTela = PagTela('%s/pagamento.glade' % path,user['nome'],user['saldo'])
        else:
            self.nomeEntry.set_text('Inválido. Digite novamente')
            self.senhaEntry.set_text('Inválido. Digite novamente')

class PagTela:
    def __init__(self,arq,userNome,userSaldo):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arq)
        self.dialogPag = self.builder.get_object('dialogPag')
        self.dialogPag.show_all()
        self.botaoSim = self.builder.get_object('botaoSim')
        self.botaoNao = self.builder.get_object('botaoNao')
        self.labelPag = self.builder.get_object('labelPagamento')
        text = userNome + " seu saldo é de R$" + str(userSaldo) + ".\n Deseja confirmar o pagamento?"
        self.labelPag.set_text(text)
        self.builder.connect_signals({"quit_win": self.quit})
    
    def quit(self,*args):
        Gtk.main_quit()

class RFID:
    
    def __init__(self,tela):
        self.tag_list = list()

        # configuração da porta serial
        self.serial_port = '/dev/ttyUSB0'
        self.port_speed = 9600
        self.max_bytes = -1
        self.ser = serial.Serial(self.serial_port, self.port_speed, timeout=3)
        self.tela = tela
#------------------------------------------------------------------
        self.channel = GLib.IOChannel(self.ser.fileno())
        self.channel.set_flags(GLib.IO_FLAG_NONBLOCK)

        self.cond = GLib.IOCondition(GLib.IOCondition.IN)
        self.channel.add_watch(self.cond,self.leituraRFID)

# #-----------------------------------------------------------------

    def leituraRFID(self,*args):
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
            if len(tag) > 0 and not self.tag_list.__contains__(tag):
                self.tag_list.append(tag)
                print(tag)
            return tag

if __name__ == '__main__':
    path = pathlib.Path(sys.argv[0])
    path = str(path.parent)
    inicio = Inicio('%s/inicio.glade' % path)
    Gtk.main()



