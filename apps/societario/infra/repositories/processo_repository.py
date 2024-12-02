import uuid
from typing import Optional, List

from apps.societario.infra.models import Processos
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.etapas import EtapasEntity


class ProcessoRepository:
    def __init__(self, model=Processos):
        self.__model = model
    
    def create(self, data: ProcessoEntity) -> Processos:
        return self.__model.objects.create(
            contabilidade=data.contabilidade,
            nome=data.nome,
            tipo_processo_id = data.tipo_processo.id,
            etapa_atual_id = data.etapa_atual.id,
            etapa_inicial_id = data.etapa_inicial.id,
            expire_at = data.expire_at
        )
    
    def get_by_id(self, id: uuid.UUID) -> Optional[Processos]:
        try:
            return self.__model.objects.get(id=id)
        except self.__model.DoesNotExist:
            return None
    
    def get_by_etapa(self, etapa: EtapasEntity) -> List[Processos]:
        return self.__model.objects.filter(etapa_atual_id=etapa.id)
