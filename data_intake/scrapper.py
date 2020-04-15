#TODO: Arrumar as solicitações do bs e ver a questão da solicitação da AVantage, eu estou usando o selenium para conseguir pegar a parte js mas não estou conseguindo :(
from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup  
import classes as  cl
import requests
import time


def B3_Scrapper():
    sessao = webdriver.Firefox(executable_path=r"/home/vv/Programs/git/b3/geckodriver")
    sessao.get('http://www.b3.com.br/pt_br/market-data-e-indices/servicos-de-dados/market-data/historico/derivativos/ajustes-do-pregao/')
    #sessao.get('https://www.tradingview.com/symbols/BMFBOVESPA-CCMK2020/') 
    elem = sessao.find_element_by_css_selector('body')  
    print(elem)
    code = BeautifulSoup(sessao.page_source,'html.parser')
    print(code) 
    sessao.close()

B3_Scrapper()


