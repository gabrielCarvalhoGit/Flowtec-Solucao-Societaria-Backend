from typing import List
from rest_framework.exceptions import NotFound

from apps.core.services.base_service import ServiceBase

from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.tarefa import TarefaEntity
from apps.societario.infra.repositories.tarefa_repository import TarefaRepository


class TarefaService(metaclass=ServiceBase):
    def __init__(
            self,
            repository = TarefaRepository()
        ):
        
        self.__repository = repository
    
    def filter_tarefas_etapa(self, etapa: EtapaEntity) -> List[TarefaEntity]:
        tarefas = self.__repository.filter_tarefas(etapa.id)

        if not tarefas:
            raise NotFound('Nenhuma tarefa encontrada para a etapa informada.')
        
        return [TarefaEntity.from_model(tarefa) for tarefa in tarefas]