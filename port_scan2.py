from socket import *
sair = ""
while sair != "S":
    endereco = input("Digite o endereço IP do servidor: ")
    porta = int(input('Digite a porta:'))
    objeto = socket(AF_INET, SOCK_STREAM)
    objeto.settimeout(0.5)
    if objeto.connect_ex((endereco, porta)):
        print(f'Porta {porta} está aberta')
    else:
        print(f'Porta {porta} está fechada')
    sair = input('Aperte <S> se deseja sair ').upper() 
    if sair == "S":
        print('Saindo do programa...')