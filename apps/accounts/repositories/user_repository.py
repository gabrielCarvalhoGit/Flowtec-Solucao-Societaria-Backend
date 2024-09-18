from apps.accounts.models import User


class UserRepository:
    def create(self, **kwargs):
        return User.objects.create_user(**kwargs)
    
    def validate_email(self, email):
        return User.objects.filter(email=email).exists()