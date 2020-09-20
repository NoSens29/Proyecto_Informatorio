from django import forms
from .models import Persona, Actividad, User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from voluntariado.models import User

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('dni','nombre','apellido','usuario','telefono','mail','direccion','contrasenia','solicitante','voluntario')


class MiUsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User #MiUsuario
        fields = ('first_name', 'last_name','dni', 'voluntario', 'solicitante')

class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields =('nombre','fecha','realizada','id_solicitante')
