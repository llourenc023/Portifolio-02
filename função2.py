def idades(idade):
    if idade >= 18:
        return "Liberado"
    else:
        return "Não liberado"
balada = idades(21)
print(balada)