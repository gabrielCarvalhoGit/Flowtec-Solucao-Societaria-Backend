from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.abertura_empresa_application import AberturaEmpresaApplication


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_process(request):
    application = AberturaEmpresaApplication()

    response = application.create(request)
    return Response({'process': response.data}, status=status.HTTP_200_OK)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_empresa_form(request):
    application = AberturaEmpresaApplication()

    response = application.formulario_abertura(request)
    return Response({'empresa': response.data}, status=status.HTTP_200_OK)

# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def empresa_form(request):
#     serializer = FormularioEmpresaSerializer(data=request.data)

#     if serializer.is_valid():
#         return Response({'formulário': serializer.validated_data}, status=status.HTTP_200_OK)
    
#     return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])

def api_overview(request):
    routes = [
        '/api/societario/',
        '/api/societario/novo-registro/',
    ]
    return Response(routes)