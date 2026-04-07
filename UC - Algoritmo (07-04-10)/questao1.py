P = int(input())  # pão
D = int(input())  # doce
B = int(input())  # bolo

pontos = P * 1 + D * 2 + B * 3

if pontos >= 150:
    print("B")
elif pontos >= 120:
    print("D")
elif pontos >= 100:
    print("P")
else:
    print("N")