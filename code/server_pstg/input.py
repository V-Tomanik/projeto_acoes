from code.data_intake.alpha_vantage_api import AvDaily
from code.data_intake.scrapper import Crawler
from code.server_pstg.config_server import ServerManager
from code.dto.dto_info_empresas import DTO_info_empresas


api = AvDaily()
g_api = api.run(api.empresas)
scrap = Crawler()
g_scrap = scrap.run(scrap.empresas)
list_dto = [DTO_info_empresas().input(**next(g_scrap)).output() for i in range(len(scrap))]
print(list_dto[1])

