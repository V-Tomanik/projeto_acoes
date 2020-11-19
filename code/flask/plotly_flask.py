import plotly 
import plotly.graph_objects as go
import plotly.express as px


import json
import pandas as pd
from code.server_pstg.config_server import ServerManager


class plotlyManager():
    
    @staticmethod
    def graph_daily_candle(empresa):
        query = f"select a.* from (select *,max(id) over (partition by ticker,date) mx_version from acoesdiario where ticker = '{empresa}')as a where mx_version = id"
        data = ServerManager().SelectAllData(query=query)
       
        df = pd.DataFrame.from_dict(data)

        grafico = [go.Candlestick(x=df['date'],open=df['open'],high=df['high'],low=df['low'],close=df['close'])]
        graficoJson = json.dumps(grafico,cls=plotly.utils.PlotlyJSONEncoder) #Transformando o grafico em json
        return graficoJson

    @staticmethod
    def table_empresa(empresa):
        query = f"select a.* from (select *,max(data_input) over (partition by papel) mx_version from empresasinfo where papel = '{empresa}')as a where mx_version = data_input"
        data = ServerManager().SelectAllData(query=query)
        return data[0]

    @staticmethod
    def graph_daily_stock_prevision(empresa):
        query = f"select a.* from (select *,max(id) over (partition by ticker,date) mx_version from acoesdiario where ticker = '{empresa}')as a where mx_version = id"
        data = ServerManager().SelectAllData(query=query)
       
        df = pd.DataFrame.from_dict(data)

        grafico = [go.Scatter(x=df['date'],y=df['close'])]
        graficoJson = json.dumps(grafico,cls=plotly.utils.PlotlyJSONEncoder) #Transformando o grafico em json
        return graficoJson


if __name__ == '__main__':
    plotlyManager.table_empresa("""'EGIE3'""")
