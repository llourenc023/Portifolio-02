from socket import *
ip = "127.0.0.1"
porta = 1006
objeto_sckt = socket(AF_INET, SOCK_DGRAM)
objeto_sckt.bind((ip, porta))
print('Aguardando cliente.......')
while True:
	mensagem_cliente, cliente = objeto_sckt.recvfrom(65535)
	msg_decode = mensagem_cliente.decode('utf-8')
	print(f'Mensagem do cliente {cliente}: {msg_decode}')
	if mensagem_cliente.lower() == "sair":
		print('...Conexão encerrada...')
		break
	resposta = input('Digite sua resposta: ')
	objeto_sckt.sendto(resposta.encode('utf-8'), cliente)
objeto_sckt.close()