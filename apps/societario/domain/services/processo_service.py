import uuid
from typing import List
from django.db import transaction
from rest_framework.exceptions import NotFound, ValidationError

from apps.core.services.base_service import ServiceBase
from apps.contabilidades.services.contabilidade_service import ContService

from apps.societario.domain.services.etapa_service import EtapaService
from apps.societario.domain.services.tipo_processo_service import TipoProcessoService
from apps.societario.domain.services.status_tarefa_service import StatusTarefaService

from apps.societario.infra.repositories.etapa_repository import EtapaRepository
from apps.societario.infra.repositories.processo_repository import ProcessoRepository

from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.domain.entities.detalhes_processo import ProcessoDetalhadoEntity


class ProcessoService(metaclass=ServiceBase):
    def __init__(
            self,
            repository = ProcessoRepository(),
            etapa_repository = EtapaRepository(),
            cont_service = ContService(),
            etapa_service = EtapaService(),
            tipo_processo_service = TipoProcessoService(),
            status_tarefa_service = StatusTarefaService()
        ):

        self.__repository = repository
        self.__etapa_repository = etapa_repository
        self.__contabilidade_service = cont_service
        self.__etapa_service = etapa_service
        self.__tipo_processo_service = tipo_processo_service
        self.__status_tarefa_service = status_tarefa_service

    def get_processo(self, id: uuid.UUID):
        if not id:
            raise ValidationError({'processo_id': ['Parâmetro obrigatório.']})
        
        processo = self.__repository.get_by_id(id)
        if not processo:
            raise NotFound('Processo não encontrado.')
        
        return ProcessoEntity(
            id=processo.id,
            contabilidade=processo.contabilidade,
            nome=processo.nome,
            tipo_processo=processo.tipo_processo,
            etapa=processo.etapa,
            observacao=processo.observacao,
            created_at=processo.created_at,
            expire_at=processo.expire_at
        )
    
    @transaction.atomic
    def get_detalhes_processo(self, id: uuid.UUID) -> ProcessoDetalhadoEntity:
        if not id:
            raise ValidationError({'processo_id': ['Parâmetro obrigatório.']})
        
        processo = self.__repository.get_by_id(id)
        if not processo:
            raise NotFound('Processo não encontrado.')
        
        status_tarefas = self.__status_tarefa_service.filter_status_tarefas_processo(processo)
        return ProcessoDetalhadoEntity(
            id=processo.id,
            contabilidade=processo.contabilidade,
            nome=processo.nome,
            tipo_processo=processo.tipo_processo,
            etapa=processo.etapa,
            observacao=processo.observacao,
            tarefas=status_tarefas,
            formulario_abertura_id=processo.formulario_abertura.id if hasattr(processo, 'formulario_abertura') else None,
            created_at=processo.created_at,
            expire_at=processo.expire_at
        )

    @transaction.atomic
    def create_processo(self, request, **data) -> ProcessoEntity:
        nome = data.get('nome')

        contabilidade_id = data.get('contabilidade_id')
        tipo_processo_id = data.get('tipo_processo_id')
        etapa_id = data.get('etapa_id')

        contabilidade = self.__contabilidade_service.get_contabilidade(contabilidade_id, request)
        tipo_processo = self.__tipo_processo_service.get_tipo_processo(tipo_processo_id)
        etapa = self.__etapa_service.get_etapa(etapa_id)

        response = ProcessoEntity(
            contabilidade=contabilidade,
            nome=nome,
            tipo_processo=tipo_processo,
            etapa=etapa
        )
        
        self.__repository.create(response)
        self.__status_tarefa_service.create_tarefas(response, etapa)

        return response

    @transaction.atomic
    def update_processo(self, **data) -> ProcessoDetalhadoEntity:
        processo_id = data.get('processo_id')
        etapa_id = data.get('etapa_id', None)
        tarefas = data.get('tarefas', None)
        observacao = data.get('observacao', None)

        processo = self.get_detalhes_processo(processo_id)
        etapa = self.__etapa_service.get_etapa(etapa_id) if etapa_id else None

        if tarefas:
            validated_tarefas = processo.update_model(tarefas)
            self.__status_tarefa_service.update_status_tarefas(validated_tarefas)

        if etapa:
            if etapa.ordem < processo.etapa.ordem:
                self.__status_tarefa_service.delete_status_tarefas(processo)
            elif etapa.ordem > processo.etapa.ordem:
                if processo.etapa.ordem == 4:
                    tarefas_obrigatorias = [t for t in processo.tarefas if t.tarefa.obrigatoria]
                    tarefas_nao_concluidas = [t for t in tarefas_obrigatorias if not t.concluida and not t.nao_aplicavel]
                    
                    if tarefas_nao_concluidas:
                        raise ValidationError({
                            'tarefas': 'Não é possível avançar para a próxima etapa. Existem tarefas obrigatórias que não foram concluídas ou marcadas como não aplicáveis.'
                        })
                
                self.__status_tarefa_service.create_tarefas(processo, etapa)
            
            processo.etapa = etapa
            self.__repository.update_etapa(processo)
        
        if observacao:
            processo.observacao = observacao
            self.__repository.create_observacao(processo)
    
    def delete_proceso(self, id) -> None:
        if not self.__repository.exists_by_id(id):
            raise NotFound('Processo não encontrado.')

        self.__repository.delete(id)

    def list_processos_etapas(self) -> List[dict]:
        response = []
        etapas = self.__etapa_repository.list_processos_by_etapa()

        for etapa in etapas:
            processos = etapa.processos.all()
            processos_entities = [ProcessoEntity.from_model(processo) for processo in processos]

            etapa_data = {
                "id": etapa.id,
                "nome": etapa.nome,
                "ordem": etapa.ordem,
            }

            if processos_entities:
                etapa_data['processos'] = processos_entities
            
            response.append(etapa_data)
        
        return response