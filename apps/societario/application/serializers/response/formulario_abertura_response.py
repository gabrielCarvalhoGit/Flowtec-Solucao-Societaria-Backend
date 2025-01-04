from rest_framework import serializers
from apps.societario.infra.models import FormularioAberturaEmpresa

from .socio_response import SocioResponseSerializer
from .endereco_response import EnderecoResponseSerializer
from .info_adicionais_response import InfoAdicionaisResponseSerializer


class FormularioAberturaResponseSerializer(serializers.ModelSerializer):
    processo = serializers.UUIDField(source='processo.id')
    endereco = EnderecoResponseSerializer()
    info_adicionais = InfoAdicionaisResponseSerializer()
    socios = SocioResponseSerializer(required=False, allow_null=True, many=True)

    class Meta:
        model = FormularioAberturaEmpresa
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation.pop('updated_at')

        endereco = representation.pop('endereco')
        if endereco:
            representation['endereco'] = endereco

        info_adicionais = representation.pop('info_adicionais')
        if info_adicionais:
            representation['info_adicionais'] = info_adicionais

        socios = representation.pop('socios')
        if not socios:
            representation['socios'] = []
        else:
            representation['socios'] = socios

        return representation