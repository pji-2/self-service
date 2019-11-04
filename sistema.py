#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import sys
import serial
from classes import Cliente, Produto, Venda


def leituraRFID():
    serial_port = '/dev/ttyUSB0'
    port_speed = 9600
    max_bytes = -1
    ser = serial.Serial(serial_port, port_speed, timeout=3)
    tag_list = ser.readlines(max_bytes)
    tag_list = set(tag_list)
    print(tag_list)


if __name__ == '__main__':
    # iniciando o sistema
    print("iniciando o sistema")
    nome = input('insira o nome: ')
    id = input('insira cpf: ')
    saldo = 500
    senha = "senha1234"
    c = Cliente(nome, id, saldo, senha)

    # leitura dos produtos
    print("passe os produtos")
   # leituraRFID()

    # autenticação
    print("autenticação")

    # finalizando a venda
    print("finalizando a venda")
