import requests
from bs4 import BeautifulSoup as bs


class Crawler():
    """Classe Pai dos crawlers, extrair a tabela de dados financeiros das páginas do Fundamentus"""

    def __init__(self):
        self.header = {'user-agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}

        self.empresas  = ['ITSA4','ITUB4','WEGE3','SUZB3','EGIE3','FLRY3']

    def extract(self,papel):
        """Executa o crawler"""
        url = f"https://www.fundamentus.com.br/detalhes.php?papel={papel}"
        DataPagina ={}
        response = requests.get(url = url, headers=self.header).text
        soup= bs(response,'html.parser')
        for a in soup.find_all('table'):
            for b in a.find_all('tr'):
                label = [l.text.replace('?','') for l in b.find_all('td',class_= 'label')]
                data =  [d.text.replace('\n','').replace(' ','') for d in b.find_all('td',class_='data')]
                for n in range(0,len(label)):
                #0-> 12 meses, 1 -> 3 meses
                    if label[n] in ('Receita Líquida','EBIT','Lucro Líquido'):
                        label[n] += f'_{n}'
                    DataPagina[label[n]] = data[n]

        return DataPagina

if __name__ == '__main__' :
    c = Crawler()
    for i in  c.empresas:
        print(c.extract(i))












