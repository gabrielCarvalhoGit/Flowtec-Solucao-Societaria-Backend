import uuid
from typing import List
from rest_framework.exceptions import ValidationError, NotFound

from apps.core.services.base_service import ServiceBase
from apps.contabilidades.services.contabilidade_service import ContService

from apps.societario.domain.entities.processo import ProcessoEntity
from apps.societario.infra.repositories.processo_repository import ProcessoRepository

from apps.societario.domain.services.etapa_service import EtapaService
from apps.societario.domain.services.tipo_processo_service import TipoProcessoService


class ProcessoService(metaclass=ServiceBase):
    def __init__(
            self,
            processo_repository = ProcessoRepository(),
            cont_service = ContService(),
            etapa_service = EtapaService(),
            tipo_processo_service = TipoProcessoService()
        ):

        self.__repository = processo_repository
        self.__contabilidade_service = cont_service
        self.__etapa_service = etapa_service
        self.__tipo_processo_service = tipo_processo_service
        
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
        processo = self.__repository.create(response)

        response.id = processo.id
        response.created_at = processo.created_at

        return response
    
    def get_processo(self, id: uuid.UUID) -> ProcessoEntity:
        if not id:
            raise ValidationError({'processo_id': ['Parâmetro obrigatório.']})
        
        processo = self.__repository.get_by_id(id)
        if not processo:
            raise NotFound('Processo não encontrado.')
        
        return ProcessoEntity.from_model(processo)

    def list_processos_etapas(self) -> List[dict]:
        response = []
        etapas = self.__etapa_service.list_etapas()

        for etapa in etapas:
            processos = self.__repository.get_by_etapa(etapa)
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