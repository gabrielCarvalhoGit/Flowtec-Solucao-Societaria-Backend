from decimal import Decimal
from typing import List, Optional
from django.utils import timezone
from datetime import date, datetime
from dataclasses import dataclass, field

from rest_framework.exceptions import ValidationError
from apps.societario.domain.validators.validator import phone_number_validate

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.socio import SocioEntity
from apps.societario.domain.entities.endereco import EnderecoEntity
from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.info_adicionais import InfoAdicionaisEntity


@dataclass(kw_only=True)
class FormularioAberturaEmpresaEntity(EntityBase):
    processo: ProcessoEntity
    opcoes_nome_empresa: List[str]
    nome_fantasia: str
    endereco: EnderecoEntity
    inscricao_imob: str
    telefone: str
    email: str
    val_capital_social: Decimal
    capital_integralizado: bool = True
    data_integralizacao: Optional[date] = None
    empresa_anexa_resid: bool = False
    endereco_apenas_contato: bool = False
    area_empresa: Decimal = None
    info_adicionais: InfoAdicionaisEntity
    socios: Optional[List[SocioEntity]] = None
    created_at: datetime = field(default_factory=timezone.now)
    updated_at: datetime = field(default=None)

    def __post_init__(self):
        self.telefone = phone_number_validate(self.telefone)
        
        if len(self.opcoes_nome_empresa) != 3:
            raise ValidationError("O campo 'opcoes_nome_empresa' deve conter três opções de nome.")
        
        if not self.capital_integralizado and not self.data_integralizacao:
            raise ValidationError("O campo 'data_integralizacao' é obrigatório quando o capital não será totalmente integralizado.")
        
        if self.endereco_apenas_contato and self.area_empresa is not None: 
            raise ValidationError("Quando 'endereco_apenas_contato' é True, o campo 'area_empresa' deve ser vazio.") 
        elif not self.endereco_apenas_contato and self.area_empresa is None: 
            raise ValidationError("Quando 'endereco_apenas_contato' é False, o campo 'area_empresa' é obrigatório.")
    
    @classmethod
    def from_model(cls, model_instance) -> "FormularioAberturaEmpresaEntity":
        model_data = {field.name: getattr(model_instance, field.name) for field in model_instance._meta.fields}

        if model_instance.socios.exists():
            model_data['socios'] = model_instance.socios.all()
        else:
            model_data['socios'] = None
        
        entity = cls(**model_data)
        entity.__post_init__()
        
        return entity