from datetime import date
from dataclasses import dataclass

from apps.core.domain.entities.base_entity import EntityBase


@dataclass(kw_only=True)
class ContabilidadeEntity(EntityBase):
    cnpj: str
    data_abertura: date
    situacao: str
    tipo: str
    nome: str
    nome_fantasia: str
    porte: str
    natureza_juridica: str
    cod_atividade_principal: str
    desc_atividade_principal: str
    endereco: str
    cep: str