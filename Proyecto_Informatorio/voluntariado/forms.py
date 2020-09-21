from django import forms

from .models import Persona, Actividad, MiUsuario, Contacto

from django.contrib.auth.forms import UserCreationForm


class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = ('dni','nombre','apellido',,'usuario','telefono','mail','direccion','contrasenia','solicitante','voluntario')

	
	

class MiUsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MiUsuario
        fields = ('mi_usuario','dni', 'voluntario', 'solicitante')

	
class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields =('nombre','fecha','realizada','id_solicitante')










class ContactoForm(forms.ModelForm):
	
	class Meta:
		model = Contacto 
		fields = ('tu_nombre','tu_direccion_de_correo','tu_mensaje')
