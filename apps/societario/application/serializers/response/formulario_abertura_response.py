from rest_framework import serializers
from apps.societario.infra.models import FormularioAberturaEmpresa

from .endereco_response import EnderecoResponseSerializer
from .info_adicionais_response import InfoAdicionaisResponseSerializer


class FormularioAberturaResponseSerializer(serializers.ModelSerializer):
    endereco = EnderecoResponseSerializer()
    info_adicionais = InfoAdicionaisResponseSerializer()

    class Meta:
        model = FormularioAberturaEmpresa
        exclude = ['processo']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation.pop('updated_at')
        
        endereco = representation.pop('endereco')
        info_adicionais = representation.pop('info_adicionais')

        if endereco:
            representation['endereco'] = endereco
        if info_adicionais.get('resp_tecnica'):
            representation['info_adicionais'] = info_adicionais

        return representation