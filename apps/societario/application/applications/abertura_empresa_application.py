from rest_framework.exceptions import ValidationError

from apps.societario.application.serializers.request.abertura_empresa_request import CreateProcessRequestSerializer, FormularioAberturaRequestSerializer
from apps.societario.application.serializers.response.abertura_empresa_response import CreateProcessResponseSerializer, FormularioAberturaResponseSerializer

from apps.societario.domain.services.societario_service import AberturaEmpresaService


class AberturaEmpresaApplication:
    def __init__(self, service=AberturaEmpresaService()):
        self.__service = service
    
    def create(self, request) -> CreateProcessResponseSerializer:
        serializer_request = CreateProcessRequestSerializer(data=request.data)

        if serializer_request.is_valid():
            empresa = self.__service.create_empresa(request, **serializer_request.validated_data)
            serializer_response = CreateProcessResponseSerializer(empresa)

            return serializer_response
        
        raise ValidationError(serializer_request.errors)
    
    def formulario_abertura(self, request):
        serializer_request = FormularioAberturaRequestSerializer(data=request.data)

        if serializer_request.is_valid():
            empresa = self.__service.formulario_abertura(**serializer_request.validated_data)
            serializer_response = FormularioAberturaResponseSerializer(empresa)

            return serializer_response
        
        raise ValidationError(serializer_request.errors)