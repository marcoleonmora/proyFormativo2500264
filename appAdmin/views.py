from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from .forms import CategHorasForm

from django.http import JsonResponse
import json

from .models import *

# *********************************************************************************
"""
Usa Formulario para CRUD tabla CategHoras, edita o crea un registro
"""
def editarHoras(request):

    context = {
        'nombreForm': 'Editar Horas',
        'ruta': 'categHoras',
    }

    if request.method == 'POST':
        id = int(request.POST['categoria'])
        descrip = request.POST['descripCategHora']
        recargo = request.POST['recargo']
        
        if len(descrip) > 0 and len(recargo) > 0:
            if id > 0:
                existe = CategHoras.objects.filter(id=id).exists()
                if existe:
                    regHora = CategHoras.objects.get(id=id)
                    regHora.descripCategHora = descrip
                    regHora.recargo = recargo
                    regHora.save()
                else:
                    context['alarma'] = 'El registro con PK= ' +str(id)+' no existe' 
            else: 
                regHora = CategHoras(descripCategHora=descrip, recargo=recargo)
                regHora.save() 
                context['mensaje'] = 'Registro creado' 
        else:
            context['alarma'] = 'Debe diligenciar la descripción y el recargo'   
    #--En cualquier caso...
    context['form'] = CategHorasForm()
    return render(request, 'plantillaForm.html', context)


# *********************************************************************************
"""
    Usa AJAX para enviar datos de un tipo de hora, en formato JSON
"""
def consultarHora(request):
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            #Toma la data enviada por el cliente
            data = json.load(request)
            id = data.get('id')
            #Lee el registro 
            regHora = CategHoras.objects.get(id=id)
            data = {
                'descripCategHora' : regHora.descripCategHora, 
                'recargo' : regHora.recargo,       
            }
            return JsonResponse(data)
    else:
        data = {
            'error' : 'No es AJAX',    
        }
        return JsonResponse(data)

# *********************************************************************************
"""
    Funcion para editar la tabla Insumos
"""
def editarInsumos(request):
    context = {}
    #Si es AJAX Y POST:
    is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    if is_ajax:
        if request.method == 'POST':
            #consular registro insumo
            data = json.load(request)
            id1 = data.get('id')
            regInsumo = Insumo.objects.get(id=id1)            
            #responder JSON
            data = {
                'categMaterial' : regInsumo.categMaterial.id,
                'unidadMedida'  : regInsumo.unidadMedida.id,
                'descripInsumo' : regInsumo.descripInsumo,    
            }

            return JsonResponse(data)

    #Si es POST:
    if request.method == 'POST':
        #validar datos del formulario
        id = int(request.POST['insumo_id'])
        descripInsumo = request.POST['descripInsumo']
        categ_id = int(request.POST['categ_id'])
        unidad_id = int(request.POST['unidad_id'])

        ok = True
        if len(descripInsumo) == 0:
            ok = False
        if categ_id != 0:
            regcateg = CategMaterial.objects.get(id= categ_id)
        else:
            ok = False
        if unidad_id != 0:
            regUnidad = UnidadMedida.objects.get(id= unidad_id)
        else:
            ok = False
        
        if ok:
            #Si insumo.id = 0:
            if id == 0:
                #crear registro
                regInsumo = Insumo(categMaterial= regcateg, unidadMedida= regUnidad, descripInsumo=descripInsumo)
                regInsumo.save()
            #SINO
            else:
                #modificar registro
                regInsumo = Insumo.objects.get(id=id)
                regInsumo.categMaterial = regcateg
                regInsumo.unidadMedida = regUnidad
                regInsumo.descripInsumo = descripInsumo
                regInsumo.save()
        else:
            context['alarma']= 'Por favor seleccione todos los datos.'

   
    #consultar unidades de medida
    listaUnidades = UnidadMedida.objects.all().values('id', 'descripUnidadMedida')
    #consultar categorias de material
    listaCategorias = CategMaterial.objects.all().values('id', 'descripCategMaterial')
    #consular insumos
    listaInsumos = Insumo.objects.all().values('id', 'descripInsumo', 'categMaterial__id', 'unidadMedida__id')
    #crear contexto
   
    context['unidades'] = listaUnidades
    context['categorias'] = listaCategorias
    context['insumos'] = listaInsumos

    #renderizar
    return render(request, 'insumos.html', context)

# *********************************************************************************


# *********************************************************************************


# *********************************************************************************
