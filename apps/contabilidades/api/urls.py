from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_overview, name='api_root'),

    path('list-contabilidades/', views.get_list_contabilidades, name='list_contabilidades'),

    path('create-contabilidade/', views.create_contabilidade, name='create_contabilidade'),
    path('get-contabilidade/', views.get_contabilidade, name='get_contabilidade'),
    path('delete-contabilidade/<uuid:id>/', views.delete_contabilidade, name='delete_contabilidade'),
]