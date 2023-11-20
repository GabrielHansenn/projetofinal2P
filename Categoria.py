from Produto import Produto

class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        for produto in self.produtos:
            print(produto)

    def encontrar_produto(self, nome_produto):
        for produto in self.produtos:
            if produto.nome == nome_produto:
                return produto
        return None

