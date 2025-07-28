from socket import *
servidor = input('Digite o IP do servidor: ')

for porta in range(1, 65535):
	objeto = socket(AF_INET, SOCK_STREAM)
	objeto.settimeout(0.5)
	if objeto.connect_ex((servidor, porta)):
		print(porta)