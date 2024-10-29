from apps.accounts.models import User


class UserRepository:
    def get_by_id(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None

    def create(self, **validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, user, **validated_data):
        if 'profile_picture' in validated_data:
            if validated_data['profile_picture'] is None:
                user.profile_picture.delete(save=False)
                user.profile_picture = None
                
        for key, value in validated_data.items():
            setattr(user, key, value)
        
        user.save()
        return user

    def delete(self, user):
        user.delete()

    def exists_by_email(self, email):
        return User.objects.filter(email=email).exists()