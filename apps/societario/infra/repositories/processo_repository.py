from apps.societario.infra.models import Processo
from apps.societario.domain.entities.processo_entity import ProcessoEntity


class ProcessoRepository:
    def __init__(self, model=Processo):
        self.__model = model
    
    def create(self, data: ProcessoEntity) -> Processo:
        return self.__model.objects.create(
            contabilidade=data.contabilidade,
            nome=data.nome,
            tipo_processo = data.tipo_processo,
            etapa_atual = data.etapa_atual,
            etapa_inicial = data.etapa_inicial,
            expire_at = data.expire_at
        )