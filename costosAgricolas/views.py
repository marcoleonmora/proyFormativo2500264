from django.shortcuts import render

def home(request):
    context = {
        'titulo': 'SECMA',
        'nombreForm': 'Página de inicio'
    }
    return render(request, 'home.html', context)

