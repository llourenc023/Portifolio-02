from socket import *
ip = input('Digite o endereço IP: ')
url = gethostbyaddr(ip)
print(f"A o servidor correspondente ao IP {ip} é: {url}")