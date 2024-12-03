from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.etapa_application import EtapaApplication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_etapa(request):
    application = EtapaApplication()

    response = application.get(request)
    return Response({'etapa': response.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_etapas(request):
    application = EtapaApplication()

    response = application.list_etapas()
    return Response({'etapas': response.data}, status=status.HTTP_200_OK)