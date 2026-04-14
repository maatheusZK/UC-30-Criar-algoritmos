def soma_segura(a, b):
    try:
        resultado = a + b
        print(resultado)
    except TypeError:
        print("Entrada inválida")


def divisao(x, y):
    try:
        resultado = x / y
        print(resultado)
    except ZeroDivisionError:
        print("Não divida por zero!")
    except TypeError:
        print("Entrada inválida")


soma_segura(5, 3)
divisao(10, 2)
divisao(10, 0)
soma_segura(5, "a")