from apps.societario.domain.services.etapa_service import EtapaService
from apps.societario.application.serializers.response.etapa_response import EtapaResponseSerializer


class EtapaApplication:
    def __init__(self, service = EtapaService()):
        self.__service = service
    
    def get(self, request) -> EtapaResponseSerializer:
        id = request.query_params.get('etapa_id', None)

        etapa = self.__service.get_etapa(id)
        response = EtapaResponseSerializer(etapa)

        return response
    
    def list_etapas(self) -> EtapaResponseSerializer:
        etapas = self.__service.list_etapas()
        response = EtapaResponseSerializer(etapas, many=True)

        return response