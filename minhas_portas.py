from socket import *
print(f"Domínio: {getservbyname("domain")}")
print(f"HTTPS: {getservbyname("https")}")
print(f"FTP: {getservbyname("ftp")}")