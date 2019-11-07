import serial

def leituraRFID():
    tag_list = list()

    # configuração da porta serial
    serial_port = '/dev/ttyUSB0'
    port_speed = 9600
    max_bytes = -1
    ser = serial.Serial(serial_port, port_speed, timeout=3)

    while True:
        # ler somente uma linha (sequencia de bytes)
        print('lendo:')
        tag = bytearray()
        tag = ser.readline(max_bytes)

        if not tag_list.__contains__(tag):
            tag_list.append(tag)
            print(tag_list)
            # busco o produto no banco de dados
            # se produto existir > exibir produto em tela
            # se nao > exibir mensagem de erro ~OU~ nao exibir nada
