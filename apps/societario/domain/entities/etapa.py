from dataclasses import dataclass
from apps.core.domain.entities.base_entity import EntityBase


@dataclass(kw_only=True)
class EtapaEntity(EntityBase):
    nome: str
    ordem: int

    @classmethod
    def from_model(cls, model_instance) -> "EtapaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)