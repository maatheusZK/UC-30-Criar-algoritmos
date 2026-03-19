def tipo_magia(fogo, agua):
    if fogo and agua:
        return "Vapor"
    elif fogo:
        return "Fogo"
    elif agua:
        return "Água"
    else:
        return "Sem magia"

print(tipo_magia(True, True))
print(tipo_magia(True, False))
print(tipo_magia(False, True))
print(tipo_magia(False, False))