from socket import *
sair = "N"
while sair != "S":
	url = input("Digite a URL: ")
	ip = gethostbyname(url)
	print(f"O IP do site {url} é: {ip}")
	sair = input('Deseja sair? Digite <S> para sim e qualquer caractere para não sair ').upper()
	if sair == "S" or sair == "s":
		print("...SAINDO...")
	