#continuação da aula passada.


nome = input("Digite seu nome: ")
senhaCorreta = "123456"

tentativa = 3

while tentativa > 0:
    senha = input("Digite sua senha: ")

    if senha == senhaCorreta:
        print(f"Olá, {nome}. Seja bem-vindo!")
        break
    else:
        tentativa -= 1

        if tentativa == 2:
            print("Senha errada! Você em 2 tentativas.")
        elif tentativa == 1:
            print("Senha errada! Você em 1 tentativa.")
        else: 
            print("Senha bloqueada!")