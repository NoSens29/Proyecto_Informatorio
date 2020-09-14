from django.shortcuts import render, HttpResponse
from django.template import loader
from .models import Persona, Actividad
from .forms import PersonaForm

# Create your views here.
def home(request):
	num_voluntarios = Persona.objects.filter(voluntario=True).count() #del modelo de Persona cuento todos los que están como voluntarios
	num_favores = Actividad.objects.count() #del modelo de Actividad cuento todas las actividades cargadas
	num_faltantes = Actividad.objects.filter(realizada=False).count()

	return render(request, "voluntariado/home.html",context={'num_voluntarios':num_voluntarios,'num_favores':num_favores,'num_faltantes':num_faltantes})

def registrar_voluntario(request):
	if request.POST:
		POST = request.POST
		nuevo_registro = Persona(dni=POST['dni'], nombre=POST['name'],
			apellido=POST['surname'], telefono=POST['phone'], mail=POST['email'], direccion=POST['adress'], voluntario=POST['voluntary'], administrador=POST['admin'], solicitante=POST['solicitant'], contrasenia=POST['password']) 
		nuevo_registro.save()

	return render(request, 'voluntariado/voluntario.html')

def registrar_persona(request):
	form = PersonaForm
	return render(request, 'voluntariado/persona_new.html', {'form': form})
