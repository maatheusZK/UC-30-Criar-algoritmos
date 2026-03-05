nomes = ["Ana", "Bruno", "Carlos", "Diana"]
print("Nomes: ", nomes)

nomes.remove("Bruno")
print("Lista atualizada: ", nomes)

# removido = nome.pop()
removido = nomes.pop(1)
print(f"Removido: {removido}")
print("Após pop(): ", nomes)


# del - remover pelo indece
del nomes[0]
print("Após del nomes[0]: ", nomes)

# clear: esvazia
nomes.clear()
print("Lista atualizada: ", nomes)

