import os
import requests
import time

key = 'IB72OMPOLJYNWAFU'

class AV_api_daily_ibov():
    def __init__(self,key):
        self.key =  key 
        self.symbol = '^BVSP'
        self.function = 'TIME_SERIES_DAILY' 
        self.url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={}&apikey={}".format(self.symbol,self.key)
    
    def request(self):
        request =  requests.request('GET',url= self.url)
        return request.json()
        

    
if __name__ ==  '__main__':
    print(AV_api_daily_ibov(key).request())
