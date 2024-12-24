from django.utils import timezone
from dataclasses import dataclass, field
from datetime import date, datetime, timedelta

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.tipo_processo import TipoProcessoEntity

from apps.contabilidades.domain.entities.contabilidade_entity import ContabilidadeEntity


@dataclass(kw_only=True)
class ProcessoEntity(EntityBase):
    contabilidade: ContabilidadeEntity
    nome: str
    tipo_processo: TipoProcessoEntity
    etapa: EtapaEntity
    created_at: datetime = field(default_factory=timezone.now)
    expire_at: date = None

    def __post_init__(self):
        if self.expire_at is None:
            self.expire_at = timezone.localdate() + timedelta(days=90)
    
    @classmethod
    def from_model(cls, model_instance) -> "ProcessoEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)