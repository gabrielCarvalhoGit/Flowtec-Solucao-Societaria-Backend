from apps.societario.domain.services.tipo_processo_service import TipoProcessoService
from apps.societario.application.serializers.response.tipo_processo_response import TipoProcessoResponseSerializer


class TipoProcessoApplication:
    def __init__(self, service=TipoProcessoService()):
        self.__service = service
    
    def get(self, request) -> TipoProcessoResponseSerializer:
        id = request.query_params.get('id', None)

        tipo_processo = self.__service.get_tipo_processo(id)
        response = TipoProcessoResponseSerializer(tipo_processo)

        return response
    
    def list_tipo_processo(self) -> TipoProcessoResponseSerializer:
        tipos_processo = self.__service.list_tipo_processo()
        response = TipoProcessoResponseSerializer(tipos_processo, many=True)

        return response