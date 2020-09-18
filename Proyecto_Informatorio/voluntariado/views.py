from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from .models import Persona, Actividad
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.
def home(request):
	num_voluntarios = Persona.objects.filter(voluntario=True).count() #del modelo de Persona cuento todos los que están como voluntarios
	num_favores = Actividad.objects.count() #del modelo de Actividad cuento todas las actividades cargadas
	num_faltantes = Actividad.objects.filter(realizada=False).count()

	return render(request, "voluntariado/home.html",context={'num_voluntarios':num_voluntarios,'num_favores':num_favores,'num_faltantes':num_faltantes})


#def login(request):
#	return render(request, 'voluntariado/login.html')

	
def registrar_voluntario(request):
	if request.POST:
		POST = request.POST
		nuevo_registro = Persona(dni=POST['dni'], nombre=POST['name'],
			apellido=POST['surname'], telefono=POST['phone'], mail=POST['email'], direccion=POST['adress'], voluntario=POST['voluntary'], 
			administrador=POST['admin'], solicitante=POST['solicitant'], contrasenia=POST['password'],usuario=POST['username']) 
		nuevo_registro.save()
		
	return render(request, 'voluntariado/voluntario.html')

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

def Historiadefavores(request):
	return render(request,'voluntariado/Historiadefavores.html')

def contacto(request):
	return render(request,'voluntariado/contacto.html')

def donaciones(request):
	return render(request,"voluntariado/donaciones.html")
