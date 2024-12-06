import uuid
from typing import List
from apps.societario.infra.models import Tarefa


class TarefaRepository():
    def __init__(self, model=Tarefa):
        self.__model = model
    
    def filter_tarefas(self, etapa_id: uuid.UUID) -> List[Tarefa]:
        return self.__model.objects.filter(etapa_id=etapa_id).order_by('ordem')