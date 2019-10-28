class Cliente(object):
    def __init__(self, nome, CPF, saldo, senha):
        self.nome = nome
        self.CPF = CPF
        self.saldo = saldo
        self.senha = senha

    def buscaCliente(self, cpf):
        if self.CPF == cpf:
            return self
        else: return "Cliente sem cadastro"

    def confereSenha(self, senha):
        if self.senha == senha:
            return self
        else: return "Senha incorreta"

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
