login1 = "procopio"
senha1 = 12345

login2 = "paiva"
senha2 = 54321

user = input("Digite seu usuário: ")
password = int(input("Digite sua senha: "))

if user == login1 and senha1 == password or user == login2 and senha2 == password:
    print("Seja bem vindo!")
else: 
    print("Usuário e senha não conferem.")
