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
    for item in tag_list:
        prodDic = firebase.get('/products',item)
        valor = prodDic['valor']
        soma = soma + int(valor)
        print(prodDic['nome'],'R$',valor)   
    return soma
    
def autenticacao(id,senha,firebase):

    dicNulo = {'nome':'null'}
    clientDic = firebase.get('/clients',id)
    if(clientDic['senha'] == senha):
        return clientDic
    else:
        return dicNulo