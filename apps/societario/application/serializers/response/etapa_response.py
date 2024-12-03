from rest_framework import serializers
from apps.societario.infra.models import Etapa


class EtapaResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapa
        fields = '__all__'