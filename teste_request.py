import requests

from tkinter import *

"""vai importar todos dados do TKinter sem precisar mencionar a biblioteca ao chamar o código"""

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dollar = requisicao_dic["USDBRL"]["bid"]
    cotacao_euro = requisicao_dic["EURBRL"]["bid"]
    cotacao_btc = requisicao_dic["BTCBRL"]["bid"]

    texto = f'''
    dolár: {cotacao_dollar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
    '''
    print(texto)
    texto_cotacao['text'] = texto

"""A bibliotéca TKinter ajuda a executar um sistema com janelas, é possivel modificar a janelas com alguns argumentos 
tal como o argumento do tipo geometry que pode ser passado  as dimensões
        Tk()
        .geometry( dimensões )
        .title( "digite um title")
        Label( nomejanela, text="digite o label")
        Button (janela, text="textodo botao", command="digite o comando")
        .grid( Define a posição do arquivo dentro do programa" column= , row=, padx=, pady= )
        .mainloop() finaliza a função
"""
janela = Tk()

janela.title("Cotação atual das moedas")

janela.geometry("400x400")

"""define o espaçamento da janela"""

texto_orientacao = Label(janela, text="Click no botão para ver a cotação das medas ")

texto_orientacao.grid(column = 0, row = 0, padx=20, pady=20)

botao = Button(janela, text="Buscar cotação DOLLAR/EURO/BTC", command= pegar_cotacoes)

botao.grid(column = 0, row = 1, padx=20, pady=20)

texto_cotacao = Label(janela, text="", padx=20, pady=20)

texto_cotacao.grid(column = 0, row = 3, padx=20, pady=20)

janela.mainloop()

