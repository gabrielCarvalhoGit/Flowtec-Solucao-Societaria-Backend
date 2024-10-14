from rest_framework.exceptions import ValidationError, NotFound

from apps.societario.repositories.societario_repository import SocietarioRepository


class SocietarioService:
    def __init__(self):
        self.repository = SocietarioRepository()
    
    def create_empresa(self, **validated_data):
        return self.repository.create(**validated_data)