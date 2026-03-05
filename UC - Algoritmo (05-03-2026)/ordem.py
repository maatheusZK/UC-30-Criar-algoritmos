import random

numeros = ["4", "2", "5", "3", "1"]
print("Lista original: " , numeros)

# sort crescente
numeros.sort()
print("Após sort(): ", numeros)

# sort decrescente
numeros.sort(reverse=True)
print("Após sort(): ", numeros)

# embaralha
random.shuffle(numeros)
print("Lista embaralhada: ", numeros)