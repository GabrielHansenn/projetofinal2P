from Produto import Produto
from Categoria import Categoria


class Sistema:
    def __init__(self):
        self.categorias = []

    def adicionar_categoria(self, categoria):
        self.categorias.append(categoria)

    def listar_categorias(self):
        for categoria in self.categorias:
            print(categoria.nome)

    def encontrar_categoria(self, nome_categoria):
        for categoria in self.categorias:
            if categoria.nome == nome_categoria:
                return categoria
        return None

    def salvar_em_arquivo(self):
        with open("estoque.txt", "w") as file:
            for categoria in self.categorias:
                for produto in categoria.produtos:
                    file.write(f"{categoria.nome} - {produto.nome} - {produto.estoque}\n")
