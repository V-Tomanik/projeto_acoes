from datetime import date

class DTO_info_empresas:
    def __init__(self):
        """ Data Transfer Object

        Servem para garantir a consistência das informações,
        de um lugar para outro. Futuramente pretendo tratar as informações antes
        de importar para a tabela (eu sei que não é o ideal) e usarei isso para
        garantir as informações

        param:
            data_input
            papel
            tipo
            empresa
            setor
            valor_mercado
            ultimo_balanco
            valor_firma
            n_acoes
            pl
            lpa
            preco_valorpatr
            p_ativos
            roic
            roe
            marg_liq
            porcentagem_dozemeses
        """

        self.data_input = date.today()
        self.papel = None
        self.tipo = None
        self.empresa = None
        self.setor = None
        self.valor_mercado = None
        self.ultimo_balanco = None
        self.valor_firma = None
        self.n_acoes = None
        self.pl = None
        self.lpa = None
        self.preco_valorpatr = None
        self.p_ativos = None
        self.roic = None
        self.roe = None
        self.marg_liq = None
        self.porcentagem_dozemeses = None

    def input(self,**kargs):
        """Método de inportação de dados

            param:
                metodo(av)
        """
        self.papel = kargs['Papel']
        self.tipo = kargs['Tipo']
        self.empresa = kargs['Empresa']
        self.setor = kargs['Setor']
        self.valor_mercado = kargs['Valor de mercado']
        self.ultimo_balanco = kargs['Últ balanço processado']
        self.valor_firma = kargs['Valor da firma']
        self.n_acoes = kargs['Nro. Ações']
        self.pl = kargs['P/L']
        self.lpa = kargs['LPA']
        self.preco_valorpatr = kargs['P/VP']
        self.p_ativos = kargs['P/Ativos']
        self.roic = kargs['ROIC']
        self.roe = kargs['ROE']
        self.marg_liq = kargs['Marg. Líquida']
        self.porcentagem_dozemeses = kargs['12 meses']
        
        return self
     
    def output(self):
        """Função conseguir a funcionalidade __dict__ mas
        ainda protegendo ela"""
        return self.__dict__

    def get_table(self):
        return 'empresasinfo'


if __name__ == '__main__':
    DTO_info_empresas().input
