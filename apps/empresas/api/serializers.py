from rest_framework import serializers
from apps.empresas.models import Empresa


class EmpresaSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)
    
    class Meta:
        model = Empresa
        fields = '__all__'

class EmpresaCreateSerializer(serializers.Serializer):
    cnpj = serializers.CharField(max_length=18, required=True)
    contabilidade_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=True)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data) 
    
# class AberturaEmpresaCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AberturaEmpresa
#         fields = [
#             'nome_primario', 
#             'nome_secundario', 
#             'nome_terciario', 
#             'atividade_principal', 
#             'cep', 
#             'responsavel', 
#             'email', 
#             'telefone'
#         ]

