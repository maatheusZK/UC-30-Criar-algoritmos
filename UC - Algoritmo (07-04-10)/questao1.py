P = int(input())  # pão
D = int(input())  # doce
B = int(input())  # bolo

pontos = P + D + B

if pontos >= 150:
    print("B")
elif pontos >= 120:
    print("D")
elif pontos >= 100:
    print("P")
else:
    print("N")