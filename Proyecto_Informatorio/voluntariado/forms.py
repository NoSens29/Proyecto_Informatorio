from django import forms

from .models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('dni','nombre','apellido',,'usuario','telefono','mail','direccion','contrasenia','solicitante','voluntario')