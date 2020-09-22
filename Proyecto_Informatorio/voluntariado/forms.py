from django import forms
<<<<<<< HEAD

from .models import Persona, Actividad, MiUsuario, Contacto

from django.contrib.auth.forms import UserCreationForm


=======
from .models import Person, Actividad
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
#from voluntariado.models import User

'''
>>>>>>> 873f8aec17a013b0034b05b9d4403dac83e888e4
class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona

        fields = ('dni','nombre','apellido','usuario','telefono','mail','direccion','contrasenia','solicitante','voluntario')

<<<<<<< HEAD
	
	

class MiUsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MiUsuario
        fields = ('mi_usuario','dni', 'voluntario', 'solicitante')

	
=======
class MiUsuarioCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User #MiUsuario
        fields = ('first_name', 'last_name','dni', 'voluntario', 'solicitante')
'''
>>>>>>> 873f8aec17a013b0034b05b9d4403dac83e888e4
class ActividadForm(forms.ModelForm):
	class Meta:
		model = Actividad
		fields =('nombre','fecha','realizada','id_solicitante')










class ContactoForm(forms.ModelForm):
	
	class Meta:
		model = Contacto 
		fields = ('tu_nombre','tu_direccion_de_correo','tu_mensaje')
