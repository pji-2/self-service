def getCliente(id,firebase):
    #o id precisa ser ajustado                                                                                                                                                                                                                                                           
    result = firebase.get('/clients',id)                                                                                
    return result 
#incluir id na assinatura
def getProduto(id,firebase):                                                                                                                                                                                                                                                           
    result = firebase.get('/products',id)                                                                            
    return result  