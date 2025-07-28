from socket import *
server = "127.0.0.1l"
port = 1006
objeto = socket(AF_INET, SOCK_DGRAM)
print('Enviando dados ao servidor ', server)
while True:
	mensagem = input('Digite algo ("sair" para sair): ').encode('utf-8')
	objeto.sendto(mensagem, (server, port))
	if mensagem.lower() == "sair":
		print('... conexão encerrada ...')
		break
	resp_server, endereco = objeto.recivfrom(1024)
	print(f'Resposta do servidor {endereco}: {resp_server.decode("utf-8")}')
objeto.close()