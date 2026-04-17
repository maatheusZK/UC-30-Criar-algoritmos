# 1)
print("Hello, World!")

print("\n")

# 2)
idade = int(input("Digite sua idade: "))
if idade >= 16:
    print("Pode votar!")
else: 
    print("Ainda não pode votar.")

print("\n")

# 3)
total = 0
while True:
    valor = float(input("Digite um valor (0 para parar): "))
    
    if valor == 0:
        break
    
    total += valor

print("Total final:", total)

print("\n")

# 4)
def calcular_imc():
    try:
        peso = float(input("Digite o peso: "))
        altura = float(input("Digite a altura: "))
        
        imc = peso / (altura ** 2)
        
        if imc < 18.5:
            print("Magro")
        elif imc <= 24.9:
            print("Normal")
        else:
            print("Acima do peso")
    
    except:
        print("Entrada inválida!")

calcular_imc()

print("\n")

# 5) 
amigos = ["Neymar", "Messi", "Cristiano Ronaldo", "Romário"]
quantidade = len(amigos)

if quantidade % 2 == 0:
    print("Quantidade par")
else:
    print("Quantidade ímpar")

print("\n")

# 6)
temperaturas = []
for i in range(7):
    temp = float(input(f"Digite a temperatura do dia {i+1}: "))
    temperaturas.append(temp)

media = sum(temperaturas) / 7

print(f"Média da semana: {media:.1f}")

print("\n")

# 7)
vendas = [120, 55, 300, 41, 200, 75]
soma = 0

for valor in vendas:
    if valor % 2 == 0:
        soma += valor

print("Soma dos valores pares:", soma)

print("\n")

# 8)
try:
    valor = float(input("Digite o valor da compra: "))

    if valor > 500:
        desconto = 0.20
    elif valor >= 200:
        desconto = 0.10
    else:
        desconto = 0

    preco_final = valor - (valor * desconto)

    print("Preço final: R$", preco_final)

except:
    print("Entrada inválida!")

print("\n")

# 11)
alunos_idades = [10,15,13,16,12]
alunos_idades.sort()

print(alunos_idades)

print("\n")

# 12)
try:
    def calculadora():
        opcao = ""

        while opcao != "0":
            print("CALCULADORA")
            print("1 - Soma")
            print("2 - Subtração")
            print("3 - Multiplicação")
            print("4 - Divisão")
            print("5 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "5":
                print("Fim do programa")

            elif opcao == "1":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("Resultado:", a + b)

            elif opcao == "2":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("Resultado:", a - b)

            elif opcao == "3":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("Resultado:", a * b)

            elif opcao == "4":
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            
            if b == 0:
                print("Erro: não pode dividir por zero")
            else:
                print("Resultado:", a / b)

        else:
            print("Opção inválida")
except:
    print("Entrada inválida")

calculadora()