from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from apps.contabilidades.api.serializers import ContSerializer, ContCreateSerializer
from apps.contabilidades.services.contabilidade_service import ContService


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_contabilidade(request, id):
    service = ContService()

    try:
        contabilidade = service.get_contabilidade(id)
        cont_serializer = ContSerializer(contabilidade, many=False)

        return Response({'contabilidade': cont_serializer.data}, status=status.HTTP_200_OK)
    except NotFound as e:
        return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_list_contabilidades(request):
    pass

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_contabilidade(request):
    serializer = ContCreateSerializer(data=request.data)

    if serializer.is_valid():
        service = ContService()

        try: 
            contabilidade = service.create_cont(**serializer.validated_data)
            cont_serializer = ContSerializer(contabilidade, many=False)

            return Response({'contabilidade': cont_serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'detail': str(e.detail[0])}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'detail': serializer.errors}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_contabilidade(request, id):
    service = ContService()

    try:
        service.delete_cont(id)
        return Response({'detail': 'Contabilidade excluida com sucesso.'}, status=status.HTTP_200_OK)
    except NotFound as e:
        return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    routes = [
        
        '/api/contabilidades/get-contabilidade/',
        '/api/contabilidades/create-contabilidade/',
    ]

    return Response(routes)