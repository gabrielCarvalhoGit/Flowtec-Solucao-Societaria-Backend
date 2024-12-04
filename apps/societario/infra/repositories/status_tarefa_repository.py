from apps.societario.infra.models import StausTarefa
from apps.societario.domain.entities.status_tarefa_entity import StatusTarefaEntity


class StatusTarefaRepository:
    def __init__(self, model=StausTarefa):
        self.__model = model