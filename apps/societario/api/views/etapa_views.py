# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view, permission_classes

# from apps.societario.api.serializers import EtapaSerializer
# from apps.societario.services.etapa_processo_service import EtapaProcessoService


# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_etapa(request):
#     service = EtapaProcessoService()
#     etapa_id = request.query_params.get('id')

#     etapa = service.get_etapa(etapa_id)
#     serializer = EtapaSerializer(etapa, many=False)

#     return Response({'etapa': serializer.data}, status=status.HTTP_200_OK)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def get_list_etapas(request):
#     service = EtapaProcessoService()

#     etapas = service.get_list_etapas()
#     serializer = EtapaSerializer(etapas, many=True)

#     return Response({'etapas': serializer.data}, status=status.HTTP_200_OK)