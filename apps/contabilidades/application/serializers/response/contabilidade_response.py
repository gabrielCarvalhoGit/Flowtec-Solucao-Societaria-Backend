from rest_framework import serializers
from apps.contabilidades.models import Contabilidade


class ContabilidadeProcessoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contabilidade
        fields = ['id', 'cnpj', 'nome']