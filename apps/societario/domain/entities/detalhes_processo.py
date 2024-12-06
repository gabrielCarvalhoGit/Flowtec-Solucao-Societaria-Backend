from typing import List
from datetime import date
from dataclasses import dataclass

from apps.core.domain.entities.base_entity import EntityBase
from apps.societario.domain.entities.etapa import EtapaEntity
from apps.societario.domain.entities.tipo_processo import TipoProcessoEntity
from apps.societario.domain.entities.status_tarefa import StatusTarefaEntity

from apps.contabilidades.domain.entities.contabilidade_entity import ContabilidadeEntity


@dataclass(kw_only=True)
class ProcessoDetalhadoEntity(EntityBase):
    contabilidade: ContabilidadeEntity
    nome: str
    tipo_processo: TipoProcessoEntity
    etapa: EtapaEntity
    tarefas: List[StatusTarefaEntity]
    expire_at: date