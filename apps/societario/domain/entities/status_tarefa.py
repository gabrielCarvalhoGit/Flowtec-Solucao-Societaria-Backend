from datetime import datetime
from django.utils import timezone
from dataclasses import dataclass, field

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.tarefa import TarefaEntity
from apps.societario.domain.entities.processo import ProcessoEntity


@dataclass(kw_only=True)
class StatusTarefaEntity(EntityBase):
    processo: ProcessoEntity
    etapa: EtapaEntity
    tarefa: TarefaEntity
    concluida: bool = False
    nao_aplicavel: bool = False
    sequencia: int
    created_at: datetime = field(default_factory=timezone.now)
    updated_at: datetime = field(default=None)

    @classmethod
    def from_model(cls, model_instance) -> "StatusTarefaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)