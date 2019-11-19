def getClient(id,firebase):
    #o id precisa ser ajustado                                                                                                                                                                                                                                                           
    result = firebase.get('/clients',id)                                                                                
    return result 
#incluir id na assinatura
def getProduct(id,firebase):                                                                                                                                                                                                                                                           
    result = firebase.get('/products',id)                                                                            
    return result  

def listProduct(tag_list,firebase):
    soma = 0
    lista_final = ""
    for item in tag_list:
        prodDic = firebase.get('/products',item)
        valor = prodDic['valor'] 
        soma = soma + int(valor)
        strValor = str(valor)
        lista_final = lista_final + prodDic['nome'] + ' R$'+ strValor + "\n" 

    lista = [lista_final,soma]
    return lista
    
def autenticacao(id,senha,firebase):

#Como tratar caso não encontre o cliente no banco de dados
    dicNulo = {'nome':'null'}
    clientDic = firebase.get('/clients',id)
    if(clientDic['senha'] == senha):
        return clientDic
    else:
        return dicNulo

def pagamento(id,firebase,debito):

    firebase.put('/clients/'+id,"saldo",debito)
    clientDic = firebase.get('/clients',id)
    return clientDic['saldo']