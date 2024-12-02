from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from apps.societario.application.applications.processo_application import ProcessosApplication


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_processo(request):
    application = ProcessosApplication()
    
    response = application.create(request)
    return Response({'processo': response.data}, status=status.HTTP_200_OK)