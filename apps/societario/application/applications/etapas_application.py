from apps.societario.domain.services.etapas_service import EtapasService
from apps.societario.application.serializers.response.etapas_response import EtapasResponseSerializer


class EtapasApplication:
    def __init__(self, service = EtapasService()):
        self.__service = service
    
    def get(self, request) -> EtapasResponseSerializer:
        id = request.query_params.get('id', None)

        etapa = self.__service.get_etapa(id)
        response = EtapasResponseSerializer(etapa)

        return response
    
    def list_etapas(self) -> EtapasResponseSerializer:
        etapas = self.__service.list_etapas()
        response = EtapasResponseSerializer(etapas, many=True)

        return response