import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import pathlib
import sys
import serial
import os
from gi.repository import GLib

class Tela:
    def __init__(self,arq):
        self.bd = Gtk.Builder()
        self.bd.add_from_file(arq)
        self.tela = self.bd.get_object('tela')
        self.tela.show_all()
        self.botaoCancelar = self.bd.get_object('botaoCancelar')
        self.botaoCancelar.show()
        self.botaoConfirmar = self.bd.get_object('botaoConfirmar')
        self.botaoCancelar.show()
        self.labelTexto = self.bd.get_object('labelTexto')
        self.labelTexto.show()
        self.bd.connect_signals({"btConfirmar_click": self.btConfirmar_click, "quit_win": self.quit})

    def btConfirmar_click(self,obj,data=None):
        path = pathlib.Path(sys.argv[0])
        path = str(path.parent)
        auth = AutenticacaoTela('%s/autenticacao.glade' % path)
        #self.labelTexto.set_text("Hello World")
        #pass

    def quit(self,*args):
        Gtk.main_quit()

class AutenticacaoTela:
    def __init__(self,arq):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(arq)
        self.authWin = self.builder.get_object('authWin')
        self.authWin.show_all()
        self.nomeEntry = self.builder.get_object('nomeEntry')
        #self.nomeEntry.show()
        self.senhaEntry=self.builder.get_object('senhaEntry')
        #self.senhaEntry.show()
        self.botaoOk = self.builder.get_object('botaoOK')
        #self.botaoOk.show()
        self.botaoCancelar = self.builder.get_object('botaoCancelar')
        #self.botaoCancelar.show()
        self.builder.connect_signals({"quit_win": self.quit})

    def quit(self,*args):
        Gtk.quit()


# class RFID:
    
#     def __init__(self):
#         self.tag_list = list()

#         # configuração da porta serial
#         self.serial_port = '/dev/ttyUSB0'
#         self.port_speed = 9600
#         self.max_bytes = -1
#         self.ser = serial.Serial(self.serial_port, self.port_speed, timeout=3)
# #------------------------------------------------------------------
#         self.channel = Glib.IOChannel(self.ser)
#         self.channel.set_flags(Glib.IO_FLAG_NONBLOCK)

#         self.cond = Glib.IOCondition(Glib.IOCondition.IN)
#         self.channel.add_watch(self.cond,self.printList)

# #-----------------------------------------------------------------

#     def leituraRFID(self):
#         while True:##
#             # ler somente uma linha (sequencia de bytes)
#             print('lendo:')
#             tag = bytearray()
#             tag = self.ser.readline(self.max_bytes)

            
#  def printList():
#     print(tag)
#     tag = tag.decode("utf-8", "ignore")
#     print(tag)
#     tag = tag.split("\r\n")[0]

#     try:
#         print(tag)
#         tag = tag.split("\x03")[1]
#     except:
#         pass
#     try:
#         print(tag)
#         tag = tag.split("\x02")[1]
#     except:
#         pass
#     if len(tag) > 0 and not self.tag_list.__contains__(tag):
#         self.tag_list.append(tag)
#         print(self.tag_list)
#         return tag


if __name__ == '__main__':
    path = pathlib.Path(sys.argv[0])
    path = str(path.parent)
    tela = Tela('%s/tela.glade' % path)
    Gtk.main()
    #rfid = RFID()



