estoque_doacoes = {}

while True:
    print("\n--- Sistema de Controle de Doações ---")
    print("1 - Cadastrar doação")
    print("2 - Ver estoque")
    print("3 - Retirar item")
    print("4 - Sair")

    opcao_menu = input("Escolha uma opção: ")

    if opcao_menu == '1':
        nome_doador = input("Nome do doador: ")
        nome_item = input("Item doado: ").strip().lower()
        entrada_quantidade = input("Quantidade: ")

        if entrada_quantidade.isdigit() and int(entrada_quantidade) > 0:
            quantidade_doada = int(entrada_quantidade)

            if nome_item in estoque_doacoes:
                estoque_doacoes[nome_item] += quantidade_doada
            else:
                estoque_doacoes[nome_item] = quantidade_doada

            print("Doação cadastrada com sucesso!")
        else:
            print("Quantidade inválida")

    elif opcao_menu == '2':
        if not estoque_doacoes:
            print("Nenhuma doação registrada")
        else:
            print("\n--- Estoque Atual ---")
            for nome_item, quantidade_item in estoque_doacoes.items():
                print(f"Item: {nome_item.capitalize()} | Quantidade: {quantidade_item}")

    elif opcao_menu == '3':
        item_retirar = input("Informe o item que deseja retirar: ").strip().lower()

        if item_retirar in estoque_doacoes:
            entrada_quantidade_retirar = input("Quantidade para retirar: ")

            if entrada_quantidade_retirar.isdigit() and int(entrada_quantidade_retirar) > 0:
                quantidade_retirada = int(entrada_quantidade_retirar)

                if quantidade_retirada <= estoque_doacoes[item_retirar]:
                    estoque_doacoes[item_retirar] -= quantidade_retirada

                    if estoque_doacoes[item_retirar] == 0:
                        del estoque_doacoes[item_retirar]

                    print("Retirada realizada")
                else:
                    print("Quantidade indisponível")
            else:
                print("Quantidade inválida")
        else:
            print("Item não encontrado")

    elif opcao_menu == '4':
        print("Encerrando sistema")
        break

    else:
        print("Opção inválida")