import requests
from tkinter import *

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

janela = Tk()
janela.title("PROGRAMA DE COTACÕES")
janela.geometry("500x500")
informacoes = Label(janela, text=" Aperte em cotar para converter a moeda de DOLLAR EURO E BTC")
informacoes.grid(column = 0, row = 1, padx = 40, pady=40)
botao = Button(janela, text="COTAR", command=pegar_cotacoes)
botao.grid(column = 0, row = 2, padx=40, pady= 40)
texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column= 0, row = 4, padx=40, pady=40)

janela.mainloop()