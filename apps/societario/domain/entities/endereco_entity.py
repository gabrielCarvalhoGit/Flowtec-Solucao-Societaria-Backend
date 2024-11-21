import re
from dataclasses import dataclass

from apps.core.domain.entities.base_entity import EntityBase


@dataclass(kw_only=True)
class EnderecoEntity(EntityBase):
    endereco_completo: str
    complemento: str
    cep: str

    def __post_init__(self):
        regex = re.compile(r'^\d{5}-?\d{3}$')

        if not regex.match(self.cep):
            raise ValueError('O formato do CEP informado é inválido.')
        
        self.cep = self.cep.replace('-', '')