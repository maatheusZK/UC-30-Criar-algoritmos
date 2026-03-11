senha = input("Digite a senha: ")

temNumero = False

for caractere in senha:
    if caractere.isdigit():
        temNumero = True
        break

if len(senha) >= 8 and temNumero:
    print("Senha válida")
else:
    print("Senha inválida")