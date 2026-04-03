from time import sleep
import funcoes

funcoes.cria_banco()
while True:
    funcoes.cabecalho("Sistema de Controle de Estoque")
    resposta = funcoes.menu(
        "Cadastrar Produto",
        "Listar Produtos",
        "Atualizar Produto",
        "Excluir Produto",
        "Sair do Programa",
    )

    if resposta == 1:
        funcoes.cabecalho("Cadastro de Produtos")
        dicionario = dict()
        dicionario["nome"] = input("Digite o nome do produto: ").strip().capitalize()
        dicionario["preco"] = funcoes.leia_float("Digite o preço do produto: ")
        dicionario["quantidade"] = funcoes.leia_int(
            f"Digite a quantidade de {dicionario['nome']} em estoque: "
        )
        funcoes.cadastrar_produto(dicionario)
        sleep(2)

    if resposta == 2:
        funcoes.cabecalho("Lista de Produtos")
        lista = funcoes.carregar_produtos()
        funcoes.mostrar_lista(lista)
        print("")
        sleep(2)

    if resposta == 3:
        funcoes.cabecalho("Atualizar Produto")
        lista = funcoes.carregar_produtos()
        funcoes.mostrar_lista(lista)
        while True:
            escolha = funcoes.leia_int("Qual o número do produto que você deseja atualizar?: ")
            if 0 < escolha <= len(lista):
                nome = input("Digite o novo nome do produto: ")
                preco = funcoes.leia_float("Digite o novo valor do produto: ")
                quant = funcoes.leia_int("Digite a nova quantidade do produto: ")
                produto = lista[escolha - 1]
                produto["nome"] = nome
                produto["preco"] = preco
                produto["quantidade"] = quant
                funcoes.salva_arquivo(lista)
                break
            else:
                print("Produto não encontrado.")

        print("")
        sleep(2)

    if resposta == 4:
        funcoes.cabecalho("Excluir Produto")
        lista = funcoes.carregar_produtos()
        funcoes.mostrar_lista(lista)
        while True:
            escolha = funcoes.leia_int("Qual o número do produto que você deseja excluir?: ")
            if 0 < escolha <= len(lista):
                del lista[escolha - 1]
                funcoes.salva_arquivo(lista)
                break
            else:
                print("Produto não encontrado.")

        print("")
        sleep(2)

    if resposta == 5:
        print("Fechando o programa...")
        sleep(2)
        break
