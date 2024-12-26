from rest_framework import serializers
from apps.societario.infra.models import InfoAdicionais


class InfoAdicionaisResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoAdicionais
        fields = '__all__'