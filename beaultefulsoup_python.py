"""This "Data Analysis" exercise uses request and beautifulSoup libraries to scan sites and collect data and list or tuples."""

"""These exercises are from the "Graduation in Digital Games" course of the subject "data analysis with python"""

from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml
import html5lib
from datetime import date


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

df_noticia = pd.DataFrame(dados, columns = ["datas", "comentarios", "explicacao", "url"])
print("---"*30)
print(df_noticia)
print("---"*30)

g1_url = 'https://g1.globo.com/'
g1_conteudo = requests.get(g1_url).text

g1_bs_conteudo = BeautifulSoup(g1_conteudo, 'html.parser')

g1_noticias = g1_bs_conteudo.find_all('div', attrs={'class': 'feed-post-body'})

print(g1_noticias[0].prettify())
print((g1_noticias[0].contents[0]))
print((g1_noticias[0].contents[1]))
print((g1_noticias[0].contents[2]))
print((g1_noticias[0].contents[3]))



g1_dados = []
for item in g1_noticias:
    conteudo1 = item.contents[0].text.strip()
    conteudo2 = item.contents[1].text.strip()
    conteudo3 = item.contents[2].text.strip()
    conteudo4 = item.contents[3].text.strip()

    g1_dados.append((conteudo1, conteudo2, conteudo3, conteudo4))

for item in g1_dados:
    print("-=" *40)
    print(f"Primeiro: {item[0]}")
    print(f"Segundo: {item[1]}")
    print(f"Terceiro: {item[2]}")
    print(f"Quarto: {item[3]}")
    print("-=" *40)


df_g1_noticias = pd.DataFrame(g1_dados, columns = ['primeiro', 'segundo', 'terceiro', 'quarto'])
print(df_g1_noticias)


sport_url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

sport_noticia = requests.get(sport_url).text

sport_noticia_bs = BeautifulSoup(sport_noticia, 'html.parser')

sport_list_noticia = sport_noticia_bs.find_all('div', attrs={'class': 'feed-postbody'})

print(sport_noticia_bs)

selic_url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados'
selic_dados = pd.read_json(selic_url)
selic_dados.drop_duplicates(keep='last', inplace=True)
selic_dados['responsável'] = 'autor'
selic_dados['DATA'] = date.today()
selic_dados['DATA'] = selic_dados['DATA'].astype('datetime64[ns]')
selic_dados['data'] = pd.to_datetime(selic_dados['data'], dayfirst=True)
selic_dados.sort_values("data", ascending=False, inplace=True)
#selic_dados.reset_index(drop=True, inplace=True)
novos_selic_index = [f'SELIC_{indice}' for indice in selic_dados.index]
selic_dados.set_index(keys=[novos_selic_index], inplace=True)

selic_dados['responsável'] = selic_dados['responsável'].str.upper()

print(selic_dados)