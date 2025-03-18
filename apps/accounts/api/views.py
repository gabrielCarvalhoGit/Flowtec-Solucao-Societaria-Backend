from django.conf import settings
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import UserSerializer, CreateUserSerializer, UpdateUserSerializer

from apps.accounts.services.user_service import UserService
from apps.accounts.services.auth_service import AuthenticationService


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email

        return token
    
    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError()
        
        return super().validate(attrs)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError:
            return Response({'detail': 'E-mail ou senha inválida.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        refresh = serializer.validated_data.get('refresh')
        access = serializer.validated_data.get('access')

        cookie_secure = settings.ENV == 'prod'
        cookie_samesite = 'None' if cookie_secure else 'Lax'

        response = Response({
            'refresh': refresh,
            'access': access
        })

        response.set_cookie(
            key='access_token',
            value=access,
            httponly=True,
            secure=cookie_secure,
            samesite=cookie_samesite
        )

        response.set_cookie(
            key='refresh_token',
            value=refresh,
            httponly=True,
            secure=cookie_secure,
            samesite=cookie_samesite
        )

        return response

class MyTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        refresh_token = request.COOKIES.get('refresh_token')

        if not refresh_token:
            return Response({"detail": "Refresh token not found in cookies."}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            refresh = RefreshToken(refresh_token)
            access = refresh.access_token

            cookie_secure = settings.ENV == 'prod'
            cookie_samesite = 'None' if cookie_secure else 'Lax'

            response = Response({
                'access': str(access)
            })

            response.set_cookie(
                key='access_token',
                value=access,
                httponly=True,
                secure=cookie_secure,
                samesite=cookie_samesite
            )

            return response
        except TokenError as e:
            raise InvalidToken(str(e))

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    service = AuthenticationService()
    service.logout(request)

    response = Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)

    response.delete_cookie('refresh_token')
    response.delete_cookie('access_token')

    return response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user(request):
    service = UserService()
    user_id = request.query_params.get('id', None)

    user = service.get_user(user_id, request)
    user_serializer = UserSerializer(user, many=False)

    return Response({'user': user_serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():
        service = UserService()

        user = service.create_user(**serializer.validated_data)
        user_serializer = UserSerializer(user, many=False)

        return Response({'user': user_serializer.data}, status=status.HTTP_200_OK)
    
    return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def update_user(request):
    service = UserService()
    user_id = request.query_params.get('id', None)

    user = service.get_user(user_id, request)
    serializer = UpdateUserSerializer(instance=user, data=request.data, partial=True)

    if serializer.is_valid():
        updated_user = service.update_user(user, **serializer.validated_data)
        user_serializer = UserSerializer(updated_user, many=False)

        return Response({'user': user_serializer.data}, status=status.HTTP_200_OK)
    
    return Response({'detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    service = UserService()
    user_id = request.query_params.get('id', None)

    service.delete_user(user_id)
    return Response({'detail': 'Usuário excluido com sucesso.'}, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_overview(request):
    routes = [
        '/api/accounts/',
        
        '/api/accounts/token/',
        '/api/accounts/token/refresh/',
        'api/accounts/token/logout/',
        
        '/api/accounts/get-user/',
        '/api/accounts/create-user/',
        '/api/accounts/update-user/',
        '/api/accounts/delete-user/'
    ]

    return Response(routes)