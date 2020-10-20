"""Classes para a armazenar as informações de cada uma das empresas"""


class DTO_Empresa():
    def __init__(self,valores_diario = None, **kwargs):
        self.papel = kwargs['papel']
        self.tipo = kwargs['tipo']
        self.empresa = kwargs['empresa']
        self.valor_mercado = kwargs['valor_mercado']
        self.pl = kwargs['pl']
        self.preco_valorpatr = kwargs['preco_valorpatr']
        self.roic = kwargs['roic']
        self.roe = kwargs['roe']
        self.marg_liq = kwargs['marg_liq']
        self.porcentagem_dozemeses = kwargs['porcentagem_dozemeses']
        self.valores_diario = valores_diario
