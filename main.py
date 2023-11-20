import os
from Categoria import Categoria
from Produto import Produto
from Sistema import Sistema

def main():
    sistema = Sistema()

    frutas_verduras = Categoria("FRUTAS E VERDURAS")
    bebidas = Categoria("BEBIDAS")
    materias_limpeza = Categoria("MATERIAS DE LIMPEZA")
    materias_higiene = Categoria("MATERIAS DE HIGIENE")

    sistema.adicionar_categoria(frutas_verduras)
    sistema.adicionar_categoria(bebidas)
    sistema.adicionar_categoria(materias_limpeza)
    sistema.adicionar_categoria(materias_higiene)

    maca = Produto("Maçã", 100)
    laranja = Produto("Laranja", 100)
    agua = Produto("Água", 100)
    sabonete = Produto("Sabonete", 100)

    frutas_verduras.adicionar_produto(maca)
    frutas_verduras.adicionar_produto(laranja)
    bebidas.adicionar_produto(agua)
    materias_higiene.adicionar_produto(sabonete)

    while True:
        print("\n ==================================")
        print("  SEJA BEM-VINDO AO NOSSO SISTEMA")
        print("    DE GERENCIAMENTO DE ESTOQUE    ")
        print(" ==================================")

        print("____________________________________")
        print("\n|     1 - LISTA DE CATEGORIAS       |")
        print("\n|     2 - LISTA DE PRODUTOS         |")
        print("\n|     3 - ADICIONAR PRODUTO         |")
        print("\n|     4 - REMOVER PRODUTO           |")
        print("\n|     5 - EDITAR ESTOQUE            |")
        print("\n|     6 - BUSCAR PRODUTO            |")
        print("____________________________________")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            print("Categorias disponíveis:")
            sistema.listar_categorias()
            input("\nPressione <enter> para continuar")
            os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == '2':
            # Abre o arquivo no modo de leitura ('r')
            with open('estoque.txt', 'r') as arquivo:
            # Lê todo o conteúdo do arquivo e armazena em uma variável
                conteudo = arquivo.read()
                print(conteudo)
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == '3':
            categoria_nome = input("Digite o nome da categoria: ")
            categoria = sistema.encontrar_categoria(categoria_nome)
            if categoria:
                nome_produto = input("Digite o nome do produto: ")
                estoque_produto = int(input("Digite a quantidade em estoque: "))
                novo_produto = Produto(nome_produto, estoque_produto)
                categoria.adicionar_produto(novo_produto)
                sistema.salvar_em_arquivo()
                print("Produto adicionado com sucesso.")
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Categoria não encontrada.")
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == '4':
            categoria_nome = input("Digite o nome da categoria: ")
            categoria = sistema.encontrar_categoria(categoria_nome)
            if categoria:
                nome_produto = input("Digite o nome do produto a ser removido: ")
                produto = categoria.encontrar_produto(nome_produto)
                if produto:
                    categoria.produtos.remove(produto)
                    sistema.salvar_em_arquivo()
                    print("Produto removido com sucesso.")
                    input("\nPressione <enter> para continuar")
                    os.system('cls' if os.name == 'nt' else 'clear')
                else:
                    print("Produto não encontrado.")
                    input("\nPressione <enter> para continuar")
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Categoria não encontrada.")
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif escolha == '5':
            categoria_nome = input("Digite o nome da categoria (EM LETRA MAIUSCULA): ")
            categoria = sistema.encontrar_categoria(categoria_nome)
            if categoria:
                nome_produto = input("Digite o nome do produto a ser editado: ")
                produto = categoria.encontrar_produto(nome_produto)
                if produto:
                    novo_estoque = int(input("Digite o novo estoque: "))
                    produto.estoque = novo_estoque
                    sistema.salvar_em_arquivo()
                    print("Estoque editado com sucesso.")
                    input("\nPressione <enter> para continuar")
                    os.system('cls' if os.name == 'nt' else 'clear')  
                else:
                    print("Produto não encontrado.")
                    input("\nPressione <enter> para continuar")
                    os.system('cls' if os.name == 'nt' else 'clear')  
            else:
                print("Categoria não encontrada.")
                input("\nPressione <enter> para continuar")
                os.system('cls' if os.name == 'nt' else 'clear')                

        elif escolha == '6':
            print("____________________________________")
            print("|     1 - CATEGORIA                |")
            print("|     2 - NOME DO PRODUTO          |")          
            print("____________________________________")  
            alternativa = input("Digite o número referente ao tipo de PROCURA que deseja: ")

            if alternativa == '1':
                print("____________________________________")
                print("\n|         BEBIDAS                |")
                print("\n|         MATERIAIS LIMPEZA      |")
                print("\n|         MATERIAIS HIGIENE      |")
                print("\n|         FRUTAS E VERDURAS      |")           
                print("____________________________________")  

                categoria_nome = input("Digite o nome da categoria (EM LETRA MAIUSCULA):  ")
                categoria = sistema.encontrar_categoria(categoria_nome)
                if categoria:
                    categoria.listar_produtos()
                else:
                    print("Categoria não encontrada.")

            elif alternativa == '2':
                nomeDigitado = input("Digite o nome do produto que deseja: ")
                if any(produto.nome == nomeDigitado for categoria in sistema.categorias for produto in categoria.produtos):
                    print("Produto presente no estoque!")
                else:
                    print("Produto não encontrado!!!")

            input("\nPressione <enter> para continuar")
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
