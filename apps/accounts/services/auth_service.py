from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from apps.core.services.base_service import ServiceBase


class AuthenticationService(metaclass=ServiceBase):
    def logout(self, request):
        refresh_token = request.COOKIES.get('refresh_token')
        
        if not refresh_token:
            raise AuthenticationFailed('Refresh token não encontrado.')
        
        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
        except TokenError:
            raise AuthenticationFailed('Token inválido.')