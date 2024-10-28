from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api_root'),

    path('create-empresa/', views.create_empresa, name='create_empresa'),
    path('get-empresa/<uuid:id>/', views.get_empresa, name='get_empresa'),
    path('delete-empresa/<uuid:id>/', views.delete_empresa, name='delete_empresa'),
]