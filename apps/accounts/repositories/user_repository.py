from apps.accounts.models import User


class UserRepository:
    def create(self, **kwargs):
        return User.objects.create_user(**kwargs)