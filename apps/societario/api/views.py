from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from apps.societario.services.societario_service import SocietarioService
from apps.societario.api.serializers import AberturaEmpresaSerializer, AberturaEmpresaCreateSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_empresa(request):
    serializer = AberturaEmpresaCreateSerializer(data=request.data)

    if serializer.is_valid():
        service = SocietarioService()

        try:
            empresa = service.create_empresa(**serializer.validated_data)
            empresa_serializer = AberturaEmpresaSerializer(empresa)

            return Response({'empresa': empresa_serializer.data}, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            return Response({'detail': str(e.detail[0])}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

    return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)