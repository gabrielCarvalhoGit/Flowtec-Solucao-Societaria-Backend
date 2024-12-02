from django.urls import path
from .views import etapas_views, tipo_processo_views, processo_views


urlpatterns = [
    path('create-processo/', processo_views.create_processo, name='create_processo'),

    path('get-etapa/', etapas_views.get_etapa, name='get_etapa'),
    path('list-etapas/', etapas_views.get_list_etapas, name='list_etapas'),

    path('get-tipo-processo/', tipo_processo_views.get_tipo_processo, name='get_tipo_processo'),
    path('list-tipo-processo/', tipo_processo_views.get_list_tipo_processo, name='list_tipo_processo')
]