from django.urls import path
from .views import (etapa_views, 
                    tipo_processo_views, 
                    processo_views, 
                    formulario_abertura_views,
                    socio_views)


urlpatterns = [
    path('create-processo/', processo_views.create_processo, name='create_processo'),
    path('update-processo/', processo_views.update_processo, name='update_processo'),
    path('get-processo/', processo_views.get_processo, name='get_processo'),
    path('list-processos-etapas/', processo_views.list_processos_etapas, name='list_processos_etapas'),

    path('get-etapa/', etapa_views.get_etapa, name='get_etapa'),
    path('list-etapas/', etapa_views.get_list_etapas, name='list_etapas'),

    path('get-tipo-processo/', tipo_processo_views.get_tipo_processo, name='get_tipo_processo'),
    path('list-tipo-processo/', tipo_processo_views.get_list_tipo_processo, name='list_tipo_processo'),

    path('create-form-abertura/', formulario_abertura_views.create_form, name='create_form'),
    path('update-form-abertura/', formulario_abertura_views.update_form, name='update_form'),
    path('get-form-abertura/', formulario_abertura_views.get_form, name='get_form'),
    path('create-socios/', socio_views.create_socios, name='create_socios')
]