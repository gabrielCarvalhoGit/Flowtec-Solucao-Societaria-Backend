from rest_framework.exceptions import ValidationError

from apps.societario.domain.services.formulario_abertura_service import FormularioAberturaService
from apps.societario.application.serializers.request.formulario_abertura_request import FormularioAberturaRequestSerializer
from apps.societario.application.serializers.response.formulario_abertura_response import FormularioAberturaResponseSerializer


class FormularioAberturaApplication:
    def __init__(self, service=FormularioAberturaService()):
        self.__service = service
    
    def create(self, request):
        serializer_request = FormularioAberturaRequestSerializer(data=request.data)

        if serializer_request.is_valid():
            form = self.__service.create_form(**serializer_request.validated_data)
            response = FormularioAberturaResponseSerializer(form)

            return response

        raise ValidationError(serializer_request.errors)
    
    def get(self, request):
        id = request.query_params.get('form_id', None)

        form = self.__service.get_form(id)
        response = FormularioAberturaResponseSerializer(form)

        return response