from typing import Optional
from dataclasses import dataclass

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapa import EtapaEntity


@dataclass(kw_only=True)
class TarefaEntity(EntityBase):
    descricao: str
    etapa: EtapaEntity
    ordem: int
    obrigatoria: Optional[bool] = False

    @classmethod
    def from_model(cls, model_instance) -> "TarefaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)