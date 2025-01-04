from rest_framework import serializers


class InfoAdicionaisRequestSerializer(serializers.Serializer):
    resp_tecnica = serializers.BooleanField(default=False)
    nome_responsavel = serializers.CharField(max_length=80, required=False, allow_blank=True)
    nmr_carteira_profissional = serializers.CharField(max_length=11, required=False, allow_blank=True)
    uf = serializers.CharField(max_length=2, required=False, allow_blank=True)
    area_resp = serializers.CharField(max_length=50, required=False, allow_blank=True)