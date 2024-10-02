from apps.accounts.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    contabilidade = serializers.CharField(source='contabilidade.nome', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'contabilidade', 'is_admin_contabilidade', 'date_joined']

class CreateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, required=True)
    last_name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)

    contabilidade_id = serializers.UUIDField(format='hex_verbose', write_only=True, required=False)
    is_admin_contabilidade = serializers.BooleanField(default=False)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)
    
class UpdateUserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=50, required=False)
    last_name = serializers.CharField(max_length=100, required=False)

    def to_internal_value(self, data):
        allowed_fields = set(self.fields.keys())

        for field in data:
            if field not in allowed_fields:
                raise serializers.ValidationError({field: 'Parâmetro inválido.'})
            
        return super().to_internal_value(data)