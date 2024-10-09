from django.contrib import admin
from django.urls import path, include  # Asegúrate de que 'include' esté importado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('topos.urls')),  # Utiliza 'include' aquí
]

