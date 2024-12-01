from apps.core.services.base_service import ServiceBase
from apps.contabilidades.services.contabilidade_service import ContService

from apps.societario.domain.entities.processo_entity import ProcessoEntity
from apps.societario.infra.repositories.processo_repository import ProcessoRepository

from apps.societario.domain.services.etapas_service import EtapasService
from apps.societario.domain.services.tipo_processo_service import TipoProcessoService


class ProcessoService(metaclass=ServiceBase):
    def __init__(
            self,
            processo_repository = ProcessoRepository(),
            cont_service = ContService(),
            etapa_service = EtapasService(),
            tipo_processo_service = TipoProcessoService()
        ):

        self.__repository = processo_repository
        self.__contabilidade_service = cont_service
        self.__etapa_service = etapa_service
        self.__tipo_processo_service = tipo_processo_service
        
    def create_process(self, request, **data):
        nome = data.get('nome')

        contabilidade_id = data.get('contabilidade_id')
        tipo_processo_id = data.get('tipo_processo_id')
        etapa_id = data.get('etapa_atual_id')

        contabilidade = self.__contabilidade_service.get_contabilidade(contabilidade_id, request)
        tipo_processo = self.__tipo_processo_service.get_tipo_processo(tipo_processo_id)
        etapa = self.__etapa_service.get_etapa(etapa_id)

        response = ProcessoEntity(
            contabilidade=contabilidade,
            nome=nome,
            tipo_processo=tipo_processo,
            etapa_atual=etapa,
            etapa_inicial=etapa
        )
        processo = self.__repository.create(response)

        response.id = processo.id
        response.created_at = processo.created_at

        return response