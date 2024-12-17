import uuid
from typing import List

from apps.societario.infra.models import StatusTarefa
from apps.societario.domain.entities.status_tarefa import StatusTarefaEntity


class StatusTarefaRepository:
    def __init__(self, model=StatusTarefa):
        self.__model = model

    def bulk_create(self, data: List[StatusTarefaEntity]) -> List[StatusTarefa]:
        status_tarefa_models = [
            StatusTarefa(
                processo_id=item.processo.id,
                etapa_id=item.etapa.id,
                tarefa_id=item.tarefa.id,
                concluida=item.concluida,
                sequencia=item.sequencia
            ) for item in data
        ]
        return self.__model.objects.bulk_create(status_tarefa_models)
    
    def bulk_update(self, data: List[StatusTarefaEntity]) -> List[StatusTarefa]:
        status_tarefa_models = [
            StatusTarefa(
                id=item.id,
                processo_id=item.processo.id,
                etapa_id=item.etapa.id,
                tarefa_id=item.tarefa.id,
                concluida=item.concluida,
                sequencia=item.sequencia
            ) for item in data
        ]
        return self.__model.objects.bulk_update(status_tarefa_models, ['concluida'])
    
    def interval_delete(self, processo_id: uuid.UUID, start: int, end: int):
        return self.__model.objects.filter(
            processo_id=processo_id,
            etapa__ordem__lt=start,
            etapa__ordem__gte=end
        ).delete()
    
    def filter_by_processo(self, processo_id: uuid.UUID) -> List[StatusTarefa]:
        return self.__model.objects.filter(processo_id=processo_id).select_related(
            'tarefa', 
            'etapa'
        ).order_by('etapa__ordem', 'sequencia')