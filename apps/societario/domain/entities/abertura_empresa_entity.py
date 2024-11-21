from decimal import Decimal
from typing import Optional, List
from dataclasses import dataclass
from datetime import date, timedelta

from django.utils import timezone
from rest_framework.exceptions import ValidationError

from .etapa_entity import EtapaEntity
from .socios_entity import SocioEntity
from .endereco_entity import EnderecoEntity
from .info_adic_entity import InfoAdicEntity

from apps.core.domain.entities.base_entity import EntityBase
from apps.contabilidades.domain.entities.contabilidade_entity import ContabilidadeEntity


@dataclass(kw_only=True)
class AberturaEmpresaEntity(EntityBase):
    contabilidade: ContabilidadeEntity
    etapa: Optional[EtapaEntity]

    nome: str
    opcoes_nomes_empresa: Optional[List[str]]
    nome_fantasia: Optional[str]

    endereco: Optional[EnderecoEntity]
    inscricao_imob: Optional[str]

    telefone: Optional[str]
    email: Optional[str]

    val_capital_social: Optional[Decimal]
    capital_integralizado: Optional[bool]
    data_integralizacao: Optional[date]

    area_empresa: Optional[Decimal]
    empresa_anexa_resid: Optional[bool]
    endereco_apenas_contato: Optional[bool]

    info_adic: Optional[InfoAdicEntity]
    expire_at: date

    @classmethod
    def new(cls, nome: str, contabilidade: ContabilidadeEntity) -> "AberturaEmpresaEntity":
        expire_at = timezone.localdate() + timedelta(days=90)

        return cls(
            nome=nome,
            contabilidade=contabilidade,
            expire_at=expire_at
        )
    
    @classmethod
    def validate_form(cls, self, **kwargs):
        endereco = EnderecoEntity(**kwargs['endereco'])
        kwargs['endereco'] = endereco

        if not kwargs['capital_integralizado'] and not kwargs.get('data_integralizacao'):
            raise ValidationError("Quando o capital não será totalmente integralizado, o campo 'data_integralizacao' é obrigatório.")
        
        if kwargs['endereco_apenas_contato']:
            kwargs['area_empresa'] = None
        
        info_adic = InfoAdicEntity(**kwargs['info_adic'])
        kwargs['info_adic'] = info_adic

        return {k: v for k, v in kwargs.items() if hasattr(self, k)}

    @classmethod
    def from_model(cls, model_instance) -> "AberturaEmpresaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}
        return cls(**model_data)