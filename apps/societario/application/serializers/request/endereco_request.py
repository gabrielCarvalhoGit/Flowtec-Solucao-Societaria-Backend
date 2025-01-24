from rest_framework import serializers


class EnderecoRequestSerializer(serializers.Serializer):
    rua = serializers.CharField(max_length=80)
    numero = serializers.IntegerField()
    bairro = serializers.CharField(max_length=80)
    complemento = serializers.CharField(max_length=100, required=False, allow_blank=True)
    cep = serializers.CharField()
    municipio = serializers.CharField(max_length=60)
    uf = serializers.CharField(max_length=2)

class EnderecoUpdateRequestSerializer(serializers.Serializer):
    rua = serializers.CharField(max_length=80, required=False)
    numero = serializers.IntegerField(required=False)
    bairro = serializers.CharField(max_length=80, required=False)
    complemento = serializers.CharField(max_length=100, required=False, allow_blank=True)
    cep = serializers.CharField(required=False)
    municipio = serializers.CharField(max_length=60, required=False)
    uf = serializers.CharField(max_length=2, required=False)