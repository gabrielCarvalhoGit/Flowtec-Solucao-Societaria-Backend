from typing import Optional
from dataclasses import dataclass
from rest_framework.exceptions import ValidationError

from apps.core.domain.entities.base_entity import EntityBase


@dataclass(kw_only=True)
class InfoAdicionaisEntity(EntityBase):
    resp_tecnica: bool
    nome_responsavel: Optional[str] = None
    nmr_carteira_profissional: Optional[str] = None
    uf: Optional[str] = None
    area_resp: Optional[str] = None

    def __post_init__(self):
        if self.resp_tecnica:
            if not all([self.nome_responsavel, self.nmr_carteira_profissional, self.uf, self.area_resp]):
                raise ValidationError("Todos os campos devem ser preenchidos quando 'resp_tecnica' é True.")
        else:
            if any([self.nome_responsavel, self.nmr_carteira_profissional, self.uf, self.area_resp]):
                raise ValidationError("Todos os campos devem estar vazios quando 'resp_tecnica' é False.")
    
    def update(self, **data):
        for field, value in data.items():
            if field not in self.__dataclass_fields__:
                continue

            if field == 'resp_tecnica' and value == False:
                self.id = None

            setattr(self, field, value)
        
        self.__post_init__()
    
    @classmethod
    def from_model(cls, model_instance):
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}

        entity = cls(**model_data)
        entity.__post_init__()
        
        return entity