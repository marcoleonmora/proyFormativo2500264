from django import forms
from .models import *
#----------------------------------------------------
class CategHorasForm(forms.Form):
    lista1= CategHoras.objects.all().values_list('id', 'descripCategHora')
    lista = [(0, 'Seleccione una categoria de Hora...'),]
    for elem in lista1:
        lista.append(elem) 

    categoria = forms.ChoiceField(choices = lista, label='Lista Categorias de Horas')
    descripCategHora = forms.CharField(label='Descripción de la Categoría')
    recargo = forms.DecimalField(label='Porcentaje de Recargo')

#----------------------------------------------------


#----------------------------------------------------