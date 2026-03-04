nome1 = "Matheus"
nome2 = "Gayo"
nome3 = "Weverton"

nomes = ["Matheus", "Gayo", "Weverton"]
print(nomes)

dados = ["Carol", 0, 1.70, True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

# adicionar = input("Digite um animal: ")
# lista.append(adicionar)


lista = ["Cachorro", "Gato"] 
print("Original: ", lista)
lista.append("Coelho") # add no fim da lsita
print("Atualizada: ", lista)

lista.insert(1, "Grilo") # add na posição determinada
print("Atualizado: ", lista)

lista.extend(["Macaco", "Ovelha"]) # add mais de um dado de uma vez
print("Lista final: ", lista)




