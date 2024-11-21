from rest_framework import serializers


class EnderecoRequestSerializer(serializers.Serializer):
    endereco_completo = serializers.CharField(max_length=255, required=True)
    complemento = serializers.CharField(max_length=80, required=True)
    cep = serializers.CharField(max_length=9, required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)