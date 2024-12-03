import uuid
from typing import Optional, List

from apps.societario.infra.models import Processo
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.etapa import EtapaEntity


class ProcessoRepository:
    def __init__(self, model=Processo):
        self.__model = model
    
    def create(self, data: ProcessoEntity) -> Processo:
        return self.__model.objects.create(
            contabilidade=data.contabilidade,
            nome=data.nome,
            tipo_processo_id = data.tipo_processo.id,
            etapa_atual_id = data.etapa_atual.id,
            etapa_inicial_id = data.etapa_inicial.id,
            expire_at = data.expire_at
        )
    
    def get_by_id(self, id: uuid.UUID) -> Optional[Processo]:
        try:
            return self.__model.objects.get(id=id)
        except self.__model.DoesNotExist:
            return None
    
    def get_by_etapa(self, etapa: EtapaEntity) -> List[Processo]:
        return self.__model.objects.filter(etapa_atual_id=etapa.id)
