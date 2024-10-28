from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api_root'),
    path('novo-registro/', views.iniciar_registro_empresa, name='novo_registro'),
]