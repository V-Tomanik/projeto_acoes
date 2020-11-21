from datetime import datetime

class DTO_acoes_diario:
    def __init__(self):
        """ Data Transfer Object

        Servem para garantir a consistência das informações,
        de um lugar para outro. Futuramente pretendo tratar as informações antes
        de importar para a tabela (eu sei que não é o ideal) e usarei isso para
        garantir as informações

        param:
            ticker: Ticker representativo da empresa na b3
            date: data analisada
            open: valor de abertura
            close: valor de fechamento
            high: máxima diaria
            low: minima diaria
            volume: volume diario
        """
        self.ticker = None
        self.date = None
        self.open = None
        self.high = None
        self.low  = None
        self.close = None
        self.volume = None

    def input(self,**kargs):
        """Método de inportação de dados

            param:
                metodo(av)
        """
        self.ticker = kargs['ticker'].split('.')[0]
        self.date = datetime.strptime(kargs['date'],'%Y-%m-%d').date()
        self.open = kargs['1. open']
        self.high = kargs['2. high']
        self.low  = kargs['3. low']
        self.close = kargs['4. close'] 
        self.volume = kargs['5. volume'] 

       
        return self
     
    def output(self):
        """Função conseguir a funcionalidade __dict__ mas
        ainda protegendo ela"""
        return self.__dict__

    def get_table(self):
        return 'acoesdiario'



