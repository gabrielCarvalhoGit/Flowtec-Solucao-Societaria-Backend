from rest_framework.exceptions import ValidationError

from apps.societario.domain.services.socio_service import SocioService
from apps.societario.application.serializers.request.socio_request import SocioRequestSerializer
from apps.societario.application.serializers.response.socio_response import SocioResponseSerializer


class SocioApplication:
    def __init__(self, service=SocioService()):
        self.__service = service
    
    def create(self, request):
        serializer_requrest = SocioRequestSerializer(data=request.data)

        if serializer_requrest.is_valid():
            socios = self.__service.create_socios(**serializer_requrest.validated_data)
            response = SocioResponseSerializer(socios, many=True)

            return response

        raise ValidationError(serializer_requrest.errors)