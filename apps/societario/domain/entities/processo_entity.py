from dataclasses import dataclass
from django.utils import timezone
from datetime import date, timedelta

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapas_entity import EtapasEntity
from apps.societario.domain.entities.tipo_processo_entity import TipoProcessoEntity

from apps.contabilidades.domain.entities.contabilidade_entity import ContabilidadeEntity


@dataclass(kw_only=True)
class ProcessoEntity(EntityBase):
    contabilidade: ContabilidadeEntity
    nome: str

    tipo_processo: TipoProcessoEntity
    etapa_atual: EtapasEntity
    etapa_inicial: EtapasEntity

    expire_at: date

    def __post_init__(self):
        if not self.expire_at:
            self.expire_at = timezone.localdate() + timedelta(days=90)