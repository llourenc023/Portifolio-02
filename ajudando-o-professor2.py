print("... Programa Ajudando o Professor ...")
notas = []
opcao = 0
while opcao != 4:
    print("1-Cadastrar nota\n2-Exibir notas\n3-Exibir média\n4-Sair")
    opcao = int(input("Escolha sua opção: "))
    if opcao == 1:
        nota = float(input("Digite a nota:"))
        notas.append(nota)
        for i in notas:
            print(f"Notas: {i}")
    elif opcao == 2:
        for i in notas:
            print(f"Notas: {i}", end="")
    elif opcao == 3:
        media = sum(notas) / len(notas)
        print(f"Média: {media}")
    elif opcao == 4:
        print("... Saindo ...")
    else:
        print("Opção inválida")

