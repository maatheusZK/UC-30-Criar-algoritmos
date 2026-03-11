valor = float(input("Digite o valor da compra: "))

if valor < 100:
    desconto = 0
elif valor < 500:
    desconto = valor * 0.05
elif valor < 1000:
    desconto = valor * 0.10
else:
    desconto = valor * 0.15

valorFinal = valor - desconto

print("Valor original: R$", valor)
print("Desconto: R$", desconto)
print("Valor final: R$", valorFinal)