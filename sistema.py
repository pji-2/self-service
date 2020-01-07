#import sys
from leituraRFID import leituraRFID
from classes import Cliente, Produto, Venda
from firebase import firebase
from firebase.firebase import FirebaseAuthentication, FirebaseApplication
from database import getClient, getProduct, listProduct, autenticacao, pagamento

if __name__ == '__main__':

   
    authentication = firebase.FirebaseAuthentication(
        'key', 'e-mail', True, True)
    firebase = FirebaseApplication(
        'link', authentication)

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


    print(valor_final[0])
    print("Valor total: R$",valor_final[1])
 #   print(valor_final[1])
    # print("O valor final é R$",valor_final)
    # print("\n")


    while(True):
        opcao = input("Digite 1 para confirmar ou 0 para cancelar\n")
        if(opcao == '1'):
            user = input("Digite usuário:")
            psw = input("Digite senha:")
            dicUser = autenticacao(user,psw,firebase)

            if(dicUser['nome']=='null'):
                # A senha errada não está funcionando
                novaTentativa=input("Usuário ou senhas incorretos!\n Digite 1 para tentar novamente ou 0 para sair:\n")
                if(novaTentativa == '0'):
                    break
            else:
                print("Olá",dicUser['nome'], "seu saldo é R$",dicUser['saldo'],"\n")
                conf = input("Digite 1 para confirmar pagamento e 0 para cancelar\n")
                if(conf == '1'):
                    debito = int(dicUser['saldo']) - int(valor_final[1])
                    if(debito < 0):
                        print("Saldo insuficiente")
                    else:
                        saldo = pagamento(user,firebase,debito)
                        print("Seu saldo atual é R$",saldo)

                break
        else:
            print("Operação cancelada\n")





#12345612345
#testecamilla
