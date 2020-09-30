from . import models_pstq as model
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import insert
import os
from dotenv import load_dotenv

load_dotenv()

class ServerManager():
    def __init__(self):
        # postgres+psycop2://<username>:<password>@<IP>:<Port>/<Database_name>
        self.DataBaseUri = os.environ['server_url']
        self.engine = create_engine(self.DataBaseUri)

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
        # Se conecta à engine e executa o statement
        conn = self.engine.connect()
        conn.execute(ins)

    def SelectData(self,TableName):
        """Função para conseguir as informações na tabela selecionada"""

        metadata = MetaData(bind=self.engine)




    def CreateTables(self):
        model.Table.metadata.create_all(self.engine)

















if __name__ == '__main__':
    chave = {'date': '22/07/2020','open':43.1,'high':33.1,'low':9.1,'close':329,'volume':13}
    ServerManager().InsertData('IBV_Daily',**chave)
