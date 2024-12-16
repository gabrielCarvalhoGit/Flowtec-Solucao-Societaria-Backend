from typing import List
from datetime import date
from dataclasses import dataclass

from rest_framework.exceptions import ValidationError

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

    def update_model(self, etapa: EtapaEntity | None, tarefas: List[dict]):
        if etapa:
            self.etapa = etapa
        
        ids_processo = set(tarefa.id for tarefa in self.tarefas)
        ids_tarefas = set(tarefa.get(id) for tarefa in tarefas)

        invalid_ids = ids_tarefas.difference(ids_processo)
        if invalid_ids:
            raise ValidationError(f'As tarefas com os seguintes IDs não foram encontradas: {', '.join(map(str, invalid_ids))}')
        
        for tarefa in tarefas:
            tarefa_id = tarefa.get('id')
            tarefa_processo = next((t for t in self.tarefas if t.id == tarefa_id), None)

            if tarefa_processo:
                concluida = tarefa.get('concluida')