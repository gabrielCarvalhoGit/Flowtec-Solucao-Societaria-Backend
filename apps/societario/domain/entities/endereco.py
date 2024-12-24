import re
import uuid
from dataclasses import dataclass, field
from apps.core.domain.entities.base_entity import EntityBase


@dataclass(kw_only=True)
class EnderecoEntity:
    id: uuid.UUID = field(default_factory=uuid.uuid4)
    rua: str
    numero: int
    bairro: str
    complemento: str
    cep: str
    municipio: str
    uf: str

    def __post_init__(self):
        regex = re.compile(r'^\d{5}-?\d{3}$')
        if not regex.fullmatch(self.cep):
            raise ValueError('O formato do CEP informado é inválido.')
        
        self.cep = self.cep.replace('-', '')