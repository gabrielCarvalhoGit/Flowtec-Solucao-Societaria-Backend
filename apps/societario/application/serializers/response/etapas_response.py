from rest_framework import serializers
from apps.societario.infra.models import Etapas


class EtapasResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etapas
        fields = '__all__'