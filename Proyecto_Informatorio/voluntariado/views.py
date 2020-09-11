from django.shortcuts import render, HttpResponse
from .models import Persona, Actividad

# Create your views here.
def home(request):
	num_voluntarios = Persona.objects.filter(voluntario=True).count() #del modelo de Persona cuento todos los que están como voluntarios
	num_favores = Actividad.objects.count() #del modelo de Actividad cuento todas las actividades cargadas
	num_faltantes = Actividad.objects.filter(realizada=False).count()

	return render(request, "voluntariado/home.html",context={'num_voluntarios':num_voluntarios,'num_favores':num_favores,'num_faltantes':num_faltantes})

