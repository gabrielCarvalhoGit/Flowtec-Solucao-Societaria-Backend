from rest_framework.exceptions import ValidationError

from apps.societario.domain.services.processo_service import ProcessoService
from apps.societario.application.serializers.request.processo_request import ProcessosRequestSerializer
from apps.societario.application.serializers.response.processo_response import ProcessoResponseSerializer


class ProcessosApplication:
    def __init__(self, service=ProcessoService()):
        self.__service = service
    
    def create(self, request) -> ProcessoResponseSerializer:
        serializer_request = ProcessosRequestSerializer(data=request.data)

        if serializer_request.is_valid():
            processo = self.__service.create_processo(request, **serializer_request.validated_data)
            response = ProcessoResponseSerializer(processo)

            return response

        raise ValidationError(serializer_request.errors)