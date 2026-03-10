# Sem dicionário
matricula1 = 2026001
nome1 = "Allana"
telefone1 = "99999-8888"

# Com dicionário
aluno = {
    "matricula": 2026001,
    "nome": "Allana",
    "telefone": "99999-8888"
}

print(aluno)

contato = {
    "@neymarjunior": "Neymar Junior",
    "@lionelmessi": "Lionel Messi",
    "@rayan77": "Rayan",
    "@joaocarlo123": "João CARLO",
    "@vascodagama":  "Vasco da Gama."
}

print(contato)
print(type(contato))

# Acesso direto
print(contato["@neymarjunior"])

# Acesso seguro com get()
print(contato.get("@lionelmessi"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))


#add novo elemento
contato["@caçarato7"] = "Caça Rato"
print("Após add: ", contato)

#atualiza elemento existente 
contato["@lionelmessi"] = "Lionel messi"
print("Após add: ", contato)

contato.update({
        "@rayan77": "Rayan",
        "@vascodagama": "Vasco da Gama"
    })

print("Após atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@neymarjunior")
print(f"Removido: {removido}")
print("Após o pop: ", contato)

#del remove sem retornar
del contato["@lionelmessi"]
print("Após o del: ", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia: ", copia)

print("Número de contatos: ", len(contato)) #tamanho dicio

#verificar existência
if "@joaocarlo123" in contato:
    print(f"Encontrado: {contato['@joaocarlo123']}")

if "@inexistente" in contato:
    print("Existe.")
else:
    print("Não existe.")