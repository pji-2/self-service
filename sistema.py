#import sys
from leituraRFID import leituraRFID
from classes import Cliente, Produto, Venda
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication
from database import getClient, getProduct, listProduct, autenticacao

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

    # finalizando a venda
    print("finalizando a venda")
    print('\n')

    #lista para teste sem módulo
    listTag = ['2200D879C9','2200D879CA','2200D879C4','2200D879C8','2200D879C7']

    valor_final = listProduct(listTag,firebase)

    print("O valor final é R$",valor_final)
    print("\n")


    while(True):
        opcao = input("Digite 1 para confirmar ou 0 para cancelar\n")
        if(opcao == '1'):
            user = input("Digite usuário:")
            psw = input("Digite senha:")
            dicUser = autenticacao(user,psw,firebase)

            if(dicUser['nome']=='null'):
                novaTentativa=input("Usuário ou senhas incorretos!\n Digite 1 para tentar novamente ou 0 para sair:\n")
                if(novaTentativa == '0'):
                    break

            else:
                print("Olá",dicUser['nome'], "seu saldo é R$",dicUser['saldo'],"\n")
                conf = input("Digite 1 para confirmar pagamento e 0 para cancelar")
                if(conf == '1'):
                    print("Fazer débito")
                break
        else:
            print("Operação cancelada")





#12345612345
#testecamilla