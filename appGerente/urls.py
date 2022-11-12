
from django.urls import path
from . import views

urlpatterns = [
    path('lotes/', views.editarLotes, name='lotes'),
   

]