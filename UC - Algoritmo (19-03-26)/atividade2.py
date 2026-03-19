saldo = float(input("Digite o valor do saldo: "))
saque = float(input("Digite o valor do saque: "))

def saldo_final(saldo, saque):
    if saque > saldo:
        return "Saldo insuficiente"
    
    if saque > 1000:
        taxa = saque * 0.02
    else:
        taxa = 0
    
    resto = saldo - saque - taxa
    return resto

resultado = saldo_final(saldo, saque)
print(f"Seu saldo final é de {resultado}")