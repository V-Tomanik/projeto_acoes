from code.data_intake.alpha_vantage_api import AvDaily
from code.data_intake.scrapper import Crawler
from code.server_pstg.config_server import ServerManager
from code.dto.dto_info_empresas import DTO_info_empresas
from code.dto.dto_acoesdiario import DTO_acoes_diario

api = AvDaily()
scrap = Crawler()
#for empresa in scrap.empresas:
#    obj_dto_infoempresa = DTO_info_empresas().input(**scrap.extract(empresa)) #Faz a coleta dos dados
#    ServerManager().InsertData(obj_dto_infoempresa.get_table(),**obj_dto_infoempresa.output()) #Faz o importacao para o banco
#    print(f'Importanto dados sobre {empresa}')
print('Empresas info importado')

for empresa in api.empresas:
    request = api.request(empresa)
    for key, value in request.items():
        value['date'] = key #Adiciono a data como um parametro para ser importado ao banco
        value['ticker'] = empresa
        obj_dto_acoesdiario = DTO_acoes_diario().input(**value)
        ServerManager().InsertData(obj_dto_acoesdiario.get_table(),**obj_dto_acoesdiario.output())
    print(f'Importanto dados sobre {empresa}')
print('Dados diario importado')
