from django.db import models

# Create your models here.

class Persona(models.Model):
	id = models.IntegerField(primary_key = True, editable=False)
	dni = models.IntegerField()
	nombre = models.CharField(max_length=60)
	apellido = models.CharField(max_length=60)
	telefono = models.CharField(max_length=20)
	mail = models.EmailField()
	direccion = models.CharField(max_length=100)
	administrador = models.BooleanField()
	voluntario = models.BooleanField(null=True, blank=True)
	solicitante = models.BooleanField(null=True, blank=True)
	contrasenia = models.CharField(max_length=60, default="usuario")

	def __str__(self):
		return (self.nombre + ', '+self.apellido)

class Actividad(models.Model):
	id = models.IntegerField(primary_key=True, editable=False)
	nombre = models.CharField(max_length=60)
	fecha = models.DateField()
	realizada = models.BooleanField()
	id_solicitante = models.ForeignKey('Persona', on_delete = models.SET_NULL, null=True, blank=True, related_name = 'actividadesSol')
	id_voluntario = models.ForeignKey('Persona', on_delete = models.SET_NULL, null=True, blank=True, related_name = 'actividadesVol')
	

	def __str__(self):
		return (self.nombre + ' Fecha: '+str(self.fecha))