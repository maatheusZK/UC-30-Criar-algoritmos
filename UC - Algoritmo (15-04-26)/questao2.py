def calcular_total():
    precos = []

    for i in range(2):
        try:
            preco = float(input(f"Digite o preço do {i+1}º produto: "))
            precos.append(preco)
        except ValueError:
            print("Erro: os preços devem ser numéricos.")
            return 

    total = sum(precos)
    print(f"Valor total da compra: R$ {total}")

calcular_total()