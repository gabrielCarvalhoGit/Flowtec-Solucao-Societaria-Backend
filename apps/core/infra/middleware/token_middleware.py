from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class TokenRefreshMiddleware(MiddlewareMixin):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if access_token and not self.is_token_valid(access_token):
            if refresh_token:
                try:
                    refresh = RefreshToken(refresh_token)
                    new_access_token = str(refresh.access_token)

                    request.META['HTTP_AUTHORIZATION'] = f'Bearer {new_access_token}'
                    request.new_token = new_access_token
                except TokenError:
                    return JsonResponse({'detail': 'Session expired.'}, status=401)
            else:
                return JsonResponse({'detail': 'Authentication required.'}, status=401)
        
        response = self.get_response(request)

        if hasattr(request, 'new_token'):
            response.set_cookie(
                key='access_token',
                value=request.new_token,
                httponly=True,
                secure=True,
                samesite='None'
            )
        return response
    
    def is_token_valid(self, token):
        try:
            AccessToken(token)
            return True
        except TokenError:
            return False