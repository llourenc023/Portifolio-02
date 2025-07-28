from requests import *
from bs4 import BeautifulSoup
url = "https://www.uol.com.br"
requisitar = get(url)
limpar = BeautifulSoup(requisitar.text, "html.parser")
extrair = limpar.get_text().split()
with open('wordlist.txt', 'w') as arquivo_wdlst:
	for item in extrair:
		arquivo_wdlst.write(item + '\n')