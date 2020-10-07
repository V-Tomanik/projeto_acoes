"""
Estrutura das tabelas do servidor local para o servidor Postgres
"""

#Biblioteca para declaração de classes para as tabelas do servidor
from  sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import Column, Float, Date, String, Integer #Importa os tipo



Table = declarative_base()

class B3Daily(Table):
    """ Tabela Representativa para a API Alpha Vantage Diaria """

    __tablename__ = 'acoesdiario'
    id = Column(Integer, primary_key = True, autoincrement=True)
    ticker = Column(String(50))
    date = Column(Date)
    open = Column(Float)
    high = Column(Float)
    low  = Column(Float)
    close = Column(Float)
    volume = Column(Float)

    def __repr__(self): #Cria a representação quando tentamos printar os objetos da tabela
        #todo: Mudar isso
        return 'id={},ticker={},Date={}, open={}, high={}, low = {}, close = {}, volume ={}'.format(
            self.id,self.ticker,self.date,self.open,self.high,self.low,self.close,self.volume)


class InfoEmpresas(Table):
    """ Tabela para informações das empresas """

    __tablename__ = 'empresasinfo'
    id = Column(Integer, primary_key = True, autoincrement=True)
    data_input = Column(Date)
    papel = Column(String(50))
    tipo = Column(String(50))
    empresa = Column(String(50))
    setor = Column(String(50))
    valor_mercado = Column(String(50))
    ultimo_balanco = Column(String(50))
    valor_firma = Column(String(50))
    n_acoes = Column(String(50))
    pl = Column(String(50))
    lpa = Column(String(50))
    preco_valorpatr = Column(String(50))
    p_ativos = Column(String(50))
    roic = Column(String(50))
    roe = Column(String(50))
    marg_liq = Column(String(50))
    porcentagem_dozemeses = Column(String(50))

    def __repr__(self): #Cria a representação quando tentamos printar os objetos da tabela
        return '<Papel={}, Tipo={}, Empresa={}, Setor = {}, Valor_mercado = {}'.format(
            self.papel,self.tipo,self.empresa,self.setor,self.valor_mercado)
