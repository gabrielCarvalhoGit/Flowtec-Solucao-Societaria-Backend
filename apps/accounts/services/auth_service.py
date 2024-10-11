from rest_framework.exceptions import ValidationError

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError


class AuthenticationService:
    def logout(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            raise ValidationError('Refresh token não encontrado.')
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            raise ValidationError('Token inválido.')