from django.utils.crypto import get_random_string
from apps.accounts.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def create_super_user(self, **kwargs):
        password_temp = get_random_string(length=8)

        kwargs['is_custom_superuser'] = True
        kwargs['password'] = password_temp

        user = self.repository.create(**kwargs)
        return user