from typing import Optional
from dataclasses import dataclass, field

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.tarefa_entity import TarefaEntity


@dataclass(kw_only=True)
class StatusTarefaEntity(EntityBase):
    processo: ProcessoEntity
    etapa: EtapaEntity

    tarefa: TarefaEntity
    concluida: Optional[bool] = field(default=False)
    sequencia = int

    @classmethod
    def from_model(cls, model_instance) -> "StatusTarefaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)