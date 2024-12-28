import re
from typing import Optional
from dataclasses import dataclass, field

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.validators.validator import cep_validate


@dataclass(kw_only=True)
class EnderecoEntity(EntityBase):
    rua: str
    numero: int
    bairro: str
    complemento: Optional[str] = field(default=None)
    cep: str
    municipio: str
    uf: str

    def __post_init__(self):
        self.cep = cep_validate(self.cep)