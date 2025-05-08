from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.processo_application import ProcessoApplication


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_processo(request):
    application = ProcessoApplication()
    
    response = application.create(request)
    return Response({'processo': response.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_processo(request):
    application = ProcessoApplication()

    response = application.update(request)
    return Response({'detail': response}, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_processo(request):
    application = ProcessoApplication()

    response = application.delete(request)
    return Response({'detail': response}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_processo(request):
    application = ProcessoApplication()

    response = application.get(request)
    return Response({'processo': response.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_processos_etapas(request):
    application = ProcessoApplication()

    response = application.get_processos_etapas()
    return Response({'processos_por_etapa': response.data}, status=status.HTTP_200_OK)