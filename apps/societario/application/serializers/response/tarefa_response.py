from rest_framework import serializers
from apps.societario.infra.models import Tarefa

from apps.societario.application.serializers.response.etapa_response import EtapaResponseSerializer


class TarefaResponseSerializer(serializers.ModelSerializer):
    etapa = EtapaResponseSerializer()

    class Meta:
        model = Tarefa
        fields = ['id', 'descricao', 'etapa', 'obrigatoria']