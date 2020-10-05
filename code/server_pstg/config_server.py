import os

from dotenv import load_dotenv
from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.sql import insert, text 
import models_pstq as model

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
    #dado = {'id':0,'date':'2020/10/01','open':34.1,'high':70,'low':3.1,'close':40.1,'volume':300}
    #ServerManager().InsertData('AcoesDiario',**dado)
    for i in ServerManager().SelectData("SELECT * from AcoesDiario"):
        print(i)
