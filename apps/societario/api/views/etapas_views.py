from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.etapas_application import EtapasApplication


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_etapa(request):
    application = EtapasApplication()

    response = application.get(request)
    return Response({'etapa': response.data}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_list_etapas(request):
#     service = EtapaProcessoService()

#     etapas = service.get_list_etapas()
#     serializer = EtapaSerializer(etapas, many=True)

#     return Response({'etapas': serializer.data}, status=status.HTTP_200_OK)