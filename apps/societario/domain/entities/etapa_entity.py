from dataclasses import dataclass
from apps.core.domain.entities.base_entity import EntityBase


dataclass(kw_only=True)
class EtapaEntity(EntityBase):
    nome_etapa: str