import re
import uuid
from typing import Optional
from dataclasses import dataclass, field
from apps.core.domain.entities.base_entity import EntityBase


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
        regex = re.compile(r'^\d{5}-?\d{3}$')
        if not regex.fullmatch(self.cep):
            raise ValueError('O formato do CEP informado é inválido.')
        
        self.cep = self.cep.replace('-', '')