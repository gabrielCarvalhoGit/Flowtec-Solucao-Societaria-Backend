from django.urls import path
from . import views


urlpatterns = [
    path('abrir-empresa/', views.create_empresa, name='abrir_empresa'),
]