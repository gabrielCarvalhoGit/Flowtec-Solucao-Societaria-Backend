from rest_framework import serializers

from apps.societario.application.serializers.request.endereco_request import EnderecoRequestSerializer
from apps.societario.application.serializers.request.info_adicionais_request import InfoAdicionaisRequestSerializer


class FormularioAberturaRequestSerializer(serializers.Serializer):
    processo_id = serializers.UUIDField(format='hex_verbose', write_only=True)
    opcoes_nome_empresa = serializers.ListField(child=serializers.CharField(max_length=120))
    nome_fantasia = serializers.CharField(max_length=120)

    endereco = EnderecoRequestSerializer()
    inscricao_imob = serializers.CharField(max_length=20)

    telefone = serializers.CharField()
    email = serializers.EmailField()

    val_capital_social = serializers.DecimalField(max_digits=10, decimal_places=2)
    capital_integralizado = serializers.BooleanField(default=True)
    data_integralizacao = serializers.DateField(required=False)

    empresa_anexa_resid = serializers.BooleanField(default=False)
    endereco_apenas_contato = serializers.BooleanField(default=False)
    area_empresa = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)

    info_adicionais = InfoAdicionaisRequestSerializer()