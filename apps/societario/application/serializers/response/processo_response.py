from rest_framework import serializers

from apps.societario.infra.models import Processos, Etapas
from apps.contabilidades.application.serializers.response.contabilidade_response import ContabilidadeProcessoResponseSerializer

from .etapas_response import EtapasResponseSerializer
from .tipo_processo_response import TipoProcessoResponseSerializer


class ProcessoResponseSerializer(serializers.ModelSerializer):
    contabilidade = ContabilidadeProcessoResponseSerializer()
    tipo_processo = TipoProcessoResponseSerializer()
    etapa_atual = EtapasResponseSerializer(required=False)
    etapa_inicial = EtapasResponseSerializer(required=False)
    
    class Meta:
        model = Processos
        fields = ['id', 'nome', 'contabilidade', 'tipo_processo', 'etapa_atual', 'etapa_inicial', 'expire_at', 'created_at']

class ProcessosEtapaResponseSerializer(serializers.ModelSerializer):
    processos = ProcessoResponseSerializer(many=True, required=False)
    
    class Meta:
        model = Etapas
        fields = ['id', 'nome', 'ordem', 'processos']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not representation.get('processos'):
            representation['processos'] = []
        
        return representation