from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.tipo_processo_application import TipoProcessoApplication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_tipo_processo(request):
    application = TipoProcessoApplication()

    response = application.get(request)
    return Response({'tipo_processo': response.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_tipo_processo(request):
    application = TipoProcessoApplication()

    response = application.list_tipo_processo()
    return Response({'tipo_processo': response.data}, status=status.HTTP_200_OK)