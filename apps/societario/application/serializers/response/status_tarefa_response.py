from rest_framework import serializers
from apps.societario.infra.models import StatusTarefa

from apps.societario.application.serializers.response.etapa_response import EtapaResponseSerializer
from apps.societario.application.serializers.response.tarefa_response import TarefaResponseSerializer


class StatusTarefaResponseSerializer(serializers.ModelSerializer):
        etapa = EtapaResponseSerializer()
        tarefa = TarefaResponseSerializer()

        class Meta:
                model = StatusTarefa
                fields = ['id', 'etapa', 'tarefa', 'concluida', 'sequencia', 'nao_aplicavel']