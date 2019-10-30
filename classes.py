class Cliente(object):
    

    def __init__(self, nome, CPF, saldo, senha):
        self.nome = nome
        self.CPF = CPF
        self.saldo = saldo
        self.senha = senha

    def buscaCPF(self, cpf, true=None, false=None):
        if self.CPF == cpf:
            return self.CPF==cpf
        else: return self.CPF!=cpf

    def confereSenha(self, senha):
        if self.senha == senha:
            return self.senha==senha
        else: return self.senha!=senha

    def retornaCliente(self, cpf):
        if self.CPF == cpf:
            return self

    def retornaNome(self):
        return self.nome

class Produto(object):
    def __init__(self, nome, codigo, valor, quantidadeEmEstoque):
        self.nome = nome
        self.codigo = codigo
        self.valor = valor
        self.quantidadeEmEstoque = quantidadeEmEstoque


class Venda(object):
    def __init__(self, idCliente, idProduto, data, quantidade):
        self.idCliente = idCliente
        self.idProduto - idProduto
        self.data = data
        self.quantidade = quantidade
