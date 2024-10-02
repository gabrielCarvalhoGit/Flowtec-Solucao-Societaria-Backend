from apps.accounts.models import User


class UserRepository:
    def get_by_id(self, user_id):
        return User.objects.get(id=user_id)
    
    def create(self, **kwargs):
        return User.objects.create_user(**kwargs)
    
    def validate_email(self, email):
        return User.objects.filter(email=email).exists()