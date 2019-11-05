#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#import sys

import serial
from classes import Cliente, Produto, Venda
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication

def leituraRFID():
    serial_port = '/dev/ttyUSB0'
    port_speed = 9600
    max_bytes = -1
    ser = serial.Serial(serial_port, port_speed, timeout=3)
    tag_list = ser.readlines(max_bytes)
    tag_list = set(tag_list)
    print(tag_list)

if __name__ == '__main__':


   # authentication = firebase.FirebaseAuthentication(oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap, elisa.rodrigues444@gmail.com, extra={'id': 123})
    authentication = firebase.FirebaseAuthentication('oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap', 'elisa.rodrigues444@gmail.com', True, True)
    firebase = FirebaseApplication('https://pji2-ade1a.firebaseio.com', authentication)

    elisa = {"nome" : "elisa", "cpf" : 12345678912, "saldo" : 500, "senha" : "testeelisa" }
    camilla = {"nome": "camilla", "cpf" : 12345612345, "saldo" : 500, "senha" : "testecamilla" }
    sarom = {"nome": "sarom", "cpf": 12378912378, "saldo": 500, "senha": "testesarom"}

    #snapshot = firebase.post('/clients', sarom) -- para adicionar novos clientes no bando de dados

    # iniciando o sistema
    print("iniciando o sistema")
   
    # leitura dos produtos
    print("passe os produtos")
    leituraRFID()
    
    # autenticação
    print("autenticação")
    #autenticacao(c)

    # finalizando a venda
    print("finalizando a venda")

