from asyncio.windows_events import NULL
from django.shortcuts import render, redirect
from appGerente.models import *
from .models import Usuarios

from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def registrarse(request):
	context = {
		'titulo': 'registro',
		'nombreForm': 'Formulario de Registro',
	}

	if request.method == 'POST':
		tipoUsuario = request.POST['tipoUsuario']
		email = request.POST['email']
		password = request.POST['password']
		confirm_password = request.POST['confirmPassword']
		phone_number = request.POST['phone_number']

		user = NULL
        # VALIDACION DE CAMPOS
		ok = True
		if password != confirm_password:
			context['alarma']= '¡El password no coincide!'
			ok = False
		if not password or len(password) < 5:
			context['alarma']= 'Ingrese un password de 5 o mas caracteres'
			ok = False
		if not email:
			context['alarma']= 'Ingrese el correo electrónico'
			ok = False

		
		if ok:  #Hasta aca, todos los datos bien...
			username = email.split('@')[0]
			if tipoUsuario == '2':  #Gerente de finca, buscar en fincas
				existe = Finca.objects.filter(correoGerente=email).exists()
				if not existe:
					context['alarma']= 'El correo no esta registrado'
				else:
					existe = Usuarios.objects.filter(email=email).exists()
					if not existe:  #Crear usuario
						regGerente = Finca.objects.get(correoGerente=email)
						user = Usuarios.objects.create_user(first_name=regGerente.nombreGerente, 
							last_name=regGerente.apellidoGerente, username=username, email=email, password=password)
						user.phone_number = phone_number
						user.finca = regGerente
						user.rol= '2'
						user.save()
						context['mensaje']= 'Gerente registrado con exito!'
						return redirect('login')
					else:
						context['alarma']= 'El usuario YA esta registrado'

			elif tipoUsuario == '3': # Asistente de finca, buscar en 
				existe = Trabajador.objects.filter(emailTrabajador=email, rol= '1').exists()
				if not existe:
					context['alarma']= 'El correo no esta registrado'
				else:
					existe = Usuarios.objects.filter(email=email).exists()
					if not existe:  #Crear usuario
						regTrabajador = Trabajador.objects.get(emailTrabajador=email)
						#Buscar la finca
						regFinca = regTrabajador.finca


						user = Usuarios.objects.create_user(first_name=regTrabajador.nombreTrabajador, 
							last_name=regTrabajador.nombreTrabajador, username=username, email=email, password=password)
						user.phone_number = phone_number
						user.finca = regFinca
						user.rol= '3'
						user.save()
						context['mensaje']= 'Asistente registrado con exito!'
						return redirect('login')
					else:
						context['alarma']= 'El usuario YA esta registrado'
			else:
				context['alarma']= 'Registro no permitido'


	return render(request, 'usuarios/registro.html', context)

#******** CONTROL DE INGRESO DE USUARIOS  ***********************************************************
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, 'usuarios/login.html', {'alarma': 'Correo o password no valido!'})
    else:
        return render(request, 'usuarios/login.html')


#********* DESACTIVACION DEL USUARIO **********************************************************
@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

