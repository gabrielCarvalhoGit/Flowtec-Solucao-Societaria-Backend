from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from apps.empresas.services.empresa_service import EmpresaService
from apps.empresas.api.serializers import EmpresaSerializer, EmpresaCreateSerializer, AberturaEmpresaCreateSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_empresa(request, id):
    service = EmpresaService()

    try:
        empresa = service.get_empresa(id)
        empresa_serializer = EmpresaSerializer(empresa, many=False)

        return Response({'empresa': empresa_serializer.data}, status=status.HTTP_200_OK)
    except NotFound as e:
        return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_empresa(request):
    serializer = EmpresaCreateSerializer(data=request.data)

    if serializer.is_valid():
        service = EmpresaService()

        try:
            empresa = service.create_empresa(**serializer.validated_data)
            empresa_serializer = EmpresaSerializer(empresa, many=False)

            return Response({'empresa': empresa_serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'detail': str(e.detail[0])}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

    return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_empresa(request, id):
    service = EmpresaService()

    try:
        service.delete_empresa(id)
        return Response({'detail': 'Empresa excluida com sucesso.'}, status=status.HTTP_200_OK)
    except NotFound as e:
        return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def create_empresa_formulario(request):
    serializer = AberturaEmpresaCreateSerializer(data=request.data)

    if serializer.is_valid():
        service = EmpresaService()

        try:
            empresa = service.create_empresa_form(**serializer.validated_data)
            empresa_serializer = AberturaEmpresaCreateSerializer(empresa)

            return Response({'empresa': empresa_serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'detail': str(e.detail[0])}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

    return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    