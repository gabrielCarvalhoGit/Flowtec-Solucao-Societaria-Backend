from rest_framework.exceptions import AuthenticationFailed

from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        if not hasattr(request, 'new_token'):
            auth_cookie = request.COOKIES.get('access_token')
            if auth_cookie:
                request.META['HTTP_AUTHORIZATION'] = f'Bearer {auth_cookie}'
        
        try:
            return super().authenticate(request)
        except InvalidToken:
            raise AuthenticationFailed('Invalid or expired token.')