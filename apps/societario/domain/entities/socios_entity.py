from dataclasses import dataclass
from typing import Optional
from datetime import date

from .endereco_entity import EnderecoEntity


class EstadoCivil:
    ESTADO_CIVIL_CHOICES = [
        ('solteiro', 'Solteiro'),
        ('casado', 'Casado'),
        ('separado', 'Separado judicialmente'),
        ('divorciado', 'Divorciado'),
        ('viuvo', 'Viúvo')
    ]
    
    def __init__(self, estado_civil: str):
        if estado_civil not in dict(self.ESTADO_CIVIL_CHOICES):
            raise ValueError(f"Estado civil inválido: {estado_civil}")
        self.estado_civil = estado_civil

class RegimeCasamento:
    REGIME_CASAMENTO_CHOICES = [
        ('separacao_total', 'Separação total de bens'),
        ('comunhao_parcial', 'Comunhão parcial de bens'),
        ('comunhao_universal', 'Comunhão universal de bens'),
        ('participacao_final', 'Participação final nos aquestos')
    ]
    
    def __init__(self, regime_casamento: Optional[str] = None):
        if regime_casamento and regime_casamento not in dict(self.REGIME_CASAMENTO_CHOICES):
            raise ValueError(f"Regime de casamento inválido: {regime_casamento}")
        self.regime_casamento = regime_casamento

class TipoAdministrador:
    TIPO_ADMINISTRADOR_CHOICES = [
        ('conjunto', 'Conjunto'),
        ('isoladamente', 'Isoladamente'),
        ('nao_aplica', 'Não se aplica')
    ]
    
    def __init__(self, tipo_administrador: str):
        if tipo_administrador not in dict(self.TIPO_ADMINISTRADOR_CHOICES):
            raise ValueError(f"Tipo de administrador inválido: {tipo_administrador}")
        self.tipo_administrador = tipo_administrador

@dataclass(kw_only=True)
class SocioEntity:
    nome: str
    nacionalidade: str
    data_nascimento: date
    estado_civil: EstadoCivil
    regime_casamento: Optional[RegimeCasamento]
    profissao: str
    cpf: str
    rg: str
    orgao_expedidor: str
    uf: str
    administrador: bool
    tipo_administrador: TipoAdministrador
    qtd_cotas: int
    endereco: EnderecoEntity