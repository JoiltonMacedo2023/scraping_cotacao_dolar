import requests
from bs4 import BeautifulSoup
import json

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

response = requests.get(
    'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar', headers=headers)

# print(response)
# print()
# print(response.text)
site = BeautifulSoup(response.text, 'html.parser')
# print(site.prettify())

titulo = site.find('title')

pesquisa = site.find('textarea', class_='gLFyf')
# print(pesquisa['value'])  # pode usar .text

cotacao_dolar = site.find('span', attrs={'class': 'DFlfde SwHCTb'})
# print(cotacao_dolar.get_text())  # ['data-value']

data_hora = site.find('div', attrs={'class': 'k0Rg6d hqAUc'})

fonte = site.find('span', attrs={'class': 'NXHf6d'})
fonte_link = fonte.parent['href']

dados = {
    'titulo': titulo.get_text(),
    'pesquisa google': pesquisa['value'],
    'cotacao do dolar de hoje': f'R$ {cotacao_dolar.get_text()}',
    'data_hora': {
        'texto': f' Data/hora: {data_hora.get_text()}',
        'fontes': {
            'url': fonte_link
        }
    }
}

with open('dados.json', 'w', encoding='utf-8') as json_file:
    json.dump(dados, json_file, ensure_ascii=False, indent=4)

print("Dados salvos em 'dados.json'")
