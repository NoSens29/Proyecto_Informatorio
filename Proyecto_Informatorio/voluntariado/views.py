from django.shortcuts import render, HttpResponse, redirect

from django.template import loader

from .models import Actividad,  Contacto, Person

from .forms import PersonaForm, MiUsuarioCreationForm, ActividadForm

from django.contrib.auth import authenticate

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login as do_login

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User


# Create your views here.
def home(request):
	num_voluntarios = Person.objects.filter(voluntario=True).count() #del modelo de Persona cuento todos los que están como voluntarios
	num_favores = Actividad.objects.count() #del modelo de Actividad cuento todas las actividades cargadas
	num_faltantes = Actividad.objects.filter(realizada=False).count()

	return render(request, "voluntariado/home.html",context={'num_voluntarios':num_voluntarios,'num_favores':num_favores,'num_faltantes':num_faltantes})
'''
def registrar_voluntario(request):
	if request.POST:
		POST = request.POST
		nuevo_registro = Persona(dni=POST['dni'], nombre=POST['name'],
			apellido=POST['surname'], telefono=POST['phone'], mail=POST['email'], direccion=POST['adress'], voluntario=POST['voluntary'], 
			administrador=POST['admin'], solicitante=POST['solicitant'], contrasenia=POST['password'],usuario=POST['username']) 
		nuevo_registro.save()
		
	return render(request, 'voluntariado/voluntario.html')

def registrar_persona(request):
	form = PersonaForm
	return render(request, 'voluntariado/persona_new.html', {'form': form})

def registrar_solicitante(request):
	if request.POST:
		POST = request.POST
		nuevo_registro = Persona(dni=POST['dni'], nombre=POST['name'],
			apellido=POST['surname'], telefono=POST['phone'], mail=POST['email'], direccion=POST['adress'], voluntario=POST['voluntary'], administrador=POST['admin'], solicitante=POST['solicitant'], contrasenia=['password']) 
		nuevo_registro.save()

	return render(request, 'voluntariado/solicitante.html')

def registro(request):
	return render(request, 'voluntariado/registro.html')

def login(request):
	if request.POST:
		data = request.POST
		user = data['username']
		password = data['password']
		try:
			persona = Persona.objects.get(usuario=user)
			if password == persona.contrasenia:
				return redirect('Home')
		except:
			pass
	return render(request, 'voluntariado/login.html')
'''
def Historiadefavores(request):
	return render(request,'voluntariado/Historiadefavores.html')



def donaciones(request):
	return render(request,"voluntariado/donaciones.html")


def login2(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('Home')

    # Si llegamos al final renderizamos el formulario
    return render(request, "voluntariado/login2.html", {'form': form})
'''
def registro_miusuario(request):
	# Creamos el formulario de autenticación vacío
	form = MiUsuarioCreationForm()
	if request.method == "POST":
		# Añadimos los datos recibidos al formulario
		form = MiUsuarioCreationForm(data=request.POST)
		# Si el formulario es válido...
		if form.is_valid():
			# Creamos la nueva cuenta de usuario
			user = form.save()
			# Si el usuario se crea correctamente
			if user is not None:
				# Hacemos el login manualmente
				do_login(request, user)
				# Y le redireccionamos a la portada
				return redirect('/')
	# Si llegamos al final renderizamos el formulario
	return render(request, "voluntariado/registro_miusuario.html", {'form':form})
'''
def registro_person(request):
	if request.method == "POST":
		data = request.POST
		user = User.objects.create_user(first_name=data['name'], last_name=data['surname'],password=data['password'],username=data['username'],email=data['email'])
#		user = User.objects.get(username=data['username'])
		person = Person.objects.create(user=user,dni=data['dni'],telefono=data['phone'],direccion=data['adress'],voluntario=data['voluntario'],solicitante=data['solicitant'])
		
		if person is not None:
			do_login(request, user)

			return redirect('Home')	

	return render(request, "voluntariado/registro.html")

def registro_actividad(request):
	#Establezco que formulario voy a utilizar
	form = ActividadForm
	#Consulto si el request viene con post o es la primera vez que se ejecuta
	if request.method == "POST":
		#Añadimos los datos recibidos a la variable form
		form = ActividadForm(data=request.POST)
		#consultamos si el formulario es válido
		if form.is_valid():
			#registramos la actividad
			actividad = form.save()

			return redirect('Home')
	return render(request, "voluntariado/registro_actividad.html", {'form':form})



def contacto(request):
	if request.POST:
		POST= request.POST
		nuevo_contacto = Contacto(tu_nombre=POST['nombre'], tu_direccion_de_correo=POST['email'], tu_mensaje=POST['mensaje'])
		nuevo_contacto.save()
		
	return render(request,'voluntariado/contacto.html')
