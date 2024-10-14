from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/accounts/', include('apps.accounts.api.urls')),
    path('api/contabilidades/', include('apps.contabilidades.api.urls')),
    path('api/empresas/', include('apps.empresas.api.urls')),
    path('api/societario/', include('apps.societario.api.urls')),
]