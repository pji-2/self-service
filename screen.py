import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk,Glib
import pathlib
import sys
import serial

class Tela:
    def __init__(self,arq):
        self.bd = Gtk.Builder()
        self.bd.add_from_file(arq)
        self.bd.connect_signals(self)
        self.tela = self.bd.get_object('tela')
        self.tela.show_all()
        self.botaoCancelar = self.bd.get_object('botaoCancelar')
        self.botaoCancelar.show()
        self.botaoConfirmar = self.bd.get_object('botaoConfirmar')
        self.botaoCancelar.show()
        self.labelTexto = self.bd.get_object('labelTexto')
        self.labelTexto.show()


    def btConfirmar_click(self,obj,data=None):
        self.labelTexto.set_text("Hello World")

    def quit(self,*args):
        Gtk.main_quit()


class RFID:

    def __init__(self):
        self.tag_list = list()

        # configuração da porta serial
        self.serial_port = '/dev/ttyUSB0'
        self.port_speed = 9600
        self.max_bytes = -1
        self.ser = serial.Serial(self.serial_port, self.port_speed, timeout=3)
#------------------------------------------------------------------
        self.channel = Glib.IOChannel(self.ser)
        self.channel.set_flags(Glib.IO_FLAG_NONBLOCK)

        self.cond = Glib.IOCondition(Glib.IOCondition.IN)
        self.channel.add_watch(self.cond,printList,self.ser)

#-----------------------------------------------------------------

    def leituraRFID(self):
        while True:
            # ler somente uma linha (sequencia de bytes)
            print('lendo:')
            tag = bytearray()
            tag = self.ser.readline(self.max_bytes)

            
    def printList(tag):
            print(tag)
            tag = tag.decode("utf-8", "ignore")
            print(tag)
            tag = tag.split("\r\n")[0]

            try:
                print(tag)
                tag = tag.split("\x03")[1]
            except:
                pass
            try:
                print(tag)
                tag = tag.split("\x02")[1]
            except:
                pass
            if len(tag) > 0 and not self.tag_list.__contains__(tag):
                self.tag_list.append(tag)
                print(self.tag_list)
                return tag


if __name__ == '__main__':
    path = pathlib.Path(sys.argv[0])
    path = str(path.parent)
    tela = Tela('%s/tela.glade' % path)
    Gtk.main()
    rfid = RFID()



