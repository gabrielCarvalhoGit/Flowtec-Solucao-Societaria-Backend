from rest_framework import serializers
from apps.contabilidades.models import Contabilidade

class ContSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contabilidade
        fields = '__all__'

class ContCreateSerializer(serializers.Serializer):
    cnpj = serializers.CharField(max_length=18, required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)