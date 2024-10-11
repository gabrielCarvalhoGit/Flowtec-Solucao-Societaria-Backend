from django.utils.crypto import get_random_string

from rest_framework.exceptions import ValidationError, NotFound

from apps.accounts.models import User
from apps.accounts.repositories.user_repository import UserRepository
from apps.contabilidades.services.contabilidade_service import ContService


class UserService:
    def __init__(self):
        self.repository = UserRepository()
        self.contabilidade_service = ContService()
    
    def get_user(self, user_id=None, request=None):
        if user_id:
            try:
                user = self.repository.get_by_id(user_id)
                return user
            except User.DoesNotExist:
                raise NotFound('Usuário não encontrado.')
        else:
            return request.user
    
    def create_user(self, **validated_data):
        contabilidade_id = validated_data.get('contabilidade_id')

        if not contabilidade_id:
            raise ValidationError('Para cadastrar um usuário em uma contabilidade, é necessário informar a contabilidade associada.')
        
        if self.repository.validate_email(validated_data['email']):
            raise ValidationError('Este e-mail já está em uso.')
        
        contabilidade = self.contabilidade_service.get_contabilidade(contabilidade_id)

        validated_data['contabilidade'] = contabilidade
        validated_data['password'] = get_random_string(length=8)

        user = self.repository.create(**validated_data)
        return user
    
    def update_user(self, user_id, **validated_data):
        user = self.get_user(user_id)
        return self.repository.update(user, **validated_data)
    
    def delete_user(self, user_id):
        user = self.get_user(user_id)
        self.repository.delete(user)