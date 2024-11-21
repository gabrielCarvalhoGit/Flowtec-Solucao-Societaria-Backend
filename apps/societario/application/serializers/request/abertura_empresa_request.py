from rest_framework import serializers

from .endereco_request import EnderecoRequestSerializer
from .info_adic_request import InfoAdicRequestSerializer


class CreateProcessRequestSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100, required=True)
    contabilidade_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)
    
class FormularioAberturaRequestSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose', write_only=True, required=True)
    etapa_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)

    opcoes_nomes_empresa = serializers.ListField(child=serializers.CharField(max_length=100), max_length=3, required=True)
    nome_fantasia = serializers.CharField(max_length=100, required=True)

    endereco = EnderecoRequestSerializer(required=True)
    inscricao_imob = serializers.CharField(max_length=20, required=True)

    telefone = serializers.CharField(max_length=12, required=True)
    email = serializers.EmailField(required=True)

    val_capital_social = serializers.DecimalField(max_digits=10, decimal_places=2, required=True)
    capital_integralizado = serializers.BooleanField(default=False)
    data_integralizacao = serializers.DateField(required=False)

    area_empresa = serializers.DecimalField(max_digits=10, decimal_places=2, required=False)
    empresa_anexa_resid = serializers.BooleanField(default=False)
    endereco_apenas_contato = serializers.BooleanField(default=False)

    info_adic = InfoAdicRequestSerializer(required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)