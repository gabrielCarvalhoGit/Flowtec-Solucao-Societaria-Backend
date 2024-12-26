from rest_framework import serializers
from apps.societario.infra.models import Endereco


class EnderecoResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'