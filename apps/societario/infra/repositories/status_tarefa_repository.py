import uuid
from typing import List

from apps.societario.infra.models import StatusTarefa
from apps.societario.domain.entities.status_tarefa import StatusTarefaEntity


class StatusTarefaRepository:
    def __init__(self, model=StatusTarefa):
        self.__model = model

    def bulk_create(self, data: List[StatusTarefaEntity]) -> List[StatusTarefa]:
        model_instances = [
            self.__model(
                id=item.id,
                processo_id=item.processo.id,
                etapa_id=item.etapa.id,
                tarefa_id=item.tarefa.id,
                concluida=item.concluida,
                nao_aplicavel=item.nao_aplicavel,
                sequencia=item.sequencia,
                created_at=item.created_at
            ) for item in data
        ]
        self.__model.objects.bulk_create(model_instances)
    
    def bulk_update(self, data: List[StatusTarefaEntity]) -> List[StatusTarefa]:
        status_tarefa_models = [
            self.__model(
                id=item.id,
                processo_id=item.processo.id,
                etapa_id=item.etapa.id,
                tarefa_id=item.tarefa.id,
                concluida=item.concluida,
                nao_aplicavel=item.nao_aplicavel,
                sequencia=item.sequencia
            ) for item in data
        ]
        return self.__model.objects.bulk_update(status_tarefa_models, ['concluida', 'nao_aplicavel'])
    
    def delete(self, processo_id: uuid.UUID, etapa_id: uuid.UUID):
        return self.__model.objects.filter(
            processo_id=processo_id,
            etapa_id=etapa_id
        ).delete()
    
    def filter_by_processo(self, processo_id: uuid.UUID) -> List[StatusTarefa]:
        return self.__model.objects.filter(processo_id=processo_id).select_related(
            'tarefa', 
            'etapa'
        ).order_by('etapa__ordem', 'sequencia')