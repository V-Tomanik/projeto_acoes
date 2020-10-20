from flask import Flask, render_template
import numpy as np
import pandas as pd
import plotly.graph_objs as go
import json
import plotly
import dto

#Define a porta do servidor
#app.run(host ='numero do host', port=porta)
dados_diario = [{'ticker':'ITUB3','date':'2020-10-01','open':14.5,
        'high':50,'low':9.4,'close':20,'volume':340},
        {'ticker':'ITS3','date':'2020/10/02','open':00.1,'high':90,'low':8.1,'close':42.1,'volume':330}]

dados_empresa = {'papel':'ITUB3','tipo':'ON N1','empresa':'ITAUUNIBANCO','valor_mercado':'21000',
        'pl':'10,58','preco_valorpatr':'1.67','roic':'-','roe':'15.6%','marg_liq':'0.0%',
        'porcentagem_dozemeses':'-23.5%'}
itub = dto.DTO_Empresa(valores_diario=dados_diario,**dados_empresa)
dados_diario = [{'ticker':'ITAs4','date':'2020-10-01','open':14.5,
        'high':50,'low':9.4,'close':20,'volume':340},
        {'ticker':'ITS3','date':'2020/10/02','open':00.1,'high':90,'low':8.1,'close':42.1,'volume':330}]

dados_empresa = {'papel':'ITSA4','tipo':'ON N1','empresa':'ITAUSA','valor_mercado':'16000',
        'pl':'5,58','preco_valorpatr':'1.67','roic':'-','roe':'5.8%','marg_liq':'0.0%',
        'porcentagem_dozemeses':'-53.5%'}
itausa = dto.DTO_Empresa(valores_diario=dados_diario,**dados_empresa)


def create_plot():


    N = 40
    x = np.linspace(0, 1, N)
    y = np.random.randn(N)
    df = pd.DataFrame({'x': x, 'y': y}) # creating a sample dataframe


    data = [
        go.Bar(
            x=df['x'], # assign x as the dataframe column 'x'
            y=df['y']
        )
    ]

    graphJSON = json.dumps(data, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON




#==============================================================================






lista = [itub,itausa]
#Cria o objeto flask
server = Flask(__name__)

@server.route('/')
def home():
    bar = create_plot()
    return render_template('main.html',empresas=lista,plot =bar)


server.run(debug= True)
