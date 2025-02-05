from rest_framework import serializers
from apps.societario.application.serializers.request.endereco_request import EnderecoRequestSerializer


class SocioInfoSerializer(serializers.Serializer):
    id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)
    nome = serializers.CharField(max_length=100)
    nacionalidade = serializers.CharField(max_length=25)
    data_nascimento = serializers.DateField()
    estado_civil = serializers.CharField(max_length=10)
    regime_casamento = serializers.CharField(max_length=20, required=False, allow_blank=True)
    profissao = serializers.CharField(max_length=50)
    cpf = serializers.CharField()
    rg = serializers.CharField(max_length=14)
    orgao_expedidor = serializers.CharField(max_length=8)
    uf = serializers.CharField(max_length=2)
    administrador = serializers.BooleanField(default=True)
    tipo_administrador = serializers.CharField(max_length=15, required=False, allow_blank=True)
    qtd_cotas = serializers.IntegerField()
    endereco = EnderecoRequestSerializer()

class SocioRequestSerializer(serializers.Serializer):
    empresa_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)
    socios = serializers.ListField(child=SocioInfoSerializer())

    def validate(self, data):
        if self.partial:
            if 'empresa_id' not in data:
                raise serializers.ValidationError({'empresa_id': ['Este campo é obrigatório.']})

            socios = data.get('socios', [])
            if isinstance(socios, dict):
                socios = [socios]

            errors = {}
            for index, socio in enumerate(socios):
                if 'id' not in socio:
                    errors[f'socio[{index}].id'] = ['Este campo é obrigatório.']
            
            if errors:
                raise serializers.ValidationError(errors)

        return data