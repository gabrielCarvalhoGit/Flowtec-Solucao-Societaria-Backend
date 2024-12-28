from rest_framework import serializers

from apps.societario.infra.models import Socio
from apps.societario.application.serializers.response.endereco_response import EnderecoResponseSerializer

class SocioResponseSerializer(serializers.ModelSerializer):
    endereco = EnderecoResponseSerializer()

    class Meta:
        model = Socio
        exclude = ['empresa']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        endereco = representation.pop('endereco')
        if endereco:
            representation['endereco'] = endereco

        return representation