import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.sql import insert, text
import models_pstq as model
from datetime import date
load_dotenv()

class ServerManager():
    def __init__(self):
        # postgres+psycop2://<username>:<password>@<IP>:<Port>/<Database_name>
        self.DataBaseUri = os.environ['server_url']
        self.engine = create_engine(self.DataBaseUri)
        self.conn = self.engine.connect()

    def InsertData(self,TableName,**kargs):
        """ Função para adicionar dados na tabela
                TableName: Nome da tabela alvo
                kargs: Dados a serem inseridos
        """
        #Informa as informações da tabela e mostra o db alvo
        metadata = MetaData(bind = self.engine)
        tabela = Table(TableName,metadata,autoload=True)

        #Cria o insert statement
        ins = insert(tabela).values(**kargs)
        #Se conecta à engine e executa o statement
        self.conn.execute(ins)

    def SelectData(self, Query):
        """Função para conseguir as informações na tabela selecionada
            parametros{
        """
        s= text('SELECT * FROM "AcoesDiario"')
        return self.conn.execute(s)

    def CreateTables(self):
        model.Table.metadata.create_all(self.engine)


if __name__ == '__main__':
    pass
    #ServerManager().CreateTables()
    #dado = [{'ticker':'ITS3','date':'2020/10/02','open':00.1,'high':90,'low':8.1,'close':42.1,'volume':330},{'ticker':'ITS3','date':'2020/10/03','open':37.1,'high':80,'low':5.1,'close':42.1,'volume':500}]
    #dado = [{'data_input': date.today(), 'papel': 'WEGE3', 'tipo': 'ONN1', 'empresa': 'WEGSAONN1', 'setor': 'MáquinaseEquipamentos', 'valor_mercado': '164.535.000.000', 'ultimo_balanco': '30/09/2020', 'valor_firma': '162.907.000.000', 'n_acoes': '2.098.660.000', 'pl': '78,38', 'lpa': '1,00', 'preco_valorpatr': '14,79', 'p_ativos': '8,64', 'roic': '20,5%', 'roe': '18,9%', 'marg_liq': '13,1%', 'porcentagem_dozemeses': '223,28%'}]
    #for i in dado:
    #    ServerManager().InsertData('empresasinfo',**i)
    #for i in ServerManager().SelectData("SELECT * from AcoesDiario"):
        #print(i)
