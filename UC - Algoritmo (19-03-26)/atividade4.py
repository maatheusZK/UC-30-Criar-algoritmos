pontos = int(input("Digite a pontuação inicial: "))
tempo = int(input("Digite o tempo: "))

def pontuacao_total(pontos, tempo):
    if tempo < 30:
        pontos += 50
    elif tempo > 100:
        pontos -= 20
    
    if pontos >= 200:
        return f"Parabéns! {pontos} é um recorde!"
    else:
        return pontos

resultado = pontuacao_total(pontos, tempo)
print("Resultado:", resultado)