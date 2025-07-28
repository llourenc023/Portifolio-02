from socket import *
endereco = '127.0.0.1'  # Endereço do servidor
porta = 1004
objeto = socket(AF_INET, SOCK_STREAM)
objeto.bind((endereco, porta))
objeto.listen(6)
print('Aguardando cliente...')
while True: # Estabelecendo conexões
	conexao, cliente = objeto.accept()
	print(f'Conectado com {cliente}')
	while True: # Troca de mensagens
		msg_cliente = conexao.recv(1024).decode('utf-8')
		if msg_cliente.lower() == "sair" or msg_cliente == "":
			print("Cliente saiu")
			break
			
		print(f'Mensagem: {msg_cliente} \ndo cliente {cliente}')
		msg_procliente = (input('Sua resposta: '))
		conexao.send(msg_procliente.encode('utf-8'))
	conexao.close()
