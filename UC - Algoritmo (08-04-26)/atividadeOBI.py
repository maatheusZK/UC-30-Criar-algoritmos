n = int(input("Números infectados no dia 0: "))
r = int(input("Fator reprodutivo da infecção: "))
p = int(input("Número alvo de pessoas infectadas: "))

total = n
novos = n
dias = 0

while total < p:
    novos = novos * r 
    total += novos
    dias += 1

print(dias)