from rest_framework_simplejwt.authentication import JWTAuthentication


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        auth_cookie = request.COOKIES.get('access_token')
        if auth_cookie:
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {auth_cookie}'

        return super().authenticate(request)