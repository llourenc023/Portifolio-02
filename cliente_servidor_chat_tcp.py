from socket import *
server = input('Digite o endereço do servidor: ')
port = int(input('Digite o número da porta: '))
objeto = socket(AF_INET, SOCK_STREAM)
objeto.connect((server, port))
print('Contectado ao servidor {server}')
while True:
	msg = input('Digite algo ("sair" para sair): ')
	objeto.send(msg.encode('utf-8'))
	if msg.lower() == "sair":
		print('Saindo...')
		break
	resp = objeto.recv(1024).decode('utf-8')
	print(f'Resposta do servidor: {resp}')
objeto.close()
print('Conexão encerrada')