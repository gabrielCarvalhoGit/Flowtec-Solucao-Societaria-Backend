import re
import uuid
from typing import Optional
from django.utils import timezone
from datetime import date, datetime
from dataclasses import dataclass, field

from rest_framework.exceptions import ValidationError

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.endereco import EnderecoEntity
from apps.societario.domain.validators.validator import cpf_validate


@dataclass(kw_only=True)
class SocioEntity(EntityBase):
    ESTADO_CIVIL_CHOICES = [
        'solteiro', 'casado', 'separado', 'divorciado', 'viuvo'
    ]

    REGIME_CASAMENTO_CHOICES = [
        'separacao_total', 'comunhao_parcial', 'comunhao_universal', 'participacao_final'
    ]

    TIPO_ADMINISTRADOR_CHOICES = [
        'conjunto', 'isoladamente', 'nao_aplica'
    ]

    empresa_id: uuid.UUID
    nome: str 
    nacionalidade: str 
    data_nascimento: date 
    estado_civil: str 
    regime_casamento: Optional[str] = None 
    profissao: str 
    cpf: str 
    rg: str 
    orgao_expedidor: str
    uf: str 
    administrador: bool = True 
    tipo_administrador: Optional[str] = None
    qtd_cotas: int 
    endereco: EnderecoEntity
    created_at: datetime = field(default_factory=timezone.now)
    updated_at: datetime = field(default=None)

    def __post_init__(self):
        self.cpf = cpf_validate(self.cpf)
        self.rg = re.sub(r'\D', '', self.rg)
        self.endereco = EnderecoEntity(**self.endereco)
        
        if self.estado_civil not in self.ESTADO_CIVIL_CHOICES:
            raise ValueError(f"Estado civil inválido para o sócio '{self.nome}'. Opções válidas: {', '.join(self.ESTADO_CIVIL_CHOICES)}")
        elif self.estado_civil == 'casado' and not self.regime_casamento:
            raise ValidationError("O campo 'regime_casamento' é obrigatório quando o sócio é casado.")
        elif self.estado_civil != 'casado' and self.regime_casamento:
            raise ValidationError("O campo 'regime_casamento' deve ser vazio quando o sócio não é casado.")
        elif self.regime_casamento and self.regime_casamento not in self.REGIME_CASAMENTO_CHOICES:
            raise ValueError(f"Regime de casamento inválido para o sócio '{self.nome}'. Opções válidas: {', '.join(self.REGIME_CASAMENTO_CHOICES)}")
        
        if self.administrador and not self.tipo_administrador:
            raise ValidationError("Quando 'administrador' é true, o campo 'tipo_administrador' é obrigatório.")
        elif not self.administrador and self.tipo_administrador:
            raise ValidationError("Quando 'administrador' é false, o campo 'tipo_administrador' deve ser vazio.")
        elif self.tipo_administrador and self.tipo_administrador not in self.TIPO_ADMINISTRADOR_CHOICES: 
            raise ValueError(f"Tipo de administrador inválido para o sócio '{self.nome}'. Opções válidas: {', '.join(self.TIPO_ADMINISTRADOR_CHOICES)}")