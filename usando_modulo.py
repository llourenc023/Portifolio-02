import modulo1
n1 = float(input("Escolha o primeiro número: "))
n2 = float(input("Escolha o segundo: "))
escolha = " "
print("As opções são: \n1 - Somar\n2 - Dividir\n3 - Multiplicar \n4 - Subtrair \n5 - Sair")
while escolha != 5:
    escolha = int(input("Escolha a opção: "))
    if escolha == 1:
        soma = modulo1.somar(n1, n2)
        print(f"A soma de {n1} e {n2} é: {soma}")
        break
    elif escolha == 2:
        divisao = modulo1.dividir(n1, n2)
        print(f"A divisão entre {n1} e {n2} é: {divisao}") 
        break
    elif escolha == 3: 
        multiplicacao = modulo1.multiplicar(n1,n2)
        print(f"A multiplicação entre {n1} e {n2} é: {multiplicacao}")
        break
    elif escolha == 4:
        subtracao = modulo1.subtrair(n1, n2)
        print(f"A subtração entre {n1} e {n2} é: {subtracao}")
        break
    elif escolha == 5:
        modulo1.saida()
        break
    else:
        print("Opção inválida, tente novamente!")
    
