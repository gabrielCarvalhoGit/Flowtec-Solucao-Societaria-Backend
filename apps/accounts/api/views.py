from uuid import UUID
from django.contrib.auth import authenticate

from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.exceptions import NotFound, ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .serializers import UserSerializer, CreateUserSerializer

from apps.accounts.services.user_service import UserService


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
            raise serializers.ValidationError({'detail': 'Email ou senha inválido.'})
        
        return super().validate(attrs)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)

    if serializer.is_valid():
        service = UserService()

        try:
            user = service.create_user(**serializer.validated_data)
            user_serializer = UserSerializer(user, many=False)

            return Response({'user': user_serializer.data}, status=status.HTTP_200_OK)
        except ValidationError as e:
            return Response({'detail': str(e.detail[0])}, status=status.HTTP_400_BAD_REQUEST)
        except NotFound as e:
            return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_user(request, id):
    service = UserService()

    try:
        user = service.get_user(id)
    except NotFound as e:
        return Response({'detail': str(e.detail)}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
@permission_classes([AllowAny])
def api_overview(request):
    routes = [
        '/api/accounts/token/',
        '/api/accounts/token/refresh/',

        '/api/accounts/create-super-user/'
    ]

    return Response(routes)