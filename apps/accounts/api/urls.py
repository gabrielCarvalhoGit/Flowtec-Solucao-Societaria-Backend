from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views
from .views import MyTokenObtainPairView


urlpatterns = [
    path('', views.api_overview, name='api_root'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('create-user-admin-contabilidade/<uuid:contabilidade_id>/', views.create_user_admin_cont, name='create_user_admin_contabilidade'),
    path('create-user/', views.create_user, name='create_user'),
    path('update-user/<uuid:id>'),
]