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
    
    def update(self, **data):
        for field, value in data.items():
            if field not in self.__dataclass_fields__:
                continue

            setattr(self, field, value)
        
        self.__post_init__()
    
    @classmethod
    def from_model(cls, model_instance):
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}

        entity = cls(**model_data)
        entity.__post_init__()
        
        return entity