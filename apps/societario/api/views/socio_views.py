from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.socio_application import SocioApplication


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_socios(request):
    application = SocioApplication()

    response = application.create(request)
    return Response({'socios': response.data}, status=status.HTTP_200_OK)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_socios(request):
    application = SocioApplication()

    response = application.update(request)
    return Response({'socios': response.data}, status=status.HTTP_200_OK)