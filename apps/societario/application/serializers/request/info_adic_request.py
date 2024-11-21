from rest_framework import serializers


class InfoAdicRequestSerializer(serializers.Serializer):
    resp_tecnica = serializers.BooleanField(default=False)
    nome_reponsavel = serializers.CharField(max_length=80, required=False)
    nmr_carteira_profissional = serializers.CharField(max_length=11, required=False)
    uf = serializers.CharField(max_length=2, required=False)
    area_resp = serializers.CharField(max_length=50, required=False)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)