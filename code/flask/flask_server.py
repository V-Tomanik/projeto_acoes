import os

from dotenv import load_dotenv
from code.flask.plotly_flask import plotlyManager as pm
from flask import Flask, render_template

load_dotenv()

#Define a porta do servidor
#app.run(host ='numero do host', port=porta)

#Cria o objeto flask
server = Flask(__name__)


@server.route('/')
def home():
    empresas = ['ITSA4','ITUB4','WEGE3','SUZB3','EGIE3','FLRY3']
    linhas = [[pm.graph_daily_candle(f"{empresa}"),pm.graph_daily_stock_prevision(f"{empresa}"),
             pm.table_empresa(f"{empresa}"),empresa]
            for empresa in empresas]
    return render_template('main.html',empresas = linhas)


if __name__ == '__main__':
    server.run()
