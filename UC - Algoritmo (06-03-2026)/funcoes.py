notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("Notas: ", notas)

print("Menor: ", min(notas))
print("Maior: ", max(notas))
print("Soma: ", sum(notas))
print("Média: ", sum(notas) / len(notas), "\n")


nomes = ["Adriana", "Breno", "Carla", "Daniel"]

#apenas o elemento
print("Usando FOR simples: ")
for nome in nomes :
    print(f"Olá, {nome}!")

#indice e elemnto
print("\n Usando enumerate: ")
for indice, nome in enumerate(nomes):
    print(f"Posição {indice}: {nome}", "")


original = ["A", "F", "C"]
copia = list(original)

print("\n Original: ", original)
print("Cópia: ", copia)
print("São iguais: ", original == copia, "\n")

copia.append("D")
print("Original: ", original)
print("Cópia: ", copia)
print("São iguais: ", original == copia)