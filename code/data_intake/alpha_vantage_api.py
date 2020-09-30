import os
import requests
from dotenv import load_dotenv
load_dotenv()

key = os.environ['key_av']

class AvDaily():
    def __init__(self, symbol):
        self.key = key
        self.symbol = symbol
        self.function = 'TIME_SERIES_DAILY'
        self.url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(self.symbol, self.key)

    def request(self):
        request = requests.request('GET', url=self.url)
        return request.json()


class AvDailyItsa4(AvDaily):
    def __init__(self):
        super().__init__('ITSA4.SAO')


class AvDailyItub(AvDaily):
    def __init__(self):
        super().__init__('ITUB4.SAO')


class AvDailyWeg(AvDaily):
    def __init__(self):
        super().__init__('WEGE3.SAO')


class AvDailySuzano(AvDaily):
    def __init__(self):
        super().__init__('SUZB3.SAO')


class AvDailyEngie(AvDaily):
    def __init__(self):
        super().__init__('EGIE3.SAO')


class AvDailyFleury(AvDaily):
    def __init__(self):
        super().__init__('FLRY3.SAO')

# Americanas


class AvDailyWellsF(AvDaily):
    def __init__(self):
        super().__init__('WEGRX')


class AvSearch():
    def __init__(self, chave, target):
        self.key = chave
        self.symbol = target
        self.function = 'function=SYMBOL_SEARCH'
        self.url = "https://www.alphavantage.co/query?{}&keywords={}&apikey={}".format(self.function, self.symbol, self.key)

    def request(self):
        request = requests.request('GET', url=self.url)
        return request.json()

if __name__ == '__main__':
    print(AvDailyEngie().request())
