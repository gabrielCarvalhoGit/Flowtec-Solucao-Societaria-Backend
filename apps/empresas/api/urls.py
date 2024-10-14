from django.urls import path
from . import views


urlpatterns = [
    path('create-empresa/', views.create_empresa, name='create_empresa'),
    path('get-empresa/<uuid:id>/', views.get_empresa, name='get_empresa'),
    path('delete-empresa/<uuid:id>/', views.delete_empresa, name='delete_empresa'),
    
    #path('create-empresa-formulario/', views.create_empresa_formulario, name='create_empresa_formulario'),
]