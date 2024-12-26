from rest_framework import serializers


class InfoAdicionaisRequestSerializer(serializers.Serializer):
    resp_tecnica = serializers.BooleanField(default=False)
    nome_responsavel = serializers.CharField(max_length=80, required=False)
    nmr_carteira_profissional = serializers.CharField(max_length=11, required=False)
    uf = serializers.CharField(max_length=2, required=False)
    area_resp = serializers.CharField(max_length=50, required=False)