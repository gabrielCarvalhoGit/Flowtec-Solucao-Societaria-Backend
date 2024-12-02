from apps.societario.infra.models import Processos
from apps.societario.domain.entities.processo_entity import ProcessoEntity


class ProcessoRepository:
    def __init__(self, model=Processos):
        self.__model = model
    
    def create(self, data: ProcessoEntity) -> Processos:
        return self.__model.objects.create(
            contabilidade=data.contabilidade,
            nome=data.nome,
            tipo_processo_id = data.tipo_processo.id,
            etapa_atual_id = data.etapa_atual.id,
            etapa_inicial_id = data.etapa_inicial.id,
            expire_at = data.expire_at
        )