from rest_framework import serializers
from apps.societario.infra.models import AberturaEmpresa


class CreateProcessResponseSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)
    
    class Meta:
        model = AberturaEmpresa
        fields = ['id', 'nome', 'contabilidade', 'expire_at', 'created_at']

class FormularioAberturaResponseSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)

    class Meta:
        model = AberturaEmpresa
        fields = '__all__'