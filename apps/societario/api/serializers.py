from rest_framework import serializers
from apps.societario.models import AberturaEmpresa


class AberturaEmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = AberturaEmpresa
        fields = '__all__'

class AberturaEmpresaCreateSerializer(serializers.Serializer):
    nome_primario = serializers.CharField(max_length=100)
    nome_secundario = serializers.CharField(max_length=100)
    nome_terciario = serializers.CharField(max_length=100)

    atividade_principal = serializers.CharField(max_length=150)
    cep = serializers.CharField(max_length=9)

    responsavel = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    telefone = serializers.CharField(max_length=12)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data) 