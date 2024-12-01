from django.urls import path
from .views import etapas_views, tipo_processo_views


urlpatterns = [
#     path('', societario_views.api_overview, name='api_root'),
#     path('criar-processo/', societario_views.create_process, name='create_process'),
#     path('formulario-abertura/', societario_views.update_empresa_form, name='abertura_form')
#     # path('empresa-form/', societario_views.empresa_form, name='abrir_empresa_form'),

    path('get-etapa/', etapas_views.get_etapa, name='get_etapa'),
    path('list-etapas/', etapas_views.get_list_etapas, name='list_etapas'),

    path('get-tipo-processo/', tipo_processo_views.get_tipo_processo, name='get_tipo_processo'),
    path('list-tipo-processo/', tipo_processo_views.get_list_tipo_processo, name='list_tipo_processo')
]