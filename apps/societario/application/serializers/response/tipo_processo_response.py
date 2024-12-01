from rest_framework import serializers
from apps.societario.infra.models import TipoProcesso


class TipoProcessoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProcesso
        fields = '__all__'