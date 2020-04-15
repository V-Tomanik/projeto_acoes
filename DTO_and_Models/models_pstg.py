from  sqlalchemy.ext.declarative import declarative_base #Biblioteca para declaração de classes para as tabelas do servidor
from  sqlalchemy import Column, Float, String, Date #Importa os tipos que serão usados na tabela

Table = declarative_base()

class IBV_Daily(Table):
    __tablename__ = 'IBV_Daily'
    date = Column(Date, primary_key = True)
    open = Column(Float)
    high = Column(Float)
    low  = Column(Float)
    close = Column(Float)
    volume = Column(Float)


    def __repr__(self): #Cria a representação quando tentamos printar os objetos da tabela
        return '<Date={}, open={}, high={}, low = {}, close = {}, volume ={}'.format(
            self.date,self.open,self.high,self.low,self.close,self.volume)





