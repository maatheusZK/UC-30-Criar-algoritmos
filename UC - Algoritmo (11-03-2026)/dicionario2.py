contato = {
    "@camila": "Camila",
    "@paolla": "Paolla",
    "@sheron": "Sheron",
    "@bruna": "Bruna"
}

# Obter chaves
print("Chaves: ")
for insta in contato.keys():
    print(insta)

# Obter valores
print("\n Valores: ")
for nome in contato.values():
    print(nome)

# Obter pares
print("\n Pares ")
for insta, nome in contato.items():
    print(f"{insta} --> {nome}")

contato = {
    "@camila": 1.70,
    "@paolla": 1.80,
    "@sheron": 1.55,
    "@bruna": 1.60
}


print("Ordenando por chave: ")
for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m")

from operator import itemgetter
print("\n Ordenado por valor (Altura): ")
for insta, estatura in sorted(contato.items(), key = itemgetter(1)):
    print(f"{insta} --> {estatura:.2f}m")