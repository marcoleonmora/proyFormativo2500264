from asyncio.windows_events import NULL
from django.shortcuts import render
from appGerente.models import Finca
from .models import Usuarios


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
		if ok and tipoUsuario == '2':
			existe = Finca.objects.filter(correoGerente=email).exists()
			if not existe:
				context['alarma']= 'El correo no esta registrado'
			else:
				existe = Usuarios.objects.filter(email=email).exists()
				if not existe:  #Crear usuario
					regGerente = Finca.objects.get(correoGerente=email)
					username = email.split('@')[0]
					user = Usuarios.objects.create_user(first_name=regGerente.nombreGerente, 
						last_name=regGerente.apellidoGerente, username=username, email=email, password=password)
					user.phone_number = phone_number
					user.finca = regGerente
					user.rol= '2'
					user.save()
					context['mensaje']= 'Gerente registrado con exito!'
				else:
					context['alarma']= 'El usurio YA esta registrado'

	return render(request, 'usuarios/registro.html', context)

