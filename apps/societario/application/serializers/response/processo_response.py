from rest_framework import serializers

from apps.societario.infra.models import Processo, Etapa
from apps.contabilidades.application.serializers.response.contabilidade_response import ContabilidadeProcessoResponseSerializer

from .etapa_response import EtapaResponseSerializer
from .tipo_processo_response import TipoProcessoResponseSerializer


class ProcessoResponseSerializer(serializers.ModelSerializer):
    contabilidade = ContabilidadeProcessoResponseSerializer()
    tipo_processo = TipoProcessoResponseSerializer()
    etapa = EtapaResponseSerializer(required=False)
    
    class Meta:
        model = Processo
        fields = ['id', 'nome', 'contabilidade', 'tipo_processo', 'etapa', 'expire_at', 'created_at']

class ProcessoEtapaResponseSerializer(serializers.ModelSerializer):
    processos = ProcessoResponseSerializer(many=True, required=False)
    
    class Meta:
        model = Etapa
        fields = ['id', 'nome', 'ordem', 'processos']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        if not representation.get('processos'):
            representation['processos'] = []
        
        for processo in representation['processos']:
            if 'etapa' in processo:
                del processo['etapa']
        
        return representation