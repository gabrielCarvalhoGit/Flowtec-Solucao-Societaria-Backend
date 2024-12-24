from typing import Optional
from django.utils import timezone
from datetime import date, datetime
from dataclasses import dataclass, field

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.endereco import EnderecoEntity
from apps.societario.domain.entities.formulario_abertura import FormularioAberturaEmpresaEntity


@dataclass(kw_only=True)
class SocioEntity(EntityBase):
    ESTADO_CIVIL_CHOICES = [
        'solteiro', 'casado', 'separado judicialmente', 'divorciado', 'viuvo'
    ]

    REGIME_CASAMENTO_CHOICES = [
        'separacao_total', 'comunhao_parcial', 'comunhao_universal', 'participacao_final'
    ]

    TIPO_ADMINISTRADOR_CHOICES = [
        'conjunto', 'isoladamente', 'nao_aplica'
    ]

    empresa: FormularioAberturaEmpresaEntity 
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
    tipo_administrador: str 
    qtd_cotas: int 
    endereco: EnderecoEntity
    created_at: datetime = field(default_factory=timezone.now)
    updated_at: datetime = field(default=None)

    def __post_init__(self):
        if self.estado_civil not in self.ESTADO_CIVIL_CHOICES:
            raise ValueError(f"Estado civil inválido para o sócio '{self.nome}'. Opções válidas: {', '.join(self.ESTADO_CIVIL_CHOICES)}")
        
        if self.regime_casamento and self.regime_casamento not in self.REGIME_CASAMENTO_CHOICES:
            raise ValueError(f"Regime de casamento inválido para o sócio '{self.nome}'. Opções válidas: {', '.join(self.REGIME_CASAMENTO_CHOICES)}")
        
        if self.tipo_administrador not in self.TIPO_ADMINISTRADOR_CHOICES: 
            raise ValueError(f"Tipo de administrador inválido para o sócio '{self.nome}'. Opções válidas: {', '.join(self.TIPO_ADMINISTRADOR_CHOICES)}")