import uuid
from typing import List
from rest_framework.exceptions import ValidationError

from apps.core.services.base_service import ServiceBase

from apps.societario.domain.entities.tarefa_entity import TarefaEntity
from apps.societario.infra.repositories.tarefa_repository import TarefaRepository


class TarefaService(metaclass=ServiceBase):
    def __init__(
            self,
            repository = TarefaRepository()
        ):
        
        self.__repository = repository
    
    def list_tarefas_etapa(self, etapa_id: uuid.UUID) -> List[TarefaEntity]:
        tarefas = self.__repository.list_tarefas_by_etapa(etapa_id)

        if not tarefas:
            raise ValidationError('Nenhuma tarefa encontrada para a etapa informada.')
        
        return [TarefaEntity.from_model(tarefa) for tarefa in tarefas]