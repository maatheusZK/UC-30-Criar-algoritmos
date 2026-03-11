nome = input("Digite o nome do aluno: ")

matricula = int(input("Digite a matrícula: "))

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))

media = (nota1 + nota2) / 2

print("\n Relatório do aluno")
print("Nome: ", nome)
print("Matrícula: ", matricula)
print("Nota 1: ", nota1)
print("Nota 2: ", nota2)
print("Média: ", media)