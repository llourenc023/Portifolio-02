lista = []
nota = 0
while nota != -1:
    nota = int(input("Digite a nota: (escolha -1 para sair) "))
    if nota != -1:
        lista.append(nota)
    else:
        print("Finalizando o programa...")
if len(lista) > 0:
    print("A média de notas é: ", sum(lista) / len(lista))
else:
    print("Nenhuma nota foi inserida.")
