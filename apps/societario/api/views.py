from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.decorators import api_view, permission_classes

from .serializers import RegistroInicialSerializer
from apps.societario.services.societario_service import SocietarioService


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def iniciar_registro_empresa(request):
    service = SocietarioService()
    contabilidade_id = request.query_params.get('contabilidade_id', None)

    try:
        registro_empresa = service.registrar_empresa(contabilidade_id, request)
        serializer = RegistroInicialSerializer(registro_empresa, many=False)

        return Response({'registro_inicial': serializer.data}, status=status.HTTP_200_OK)
    except NotFound as e:
        return Response({'detail', str(e.detail)}, status=status.HTTP_404_NOT_FOUND)
    except ValidationError as e:
        return Response({'detail', str(e.detail)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_overview(request):
    routes = [
        '/api/societario/',
        '/api/societario/novo-registro/',
    ]
    return Response(routes)