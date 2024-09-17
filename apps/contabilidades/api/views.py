from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from apps.contabilidades.api.serializers import ContSerializer, ContCreateSerializer
from apps.contabilidades.services.contabilidade_service import ContService


@api_view(['POST'])
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