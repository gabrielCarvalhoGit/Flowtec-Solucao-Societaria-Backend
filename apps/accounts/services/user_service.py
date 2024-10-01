from django.utils.crypto import get_random_string

from rest_framework.exceptions import ValidationError

from apps.accounts.repositories.user_repository import UserRepository
from apps.contabilidades.services.contabilidade_service import ContService


class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.contabilidade_service = ContService()
    
    def create_user(self, request, **validated_data):
        if validated_data['is_admin_contabilidade'] and not validated_data['contabilidade_id']:
            raise ValidationError('')

        if self.repository.validate_email(validated_data['email']):
            raise ValidationError('Este e-mail já está em uso.')

    def create_user_admin_cont(self, contabilidade_id, **validated_data):
        if self.repository.validate_email(validated_data['email']):
            raise ValidationError('Este e-mail já está em uso.')
        
        contabilidade = self.contabilidade_service.get_contabilidade(contabilidade_id)

        validated_data['contabilidade'] = contabilidade
        validated_data['is_admin_contabilidade'] = True
        validated_data['password'] = get_random_string(length=8)

        user = self.repository.create(**validated_data)
        return user