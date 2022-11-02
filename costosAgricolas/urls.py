from django.contrib import admin
from django.urls import path, include
from . import views

# Para cambiar titulos en modulo admin
admin.site.site_header = 'Sistema Evaluador de Costos para Mypimes Agrícolas - Módulo Administrativo '       # default: "Django Administration"
admin.site.index_title = 'Módulos y Tablas'                 # default: "Site administration"
admin.site.site_title = 'HTML title from adminsitration' # default: "Django site admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('usuarios/', include('appUsuarios.urls')),
    path('apAdmin/', include('appAdmin.urls')),

]
