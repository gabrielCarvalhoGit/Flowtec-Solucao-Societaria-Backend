from django.urls import path
from . import views


urlpatterns = [
    path('create-empresa/', views.create_empresa, name='create_empresa')
]