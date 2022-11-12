from django.shortcuts import render
from .models import *

# Create your views here.
def editarLotes(request):
    regFinca = request.user.finca

    #consultar lotes
    listaLotes = Lote.objects.filter(finca=regFinca)
    print('---------------------')
    print(regFinca)
    print(listaLotes)
    return render(request, 'home.html')

