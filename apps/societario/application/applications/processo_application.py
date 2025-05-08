from rest_framework.exceptions import ValidationError

from apps.societario.domain.services.processo_service import ProcessoService
from apps.societario.application.serializers.request.processo_request import ProcessoRequestSerializer
from apps.societario.application.serializers.request.status_tarefa_request import StatusTarefaRequestSerializer
from apps.societario.application.serializers.response.processo_response import ProcessoResponseSerializer, ProcessoEtapaResponseSerializer


class ProcessoApplication:
    def __init__(self, service=ProcessoService()):
        self.__service = service
    
    def create(self, request) -> ProcessoResponseSerializer:
        serializer_request = ProcessoRequestSerializer(data=request.data)

        if serializer_request.is_valid():
            processo = self.__service.create_processo(request, **serializer_request.validated_data)
            response = ProcessoResponseSerializer(processo)

            return response

        raise ValidationError(serializer_request.errors)
    
    def update(self, request) -> ProcessoResponseSerializer:
        serializer_request = StatusTarefaRequestSerializer(data=request.data)

        if serializer_request.is_valid():
            self.__service.update_processo(**serializer_request.validated_data)

            response = 'OK'
            return response

        raise ValidationError(serializer_request.errors)
    
    def delete(self, request) -> str:
        process_id = request.query_params.get('id', None)

        if process_id:
            self.__service.delete_proceso(process_id)
            return 'Processo excluído com sucesso.'

        raise ValidationError('Id do processo é obrigatório.')

    def get(self, request):
        id = request.query_params.get('processo_id', None)

        processo = self.__service.get_detalhes_processo(id)
        response = ProcessoResponseSerializer(processo)

        return response
    
    def get_processos_etapas(self) -> ProcessoEtapaResponseSerializer:
        processos_etapas = self.__service.list_processos_etapas()
        
        response = ProcessoEtapaResponseSerializer(processos_etapas, many=True)
        return response