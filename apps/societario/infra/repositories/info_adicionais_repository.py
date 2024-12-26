from apps.societario.infra.models import InfoAdicionais
from apps.societario.domain.entities.info_adicionais import InfoAdicionaisEntity


class InfoAdicionaisRepository:
    def __init__(self, model=InfoAdicionais):
        self.__model = model
    
    def create(self, data: InfoAdicionaisEntity):
        self.__model.objects.create(
            id=data.id,
            resp_tecnica=data.resp_tecnica,
            nome_responsavel=data.nome_responsavel,
            nmr_carteira_profissional=data.nmr_carteira_profissional,
            uf=data.uf,
            area_resp=data.area_resp
        )