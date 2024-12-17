from typing import List
from datetime import date
from dataclasses import dataclass

from rest_framework.exceptions import ValidationError, NotFound

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

    def update_model(self, tarefas: List[dict]):
        ids_processo = set(tarefa.id for tarefa in self.tarefas)
        ids_tarefas = set(tarefa.get('tarefa_id') for tarefa in tarefas)

        invalid_ids = ids_tarefas.difference(ids_processo)
        if invalid_ids:
            raise NotFound(f'As tarefas com os seguintes IDs não foram encontradas: {', '.join(map(str, invalid_ids))}')
        
        updated_tarefas = []
        
        for tarefa in tarefas:
            tarefa_id = tarefa.get('tarefa_id')
            tarefa_processo = next((t for t in self.tarefas if t.id == tarefa_id), None)

            if tarefa_processo:
                concluida = tarefa.get('concluida')
                index_atual = self.tarefas.index(tarefa_processo)

                if concluida:
                    if not all(t.concluida for t in self.tarefas[:index_atual]):
                        raise ValidationError('O processo possui tarefas pendentes. Não é possível concluir a tarefa informada.')
                
                if tarefa_processo.concluida != concluida:
                    tarefa_processo.concluida = concluida
                    self.tarefas[index_atual] = tarefa_processo
                    
                    updated_tarefas.append(tarefa_processo)
            else:
                raise NotFound(f'Tarefa não encontrada: {str(tarefa_id)}')
        
        return updated_tarefas