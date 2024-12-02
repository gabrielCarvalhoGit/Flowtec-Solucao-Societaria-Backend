from rest_framework import serializers
from apps.societario.infra.models import Processos


class ProcessoResponseSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)
    tipo_processo = serializers.CharField(source='tipo_processo.descricao', read_only=True)
    etapa_atual = serializers.CharField(source='etapa_atual.nome', read_only=True)
    etapa_inicial = serializers.CharField(source='etapa_inicial.nome', read_only=True)
    
    class Meta:
        model = Processos
        fields = ['id', 'nome', 'contabilidade', 'tipo_processo', 'etapa_atual', 'etapa_inicial', 'expire_at', 'created_at']