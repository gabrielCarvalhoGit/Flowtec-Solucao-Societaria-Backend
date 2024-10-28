from rest_framework import serializers
from apps.societario.models import AberturaEmpresa


class RegistroInicialSerializer(serializers.ModelSerializer):
    class Meta:
        model = AberturaEmpresa
        fields = ['nome', 'created_at', 'expire_at', 'contabilidade', 'etapa']