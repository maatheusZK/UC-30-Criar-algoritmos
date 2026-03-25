def resumo_estatistico(notas):
    return {
        "soma": sum(notas),
        "media": sum(notas) / len(notas),
        "maior": max(notas),
        "menor": min(notas)
    }

print(resumo_estatistico([7.5, 8.0, 6.5, 9.0]))