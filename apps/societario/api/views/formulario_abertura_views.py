from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.formulario_abertura_application import FormularioAberturaApplication


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_form(request):
    application = FormularioAberturaApplication()

    response = application.create(request)
    return Response({'formulario': response.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_form(request):
    application = FormularioAberturaApplication()

    response = application.get(request)
    return Response({'formulario': response.data}, status=status.HTTP_200_OK)