from apps.societario.domain.services.etapas_service import EtapasService
from apps.societario.application.serializers.response.etapas_response import EtapasResponseSerializer


class EtapasApplication:
    def __init__(self, etapas_service = EtapasService()):
        self.__service = etapas_service
    
    def get(self, request) -> EtapasResponseSerializer:
        id = request.query_params.get('id', None)

        etapa = self.__service.get_etapa(id)
        response = EtapasResponseSerializer(etapa)

        return response