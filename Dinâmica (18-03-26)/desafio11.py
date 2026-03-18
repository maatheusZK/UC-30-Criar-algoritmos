lista = [77, 99, 10]

def somaTudo(numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

resultado = somaTudo(lista)
print(resultado)