import uuid
from typing import List
from rest_framework.exceptions import NotFound

from apps.core.services.base_service import ServiceBase
from apps.societario.domain.services.tarefa_service import TarefaService

from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.status_tarefa import StatusTarefaEntity

from apps.societario.infra.repositories.status_tarefa_repository import StatusTarefaRepository


class StatusTarefaService(metaclass=ServiceBase):
    def __init__(
            self,
            repository = StatusTarefaRepository(),
            tarefa_service = TarefaService()
        ):
        
        self.__repository = repository
        self.__tarefa_service = tarefa_service
    
    def create_tarefas(self, processo: ProcessoEntity, etapa: EtapaEntity):
        tarefas = self.__tarefa_service.filter_tarefas_etapa(etapa)

        status_tarefas = [
            StatusTarefaEntity(
                processo=processo,
                etapa=etapa,
                tarefa=tarefa,
                sequencia=tarefa.ordem
            ) for tarefa in tarefas
        ]
        return self.__repository.bulk_create(status_tarefas)
    
    def filter_status_tarefas_processo(self, processo_id: uuid.UUID) -> List[StatusTarefaEntity]:
        status_tarefas = self.__repository.filter_status_tarefas(processo_id)

        if not status_tarefas:
            raise NotFound('Nenhuma tarefa encontrada para o processo informado.')
        
        return [StatusTarefaEntity.from_model(status_tarefa) for status_tarefa in status_tarefas]