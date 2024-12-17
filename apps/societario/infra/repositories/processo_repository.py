import uuid
from typing import Optional

from apps.societario.infra.models import Processo
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.detalhes_processo import ProcessoDetalhadoEntity


class ProcessoRepository:
    def __init__(self, model=Processo):
        self.__model = model
    
    def create(self, data: ProcessoEntity) -> Processo:
        processo = self.__model.objects.create(
            contabilidade_id=data.contabilidade.id,
            nome=data.nome,
            tipo_processo_id = data.tipo_processo.id,
            etapa_id = data.etapa.id,
            expire_at = data.expire_at
        )
        
        return processo
    
    def update(self, data: ProcessoDetalhadoEntity) -> Processo:
        return self.__model.objects.filter(id=data.id).update(etapa_id=data.etapa.id)
    
    def get_by_id(self, processo_id: uuid.UUID) -> Optional[Processo]:
        try:
            return self.__model.objects.select_related(
                'contabilidade',
                'tipo_processo',
                'etapa'
            ).get(id=processo_id)
        except self.__model.DoesNotExist:
            return None