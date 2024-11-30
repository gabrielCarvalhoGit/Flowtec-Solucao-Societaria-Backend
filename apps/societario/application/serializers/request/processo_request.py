from rest_framework import serializers


class ProcessoRequestSerializer(serializers.Serializer):
    nome = serializers.CharField(max_length=100, required=True)

    contabilidade_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)
    tipo_processo_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)
    etapa_atual_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)