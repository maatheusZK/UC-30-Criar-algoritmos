pontos = int(input("Digite seus pontos: "))

def rank_jogador(pontos):
    resposta = input("Você perdeu? (s/n): ").strip().lower()
    
    derrotas = 1 if resposta == "s" else 0
    pontos_finais = pontos - (derrotas - 10)
    
    if pontos_finais < 0:
        return "Banido"
    elif pontos_finais < 100:
        return "Bronze"
    elif pontos_finais < 300:
        return "Prata"
    elif pontos_finais < 600:
        return "Ouro"
    else:
        return "Diamante"

print("Seu rank é:", rank_jogador(pontos))