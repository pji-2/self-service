#import sys
from leituraRFID import leituraRFID
from classes import Cliente, Produto, Venda
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication

if __name__ == '__main__':

   # authentication = firebase.FirebaseAuthentication(oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap, elisa.rodrigues444@gmail.com, extra={'id': 123})
    authentication = firebase.FirebaseAuthentication(
        'oiPMNklhLclGiEpFGzVmOv6AMsV6KOQSadfTLAap', 'elisa.rodrigues444@gmail.com', True, True)
    firebase = FirebaseApplication(
        'https://pji2-ade1a.firebaseio.com', authentication)

    # elisa = {"nome" : "elisa", "cpf" : 12345678912, "saldo" : 500, "senha" : "testeelisa" }
    # camilla = {"nome": "camilla", "cpf" : 12345612345, "saldo" : 500, "senha" : "testecamilla" }
    # sarom = {"nome": "sarom", "cpf": 12378912378, "saldo": 500, "senha": "testesarom"}

    # snapshot = firebase.post('/clients', sarom) -- para adicionar novos clientes no bando de dados

    # iniciando o sistema
    print("iniciando o sistema")

    # leitura dos produtos
    print("passe os produtos")

    # leituraRFID()

    # autenticação
    print("autenticação")
    # autenticacao(c)

    # finalizando a venda
    print("finalizando a venda")
    print('\n')
