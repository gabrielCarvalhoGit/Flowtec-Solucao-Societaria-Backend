from typing import Optional
from dataclasses import dataclass, field
from rest_framework.exceptions import ValidationError

from apps.core.domain.entities.base_entity import EntityBase


@dataclass(kw_only=True)
class InfoAdicEntity(EntityBase):
    resp_tecnica: bool
    nome_reponsavel: Optional[str] = field(default=None)
    nmr_carteira_profissional: Optional[str] = field(default=None)
    uf: Optional[str] = field(default=None)
    area_resp: Optional[str] = field(default=None)

    def __post_init__(self):
        if not self.resp_tecnica:
            self.nome_reponsavel = None
            self.nmr_carteira_profissional = None
            self.uf = None
            self.area_resp = None
        else:
            if not all([self.nome_reponsavel, self.nmr_carteira_profissional, self.uf, self.area_resp]):
                raise ValidationError('Quando a atividade da filial necessita de responsabilidade técnica, todos os campos devem ser preenchidos.')