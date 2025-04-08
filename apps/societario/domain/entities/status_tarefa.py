from django.utils import timezone

from typing import Optional
from datetime import datetime, date
from dataclasses import dataclass, field

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.tarefa import TarefaEntity
from apps.societario.domain.entities.processo import ProcessoEntity


@dataclass(kw_only=True)
class StatusTarefaEntity(EntityBase):
    TIPO_TRIBUTACAO_CHOICES = [
        'simples', 'lucro', 'real'
    ]

    processo: ProcessoEntity
    etapa: EtapaEntity
    tarefa: TarefaEntity
    concluida: bool = False
    nao_aplicavel: bool = False
    sequencia: int
    expire_at: Optional[date] = None
    tipo_tributacao: Optional[str] = None
    created_at: datetime = field(default_factory=timezone.now)
    updated_at: datetime = field(default=None)

    def __post_init__(self):
        if self.tipo_tributacao and self.tipo_tributacao not in self.TIPO_TRIBUTACAO_CHOICES:
            raise ValueError(f"Tibo de tributação inválida. Opções válidas: {', '.join(self.ESTADO_CIVIL_CHOICES)}")

    @classmethod
    def from_model(cls, model_instance) -> "StatusTarefaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)