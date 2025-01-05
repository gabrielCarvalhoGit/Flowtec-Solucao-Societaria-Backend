import uuid
from typing import Optional

from apps.societario.infra.models import Processo
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.detalhes_processo import ProcessoDetalhadoEntity


class ProcessoRepository:
    def __init__(self, model=Processo):
        self.__model = model
    
    def create(self, data: ProcessoEntity):
        self.__model.objects.create(
            id=data.id,
            contabilidade_id=data.contabilidade.id,
            nome=data.nome,
            tipo_processo_id=data.tipo_processo.id,
            etapa_id=data.etapa.id,
            created_at=data.created_at,
            expire_at=data.expire_at
        )
    
    def update(self, data: ProcessoDetalhadoEntity) -> Processo:
        return self.__model.objects.filter(id=data.id).update(etapa_id=data.etapa.id)
    
    def get_by_id(self, processo_id: uuid.UUID) -> Optional[Processo]:
        try:
            return self.__model.objects.select_related(
                'contabilidade',
                'tipo_processo',
                'etapa'
            ).prefetch_related(
                'formulario_abertura'
            ).get(id=processo_id)
        except self.__model.DoesNotExist:
            return None