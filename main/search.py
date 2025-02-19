from bs4 import BeautifulSoup
import requests
import os

r = requests.get("https://duckduckgo.com/?q=Inteligência+artificial+avanços&atb=v458-1&df=w&ia=web")

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())

print("Diretório de trabalho:", os.getcwd())

# Extração para arquivo em txt

with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(soup.prettify())
    print("Arquivo criado com sucesso")
