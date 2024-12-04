import uuid
from typing import List
from apps.societario.infra.models import Tarefa


class TarefaRepository():
    def __init__(self, model=Tarefa):
        self.__model = model
    
    def list_tarefas_by_etapa(self, etapa_id: uuid.UUID) -> List[Tarefa]:
        return self.__model.objects.filter(etapa_id=etapa_id).order_by('ordem')