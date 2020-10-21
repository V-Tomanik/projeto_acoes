import os
import requests
from dotenv import load_dotenv
load_dotenv()


class AvDaily():
    """ API da Alpha Vantage para dados diarios"""

    def __init__(self):
        self.key = os.environ['key_av']

    def request(self,ticket):
        """ Função que faz a solicitação"""
        url=f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticket}&apikey={self.key}"
        request = requests.request('GET', url=url)
        return request.json()


    def run(self,lista:list):
        """ Cria um interador(generator) para puxar de todos os dados das empresas

            Utiliza a funcionalidade next(generator)
        """
        for empresa in lista:
            yield self.request(empresa)


class AvSearch():
    def __init__(self, chave, target):
        """ API da Alpha Vantage para buscar empresas disponiveis na api"""

        self.key = chave
        self.symbol = target
        self.function = 'function=SYMBOL_SEARCH'
        self.url = "https://www.alphavantage.co/query?{}&keywords={}&apikey={}".format(self.function, self.symbol, self.key)

    def request(self):
        """ Função que faz a solicitação"""
        request = requests.request('GET', url=self.url)
        return request.json()

if __name__ == '__main__':
    lista_ = ['ITSA4.SAO','ITUB4.SAO','WEGE3.SAO','SUZB3.SAO','EGIE3.SAO','FLRY3.SAO','WEGRX']
    print(next(AvDaily().run(lista_)))
