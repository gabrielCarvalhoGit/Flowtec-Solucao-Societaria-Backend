from django.urls import path

from . import views
from .views import MyTokenObtainPairView, MyTokenRefreshView


urlpatterns = [
    path('', views.api_overview, name='api_root'),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('token/refresh/', MyTokenRefreshView.as_view(), name='token_refresh'),
    path('token/logout/', views.logout_user, name='logout_user'),

    path('get-user/', views.get_user, name='get_user'),
    path('create-user/', views.create_user, name='create_user'),
    path('update-user/', views.update_user, name='update_user'),
    path('delete-user/', views.delete_user, name='delete_user'),
]