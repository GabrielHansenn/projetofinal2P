
class Produto:
    def __init__(self, nome, estoque):
        self.nome = nome
        self.estoque = estoque

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        self.estoque -= quantidade

    def __str__(self):
        return f"{self.nome}: {self.estoque} em estoque"
