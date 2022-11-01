from django.urls import path
from . import views

urlpatterns = [
    path('horas/', views.editarHoras, name='categHoras'),
    path('hora/', views.consultarHora),
    path('insumos/', views.editarInsumos, name='insumos'),

]