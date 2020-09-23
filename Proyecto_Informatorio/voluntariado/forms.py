from django import forms
from .models import Persona, Actividad, Contacto
from django.contrib.auth.forms import UserCreationForm
	
class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields =('nombre','fecha','realizada','id_solicitante')

class ContactoForm(forms.ModelForm):
	
	class Meta:
		model = Contacto 
		fields = ('tu_nombre','tu_direccion_de_correo','tu_mensaje')
