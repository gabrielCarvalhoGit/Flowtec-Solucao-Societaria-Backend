from rest_framework import serializers
from apps.societario.infra.models import Socios

from .endereco_request import EnderecoRequestSerializer


class SociosRequestSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100)
    nacionalidade = serializers.CharField(max_length=25)
    data_nascimento = serializers.DateField()

    estado_civil = serializers.ChoiceField(choices=Socios.ESTADO_CIVIL_CHOICES)
    regime_casamento = serializers.ChoiceField(choices=Socios.REGIME_CASAMENTO_CHOICES)

    profissao = serializers.CharField(max_length=50)

    cpf = serializers.CharField(max_length=11)
    rg = serializers.CharField(max_length=14)
    orgao_expedidor = serializers.CharField(max_length=8)
    uf = serializers.CharField(max_length=2)

    administrador = serializers.BooleanField(default=False)
    tipo_administrador = serializers.ChoiceField(choices=Socios.TIPO_ADMINISTRADOR_CHOICES)
    
    qtd_cotas = serializers.IntegerField()
    endereco = EnderecoRequestSerializer()

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)