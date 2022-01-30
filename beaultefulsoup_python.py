"""This "Data Analysis" exercise uses request and beautifulSoup libraries to scan sites and collect data and list or tuples."""

"""These exercises are from the "Graduation in Digital Games" course of the subject "data analysis with python"""

from bs4 import BeautifulSoup
import requests


texto_html = requests.get('https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html').text

text_bs4 = BeautifulSoup( texto_html, 'html.parser')

list_noticias = text_bs4.find_all('span', attrs={'class': 'short-desc'})

print(list_noticias[0])
print('*' * 40)
print(list_noticias[0].contents[0]) #this is a simple example using the contents for extract the span tag from the html list itens.
print(list_noticias[0].contents[1])
print(list_noticias[0].contents[2])
print('*' * 40)

dados = []
for noticia in list_noticias:
    datas = noticia.contents[0].text.strip() + ', 2017'
        # in this int removed the html tags using text and used the strip for removed the space add 2017 years
    comentarios = noticia.contents[1].strip().replace("“",'').replace("”", '')
        # in this int removed the space and rplace de spacial caracters with replace.
    explicacao =  noticia.contents[2].text.strip().replace("(", '').replace(")", '')
    url = noticia.find('a')['href']
        #find the a tags e take the href of the a tags.
    dados.append((datas, comentarios, explicacao, url))

print('-=' * 40)
print('--' * 40)
print(dados[0][0])
print('--' * 40)
print(dados[0][1])
print('--' * 40)
print(dados[0][2])
print('--' * 40)
print(dados[0][3])
print('--' * 40)
print('-=' * 40)

print(len(dados))