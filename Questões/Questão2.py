produtos = [
    {"codigo": 101, "nome": "Caneta Azul", "estoque": 150},
    {"codigo": 102, "nome": "Caderno Universitário", "estoque": 75},
    {"codigo": 103, "nome": "Borracha Branca", "estoque": 200},
    {"codigo": 104, "nome": "Lápis Preto HB", "estoque": 320},
    {"codigo": 105, "nome": "Marcador de Texto Amarelo", "estoque": 90}
]

movimentacoes = []
proximo_id = 1


def buscar_produto(codigo):
    for produto in produtos:
        if produto["codigo"] == codigo:
            return produto

    return None


def realizar_movimentacao(produto, tipo, quantidade, descricao):
    global proximo_id

    if quantidade <= 0:
        print("A quantidade deve ser maior que zero.")
        return

    if tipo == "entrada":
        produto["estoque"] += quantidade

    elif tipo == "saida":
        if quantidade > produto["estoque"]:
            print("Estoque insuficiente.")
            return

        produto["estoque"] -= quantidade

    else:
        print("Tipo de movimentação inválido.")
        return

    movimentacao = {
        "id": proximo_id,
        "descricao": descricao,
        "tipo": tipo,
        "produto": produto["codigo"],
        "quantidade": quantidade
    }

    movimentacoes.append(movimentacao)

    proximo_id += 1

    print("\nMovimentação realizada com sucesso!")
    print(f"Produto: {produto['nome']}")
    print(f"Estoque final: {produto['estoque']}")


while True:
    print("\n===== CONTROLE DE ESTOQUE =====")
    print("1 - Realizar movimentação")
    print("2 - Consultar estoque")
    print("3 - Ver movimentações")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        try:
            codigo = int(input("Digite o código do produto: "))
        except ValueError:
            print("Digite um código numérico válido.")
            continue

        produto = buscar_produto(codigo)

        if produto is None:
            print("Produto não encontrado.")
            continue

        print(f"\nProduto: {produto['nome']}")
        print(f"Estoque atual: {produto['estoque']}")

        tipo = input(
            "Digite o tipo da movimentação (entrada/saida): "
        ).strip().lower()

        try:
            quantidade = int(input("Digite a quantidade: "))
        except ValueError:
            print("Digite uma quantidade numérica válida.")
            continue

        descricao = input(
            "Digite a descrição da movimentação: "
        ).strip()

        realizar_movimentacao(
            produto,
            tipo,
            quantidade,
            descricao
        )

    elif opcao == "2":

        print("\n===== ESTOQUE ATUAL =====")

        for produto in produtos:
            print(
                f"Código: {produto['codigo']} | "
                f"Produto: {produto['nome']} | "
                f"Estoque: {produto['estoque']}"
            )

    elif opcao == "3":

        print("\n===== HISTÓRICO DE MOVIMENTAÇÕES =====")

        if len(movimentacoes) == 0:
            print("Nenhuma movimentação registrada.")

        else:
            for movimentacao in movimentacoes:
                print(
                    f"ID: {movimentacao['id']} | "
                    f"Produto: {movimentacao['produto']} | "
                    f"Tipo: {movimentacao['tipo']} | "
                    f"Quantidade: {movimentacao['quantidade']} | "
                    f"Descrição: {movimentacao['descricao']}"
                )

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")