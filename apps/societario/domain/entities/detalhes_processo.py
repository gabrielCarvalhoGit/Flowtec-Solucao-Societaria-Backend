import uuid
from typing import List, Optional
from dataclasses import dataclass
from datetime import date, datetime

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
    observacao: Optional[str] = None
    tarefas: List[StatusTarefaEntity]
    formulario_abertura_id: Optional[uuid.UUID] = None
    created_at: datetime
    expire_at: date

    def update_model(self, tarefas: List[dict]):
        ids_processo = set(tarefa.id for tarefa in self.tarefas)
        ids_tarefas = set(tarefa.get('id') for tarefa in tarefas)

        invalid_ids = ids_tarefas.difference(ids_processo)
        if invalid_ids:
            raise NotFound(f'As tarefas com os seguintes IDs não foram encontradas: {', '.join(map(str, invalid_ids))}')
        
        updated_tarefas = []
        
        for tarefa in tarefas:
            tarefa_id = tarefa.get('id')
            tarefa_processo = next((t for t in self.tarefas if t.id == tarefa_id), None)

            if tarefa_processo:
                concluida = tarefa.get('concluida', None)
                nao_aplicavel = tarefa.get('nao_aplicavel', False)
                expire_at = tarefa.get('expire_at', None)
                tipo_tributacao = tarefa.get('tipo_tributacao', None)
                index_atual = self.tarefas.index(tarefa_processo)

                if concluida and nao_aplicavel:
                    raise ValidationError('Uma tarefa não pode ser marcada como concluída e não aplicável simultaneamente.')

                if concluida:
                    if not all(t.concluida or t.nao_aplicavel for t in self.tarefas[:index_atual]):
                        raise ValidationError('O processo possui tarefas pendentes. Não é possível concluir a tarefa informada.')
                
                alterado = False

                if tarefa_processo.concluida != concluida:
                    tarefa_processo.concluida = concluida
                    alterado = True

                if tarefa_processo.nao_aplicavel != nao_aplicavel:
                    tarefa_processo.nao_aplicavel = nao_aplicavel
                    alterado = True

                if expire_at and tarefa_processo.expire_at != expire_at:
                    tarefa_processo.expire_at = expire_at
                    alterado = True

                if tipo_tributacao and tarefa_processo.tipo_tributacao != tipo_tributacao:
                    tarefa_processo.tipo_tributacao = tipo_tributacao
                    alterado = True

                if alterado:
                    self.tarefas[index_atual] = tarefa_processo
                    updated_tarefas.append(tarefa_processo)
            else:
                raise NotFound(f'Tarefa não encontrada: {str(tarefa_id)}')
        
        return updated_tarefas