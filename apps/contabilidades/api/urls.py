from django.urls import path
from apps.contabilidades.api.views import create_contabilidade


urlpatterns = [
    path('create-contabilidade/', create_contabilidade, name='create_contabilidade'),
]