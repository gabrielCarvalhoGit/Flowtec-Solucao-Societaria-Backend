from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class TokenRefreshMiddleware(MiddlewareMixin):
    def process_request(self, request):
        access_token = request.COOKIES.get('access_token')
        refresh_token = request.COOKIES.get('refresh_token')

        if access_token:
            if not self.is_token_valid(access_token):
                if refresh_token:
                    try:
                        refresh = RefreshToken(refresh_token)
                        new_access_token = str(refresh.access_token)

                        response = self.get_response(request)
                        response.set_cookie(
                            key='access_token',
                            value=new_access_token,
                            httponly=True,
                            secure=True,
                            samesite='None'
                        )
                        return response
                    except TokenError:
                        return JsonResponse({'detail': 'Sessão expirada.'}, status=401)
                else:
                    return JsonResponse({'detail': 'Autenticação necessária'}, status=401)
                
        return self.get_response(request)
    
    def is_token_valid(self, token):
        try:
            AccessToken(token)
            return True
        except TokenError:
            return False