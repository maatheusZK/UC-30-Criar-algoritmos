import random

# primeira parte
numeros = [91, 34, 67, 15, 82]
print("Lista original: ", numeros)

numeros.sort()
print("Lista em odem crescente: ", numeros)

numeros.sort(reverse=True)
print("Lista em ordem decrescente: ", numeros, "\n")

# segunda parte
numeros2 = [6, 7, 8, 9, 10]
print("Lista 2 original: ", numeros2)

random.shuffle(numeros2)
print("Lista 2 embaralhada: ", numeros2, "\n")

# desafio
minhaLista = [10, 7, 99, 80, 11, 77]
minhaLista.sort()
print("Minha lista em odem crescente: ", minhaLista)

minhaLista.sort(reverse=True)
print("Minha Lista em ordem decrescente: ", minhaLista)

random.shuffle(minhaLista)
print("Minha Lista embaralhada: ", minhaLista)
